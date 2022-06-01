ss='abc' #1
print(ss[::-1])
ss2='Hel"lo Wor"ld!' #2
begin=0
end=0
flag=0
for i in range(0,len(ss2),1):
    if ss2[i]=='\"':
        if flag==0:
            begin=i
            flag=1
        else:
            end=i
print(ss2[begin+1:end])
s='9' #3
s=int(s)
s*=2
print(s)
ss4='15263654 365467474'  #4
space=ss4.find(" ")
ss4_mod=ss4[space+1:]+" "+ss4[:space]
print(ss4_mod)
ss5="nikita.garmashov@mail.ru" #5
sobaka=ss5.find("@")
print(ss5[:sobaka])
ss6="+7 (812) 134-12-324" #6
ss6_mod=''
for i in range(0,len(ss6),1):
    if ss6[i]!='-' and ss6[i]!=' ' and ss6[i]!='(' and ss6[i]!=')':
        ss6_mod+=ss6[i]
print(ss6_mod)
ss7="а роза упала на лапу Азора" #7
ss7_mod=''
for i in range(0,len(ss7),1):
    if ss7[i]!=' ':
        ss7_mod+=ss7[i]
ss7_mod=ss7_mod.lower()
if ss7_mod[::-1]==ss7_mod:
    print('Полином')
else:
    print('Не полином')




f_in=open('text.txt','r')
animal=[]
animal_dif=[]
for line in f_in:
    k=line.find(' ')
    new_animal=line[k+1:]
    k=new_animal.find(' ')
    new_animal_2=new_animal[k+1:]
    new_animal=new_animal[:k]
    k=new_animal_2.find(' ')
    gender=new_animal_2[:k]
    animal.append([new_animal,gender])
animal.sort()
for i in range(len(animal)):
    dif=animal
f_in.close()
