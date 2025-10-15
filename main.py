import os


print("Here is the listdir->",os.listdir())

print("Here is current working directory->",os.getcwd())

print("pritining *")

n=int(input("enter the rnage"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,j)
