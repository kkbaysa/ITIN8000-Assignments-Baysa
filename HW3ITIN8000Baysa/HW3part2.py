"""
Homework 3 part 2 will download data from Kaggle.com and pull information from a CSV
and then process it and export the result as a JSON file.
This assignment was completed by Kaitlyn Baysa during Fall2021 - ITIN8000
"""
import json
import os
from json import JSONDecodeError
import dask.dataframe as dd
import pandas as pd

# Create JSON file
with open("ComicCharacters.json", "w") as file:
    json.dumps({})
    file.close()

# Imports the data from dc-wikia-data.csv and marvel-wikia-data.csv
dc_data = dd.read_csv("dc-wikia-data.csv", usecols=['name', 'ALIGN', 'EYE', 'HAIR', 'SEX'], sample=10000000)


# print(len(dc_data))
# marvel_data = dd.read_csv("marvel-wikia-data-small.csv", usecols=['name', 'ALIGN', 'EYE', 'HAIR', 'SEX'])
# print(len(marvel_data))

def store(dc_data_In):
    for ind in dc_data_In.index:
        # Create an object from each record by "Character Name"
        # with object "Ownership" containing the value "Publisher" (DC or Marvel)
        # and object "Characteristics" containing the values:
        #         Alignment (Good, Bad, or Neutral)
        #         Eye Color
        #         Hair Color
        #         Gender
        characterObj = \
            {dc_data_In['name'][ind]: {
                'Ownership': 'DC',
                'Characteristics': {
                    'Alignment': dc_data_In['ALIGN'][ind],
                    'Eye Color': dc_data_In['EYE'][ind],
                    'Hair Color': dc_data_In['HAIR'][ind],
                    'Gender': dc_data_In['SEX'][ind]
                }
            }
            }

        # add record to JSON file called ComicCharacters.json
        with open("ComicCharacters.json", "r+") as fileOut:
            data = {}
            if os.path.getsize("ComicCharacters.json") > 0:
                data = json.load(fileOut)

            data.update(characterObj)
            fileOut.seek(0)
            json.dump(data, fileOut)


# ddata = dd.from_pandas(dc_data, npartitions=2)
new_df = dc_data.map_partitions(lambda part: store(part))
new_df.compute()

# Loop through each record of dc-wikia-data.csv
# for ind in dc_data.index:
#     # Create an object from each record by "Character Name"
#     # with object "Ownership" containing the value "Publisher" (DC or Marvel)
#     # and object "Characteristics" containing the values:
#     #         Alignment (Good, Bad, or Neutral)
#     #         Eye Color
#     #         Hair Color
#     #         Gender
#     characterObj = \
#         {dc_data['name'][ind]: {
#             'Ownership': 'DC',
#             'Characteristics': {
#                 'Alignment': dc_data['ALIGN'][ind],
#                 'Eye Color': dc_data['EYE'][ind],
#                 'Hair Color': dc_data['HAIR'][ind],
#                 'Gender': dc_data['SEX'][ind]
#             }
#         }
#         }
#
#     # add record to JSON file called ComicCharacters.json
#     with open("ComicCharacters.json", "r+") as file:
#         data = {}
#         if os.path.getsize("ComicCharacters.json") > 0:
#             data = json.load(file)
#
#         data.update(characterObj)
#         file.seek(0)
#         json.dump(data, file)
