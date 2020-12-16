import re

def search_and_replace_line(search, replace, line): # finds the string to be searched in a line and replces 
    pattern = re.compile(search)
    found = pattern.search(line)
    
    while found:
        line = re.sub(pattern, replace, line)
        found = pattern.search(line)
        
    return line

def main():
    search_1 = ' && ' # to be searched
    search_2 = ' \|\| '
    replace_1 = ' and ' # to be replced with
    replace_2 = ' or '
    n = int(input())
    contents = []
    
    for i in range(n):
        line = input()
        line = search_and_replace_line(search_1, replace_1, line)
        line = search_and_replace_line(search_2, replace_2, line)
        contents.append(line)
        i = i+1
        
    for i in range(n):
        print(contents[i])
        
if __name__ == '__main__':
    main()
