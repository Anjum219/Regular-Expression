import re

def main():
    regex_1 = r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$" # roman numerals
    regex_2 = r"^[7|8|9]\d{9}$" # 10 digit number starting with 7/8/9
    regex_3 = r"^[a-z][a-z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-z]+\.[a-z]{1-3}$" # email address
    regex_4 = r"^[A-Za-z][A-Za-z0-9\.\_\-]+@[A-Za-z]+\.[a-z]{1,3}$" # simplified email address
    print(str(bool(re.match(regex_4, input()))))

if __name__ == '__main__':
    main()