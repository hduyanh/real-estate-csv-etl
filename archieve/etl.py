from src.extract import *
from src.transform import *
from config.config import csv_config

x = file_reader(csv_config['file_name'], csv_config['seperator'])
file_cleaner(x)