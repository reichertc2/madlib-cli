import re
readFile = 'assets/dark_and_stormy_night_template.txt'
regex_bracket = r'{([A-Z][a-z]+)}'


def read_template(n):
    with open(n, 'r') as file:
        readFile = file.read()
        return readFile


def parse_template(file):
    fileA = read_template(file)
    string_file_b = regex_strip(fileA)
    replace_list = regex_list(fileA)
    # print(string_file_b)
    return string_file_b


def merge():
    pass


def regex_strip(string):
    # print(re.sub(r'{([A-Z][a-z]+)}', '{}',string))
    return re.sub(regex_bracket, '{}', string)


def regex_list(string):
    # split_content_list = string.split()
    new_list = []

    # found solution below here ==> https://stackoverflow.com/questions/12870178/looping-through-python-regex-matches
    pattern = re.compile(regex_bracket)
    for item in re.findall(pattern, string) :
        # print(item)
        new_list.append(item)
        # print(re.findall(pattern, string))
        # if item in re.findall(pattern, string) :
        #     revised_item = item.replace('{','')
        #     # print(revised_item)
        #     finished_item = revised_item.replace('}','')
        #     print(finished_item)
        #     new_list.append(finished_item)

    print(new_list)
    return new_list

read_template(readFile)
parse_template(readFile)
