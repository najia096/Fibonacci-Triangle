#code for no 4
import random

def fiboT(i,j):
  if ((i==0 and j==0) or (i==1 and j==0) or (i==1 and j==1) or (i==2 and j==1)):
    return 1
  elif i>j:
    return fiboT(i-1,j) + fiboT(i-2,j)
  elif i == j:
    return fiboT(i-1, j-1) + fiboT(i-2,j-2)
  return 0

f = open("FibonacciT.txt", "w")
n = random.randint(10,30)
print("Height of the Fibonacchi Triangle is: ", n)

c = input("Do you want to continue? y / n: ")

if(c[0] == "y" or c[0] == "n"):
  while (c[0] == "y"):
        for i in range(n):
          for j in range(i+1):
            f.write((str(fiboT(i,j))) + " ")
          f.write("\n")
        f.close()
        print("A Fibonacci Triangle is created on the file.")
        break
  while( c[0] == "n"):
    print("Goodbye!")
    break
else:
  print("Invalid Response!!")
