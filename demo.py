#for i in range(24,57,2):
 #   print(i)

start=int(input("enter the starting number:- "))
end=int(input("enter the last no:- "))
for no in range(start,end+1):
    if (no%2==0):
        print(no)