import csv
BASE_PATH = "./catCsv2/"
INSERT_AFTER_THIS_COL_NAME = "name"
SOURCE_COL_IND = 1

with open(BASE_PATH + 'destination.csv', newline='') as inF1:
    #list to change any line
    reader1 = list(csv.reader(inF1))
    with open(BASE_PATH + 'source.csv', newline='') as inF2:
        reader2 = csv.reader(inF2)
        with open(BASE_PATH + 'output.csv', 'w', newline='') as outF:
            writer = csv.writer(outF)

            cnt = 0
            for row2 in reader2:
                for i, row1 in enumerate(reader1):
                    #The first time you read the header of the input file
                    if cnt == 0 and i == 0:
                        cnt = 1
                        t = row1.index(INSERT_AFTER_THIS_COL_NAME)
                        reader1[i].insert(t + 1, row2[SOURCE_COL_IND])
                    else:
                        if row1[t] == row2[0]:
                            reader1[i].insert(t + 1, row2[SOURCE_COL_IND])
            writer.writerows(reader1)