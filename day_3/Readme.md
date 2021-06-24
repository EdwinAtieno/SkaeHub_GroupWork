1.Write a Python program to get the top 20 countries' data (Last Update, Country/Region, Confirmed, Deaths, Recovered) of the Novel Coronavirus (COVID-19).
2.Write a Python program to create a plot (of lines) of total deaths, confirmed, recovered and active cases Country wise where deaths greater than 200.
3.Write a Python program to get the latest number of confirmed deaths and recovered people of Novel Coronavirus (COVID-19) cases per Country/Region and per Province/State of the particular country.

Please allow the user to generate PDFs once they receive results from exercise 1,2 & 3 stated above.
Leverage the use of the Pandas package and the following COVID19 data set to complete this challenge.






Q1)
    STEP: 
        1) Analyse and organise CSV file
        2) Read Pandas documentation - https://pandas.pydata.org/docs/
        3) Filter Based on Conditions
        4) Sort the data
        5) Get top 20 countries (edited)
      
      
Q2)
    STEPS:
        1) convert the csv file to dataframe
        2) create a new collum for active cases
        3) get the total number of case in every country
        4) sort the grouped  data  by death
        5) use data that has more than 200
        6) gives the size for graphic output
        7) creates the lines in the graph  for ech information wanted
        8) add title
        9) labeling x and y
        10) ask user if to convert into pdf
          
      
Q3) 
    STEPS:
      1. Read csv
      2. select only columns required
      3. Sort the countries using the last update
      4. select last date from each country and output
      5. prompt user if they want the data in pdf
          - if yes, generate pdf
          - else if no, exit
          
 Q4) PDF:
    STEPS:
      1) import matplotlib.pyplot
      2) from matplotlib.backends.backend_pdf import PdfPages
      3) Create a converting to pdf Function
      4) Use ig  and ax-is for unpacking  this tuple into the variables, fig is useful incase you want to save as a figure later, ax is for objects in plotting methods
      5) resize subplots in a figure so that there are no overlaps between axes objects
      6) hide axes
      7) saves mutiples plotd to a file
      8) save fig
      9) close the pdf process
      
      
      
      
      
      