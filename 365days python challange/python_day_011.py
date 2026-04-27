student_details = {}
def main():
    num = int(input("Enter any number :"))
    for i in range (num):
        student_name = input("enter student name :")
        reg_number = input("enter registraition number :")
        total_marks = int(input("enter total marks :"))
        student_details[student_name] = [reg_number,total_marks]

        print(student_details)

        find = input ("enter student do you search :")
        if find not in student_details.keys():
            print("student did not found...!")

        else:
            print(f"student founded..!")
            print(f"student name    : {find}")
            print(f"registration no : {student_details[find][0]}")
            print(f"marks           : {student_details[find][1]}")    

if __name__ == "__main__":
    main()