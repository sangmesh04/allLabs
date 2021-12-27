# a) Write a Python program to store roll numbers of student in array who attended
# training program in random order. Write function for searching whether particular
# student attended training program or not, using Linear search and Sentinel search.
# b) Write a Python program to store roll numbers of student array who attended training
# program in sorted order. Write function for searching whether particular student
# attended training program or not, using Binary search and Fibonacci search

class Array:
    def input_array(self):
        n = int(input("Enter number of students who attended training program: "))
        roll_list = []
        for i in range(n):
            val = int(input("Enter roll number of "+str(i+1)+"/"+str(n)+": "))
            roll_list.append(val)
        return  roll_list

    def linear_search(self,roll_list):
        n = int(input("Enter roll number to be searched: "))
        flag = 1
        for i in range(len(roll_list)):
            if(roll_list[i] == n):
                flag = 0
                print(n,"was present and index is",i)
                break
        if(flag):
            print(n,"was absent in training program!")

    def sentinel_search(self, roll_list):
        n = int(input("Enter roll number to be searched: "))
        length = len(roll_list)
        last = roll_list[length - 1]
        roll_list[length - 1] = n
        i = 0
        while(roll_list[i] != n):
            i += 1
        roll_list[length - 1] = last
        if(i< length - 1 or roll_list[i] == n):
            print(n,"was present and index is",i)
        else:
            print(n, "was absent in training program!")

    def binary_search(self, roll_list):
        n = int(input("Enter roll number to be searched: "))
        length = len(roll_list)
        low = 0
        high = length - 1
        mid = 0
        flag = 1
        while(low<=high):
            mid = (low+high)//2
            if(roll_list[mid]<n):
                low = mid + 1
            elif(roll_list[mid]>n):
                high = mid - 1
            else:
                flag = 0
                print(n,"was present and index is",mid)
                break
        if(flag):
            print(n, "was absent in training program!")

    def fibonacci_search(self, roll_list):
        n = int(input("Enter roll number to be searched: "))
        offset = -1
        length = len(roll_list)
        flag = 1
        f0 = 0
        f1 = 1
        f2 = 1
        while(f2 < length):
            f0 = f1
            f1 = f2
            f2 = f0 + f1
        while(f2 > 1):
            i = min(offset+f0,length-1)
            if(roll_list[i] < n):
                f2 = f1
                f1 = f0
                f0 = f2 - f1
                offset = i
            elif(roll_list[i] > n):
                f2 = f0
                f1 = f1 - f0
                f0 = f2 - f1
            else:
                flag = 0
                print(n, "was present and index is", i)
                break
            if (f1) and (roll_list[length - 1] == n):
                flag = 0
                print(n, "was present and index is", i)
                break
        if (flag):
            print(n, "was absent in training program!")

roll_array = Array()
arr = roll_array.input_array()
sortedarr = sorted(arr)
option = 1
while(option>0 and option<5):
    print("<---- Menu ----> \n1. Linear Search \n2. Sentinel Search \n3. Binary Search \n4. Fibonacci Search")
    option = int(input())
    if(option == 1):
        roll_array.linear_search(arr)
    elif(option == 2):
        roll_array.sentinel_search(arr)
    elif(option == 3):
        roll_array.binary_search(sortedarr)
    elif(option == 4):
        roll_array.fibonacci_search(sortedarr)
    else:
        print("Program ended successfully!")
        exit(1)
