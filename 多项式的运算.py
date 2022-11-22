# 我们用列表表示多项式的系数 列表从多项式低次项开始
# 例如 x*x + 5x + 3 可表示为 [3, 5, 1]
# 加减法可以直接通过列表中元素加减实现
# 乘法借助加法实现
# 多项式的除法暂时没有想到好的办法处理

# 定义一个处理两个列表的函数
def add_list(L1, L2):  # 多项式加法，同次项系数相加
    R = []
    if len(L1) > len(L2):  # 默认L2比较长
        L1, L2 = L2, L1
    i = 0
    while i < len(L1):
        R.append(L1[i] + L2[i])  # 从低次项开始对应相加
        i += 1
    R = R + L2[len(L1):len(L2)]  # 较长的多项式高次项直接复制
    return R

class Poly:

    def __init__(self, alsit: list):
        self.alist = alsit

    def __add__(self, other):
        shortlist = self.alist
        longlist = other.alist
        if len(shortlist) > len(longlist):
            shortlist, longlist = longlist, shortlist
        for i in range(len(shortlist)):
            longlist[i] += shortlist[i]
        return longlist

    def __sub__(self, other):
        for i in range(len(other.alist)):
            other.alist[i] = -other.alist[i]
        return self + other

    def __mul__(self, other):
        # 创建一个临时列表
        result = []
        for element in range(len(self.alist)):
            temp = []
            for i in other.alist:
                temp.append(self.alist[element] * i)
            for j in range(element):
                temp.insert(0, 0)
            result = add_list(result, temp)
        return result


if __name__ == '__main__':
    a = Poly([1, 2, 3])
    b = Poly([1, 2])
    print(a+b)


