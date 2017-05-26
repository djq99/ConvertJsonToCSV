import json
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from collections import OrderedDict



def convertJsonToCSV(inputFile, outputFile):
    json_data = open(inputFile)
    data = json.load(json_data, object_pairs_hook=OrderedDict)

    # read permission from all values
    permission_set = set()
    for p in data.values():
        for i in p:
            permission_set.add(i)

    #convert permission set to permission list
    permission_list = list()
    permission_list.append("")
    for p in permission_set:
        permission_list.append(p)

    #convert each member who has the correspond permission into 1 otherwise 0 into a list
    result = list()
    for i, (key, value) in enumerate(data.items()):
        temp_list = list()
        for p in permission_set:
            if p in value:
                temp_list.append(1)
            else:
                temp_list.append(0)
        temp_list = ','.join(map(str, temp_list))
        result.append(key + ',' + temp_list)

    #write everything in the csv file as result
    with open(outputFile, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(permission_list)
        for r in result:
            csvfile.write(r)
            csvfile.write('\n')

def createGoogleSpreadsheet(emailAddress,outputFile):

    scope = ['https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Test-bb8747c9d5bb.json', scope)
    gc = gspread.authorize(credentials)

    sh = gc.create('Jiaqi Duan')

    sh.share(emailAddress, perm_type='user', role='writer')
    sheet = gc.open('Jiaqi Duan').sheet1

    with open(outputFile, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i,row in enumerate(spamreader):
            for j,cell in enumerate(row):
                sheet.update_cell(i+1, j+1, cell)


def main():
    convertJsonToCSV('data.json','data.csv')

    # input email address as first parameter
    createGoogleSpreadsheet("",'data.csv')

if __name__ == '__main__':
    main()


