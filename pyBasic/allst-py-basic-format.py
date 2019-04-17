""" day five demo """
""" # _author:June"""
print("如果以后需要再安装pycharm")

''' 字符格式化输出 '''
name = input("name  : ")
age = int(input("age : "))
job = input("job : ")
salary = input("salary : ")
# 判断是否长得像数字
if salary.isdigit():
    salary = int(salary)

msg = '''
------------ info of %s----
name : %s
age : %d
job : %s
salary : %f
------------end--------------
''' % (name, name, age, job, salary)

print(msg)
