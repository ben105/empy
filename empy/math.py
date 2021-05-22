from empy.data_frame import convert_time_series_to_data_frame


def average(all_time_series):
    data_frame = convert_time_series_to_data_frame(all_time_series)
    return data_frame.mean()

def sum(all_time_series):
    data_frame = convert_time_series_to_data_frame(all_time_series)
    return data_frame.sum()
