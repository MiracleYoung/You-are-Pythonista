# encoding: utf-8
n = int(input("请输入项数："))
list=[]
for a in range(1,n+1):
    an = int(1/5**0.5*(((1+5**0.5)/2)**a-((1-5**0.5)/2)**a))
    list.append(an)
print(list)