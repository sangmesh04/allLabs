# In second year computer engineering class, group A student’s play cricket, group B
# students play badminton and group C students play football.
# Write a Python program using functions to compute following: -
# a) List of students who play both cricket and badminton
# b) List of students who play either cricket or badminton but not both
# c) Number of students who play neither cricket nor badminton
# d) Number of students who play cricket and football but not badminton.
# (Note- While realizing the group, duplicate entries should be avoided, Do not use SET
# built-in functions)

class CE:
    def input_list(self):
        n = int(input("Enter number of students: "))
        student_list = []
        for i in range(n):
            a = int(input(str(i+1)+ ". "))
            student_list.append(a)
        return  student_list

    def remove_duplicate(self, student_list):
        rmv = []
        for i in student_list:
            if(i not in rmv):
                rmv.append(i)
        return  rmv

    def intersection(self, list1, list2):
        ans = []
        for i in list1:
            if(i in list2):
                ans.append(i)
        return  ans

    def union(self,list1, list2):
        ans = list1.copy()
        for i in list2:
            if(i not in ans):
                ans.append(i)
        return  ans

    def difference(self, list1, list2):
        ans = []
        for i in list1:
            if(i not in list2):
                ans.append(i)
        return  ans

student = CE()
print("Cricket")
cricket = student.remove_duplicate(student.input_list())
print("Badminton")
badminton = student.remove_duplicate(student.input_list())
print("Football")
football = student.remove_duplicate(student.input_list())

print(cricket)
print(badminton)
print(football)
option = 1
while(option>0 and option < 5):
    print("<---- Menu ----> \n1.  List of students who play both cricket and badminton \n2. List of students who play either cricket or badminton but not both \n3. Number of students who play neither cricket nor badminton \n4. Number of students who play cricket and football but not badminton.")
    option = int(input("Enter option (0 to exit): "))
    if(option == 1):
        criANDbad = student.intersection(cricket, badminton)
        print(criANDbad)
    elif(option == 2):
        onlyCiricket = student.difference(cricket, badminton)
        onlyBadminton = student.difference(badminton, cricket)
        cricketORbadminton = student.union(onlyBadminton, onlyCiricket)
        print(cricketORbadminton)
    elif(option == 3):
         cricketUbad = student.union(cricket, badminton)
         OnlyFootball = student.difference(student.union(football, cricketUbad), cricketUbad)
         print(len(OnlyFootball))
         print(OnlyFootball)
    elif(option == 4):
        criANDfoot = student.union(cricket, football)
        onluCricketAndFootball = student.difference(criANDfoot, badminton)
        print(onluCricketAndFootball)
    else:
        print("Program ended successfully!")
        exit(1)


