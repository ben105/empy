import json
import subprocess
import sys

CONFIG_PATH = 'config.json'

path_to_excel_file = input('Drag the Excel file you wish to read from here: ')
config = {
    'excel_path': path_to_excel_file.strip("'").strip('"').strip()
}

with open(CONFIG_PATH, 'w') as config_file:
    json.dump(config, config_file)

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
