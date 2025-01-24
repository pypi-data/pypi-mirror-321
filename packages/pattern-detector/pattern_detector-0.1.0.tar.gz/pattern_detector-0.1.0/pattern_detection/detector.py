import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis
from joblib import Parallel, delayed

class PatternDetector:
    def __init__(self, df, pattern, column_pattern):
        self.df = df.copy()
        self.pattern = pattern
        self.column_pattern = column_pattern
        self.similarity_dict = {}
        self.pattern1 = None
        self.window_size = None
        self.bin_parser = None
        self.len_iter = None
        self.pattern_constraints = {}

    def preprocess_pattern(self):
        """Preprocess the pattern data."""
        len_iter = 400 if len(self.pattern) >= 400 else 200
        bin_parser = 3 if len_iter == 400 else 2

        self.pattern['bin'] = self.pattern.index // bin_parser
        self.pattern1 = self.pattern.groupby('bin')[self.column_pattern].mean().to_numpy()
        self.len_iter = len_iter
        self.bin_parser = bin_parser
        self.window_size = len(self.pattern1)

        # Compute constraints
        self.pattern_constraints = {
            "max_pos": np.max(self.pattern1) + 0.1 * np.ptp(self.pattern1),
            "min_pos": np.min(self.pattern1) - 0.1 * np.ptp(self.pattern1),
            "mean_pos_upper": np.mean(self.pattern1) + 0.1 * np.ptp(self.pattern1),
            "mean_pos_lower": np.mean(self.pattern1) - 0.1 * np.ptp(self.pattern1),
            "pattern_skewness": skew(self.pattern1),
            "pattern_kurtosis": kurtosis(self.pattern1),
            "pattern_std": np.std(self.pattern1),
            "starting_point_lower": self.pattern1[0] - 0.2 * np.ptp(self.pattern1),
            "starting_point_upper": self.pattern1[0] + 0.2 * np.ptp(self.pattern1),
            "ending_point_lower": self.pattern1[-1] - 0.2 * np.ptp(self.pattern1),
            "ending_point_upper": self.pattern1[-1] + 0.2 * np.ptp(self.pattern1),
            "cross_correlation_threshold": 0.5,
        }

    def preprocess_data(self):
        """Preprocess the main data."""
        self.df['bin'] = self.df.index // self.bin_parser
        return self.df.groupby('bin')[self.column_pattern].mean().to_numpy().reshape(-1, 1)

    def apply_constraints(self, window):
        """Apply constraints to filter valid windows."""
        pc = self.pattern_constraints
        corr_coef = np.corrcoef(window, self.pattern1)[0][1]

        if (
            np.max(window) <= pc["max_pos"]
            and np.min(window) >= pc["min_pos"]
            and pc["mean_pos_upper"] >= np.mean(window) >= pc["mean_pos_lower"]
            and abs(skew(window) - pc["pattern_skewness"]) < 0.5
            and abs(kurtosis(window) - pc["pattern_kurtosis"]) < 1.0
            and pc["pattern_std"] * 0.9 <= np.std(window) <= pc["pattern_std"] * 1.1
            and corr_coef >= pc["cross_correlation_threshold"]
            and pc["starting_point_lower"] <= window[0] <= pc["starting_point_upper"]
            and pc["ending_point_lower"] <= window[-1] <= pc["ending_point_upper"]
        ):
            return True
        return False

    def compute_cosine_sim(self, data1, i, j):
        """Compute cosine similarity for a given sliding window."""
        window = data1[i:i + self.window_size - (self.len_iter // 2) + j, :].reshape(-1,)

        if len(window) != len(self.pattern1):  # Ensure dimensions match
            return i, j, 0

        # Apply constraints
        if not self.apply_constraints(window):
            return i, j, 0

        fft_pattern = np.fft.fft(self.pattern1)
        fft_window = np.fft.fft(window)

        dot_product = np.dot(np.abs(fft_pattern), np.abs(fft_window))
        norm_pattern = np.linalg.norm(np.abs(fft_pattern))
        norm_window = np.linalg.norm(np.abs(fft_window))
        similarity = dot_product / (norm_pattern * norm_window)

        return i, j, similarity

    def calculate_similarity(self):
        """Calculate sliding window cosine similarity."""
        data1 = self.preprocess_data()

        results = Parallel(n_jobs=-1)(
            delayed(self.compute_cosine_sim)(data1, i, j)
            for i in range(0, len(data1) - self.window_size, 2)
            for j in range(0, self.len_iter, self.len_iter // 40)
        )

        for i, j, similarity in results:
            if similarity > 0:
                self.similarity_dict.setdefault(i, {})[j] = similarity

    def get_top_similarities(self):
        """Extract top similarities from the similarity dictionary."""
        results = [
            {'key': key1, 'max_key': max(value, key=value.get), 'max_value': max(value.values())}
            for key1, value in self.similarity_dict.items()
        ]
        return pd.DataFrame(results)

    def find_area_of_interest(self):
        """Find areas of interest in the data."""
        self.preprocess_pattern()
        self.calculate_similarity()
        df_dist = self.get_top_similarities()

        approx_cycle_length = len(self.pattern1) * 0.95
        df_dist['app_cycle'] = (df_dist['key'] // approx_cycle_length).astype(int)
        grouped = df_dist.groupby('app_cycle')

        cyc_concat_df = pd.concat(
            [
                group.loc[group['max_value'].idxmax()].assign(cycle=idx_cyc)
                for idx_cyc, (_, group) in enumerate(grouped)
                if not group.empty and group['max_value'].max() != 0
            ],
            ignore_index=True
        )

        cyc_concat_df['start_index'] = cyc_concat_df['key']
        cyc_concat_df['end_index'] = (
            cyc_concat_df['start_index'] + self.window_size +
            cyc_concat_df['max_key'] - (self.len_iter // 2)
        )
        cyc_concat_df['shift_start'] = cyc_concat_df['start_index'].shift(1, fill_value=len(self.pattern1))
        cyc_concat_df['diff'] = cyc_concat_df['shift_start'] - cyc_concat_df['start_index']
        limit = len(self.pattern1) * 0.7
        cyc_concat_df = cyc_concat_df[cyc_concat_df['diff'] < -limit].reset_index(drop=True)
        cyc_concat_df['cycle'] = cyc_concat_df.index

        cyc_concat_df['shift_end'] = cyc_concat_df['end_index'].shift(1, fill_value=cyc_concat_df['diff'].iloc[0])
        cyc_concat_df['diff_end'] = cyc_concat_df['shift_end'] - cyc_concat_df['start_index']
        overlap = cyc_concat_df['diff_end'] > 0
        cyc_concat_df.loc[overlap, 'start_index'] += cyc_concat_df.loc[overlap, 'diff_end'] + 1

        self.df['cycle'] = np.nan
        for _, row in cyc_concat_df.iterrows():
            start, stop = int(row['start_index'] * self.bin_parser), int(row['end_index'] * self.bin_parser)
            self.df.loc[start:stop, 'cycle'] = row['cycle']

        return self.df
