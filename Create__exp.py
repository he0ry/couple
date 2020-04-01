from fractions import Fraction
import random
# 生成表达式
def get__exp(subject__num,area):
    expression = ''
    bracket = 0
    operator_num = random.randint(1, 3)  # 生成运算符数
    if operator_num != 1:  #操作数大于1
        bracket = random.choice([1,2])  #随机选择是否插入括号
        if bracket == 1:
            #在第几个数插入括号
            breaket__num1 = random.randint(0,operator_num - 1)
            if breaket__num1 == 0:
                breaket__num2 = random.randint(breaket__num1 + 1,operator_num - 1)
            else:
                breaket__num2 = random.randint(breaket__num1 + 1,operator_num)
    for i in range(2*operator_num+1):
        if i % 2 == 0:
            if random.randint(1,4) == 1:
                num = str(get_fraction(area))  #生成分数
            else:
                num = str(get__int(area))  #生成整数
            if bracket == 1:  
                if i == breaket__num1 * 2:  #插入左括号
                    num = '( ' + num 
                elif i == breaket__num2 * 2:
                    num = num + ' )'   #插入右括号
                    bracket = 0
            expression += ' ' + num   #表达式加入数或括号
        else:
            op = str(random.choice(['+','-','×','÷']))  # 随机选择运算符 (+ - × /)
            expression += ' ' + op   #表达式加入运算符
    return expression 

# 生成分数
def get_fraction(area):   
    while True:
        mum = random.randint(1, area)
        son = random.randint(1, mum*area)
        n = Fraction(son,mum)
        if '/' in str(n):
            if n > 1:
                return turn_fracrtion(n)
            return n

# 生成整数
def get__int(area):
    return random.randint(1,area)

 # 假分数转真分数
def turn_fracrtion(results): 
    return str(int(results)) + "'" + str(results - int(results))