total_mark = 0
while True:
    print("================\n=====Result=====\n================")
    Mark_1 = float(input("Bangla="))
    Mark_2 = float(input("English="))
    Mark_3 = float(input("Math="))
    Mark_4 = float(input("Biology="))
    Mark_5 = float(input("Chemistry="))
    Mark_6 = float(input("Physics="))

    total_mark = Mark_1+ Mark_2+ Mark_3+ Mark_4+ Mark_5+ Mark_6
    average = total_mark/6

    if (Mark_1 <33 or
    Mark_2 <33 or
    Mark_3 <33 or
    Mark_4 <33 or
    Mark_5 <33 or
    Mark_6 <33):
        print("Failed")
    else:
         print("Total Mark=", total_mark)
         print("Average of Mark=", average)
         if (average >= 80):
                print("Grade=A+")
         elif (average >= 70):
          print("Grade=A")
         elif (average >= 60):
          print("Grade=B")
         elif (average >= 50):
            print("Grade=C")
         elif (average >= 40):
            print("Grade=D")
         else:
            print("Grade=F")

    print("1. Check another student's result \n2. Exit")
    choice = input("Select:")
    if choice == "1":
       continue
    elif choice == "2":
       print("Thank You!")
       break
    else:
       print("Invalid Choice!")
     

