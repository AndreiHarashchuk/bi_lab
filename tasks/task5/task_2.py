import argparse
import csv
import json
import urllib.request
import xmltodict


def output_csv(file_name, content):
    with open(file_name + '.csv', 'w') as file:
        writer = csv.writer(file)
        for key, value in content.items():
            writer.writerow([key, value])


def output_json(file_name, content):
    with open(file_name + '.json', 'w') as file:
        json.dump(content, file)


def output_xml(file_name, content):
    with open(file_name + '.xml', 'w') as file:
        xml_string = xmltodict.unparse(content, pretty=True)
        file.write(xml_string)


parser = argparse.ArgumentParser()
parser.add_argument('--download',
                    help='define the url of the file',
                    default='https://transit.land/api/v1')
parser.add_argument('--format',
                    help='define the acceptable file format',
                    default='json')
args = parser.parse_args()
download_url = args.download
file_format = args.format
content = urllib.request.urlopen(download_url)
data = json.loads(content.read())
if file_format == 'json':
    output_json('output', data)
elif file_format == 'xml':
    output_xml('output', data)
elif file_format == 'csv':
    output_csv('output', data)
