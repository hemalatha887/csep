def CompoundInterest (p,r,t):
	if t==0:
		return p
	else:
		ci=p*(pow((1+r/100),t))
		return ci
p=float(input("enter the principal amount"))
r=float(input("enter the rate of interest"))
t=float(input("enter the number of years"))
ci=CompoundInterest(p,r,t)
print("compound interest is {0:5.2f}".format(ci))
