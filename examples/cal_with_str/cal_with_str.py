import operator

# دیکشنری برای اوپریتور ها

ops : dict = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}


def cal_str(*args):
    return ops[args[1]](int(args[2]),int(args[0])) 



str_things : str = input("Enter cal things : ")

new_str = ""

# جلو گیری از خطای برنامه  
for autospace in str_things:
    autospace = autospace + " "
    new_str = new_str + autospace

str_things = new_str

# مرحله نهایی
print(cal_str(*(str_things.split())))