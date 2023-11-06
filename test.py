
aaa = 10
bbb = 20

def change(arg1, arg2):
    arg1 += 2*arg1
    arg2 = 50
    return arg1, arg2

aaa, bbb = change(aaa, bbb)

print(aaa, bbb)