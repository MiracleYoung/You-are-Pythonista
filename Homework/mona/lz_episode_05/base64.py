import base64
import math

b64 = {
    'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,
    'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'a':26,'b':27,
    'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,
    'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51,'0':52,'1':53,'2':54,'3':55,
    '4':56,'5':57,'6':58,'7':59,'8':60,'9':61,'+':62,'/':63
}

b = []  # 存放解码后的二进制数


def transform(num):
    l = [5, 4, 3, 2, 1, 0]
    for x in range(6):
        if num >= pow(2, l[x]):
            b.append(1)
            num -= pow(2, l[x])
        else:
            b.append(0)


def printChar(lst):
    l = [7, 6, 5, 4, 3, 2, 1, 0]
    num_Ascall = 0
    for x in range(8):
        if lst[x] == 1:
            num_Ascall += pow(2, l[x])

    ch = chr(num_Ascall)
    print(ch, end='')

ori_s = 'Man'
print('The original string is:{}'.format(ori_s))
encodestr = base64.b64encode(ori_s.encode())
print('The base64 string is:{}'.format(encodestr))
s = encodestr.decode()

for i in range(len(s)):
    num = 0
    if s[i] is not '=':
        num = b64[s[i]]
    transform(num)

lst = []  # 存放八位二进制
lst.append(b[0])
print('The result of the decoding is:',end = '')

for x in range(1, len(b)):  # 每8位输出一个字符
    if x % 8 == 0:
        printChar(lst)
        lst.clear()
    lst.append(b[x])

printChar(lst)
