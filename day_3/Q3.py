#import libraries
import pandas as pd
import pdf_converter
#path to csv
csv_data = r"covid.csv"
#to display all the rows in the csv
covid_data = pd.set_option("display.max_rows", None, "display.max_columns", None)
#read csv
covid_data = pd.read_csv(csv_data)
#convert the date and time to pandas date and time
covid_data['Last Update'] = pd.to_datetime(covid_data['Last Update'])
#select only the columns we need
date_df = covid_data[['Country/Region', 'Province/State', 'Deaths', 'Recovered', 'Last Update']]
#sort last date by country
date_df = date_df.sort_values('Last Update').groupby('Country/Region').last().reset_index()
#output
print(date_df)
#user prompt
answer = input(" Do you want a Pdf ?Enter yes or no: ")
if answer == "yes":
    #function to convert the dataframe to PDF
    pdf_converter.convert_to_pdf(date_df," ","last_update.pdf")
elif answer == "no":
    print("Okey.")
else:
    print("Please enter yes or no.")