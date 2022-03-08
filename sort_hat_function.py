n = int(input("init "))

AV =[]
ANV = []
BV = []
BNV = []
NA = []
stud_choice= []
capacity = int(n/4)
while True:
    stud_choice = input().split()
    if len(stud_choice)>1 and stud_choice[1].isdigit():
        if int(stud_choice[1]) in AV or int(stud_choice[1]) in ANV or int(stud_choice[1]) in BV or int(stud_choice[1]) in BNV or int(stud_choice[1]) in NA :
            print("This rollnumber already exist. Duplicate entry!!!!!!!", stud_choice[1])
            continue
        if len(stud_choice[1]) != 4:
            print("Roll number is not correct")
            continue
        if stud_choice[2]== "A" and stud_choice[3] == "V":
            if len(AV)< capacity:
                AV.append(int(stud_choice[1]))
            else:
                NA.append(int(stud_choice[1]))
        elif stud_choice[2] == "A" and stud_choice[3] == "NV":
            if len(ANV)< capacity:
                ANV.append(int(stud_choice[1]))
            else:
                NA.append(int(stud_choice[1]))
        elif stud_choice[2] == "B" and stud_choice[3] == "V":
            if len(BV)< capacity:
                BV.append(int(stud_choice[1]))
            else:
                NA.append(int(stud_choice[1]))
        elif stud_choice[2] == "B" and stud_choice[3] == "NV":
            if len(BNV)< capacity:
                BNV.append(int(stud_choice[1]))
            else:
                NA.append(int(stud_choice[1]))
        else:
            NA.append(int(stud_choice[1]))
    elif stud_choice[0] == "fin":
        break

print("AV = ",AV)
print("BV = ",BV)
print("ANV = ",ANV)
print("BNV = ",BNV)
print("NA = ",NA)

        
    

