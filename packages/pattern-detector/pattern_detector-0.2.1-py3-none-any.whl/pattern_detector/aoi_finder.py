import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")
from concurrent.futures import ThreadPoolExecutor, as_completed

#import warnings
from scipy.stats import skew, kurtosis
#warnings.filterwarnings("ignore")
from scipy.fft import fft
from scipy.interpolate import interp1d


def compute_cosine_sim(data1, window_size,len_iter,pattern1,  i, j):

    window = data1[i:i + window_size - (len_iter//2) + j ,:]


    max_pos = np.max(pattern1) +  0.1 * np.ptp(pattern1) # np.ptp : calculates max-min difference
    min_pos = np.min(pattern1) - 0.1 * np.ptp(pattern1)
    mean_pos_upper = np.mean(pattern1) + 0.1 * np.ptp(pattern1)
    mean_pos_lower = np.mean(pattern1) - 0.1 * np.ptp(pattern1)
    pattern_skewness = skew(pattern1.flatten())
    pattern_kurtosis = kurtosis(pattern1.flatten())
    pattern_std = np.std( pattern1.flatten() )
    cross_correlation_threshold = 0.5  # Set a threshold for cross-correlation

    starting_point_lower = pattern1[0] - 0.2 * np.ptp(pattern1)
    starting_point_upper = pattern1[0] + 0.2 * np.ptp(pattern1)

    ending_point_lower = pattern1[-1] - 0.2 * np.ptp(pattern1)
    ending_point_upper = pattern1[-1] + 0.2 * np.ptp(pattern1)


    x_original = np.linspace(0, 1, len(window))
    x_target = np.linspace(0, 1, len(pattern1))

    window = window.reshape(-1 ,)

    interpolator = interp1d(x_original, window, kind='cubic')  # Linear interpolation

    window2 = interpolator(x_target)

    corr_coef = np.corrcoef(window2, pattern1)[0][1]

    sliding_window_max = np.max(window2)
    sliding_window_min = np.min(window2)
    sliding_window_skewness = skew(window2)
    sliding_window_kurtosis = kurtosis(window2)
    sliding_window_mean = np.mean(window2)
    sliding_window_std = np.std(window2)


    if ( sliding_window_max <= max_pos and sliding_window_min >= min_pos and
            mean_pos_upper >= sliding_window_mean >= mean_pos_lower and
            abs(sliding_window_skewness - pattern_skewness) < 0.5 and
            abs(sliding_window_kurtosis - pattern_kurtosis) < 1.0 and
            pattern_std * 0.9 <= sliding_window_std <= pattern_std * 1.1 and
            corr_coef >= cross_correlation_threshold
            and starting_point_lower<= window2[0] <= starting_point_upper and
            ending_point_lower<= window2[-1] <= ending_point_upper ):

        fft_pattern = fft(pattern1)
        fft_window = fft(window2)

        magnitude_pattern = np.abs(fft_pattern)
        magnitude_window = np.abs(fft_window)

        dot_product = np.dot(magnitude_pattern, magnitude_window)
        norm_1 = np.linalg.norm(magnitude_pattern)
        norm_2 = np.linalg.norm(magnitude_window)

        cosine_similarity = dot_product / (norm_1 * norm_2)


        return i, j, cosine_similarity

    else:
        return i, j, 0


def sliding_window_cosine_similarity(data, pattern,  column_pattern ):

    len_iter = 400 if len(pattern) >= 400 else 200
    bin_parser = 3 if len_iter == 400 else 2

    pattern[column_pattern] = pattern[column_pattern].astype(float)
    pattern.reset_index(drop=True, inplace=True)
    pattern['bin'] = pattern.index // bin_parser
    pattern1 = pattern.groupby('bin').agg({column_pattern: 'mean'}).reset_index()
    pattern1 = np.array(pattern1[column_pattern]).reshape(-1, )

    # Prepare data
    data.reset_index(drop=True, inplace=True)
    data[column_pattern] = data[column_pattern].astype(float)
    data['bin'] = data.index // bin_parser
    data1 = data.groupby('bin').agg({column_pattern: 'mean'}).reset_index()
    data1 = np.array(data1[column_pattern]).reshape(-1, 1)

    window_size = len(pattern1)
    step_size = 2

    similarity_dict = {}


    with ThreadPoolExecutor() as executor:  # Adjust max_workers based on your CPU cores
        futures = [executor.submit(compute_cosine_sim, data1, window_size, len_iter, pattern1, i, j)
                   for i in range(0, len(data1) - window_size, step_size)
                   for j in range(0, len_iter, (len_iter // 40))]
        for future in as_completed(futures):
            i, j, similarity = future.result()
            if i not in similarity_dict:
                similarity_dict[i] = {}
            similarity_dict[i][j] = similarity

    return similarity_dict, pattern1, window_size, bin_parser, len_iter


def run_area_of_interest_finder(df,pattern,column_pattern):

    similarity_dict, pattern1, window_size, bin_parser, len_iter  = sliding_window_cosine_similarity(df, pattern, column_pattern)

    approx_cycle_length = len(pattern1)*0.95

    results = []
    for key1, value in similarity_dict.items():

        max_key = max(value, key=value.get)
        max_value = value[max_key]
        results.append({'key': key1, 'max_key': max_key, 'max_value': max_value})

    df_dist = pd.DataFrame(results)

    df_dist.reset_index(inplace=True)
    df_dist['app_cycle'] = df_dist["key"] // approx_cycle_length
    df_dist["app_cycle"] = df_dist["app_cycle"].astype(int)

    yig = tuple(df_dist.groupby("app_cycle"))
    cyc_dict = {x: y for x, y in yig}

    idx_cyc = 0
    cyc_concat_df = pd.DataFrame()

    for k in cyc_dict.keys():
        df_cyc = cyc_dict[k]
        df_cyc = df_cyc[ df_cyc["max_value"] != 0 ]

        key_min_df =  df_cyc[["key","max_key","max_value"]][  df_cyc["max_value"] == np.max(df_cyc['max_value'])]
        key_min_df["cycle"] = idx_cyc
        if len(key_min_df) != 0:
            cyc_concat_df = pd.concat([cyc_concat_df,key_min_df],ignore_index=True,axis="index")
            idx_cyc += 1
        else:
            continue

    cyc_concat_df["start_index"] = cyc_concat_df["key"]
    cyc_concat_df["end_index"] = cyc_concat_df["start_index"] + window_size + cyc_concat_df["max_key"] - (len_iter//2)
    cyc_concat_df["shift_start"] = cyc_concat_df["start_index"].shift(1)

    cyc_concat_df["diff"] = cyc_concat_df["shift_start"] - cyc_concat_df["start_index"]
    cyc_concat_df["shift_start"].iloc[0] = len(pattern1)
    cyc_concat_df["diff"].iloc[0] = -len(pattern1)
    limit = len(pattern1)*.7
    cyc_concat_df = cyc_concat_df[ cyc_concat_df["diff"] < -limit ]
    cyc_concat_df.reset_index(inplace=True, drop=True)
    cyc_concat_df["cycle"] = cyc_concat_df.index

    cyc_concat_df["shift_end"] = cyc_concat_df["end_index"].shift(1)
    ######## Çakışmaları önlemek için yapıldı
    cyc_concat_df["shift_end"].iloc[0] = cyc_concat_df["diff"].iloc[0]
    cyc_concat_df["diff_end"] = cyc_concat_df["shift_end"] - cyc_concat_df["start_index"]
    cyc_concat_df["start_index"][ cyc_concat_df["diff_end"] > 0 ] =  cyc_concat_df["start_index"][ cyc_concat_df["diff_end"] > 0 ] + cyc_concat_df["diff_end"] + 1


    #df = data.copy()
    df.reset_index(drop=True,inplace=True)
    for i in cyc_concat_df["cycle"].unique():
        start = cyc_concat_df["start_index"][cyc_concat_df["cycle"] == i].values[0]*bin_parser
        stop = cyc_concat_df["end_index"][cyc_concat_df["cycle"] == i].values[0]*bin_parser
        #print(start, stop, i, stop-start)
        df.loc[start:stop,"cycle"] = int(i)


    return df
