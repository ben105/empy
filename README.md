# Future Enhancements

## Scope

- Read from the CSV files
- Calculate aggregates
- Write results to the Excel spreadsheet
- Maintain macros in Excel

## Questions

- Can we get VBA to run Python?

# Getting Started

## Setup

All you need to do to get started is run the setup script, `python3 setup.py`. You will be asked to drag the Excel file into the terminal, this will store the file path in the configuration file.

## Running the Script

To run the script, run
`python3 main.py`

# Using Empy

## Access Data by Cadence

The spreadsheet separates data by cadence, i.e. seconds, minutes, hours, and days. It's possible to access these data with a getter in the format of `by_[cadence]`, where the brackets represent the cadence placeholder.

For example, you can run any of the following:

```
seconds_data = empy.by_seconds()
mintues_data = empy.by_minutes()
hours_data = empy.by_hours()
days_data = empy.by_days()
```

## PGE Peak Times

The empy module has the PG&E peak times codified, for hours of the day and months of the year. Once you've retrieved data by a particular cadence, you can then access data by a particular peak time.

The empy module allows for the following PG&E peak types:

- peak times
- partial peak times
- off peak times
- super off peak times
- all of the above

Examples of access these breakdowns in code:

```
seconds_data = empy.by_seconds()

# Get peak times
data = seconds_data.peak()

# Get partial peak times
data = seconds_data.partial_peak()

# Get off peak times
data = seconds_data.off_peak()

# Get super off peak times
data = seconds_data.super_off_peak()

# Get all of the above
data = seconds_data.all()
```

## Computing Sums and Averages

Behind the scenes, empy makes use of pandas to compute aggregates across large data frames. In order to compute the average or sum in empy, follow these examples:

```
seconds_data = empy.by_seconds()
all_peak_times_data = seconds_data.all()
averages = average(all_peak_times_data)
sums = sum(all_peak_times_data)
```

# Excel XLSX format vs XLSM format

## Behavior

This script can consume the xlsm format, but will write out the results in the xlxs format. This means that if you setup this script with an XLSM file, you should reconfigure it with the XLSX file for subsequent runs. Or re-export the original file in that format to begin with.

## Reasoning

The main reason for using XLSM is to make use of macros. Python will supersede the need for macros, and therefore we do not need this format.

The openpyxl engine understands how to write XLSX files, and therefore that is the behavior of this script.

# Separation of Concerns

## Sheets

We have a couple of sheets that we care about. We can store the relevance of each sheet in a sheets module. Referencing these values will provide type safety and prevent the risk associated with naming sheets by a string literal.

Additionally, we can provide a convenient way to update the names of the sheets. The names will be stored in the config.json file for quick and easy access.

These values can be maintained in a single spot, in case their values ever change. It will greatly minimize the impact to the rest of the code base.

## Important Cell Ranges

To do any kind of meaningful processing, we must reference data from the spreadsheet. This is typically done by specifying a cell range, but that is not ideal. Cell ranges don't have much meaning to the reader, and they can change.

Instead of using literal cell ranges, we can assign the range to variables that better describe the purpose of the cells, and reference these variables instead throughout the code base. This merits another separation of concern, in a separate module, i.e. `cell_ranges.py`.

## Options

For our convenience, we must outline the various options that can be provided to this script. Some of the potential options are:

- Number of main power lines
- Data fidelity (hours/mins/secs)
- Logging level
