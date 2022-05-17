def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.8
    y=x1*w1+x2*w2
    if y<=theta:
        return 0
    elif y>theta:
        return 1

print(AND(1,1))
print(AND(1,0))
print(AND(0,1))
print(AND(0,0))