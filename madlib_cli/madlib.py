readFile = ""

def read_template(n):
    
    with open(n,'r') as file:
        readFile = file.read()
        return readFile

def parse_template(readFile):
    return readFile

def merge():
    pass

read_template('assets/dark_and_stormy_night_template.txt')