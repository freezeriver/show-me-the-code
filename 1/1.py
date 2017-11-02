# encoding = utf-8
import string,random

field = string.ascii_letters+string.digits #指定字符范围为数字+字母

# 随机生成4个由数字或字母组成的字符串
def getrandom():
    return "".join(random.sample(field,4))


# 将4组长度为4的字符串用‘-’拼接，即生成一组激活码
def concatenate():
    return '-'.join([getrandom() for i in range(4)])

#生成指定数量的激活码
def generate(n):
    return [concatenate() for i in range(n)]


if __name__ == '__main__':
    print(generate(200))