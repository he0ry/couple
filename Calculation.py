from fractions import Fraction

def get__result(exp):
    return calc_houzhui(change_houzhui(exp))

# 转为后缀表达式.运算表达式元素之间用空格隔开:
def change_houzhui(s):
    result = []  # 结果列表
    stack = []  # 栈
    s_lt = s.split(' ')
    for item in s_lt:
        if item.isnumeric() or '/' in item or '\'' in item:  # 如果当前字符为数字那么直接放入结果列表
            result.append(item)
        else:  # 如果当前字符为一切其他操作符
            if len(stack) == 0:  # 如果栈空，直接入栈
                stack.append(item)
            elif item in '×÷(':  # 如果当前字符为×÷（，直接入栈
                stack.append(item)
            elif item == ')':  # 如果右括号则全部弹出（碰到左括号停止）
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()
            # 如果当前字符为加减且栈顶为乘除，则开始弹出
            elif item in '+-' and stack[-1] in '×÷':
                if stack.count('(') == 0:  # 如果没有左括号，弹出所有
                    while stack:
                        result.append(stack.pop())
                else:  # 如果有左括号，弹到左括号为止
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)  # 弹出操作完成后将‘+-’入栈
            else:
                stack.append(item)  # 其余情况直接入栈（如当前字符为+，栈顶为+-）
    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while stack:
        result.append(stack.pop())
    # 返回字符串
    return result

#后缀表达式进行计算
def calc_houzhui(follow):
    num = []
    base_opt = ['+', '-', '×', '÷']
    for j in follow:
        if j.isnumeric():
            num.append(int(j))
        elif '/' in j or '\'' in j:
            num.append(strToFrac(j))
        if j in base_opt:
            num2 = num.pop()
            num1 = num.pop()
            if j == "+":
                num.append(num1 + num2)
            elif j == "-":
                num.append(num1 - num2)
                if num[-1] < 0:
                    return -1
            elif j == "×":
                num.append(num1 * num2)
            else:  
                if num2 == 0:
                    return -1 
                else:
                    num.append(Fraction(num1,num2))
    if num[0] > 1 and '/' in str(num[0]):
        return turn_fracrtion(num[0])
    return num[0]

#字符串变为分数
def strToFrac(string):
    #如果是带分数
    if '\'' in string:
        withFrac = string.split('\'')
        INT = int(withFrac[0])  #整数部分
        son = int((withFrac[1].split('/'))[0])  #分子部分
        mum =int((withFrac[1].split('/'))[1])  #分母部分
        return Fraction((INT*mum+son),mum)
    #如果是普通真分数
    elif '/' in string:
        son = int((string.split('/'))[0])
        mum = int((string.split('/'))[1])
        return Fraction(son,mum)
    #如果是整数
    else :
        return Fraction(int(string),1) 

 # 假分数转真分数
def turn_fracrtion(results): 
    return str(int(results)) + "'" + str(results - int(results))