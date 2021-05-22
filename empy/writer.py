import pandas
from openpyxl import load_workbook


OPTIONS = {
    'strings_to_formulas': False,
    'strings_to_urls': False,
}

def create_excel_writer(excel_path):
    book = load_workbook(excel_path)
    writer = pandas.ExcelWriter(correct_for_suffix(excel_path), engine='openpyxl', options=OPTIONS)
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    return writer

def correct_for_suffix(excel_path):
    parts = excel_path.split('.')
    parts.pop()
    return '.'.join([*parts, 'xlsx'])
