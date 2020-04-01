import os
import Calculation
import Create__exp
import datetime

#获取桌面路径
def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")

#生成问题和答案
def outp(subject__num,area):
    #生成的时间
    now = datetime.datetime.now()  
    file__time = now.time().__format__('%H.%M.%S')
    expfile = r''+get_desk_p() + r'\exercise' + file__time + '.txt'  #问题路径
    ansfile = r''+get_desk_p() + r'\answer' + file__time + '.txt'   #答案路径
    user_ansfile = r''+get_desk_p()+ r'\useranswer' + file__time + '.txt'  #用户答案路径
    with open(r''+expfile,'w') as f1, \
        open(r''+ansfile,'w') as f2:
        a = 0
        while(a < subject__num):
            expression = Create__exp.get__exp(subject__num,area)  #生成表达式
            result = Calculation.get__result(expression)  #计算答案
            if result == -1:
                continue
            f1.write(str(a+1) + '.' + expression + ' = ' + '\n')  #写入问题
            f2.write(str(a+1) + '.' + str(result) + '\n')   #写入答案
            a += 1 
    f = open(r''+ user_ansfile,'w')
    f.close()
    print('你的题目已生成\n在桌面' + r'\exercise' + file__time + '.txt')
    print('你的答案已生成\n在桌面' + r'\answer' + file__time + '.txt')
    print('请到桌面' + r'\useranswer' + file__time + '.txt' + '答题')

# 核对答案
def inp(user_answerspath,Answerspath):
    right__num = wrong__num = 0  
    right__sign = []
    wrong__sign = []
    tag = 1  #记录题号变量
    #核对答案的时间
    now = datetime.datetime.now() 
    file__time = now.time().__format__('%H.%M.%S')
    gradepath = r''+get_desk_p() + r'\grade' + file__time + '.txt'  #得分情况路径
    with open(r''+ user_answerspath,'r') as f1,\
        open(r''+ Answerspath,'r') as f2:
        for line1,line2 in zip(f1.readlines(),f2.readlines()):
            if line1.split() == line2.split():
                right__num += 1
                right__sign.append(tag)
            else:
                wrong__num += 1
                wrong__sign.append(tag)
            tag += 1
    #写入得分情况
    with open(r''+gradepath,'w') as f:
        f.write('正确数目' + str(right__num))
        f.write(str(right__sign))
        f.write('\n错误数目' + str(wrong__num))
        f.write(str(wrong__sign))
    print('你的得分情况已经放到桌面' + r'\grade' + file__time + '.txt')




