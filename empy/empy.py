import empy.sheet

from empy.config import Config
from empy.peak_hours import create_pge_breakdown
from empy.time_series import convert_to_time_series
from pandas import read_excel


class Empy:
    def __init__(self):
        self.data_frames = read_excel(Config.excel_path, sheet_name=None, engine='openpyxl')
    
    def by_seconds(self):
        seconds_data_frame = empy.sheet.get_seconds_sheet(self.data_frames)
        return self._get_pge_breakdown(seconds_data_frame)

    def by_minutes(self):
        minutes_data_frame = empy.sheet.get_minutes_sheet(self.data_frames)
        return self._get_pge_breakdown(minutes_data_frame)

    def by_hours(self):
        hour_data_frame = empy.sheet.get_hours_sheet(self.data_frames)
        return self._get_pge_breakdown(hour_data_frame)

    def by_days(self):
        days_data_frame = empy.sheet.get_days_sheet(self.data_frames)
        return self._get_pge_breakdown(days_data_frame)

    def _get_pge_breakdown(self, data_frame):
        all_row_data = empy.sheet.parse_all_rows(data_frame)
        all_time_series = [convert_to_time_series(row_data) for row_data in all_row_data]
        return create_pge_breakdown(all_time_series)
    