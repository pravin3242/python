import csv

# Initialize an empty dictionary to store the country data
countries_data = {}

# Read data from the CSV file
with open('C:\\Users\\lnv0176\\Downloads\\country.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract country name from the row
        country_name = row['Country Name']

        # Create a dictionary for the country using the other columns
        country_info = {
            'Capital': row['Capital'],
            'Currency': row['Currency']
            # Add more key-value pairs as needed
        }

        # Add the country data to the main dictionary
        countries_data[country_name] = country_info

# Print the resulting nested dictionary
print(countries_data)

# countries_with_and_of = [country for country in countries_data.keys() if 'and' in country.lower() or 'of' in country.lower()]
#
# # Print the total number of countries and the list of countries
# print(f"Total countries with 'and' or 'of' in their name: {len(countries_with_and_of)}")
# print("List of countries:", countries_with_and_of)