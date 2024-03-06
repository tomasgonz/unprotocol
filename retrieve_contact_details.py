import json
import pandas as pd
import requests
from countries import lldcs_list, ldcs_list, sids_list

# Read config information

config_values = {}

try:
    with open('config', 'r', encoding='utf-8') as file:
        for line in file:
            if '=' in line and not line.startswith('#') and line.strip():
                key, value = line.strip().split('=', 1)
                config_values[key] = value
except Exception as e:
    print(f"Error reading the config file: {e}")

output_path = config_values['path']

# URL of the JSON data
url = 'https://bluebook.unmeetings.org/data.json'

# Send a GET request to fetch the data
response = requests.get(url)

# Make sure the request was successful
if response.status_code == 200:
    # Load the JSON content
    data = response.json()
else:
    print("Failed to retrieve data:", response.status_code)

# Now `data` contains the JSON data loaded into a Python object
# You can process `data` as needed in your script
def extract_emails(country_list, excel_file_name):
    # Load the JSON data
    with open('./data.json', encoding='utf-8') as file:
        data = json.load(file)

    # Filter the data for LLDCs and extract country and email
    country_data = []
    for country in data['countries']:
        # Check if any word from lldcs_list is contained in country['MC_EntityLong']
        if any(c in country['MC_EntityLong'] for c in country_list):
            if country['MC_EntityLong'] != 'Federal Republic of Nigeria' and country['MC_EntityLong'] != 'Independent State of Papua New Guinea' and country['MC_EntityLong'] != 'Independent State of Papua New Guinea':
                country_name = country['MC_EntityLong']
                email = country['MC_eMail']
                country_data.append({'country': country_name, 'email': email})

    # Convert to DataFrame
    data_df = pd.DataFrame(country_data)

    # Saving to Excel
    excel_path = excel_file_name
    data_df.to_excel(excel_path, index=False)

    excel_path

extract_emails(lldcs_list, output_path + "lldcs_emails.xlsx")
extract_emails(ldcs_list, output_path + "ldcs_emails.xlsx")
extract_emails(sids_list, output_path + "sids_emails.xlsx")