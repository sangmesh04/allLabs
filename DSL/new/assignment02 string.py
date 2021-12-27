# Write a Python program to compute following operations on String:
# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check whether given string is palindrome or not
# d) To display index of first appearance of the substring
# e) To count the occurrences of each word in a given string

class string:
    def input_string(self):
        sentence = input("Enter any sentence: ")
        return  sentence


    def string_list(self, sentence):
        a = 0
        str_list = []
        for i in range(len(sentence)):
            if(sentence[i] == ' '):
                str_list.append(sentence[a:i])
                a = i+1
        str_list.append(sentence[a:len(sentence)])
        return  str_list

    def longest_string(self, string_list):
        long = ''
        for i in string_list:
            if(len(long) < len(i)):
                long = i
        return  long

    def frequencyOfChar(self, sentence):
        char = input("Enter any character to check it's frequency: ")
        f = 0
        for i in sentence:
            if(i == char):
                f += 1
        print("Frequency of '",char,"' in sentence is: ",f)

    def palindrome(self):
        string = input("Enter any string to check it's palindrome property: ")
        if(string == string[::-1]):
            print("The string is palindrome!")
        else:
            print("The string is not a palindrome")

    def index_substring(self,str_list):
        substring = input("Enter substring to be searched: ")
        index = 1
        flag = 1
        for i in str_list:
            if(i == substring):
                flag = 0
                print("Substring is at",index-1)
                return 0
            index += len(i) + 1
        if(flag):
            print("Substring is not present!")

    def removeDuplicate(self,str_list):
        rmv = []
        for i in str_list:
            if(i not in rmv):
                rmv.append(i)
        return  rmv

    def frequencyOfSubstring(self, str_list):
        strL = string()
        strL = strL.removeDuplicate(str_list)
        freq_list = []
        for i in strL:
            a = 0
            for j in str_list:
                if(i == j):
                    a += 1
            freq_list.append(str(i)+" : "+str(a))
        return  freq_list


mainSentence = string()
sentences = mainSentence.input_string()
string_list = mainSentence.string_list(sentences)

option = 1
while(option> 0 and option<6):
    print("<---- Menu ----> \n1. To display word with the longest length \n2. To determines the frequency of occurrence of particular character in the string \n3. To check whether given string is palindrome or not \n4. To display index of first appearance of the substring \n5. To count the occurrences of each word in a given string")
    option = int(input())
    if(option == 1):
        long = mainSentence.longest_string(string_list)
        print("Longest substring in sentence is: ", long)
    elif(option == 2):
        mainSentence.frequencyOfChar(sentences)
    elif(option == 3):
        mainSentence.palindrome()
    elif(option == 4):
        mainSentence.index_substring(string_list)
    elif(option == 5):
        allSubstring = mainSentence.frequencyOfSubstring(string_list)
        print(allSubstring)
    else:
        print("Program ended successfully!")
        exit(1)
