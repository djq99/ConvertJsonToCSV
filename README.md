# ConvertJsonToCSV
A python program converts the json file into CSV format


The folder contains 3 files:
homework.py -- is the main function that contains two functions: 
           1.convertJsonToCSV function takes two parameters: 
                      the first parameter is the json file that you want to convert.
                      the second parameter is the CSV file you want.
           2.createGoogleSpreadsheet function is to create a google spreadsheet and insert the data on your csv file. It also              contains 2 parameters: 
                      the first one is the email address you want to share with. Please fill this parameter before you run the                       program !!!
                      the second parameter is the csv file.

data.json -- is the sample json file to test

Test-bb8747c9d5bb.json -- is the credential to login in the google api


To Run it:

1. Install the dependency below in your terminal:

pip install --upgrade google-api-python-client

pip install gspread

2. Write an email address you want to share with at homework.py file and the location is:
createGoogleSpreadsheet function under main function. you should add first parameter of it.

3. python homework.py
Just wait couple of seconds then everything will be done. Cheers!
