# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 

#     1+2*3 => 7; 

#     (1+2)*3 => 9;

print('Введите строку для вычисления. Можно использовать операции +,-,/,*')
primer=input()
print(primer)
res=[]
i=0

for i in range(len(primer)):
    try:
        if int(primer[i]):

            res.append(int(primer[i]))
    except:
        res.append(primer[i])

operat={
    '+':lambda x,y:x+y,
    '*':lambda x,y:x*y,
    '-':lambda x,y:x-y,
    '/':lambda x,y:x/y
}
def calc(op,x,y):
    return operat[op](x,y)
def calculation(x,y,res):   
    i=0
    while i<len(res):
        if res[i]==x or res[i]==y:
            result=calc(res[i],res[i-1],res[i+1])
            res.insert(i+2,result)
            res.pop(i+1)
            res.pop(i)
            res.pop(i-1)
            i-=2
        i+=1

calculation('*','/',res)
calculation('+','-',res)
        
print(res)