import json
import subprocess
import sys

CONFIG_PATH = 'config.json'

config = {}
with open(CONFIG_PATH) as config_file:
    config = json.load(config_file)

path_to_excel_file = input('Drag the Excel file you wish to read from here: ')

config['excel_path'] = path_to_excel_file.strip("'").strip('"').strip().replace('\\', '')

with open(CONFIG_PATH, 'w') as config_file:
    json.dump(config, config_file, indent=4, sort_keys=True)

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
