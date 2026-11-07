a,b,c=map(int,input("Enter the side of triangle: ").split())

if a<=0 or b<=0 or c<=0:
    print("Invalid triangle")
elif a+b<=c or a+c<=b or b+c<=a:
    print("Invalid triangle")
elif a==b==c:
    print("Equilateral triangle ")
elif a==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")