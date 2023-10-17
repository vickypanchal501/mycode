import datetime


while True:
    print("Create Student MarkSheet class 1 To 12 \n".center(100))
    while True:
        try:
            class_name = int(input("Enter Class Name :- ")) 
            if class_name >= 1 and class_name <= 5:
                subject = ["Hindi","English","Grammar","Mathematics","G.K"]
                break
            elif class_name >= 6 and class_name <= 10:
                subject = ["Hindi","English","Science","Mathematics","Social Science","Sanskrit"]
                break
            elif class_name >= 11 and class_name <= 12:
                stream  = {"maths":["Physics" ,"Chemistry", "Mathematics","English","Hindi"],
                "biology":["Physics" ,"Chemistry", "Biology","English","Hindi"],"arts":["History", "Political Science", "Sociology", "Economics", "Geography", "Psychology"],"commerce":["Accountancy","Business Studies","Economics","English" , "Informatics Practices/ Mathematics", "Physical Education"]}
                stream_name = input("Enter your stream Name:-").lower()
                if stream_name in list(stream.keys()):
                    subject = list(stream[stream_name])
                break    
            elif class_name >= 0 or class_name >= 13:
                print("Invalid Class Name Please Valid Class Name. You Can only Enter 1 To 12")
                class_name = int(input("Enter Class Name :- ")) 
                break
        except ValueError:
            print("Invalid Class Name Please Valid Class Name. You Can only Enter 1 To 12")
            continue

        # print(stream[keys])
    

    s_name = input("Enter stdent Full name :- ")
    f_name  =  input("Enter Stdent Father Name :- ")


    while True:
        date_text = input("Enter Your BirthDate :- ")
        try:
            birthday = datetime.datetime.strptime(date_text, '%d/%m/%Y')
            today_date = datetime.date.today()
            
            if birthday.year > today_date.year:
                print("Incorrect date format, should be DD/MM/YYYY.")
                continue
            break    
        except ValueError:    
            print("Incorrect date format, should be DD/MM/YYYY.")
            continue  
    while True:
        try:
            Roll_no = int(input("Enter Student Roll NO :- "))
            if len(str(Roll_no)) > 10 or len(str(Roll_no)) == 0:
                print("You can only Enter maximum 10 Digit number")
                print("Please Re-Enter Roll Number")
                continue
            break

        except ValueError:
            print("Please use a integer Number")
            print("Please Re-Enter Roll Number")
            continue
    grade =[]    
    def gradefunc(ob_marks):
        for marks in ob_marks:
            if marks >= 90 and marks <= 100:
                grade.append("A+")
            elif marks >= 80 and marks <= 89:
                grade.append("A")
            elif marks >= 70 and marks <= 79:
                grade.append("B+")
            elif marks >= 60 and marks <= 69:
                grade.append("B")  
            elif marks >= 50 and marks <= 59:
                grade.append("C+")
            elif marks >= 40 and marks <= 49:
                grade.append("C")      
            elif marks >= 34 and marks <= 39:
                grade.append("D")     
            elif marks <= 33:
                grade.append("Fail")   
            else:
                print("invalid Marks")    

            


    Total_marks = []
    ob_marks = []
    max_sub = max([len(k) for k in subject])
    for i in range(len(subject)):
        Total_marks.append(100)
        while True:
            try:
                num = int(input("Enter {} Marks :-".format(subject[i])))
                if num > 100:
                    print("Invalid Marks")
                    print("You can only Enter 0 to 100")
                    continue
                break
            except ValueError:
                print("Please Use integer Number")  
                continue  
    
        ob_marks.append(num)
    sum_total = sum(Total_marks)    
    sum_obmarks = sum(ob_marks)  
    
    percentage  = sum_obmarks/sum_total * 100
    ob_marks.append(int(percentage))
    # print(subject)
    gradefunc(ob_marks)
    if "Fail" in grade:
        grade[-1] = "Fail"
    print("-"*(max_sub + 50))
    print("PROGRESS REPORT".center(max_sub + 50))
    print("-"*(max_sub + 50))
    print("  Class Name ".ljust(20),": ",class_name,end="\t")
    print("Roll Number ".rjust(18),": ",Roll_no)
    print("  Full Name ".ljust(20),": ",s_name)
    print("  Father Name ".ljust(20),": ",f_name)
    print("  Date Of Birthday ".ljust(20),": ",birthday.date())







    print('''|------|-{}---|-{}-|-{}-|-{}-|
| S.No | {}   | TotalMarks | Marks obtained | Grade |'''.format('-'* max_sub,'-'*10,'-'*14,'-'*5,"Subject".ljust(max_sub)))

    for j in range(len(subject)):
            print('''|------|-{}---|-{}-|-{}-|-{}-|
|  {}   | {}   | {} | {} | {} |'''.format('-'* max_sub,'-'*10,'-'*14,'-'*5,j+1,subject[j].ljust(max_sub),str(Total_marks[j]).center(10),str(ob_marks[j]).center(14),str(grade[j]).center(5)))
            
    print("""|{}|{}|{}|{}|
|{} | {} | {} | {} |
|{}|{}|{}|{}|""".format("-"*(max_sub+11),'-'* 12,"-"*16,"-"*7,"Total".center(max_sub + 10),str(sum_total).center(10),str(sum_obmarks).center(14),str(grade[-1]).center(5),"-"*(max_sub + 11),"-"*12,"-"*16,"-"*7))        


    print(" Percentage".ljust(15),": {:.2f}".format(percentage))
    if percentage < 33 or "Fail" in grade:
        print(" Result".ljust(15),";","FAIL")
    else:    
        print(" Result".ljust(15),":","Pass")
    print("\n")    
    
    g= input("IF you are add a one more marksheet Please Enter yes/YES Either No/no/NO :- ")
    if g == "yes" or g == "YES":
        print("\n")
        continue
    elif g == "NO"or g =="no" or g== "No":
        break