import json
import pandas as pd
import requests

lldcs_list = [
    "Afghanistan", "Armenia", "Azerbaijan", "Bhutan", "Bolivia (Plurinational State of)", "Botswana", 
    "Burkina Faso", "Burundi", "Central African Republic", "Chad", "Ethiopia", 
    "Kazakhstan", "Kyrgyzstan", "Lao People's Democratic Republic", "Lesotho", 
    "Malawi", "Mali", "Moldova", "Mongolia", "Nepal", "Niger", "North Macedonia", 
    "Paraguay", "Rwanda", "South Sudan", "Eswatini", "Tajikistan", "Turkmenistan", 
    "Uganda", "Uzbekistan", "Zambia", "Zimbabwe"
]

ldcs_list = [
    "Afghanistan", "Angola", "Bangladesh", "Benin", "Burkina Faso",
    "Burundi", "Cambodia", "Central African Republic", "Chad", "Comoros",
    "Democratic Republic of the Congo", "Djibouti", "Eritrea",
    "Ethiopia", "Gambia", "Guinea", "Guinea-Bissau", "Haiti", "Kiribati",
    "Lao People's Democratic Republic", "Lesotho", "Liberia", "Madagascar",
    "Malawi", "Mali", "Mauritania", "Mozambique", "Myanmar", "Nepal",
    "Niger", "Rwanda", "Sao Tome and Principe", "Senegal", "Sierra Leone",
    "Solomon Islands", "Somalia", "South Sudan", "Sudan",
    "Tanzania", "Timor-Leste", "Togo", "Tuvalu", "Uganda", "Vanuatu",
    "Yemen", "Zambia"
]

sids_list = [
    "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Cabo Verde",
    "Comoros", "Cook Islands", "Cuba", "Dominica", "Dominican Republic",
    "Fiji", "Grenada", "Guinea-Bissau", "Guyana", "Haiti", "Jamaica", "Kiribati",
    "Maldives", "Marshall Islands", "Mauritius", "Micronesia (Federated States of)",
    "Nauru", "Niue", "Palau", "Papua New Guinea", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "Sao Tome and Principe", "Seychelles",
    "Singapore", "Solomon Islands", "Suriname", "Timor-Leste", "Tonga",
    "Trinidad and Tobago", "Tuvalu", "Vanuatu"
]

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

extract_emails(lldcs_list, "lldcs_emails.xlsx")
extract_emails(ldcs_list, "ldcs_emails.xlsx")
extract_emails(sids_list, "sids_emails.xlsx")