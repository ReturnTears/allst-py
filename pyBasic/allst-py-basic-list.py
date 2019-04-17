#  _author: June
# _date: 2018/7/23

# Day5:list
names = 'yangyang xiaohu June'
# 定义列表a
a = ['Yangyang', 'xioahu', 'June', 'Seven', 'hello', 'ok']
# 增删改查
# 增 切片：[x:y]下标可以取范围值，含首不含尾 / [x:]从x取到最后 / [x:-1]从x取到倒数第二个值 /
#        [x:-1:1]从x一个一个取到倒数第二个值，1表示步长
#        [x::2]从左到右隔一个下标去取值
#        [x::-1]从右到左依次取值：x表示索引，::表示取到最后，-表示从右往左，数值表示步长
#        [x,y]索引可以为负值，-1表示列表List最后一个值
# print(a[-1::])

# 添加 append(默认插入到最后一个位置) insert(将数据插入到指定的位置)
# a.append("Return")
# print(a)
# a.insert(1, "Python")
# print(a)

# 修改
# a[2]='javascript'
# a[1:3]={'huseven','JavaScript'}
# print(a)

# 删除 remove pop del(del什么都可删除)
# a.remove('ok')
# b=a.pop(0)
# del a[0]
# del a
print(a)
