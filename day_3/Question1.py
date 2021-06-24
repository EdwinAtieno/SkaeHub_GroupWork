import pandas as pd
import pdf_converter
csv_data = r"covid.csv"
covid_data = pd.read_csv(csv_data, usecols=['Province/State','Country/Region','Last Update','Confirmed','Deaths','Recovered'])
print("First Five rows of data\n", covid_data.head())
print("Data shape: ", covid_data.shape)
print("Data columns:\n ", covid_data.columns)
covid_data['Last Update'] = pd.to_datetime(covid_data['Last Update'])
unique_countries = covid_data.groupby(covid_data['Country/Region']).sum()
date_df = covid_data[['Country/Region', 'Last Update']]
last_update = date_df.sort_values('Last Update').groupby('Country/Region').last()
filtered_data = pd.merge(unique_countries, last_update, on='Country/Region')
sorted = filtered_data.sort_values('Confirmed',ascending=False).reset_index()
print(sorted)
print("Top 20 Countries: \n", sorted.head(20))

#user prompt
answer = input(" Do you want a Pdf ?Enter yes or no: ")

if answer == "yes":
    #function to convert the dataframe to PDF
    pdf_converter.convert_to_pdf(sorted.head(20)," ","Top_20.pdf")
elif answer == "no":
    print("Okey.")
else:
    print("Please enter yes or no.")