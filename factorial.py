# this function is a example for recusion in python

n=int(input("Give value: "))
def myfunction(n):
    if n==0 or n==1:
        return 1
    else:
        return n * myfunction(n-1)
print(myfunction(n))