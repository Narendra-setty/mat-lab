#1.print hello world
print("Hello World")
#2.sum of two numbers
a=int(input("enter a first number: "))
b=int(input("enter a second number: "))
sum=print("sum of two numbers is" ,a+b)
#3.division of two real numbers
def inf(a):
  try:
    if "." in a:
      return float(a)
    else:
      return int(a)
  except ValueError:
    return a
a=input("Num 1")
b=input("Num 2")
a=inf(a)
b=inf(b)
if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
    print("TRUE")
else:
    print("UR INPUTS AREN'T REAL NUMBERS")
#4.dot product of two vectors
n=int(input("Enter elements in a list"))
list=[]
for i in range(n):
	a=int(input("Enter element"))
	list.append(a)
print("LIST",list)
m=int(input("Enter elements in a list"))
list1=[]
for i in range(m):
	b=int(input("Enter element"))
	list1.append(b)
print("LIST1",list1)
#dot product
dot=0
for i,j in zip(list,list1):
	dot=dot+i*j
print("DOT PRODUCT",dot)
#5.determinant of matrix
def determinant(matrix):
	if len(matrix)!=2 or len(matrix[1])!=2:
		raise ValueError("input matrix 2*2 matrix")
	return matrix[0][0]*matrix[1][1]-matrix[0][1]
matrix1=[[3,4],[3,4]]
result=determinant(matrix1)
print("Determinant",result)
