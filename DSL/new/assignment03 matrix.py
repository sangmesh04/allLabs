# Write a Python program to compute following computation on matrix:
# a) Addition of two matrices
# b) Subtraction of two matrices
# c) Multiplication of two matrices
# d) Transpose of a matrix

class Matrix:

    def list_matrix(self,lis):
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                print(lis[i][j],end=" ")
            print()

    def input_matrix(self):
        row = int(input("Enter number of rows: "))
        col = int(input("Enter number of col: "))
        matrix = []
        for i in range(row):
            row = []
            for j in range(col):
                val = int(input("matrix["+str(i+1)+","+str(j+1)+"]: "))
                row.append(val)
            matrix.append(row)
        return  matrix

    def add_matrix(self,mat1,mat2):
        r1 = len(mat1)
        c1 = len(mat1[0])
        r2 = len(mat2)
        c2 = len(mat2[0])
        add = []
        if(r1 == r2 and c1 == c2):
            print("Addition of matrices is: ")
            for i in range(r1):
                row = []
                for j in range(c1):
                    val = mat1[i][j] + mat2[i][j]
                    row.append(val)
                add.append(row)
            a = Matrix()
            a.list_matrix(add)
        else:
            print("Addition is not possible!")

    def subs_matrix(self,mat1,mat2):
        r1 = len(mat1)
        c1 = len(mat1[0])
        r2 = len(mat2)
        c2 = len(mat2[0])
        subs = []
        if (r1 == r2 and c1 == c2):
            print("Substration of matrices is: ")
            for i in range(r1):
                row = []
                for j in range(c1):
                    val = mat1[i][j]  - mat2[i][j]
                    row.append(val)
                subs.append(row)
            a = Matrix()
            a.list_matrix(subs)
        else:
            print("Subtraction is not possible!")

    def multi_matrix(self,mat1,mat2):
        r1 = len(mat1)
        c1 = len(mat1[0])
        r2 = len(mat2)
        c2 = len(mat2[0])
        multi = []
        if(c1 == r2):
            print("Multiplication of matrices is: ")
            for i in range(r1):
                row = []
                for j in range(c2):
                    val = 0
                    for k in range(r2):
                        val += mat1[i][k] * mat2[k][j]
                    row.append(val)
                multi.append(row)
            a = Matrix()
            a.list_matrix(multi)
        else:
            print("Multiplication is not possible!")

    def transpose_matrix(self,mat):
        r = len(mat)
        c = len(mat[0])
        trans = []
        for i in range(c):
            row = []
            for j in range(r):
                val = mat[j][i]
                row.append(val)
            trans.append(row)
        a = Matrix()
        a.list_matrix(trans)

matrix = Matrix()
mat1 = matrix.input_matrix()
mat2 = matrix.input_matrix()
option = 1
while(option>0 and option<5):
    print("<---- Menu ----> \n1. Addition of two matrices \n2. Subtraction of two matrices \n3. Multiplication of two matrices \n4. Transpose of a matrix")
    option = int(input())
    if(option == 1):
        matrix.add_matrix(mat1,mat2)
    elif(option == 2):
        matrix.subs_matrix(mat1,mat2)
    elif(option == 3):
        matrix.multi_matrix(mat1,mat2)
    elif(option == 4):
        print("Transpose of first matrix: ")
        matrix.transpose_matrix(mat1)
        print("Transpose of second matrix: ")
        matrix.transpose_matrix(mat2)
    else:
        print("Program ended successfully!")
        exit(1)