from empy.time_series import TS_VALUES_KEY
from pandas import DataFrame


def convert_time_series_to_data_frame(all_time_series):
    rows = [time_series[TS_VALUES_KEY] for time_series in all_time_series]
    return DataFrame(rows)
