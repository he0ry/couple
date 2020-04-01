import time
import inout

while True:
    choicefuc = input('请选择功能\n1.生成题目\n2.核对答案\n3.退出\n')
    if choicefuc == '1':
        subject__num = int(input('请输入你想生成的题目数\n'))
        area = int(input('生成数的范围\n'))
        inout.outp(subject__num,area)
    if choicefuc == '2':
        user_answerspath = input('请输入你要核对的答案的路径\n')
        Answerspath = input('请输入你的答案的路径\n')
        inout.inp(user_answerspath,Answerspath)
    elif choicefuc== '3':
        break    
