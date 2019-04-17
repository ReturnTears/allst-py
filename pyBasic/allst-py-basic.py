"""
Created on 2018年7月1日
@author: June
"""
print("打印1~10的偶数")
num = 1
while (num < 10):
    num += 1
    if num % 2 == 0:
        print(num)
'''
猜数字
'''
age = 18
flag = False
while not flag:
    inp = int(input("age is : "))
    if inp == age:
        print("猜对了")
        break
    elif inp > age:
        print("猜大了")
    else:
        print("猜小了")
print("end")
