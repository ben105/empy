# The goal of this module is to codify the PG&E peak hours.
#
# The data in this file is found from the PG&E website.
# https://www.pge.com/en_US/small-medium-business/your-account/rates-and-rate-options/time-of-use-rates.page

from empy.time_series import TS_TIMESTAMP_KEY

ALL = 'all'
PEAK = 'peak'
PARTIAL_PEAK = 'partial peak'
OFF_PEAK = 'off peak'
SUPER_OFF_PEAK = 'super off peak'

class PGEBreakdown:
    def __init__(self, time_series_list):
        self.time_series_by_peak = {}
        for time_series in time_series_list:
            peak_type = get_peak_type(time_series)
            self.time_series_by_peak.setdefault(peak_type, []).append(time_series)
            self.time_series_by_peak.setdefault(ALL, []).append(time_series)
    
    def all(self):
        return self.time_series_by_peak.get(ALL, [])
    
    def peak(self):
        return self.time_series_by_peak.get(PEAK, [])
    
    def partial_peak(self):
        return self.time_series_by_peak.get(PARTIAL_PEAK, [])

    def off_peak(self):
        return self.time_series_by_peak.get(OFF_PEAK, [])
    
    def super_off_peak(self):
        return self.time_series_by_peak.get(SUPER_OFF_PEAK, [])
    


# This is a list of peak types organized in a list of 24 items, each index represents an
# hour in the day (index 0 is 00:00am, and index 23 is 23:00pm).
SPRING_PEAK_HOURS = (
    [OFF_PEAK] * 9              # 00:00 -  8:59 (9 hours)
    + [SUPER_OFF_PEAK] * 5      #  9:00 - 13:59 (5 hours)
    + [OFF_PEAK] * 2            # 14:00 - 15:59 (2 hours)
    + [PEAK] * 5                # 16:00 - 20:59 (5 hours)
    + [OFF_PEAK] * 3            # 21:00 - 23:59 (3 hours)
)

# This is a list of peak types organized in a list of 24 items, each index represents an
# hour in the day (index 0 is 00:00am, and index 23 is 23:00pm).
SUMMER_PEAK_HOURS = (
    [OFF_PEAK] * 14             # 00:00 -  13:59 (14 hours)
    + [PARTIAL_PEAK] * 2        # 14:00 - 15:59 (2 hours)
    + [PEAK] * 5                # 16:00 - 20:59 (5 hours)
    + [PARTIAL_PEAK] * 2        # 21:00 - 22:59 (2 hours)
    + [OFF_PEAK] * 1            # 23:00 - 23:59 (1 hours)
)

# This is a list of peak types organized in a list of 24 items, each index represents an
# hour in the day (index 0 is 00:00am, and index 23 is 23:00pm).
FALL_AND_WINTER_PEAK_HOURS = (
    [OFF_PEAK] * 16             # 00:00 - 15:59 (16 hours)
    + [PEAK] * 5                # 16:00 - 20:59 (5 hours)
    + [OFF_PEAK] * 3            # 21:00 - 23:59 (3 hours)
)

# This is a list of peak data organized in a list of 12 items, each index represents a
# month (index 0 is Januaray, index 11 is December).
PEAK_BY_MONTH = [
    FALL_AND_WINTER_PEAK_HOURS,     # Jan
    FALL_AND_WINTER_PEAK_HOURS,     # Feb
    SPRING_PEAK_HOURS,              # Mar
    SPRING_PEAK_HOURS,              # Apr
    SPRING_PEAK_HOURS,              # May
    SUMMER_PEAK_HOURS,              # Jun
    SUMMER_PEAK_HOURS,              # Jul
    SUMMER_PEAK_HOURS,              # Aug
    SUMMER_PEAK_HOURS,              # Sep
    FALL_AND_WINTER_PEAK_HOURS,     # Oct
    FALL_AND_WINTER_PEAK_HOURS,     # Nov
    FALL_AND_WINTER_PEAK_HOURS,     # Dec
]

def create_pge_breakdown(time_series_list):
    return PGEBreakdown(time_series_list)

def get_peak_type(time_series):
    timestamp = time_series[TS_TIMESTAMP_KEY]
    month = timestamp.month - 1 # Needs to be zero-indexed
    hour = timestamp.hour
    relevant_peak_hours = PEAK_BY_MONTH[month]
    return relevant_peak_hours[hour]
