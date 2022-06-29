import math
p,r,t=map(float,input().split())
ci=p*1.0*math.pow((1+r/100),t)
print("{:.2f}".format(ci))