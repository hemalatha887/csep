def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)
num=int(input("Enter the number: "))
result=fact(num)
print("factorial of %d is %d"%(num,result))
