#日志统计脚本，手动归档版本
import os
import string
import re
from datatime import datetime
import time

def timer (n):
    while True:
        word_count(dir)
        print('******************\n')
        time.sleep(n)
# 统计英文字符出现的字数
def word_count(dir):
    #source目录下
    if dir=='s':
        #str=input('FileName:')
        #filename = str+'.LOG'
        filename='x.LOG'
        f = open("E:/ttttt/source/"+filename, 'rb')
        
    #result目录下
    if dir=='r':
        #str=input('FileName:')
        #filename = str+'.LOG'
        filename='y.LOG'
        f = open("E:/ttttt/result/"+filename, 'rb')
        
    s = f.read()
    s = s.decode('utf-8')

    #匹配函数名
    reObj = re.compile('\b?[g][l](\w+)\b?')
    words = reObj.findall(s)
    wordDict = dict()
    acount=0

    for word in words:
        # 如果字典中存在则数量加1，不存在等于1
        if word.lower() in wordDict:
            # 转化为小写
            wordDict[word.lower()] += 1
        else:
            wordDict[word.lower()] = 1
            acount += 1
            
    f.close()

    # 将字典转换为列表以后按照函数名排序，返回一个列表
    wordDict = sorted(wordDict.items(), key=lambda x: x[0], reverse=False)
    #des= input('DestinationName:')
    destination = 'result.LOG'
    
    # 输出单词和数量
    f1=open("E:/ttttt/des/"+destination,"w")
    for key, value in wordDict:
        f1.write('%s: %s\n' % (key, value))
    f1.close()
    
    #程序中直接打印
    #for key, value in wordDict:
       #print('%s: %s' % (key, value))
        #print('%.2f percent\n' % (acount/10))

if __name__ == '__main__':
    os.chdir('E:/ttttt')
    dir=input('Directory(s):')
    timer(5)
