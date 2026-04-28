expenses = {'food': 16000, 'traveling': 12000, 'study': 8000, 'pc': 20000}

def check_key_presence():
    key = input("Enter the key to check for its presence: ")
    if key in expenses.keys():  
        print(f"key '{key}' is present in the expense dictionary")
    else:
        print(f"key '{key}' is not present in the expense dictionary") 

def sum_dict_value():
    print("sum of all the values in the dictionary:")
    print(f"{sum(expenses.values())}")  

def main():
    check_key_presence()
    sum_dict_value()

if __name__ == "__main__":
    main()