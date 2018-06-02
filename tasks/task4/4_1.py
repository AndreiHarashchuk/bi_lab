import csv
from itertools import groupby
from pathlib import Path
import sys


def get_data_from_file(source: str, has_header: bool, *args) -> list:
    data_file = open(source, "r")
    data = []
    reader = csv.DictReader(data_file)
    for entry in reader:
        foo = {}
        for arg in args:
            foo[arg] = entry[arg]
        data.append(foo)
    data_file.close()
    if has_header:
        del data[0]
    return data


def get_top_n(data: list, n: int, key: str, *outputs):
    data = sorted(data, key=lambda k: k[key], reverse=True)
    output_file = open("top.csv", "w")
    for entry in data[:n]:
        string = "'"
        for output in outputs:
            string = string + entry[output] + "','"
        output_file.write(string[:-2] + "\n")
    output_file.close()


def get_averages(data: list, measure: str, over: str):
    result = []
    for key, grp in groupby(
            sorted(data, key=lambda k: k[over]),
            lambda k: k[over]):
        temp_dict = dict(zip([over], [key]))
        temp_list = [float(item[measure]) for item in grp]
        temp_dict[measure] = round((sum(temp_list)) / len(temp_list), 2)
        result.append(temp_dict)
    output_file = open("ratings.csv", "w")
    for entry in result:
        output_file.write("'" + entry[over] + "','" +
                          str(entry[measure]) + "'\n")
    output_file.close()


path = input("File: ")
if not Path(path).is_file():
    print("There is no such file, sorry.")
    sys.exit()
# path = "IMDB-Movie-Data.xls"
movies = get_data_from_file(path, True, "Title", "Year", "Rating")
get_top_n(movies, 250, "Rating", "Title")
get_averages(movies, "Rating", "Year")
