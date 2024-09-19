if __name__
def BMI():
     Height= eval(input("输入你的身高"+"（m）"))
     Weight=float(input("输入你的体重"+"(kg)"))
     BMI=Weight/(Height**2)
     print(BMI)
BMI()
