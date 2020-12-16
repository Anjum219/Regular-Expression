import re

def main():
    S = input() # matches k inside S and returns the indices of finding
    k = input()

    pattern = re.compile(k)
    found = pattern.search(S)
    
    if not found: 
        print('(-1, -1)')
    while found:
        print( '(' + str(found.start()) + ', ' + str(found.end()-1) + ')' ) 
        found = pattern.search(S, found.start()+1)
        
if __name__ == '__main__':
    main()
