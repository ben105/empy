from empy.math import average

def do_work(empy):
    # The following is just an example:
    seconds_data = empy.by_seconds()
    all_peak_times_data = seconds_data.all()
    averages = average(all_peak_times_data)
    print(averages)