import re
readFile = 'assets/dark_and_stormy_night_template.txt'


def read_template(n):
    
    with open(n,'r') as file:
        readFile = file.read()
        return readFile

def parse_template(file):
    fileA = read_template(file)
    string_file_b = regex_strip(fileA)
    parse_item = re.compile('{([A-Z][a-z]+)}')
    split_content_list = file.split()
    stripped_item_list = []

    
    
    print(string_file_b)
    return string_file_b




def merge():
    pass

def regex_strip(string):
    # print(re.sub(r'{([A-Z][a-z]+)}', '{}',string))
    return re.sub(r'{([A-Z][a-z]+)}', '{}',string)

def regex_list(string):


    for item in split_content_list:
        print(parse_item.match(item))
    if parse_item.match(item):
        fileA.replace(item,'7')

read_template(readFile)
parse_template(readFile)