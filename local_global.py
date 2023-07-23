x = 5
y = 7
def hello():
    global x, y
    print(x)
    print(y)

hello()
print(x)
print(y)    