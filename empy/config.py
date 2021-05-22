import json


class Config:
    excel_path = ''
    seconds_sheet = ''
    minutes_sheet = ''
    hours_sheet = ''
    days_sheet = ''

    @staticmethod
    def initialize():
        with open('config.json') as config_file:
            config_json = json.load(config_file)
            Config.excel_path = config_json['excel_path']
            Config.seconds_sheet = config_json['seconds_sheet']
            Config.minutes_sheet = config_json['minutes_sheet']
            Config.hours_sheet = config_json['hours_sheet']
            Config.days_sheet = config_json['days_sheet']
