sides=[x+1 for x in range(50)]
sides.sort(reverse=True)
#print(sides)
s=0
p=0
side1=0
side2=0
side3=0
#print(list(range(len(sides)-1)))
for x in range(len(sides)-1):
    if sides[x+1]+sides[x+2]>sides[x]:
        p = (sides[x]+sides[x+1]+sides[x+3])/2
        print(p
        s = (p*(p-sides[x])*(p-sides[x+1])*(p-sides[x+2]))**0.5
        (side1,side2,side3)=(sides[x],sides[x+1],sides[x+2])
        break
print(s,side1,side2,side3)






