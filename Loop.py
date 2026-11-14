# Nested Loop
# row=int(input("Enter number of rows:"))
# column=int(input("Enter the number of columns:"))
# i=1
# while i<=row: 
#     j=1 
#     while j<=column:
#         print(j,end='')
#         j+=1
#     i+=1
#     print()

# Loop in Range
# for x in range(50,100,10):
#     print(x,end=' ')

# a=100
# b=40
# c=-10
# for x in range(a,b,c):
#     print(x,end=' ')

# a=int(input("Enter the starting Number: "))
# b=int(input("Enter the Stop Number: "))
# c=int(input("Enter the number to Step: "))
# for x in range(a,b,c):
#     print(x,end=' ')

# row=int(input("Enter the row :"))
# column=int(input("Enter the column :"))

# for x in range(row):
#     for y in range(1,column+1):
#         print(y,end='')
#     print()

# for x in ["Yellow","Green"]:
#     print("-------------------")
#     for y in ["cat","dog"]:
#         print(x,y)
#     print()

# row=int(input("Entr the Row: "))
# column=int(input("Enter the column:"))
# pattern=input("Enter the pattern :")
# a=1
# while a<=row:
#     b=1
#     while b<=column:
#         print(pattern,end="")
#         b+=1
#     a+=1
#     print()

# row=int(input("Entr the Row: "))
# column=int(input("Enter the column:"))
# pattern=input("Enter the pattern :")
# a=1
# while a<=row:
#     b=1
#     while b<=column:
#         print(pattern,end="")
#         b+=1
#     a+=1
#     print()

# for x in range(5):
#     for y in range(0,x+1):
#         print("#",end=" ")
#     print()

# Correct Order
a=1
while a<=8:
    b=1
    while b<=a-1:        
        print("#",end=" ") 
        b=b+1       
    a+=1
    print("")
print("\n")

# Reverse Order
a=1
while a<=5:
    b=a+1
    while b<=5:        
        print("#",end=" ") 
        b=b+1       
    a+=1
    print()

