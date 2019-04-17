import random

print("Hello June, Please Start Python!")
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != k) and (i != j) and (j != k):
                print(i, j, k)
print("------------完美的分割线-----------------")

print("-----[0,1)内的随机数-----")
print("random 1 : ", random.random())
print("random 2 : ", random.random())

print("-----生成指定范围内浮点数-----")
print("random 1 : ", random.uniform(1, 10))
print("random 2 : ", random.uniform(11, 2))

print("-----生成指定范围内浮点数a<=b-----")
print("random 1 : ", random.randint(1, 10))

print("-----在递增集合中获取一个随机数-----")
print("random 2 : ", random.randrange(10, 50, 5))

print("-----在递增集合中获取一个随机数-----")
# print("random 2 : ", random.choice(10, 50, 5))
