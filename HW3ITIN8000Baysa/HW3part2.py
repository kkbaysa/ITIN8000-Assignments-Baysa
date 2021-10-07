"""
Homework 3 part 2 will download data from Kaggle.com and pull information from a CSV
and then process it and export the result as a JSON file.
This assignment was completed by Kaitlyn Baysa during Fall2021 - ITIN8000
"""
import json
import time
from multiprocessing import Process
import pandas as pd

# Imports the data from dc-wikia-data.csv and marvel-wikia-data.csv
dc_data = pd.read_csv("dc-wikia-data.csv", usecols=['name', 'ALIGN', 'EYE', 'HAIR', 'SEX'])
marvel_data = pd.read_csv("marvel-wikia-data.csv", usecols=['name', 'ALIGN', 'EYE', 'HAIR', 'SEX'])

# dictionary to store the processed data
jsonDump = {}
# keep track of how many records have been processed
counter = 0


# function to process both sets of data
def dataProcess(counterIn, dataSet, ownershipIn):
    # loop through row in datset
    for ind in dataSet.index:
        # Create an object from each record by "Character Name"
        # with object "Ownership" containing the value "Publisher" (DC or Marvel)
        # and object "Characteristics" containing the values:
        #         Alignment (Good, Bad, or Neutral)
        #         Eye Color
        #         Hair Color
        #         Gender
        characterObj = \
            {dataSet['name'][ind]: {
                'Ownership': ownershipIn,
                'Characteristics': {
                    'Alignment': dataSet['ALIGN'][ind],
                    'Eye Color': dataSet['EYE'][ind],
                    'Hair Color': dataSet['HAIR'][ind],
                    'Gender': dataSet['SEX'][ind]
                }
            }
            }
        # append object to the dictionary
        jsonDump.update(characterObj)
        # increase counter
        counterIn = counterIn + 1
    # print the number of records added
    print(str(counterIn) + " " + ownershipIn + " characters added to json file.")


if __name__ == '__main__':
    # create two processes to run the data
    p1 = Process(target=dataProcess(counter, dc_data, "DC"))
    p2 = Process(target=dataProcess(counter, marvel_data, "Marvel"))
    # start processes
    p1.start()
    p2.start()
    # wait for processes to end
    p1.join()
    p2.join()

    # add records to JSON file called ComicCharacters.json
    with open("ComicCharacters.json", "w") as fileOut:
        json.dump(jsonDump, fileOut)

# print times of execution
print(time.perf_counter())
