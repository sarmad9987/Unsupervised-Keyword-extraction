import helper
import configparser
# Function to read configuration file
def read_config():
    config = configparser.ConfigParser()
    config.read('Project.config')
    return config


#Reading settings
config = helper.read_config()

data_location = config['file location']['data']
settings1 = config['columnheaders']['column_headers']
settings2= config['Rename column headers']['Postcode']
settings3 = config['Columns for keyword extraction']['statements']
settings4= config['Parameters']['max_words']
print("\nDisplaying all settings \n")
print("File location: " + data_location)
print("column headers: " + settings1)
print("Rename column headers: " + settings2)
print("keyword extraction columns: " + settings3)
print("Parameters: " + settings4)
