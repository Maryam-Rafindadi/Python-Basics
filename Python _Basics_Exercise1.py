#format method
name = 'Maryam Rafindadi'
print('Hello, {0}'.format(name))

#grade of student
print("student scores")
mark = int(input())
score = mark
if score >= 70 and score <=100:
    print ("Your Grade is A") 
elif score >= 60 and score <= 69:
    print("Your Grade is B")  
elif score >= 50 and score <= 59:
    print ("Your Grade is C") 
elif score >= 40 and score <= 49:
    print ("Your Grade is D")  
else:
    print ("Your Grade is F") 


#All even numbers between 1 and 100 using: while and for loop
number = 1
while (number <= 100):
    if (number % 2) == 0:
        print (number)
        number + 1

#function argument
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Maryam", "Rafindadi")        


#program to add two matrix using nested loop
A = [[4,5],
    [6,7]]
B = [[1,2],
    [3,4]] 
result = [[0,0],
         [0,0]]   
for i in range (len(A)):
    for j in range (len(B)):
        result[i][j]=A[i][j] + B[i][j]  
for r in result:
    print(r)
                   

               

    

   
