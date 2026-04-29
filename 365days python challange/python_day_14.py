def common_char(string_1,string_2):
    for letter in string_1:
        if letter in string_2:
            print (f"character '{letter}' is found in the both the string ")

def main ():
    common_char ("radhe" , "krushna" )


if __name__ == "__main__" :
    main()