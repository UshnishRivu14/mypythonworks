#lambda function
fun = lambda x: x+10

print(fun(1))

#double parameters
avg = lambda x, y: (x+y)/2

print("The average is : " + str(avg(5,7)))


f = lambda x,y: print(f"{x} * {y} = {int(x)*int(y)}")
f(6,7)