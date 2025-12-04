#задание 1
my_dict = {1:'0101101', 2:'101110', 3:'1A14C', 4:'1100100',
5:'101010'}
print(my_dict)
del my_dict[3]
print(my_dict)
my_dict[10] = '0100101'
print(my_dict)
#задание 2
sl = {'</>':13, 'script':1, '__init__':10, 'self':5,
'number_9':6, '#comment':100}
print(sl)
key = (input("введите ключ:"))
element = (input("введите элемент:"))
sl[key] = element
print(sl)
#задание 3
my_dict = {}
while len(my_dict) <3:
    print (f"нужно три ключа, словарь: {my_dict}")
    while True:
        try:
            key = int(input("введите ключ:"))
            break
        except ValueError:
            print ("ключ должен быть числом")
    value = input('введите значение')
    my_dict[key] = value
print(my_dict)
#задание 4
all_d = {1:15, 4:80, 44:0, 256:15, 100:70, 101:70, 20:44, 3:9}
del_key = [1, 101, 3]
for i in del_key: all_d.pop(i)
print (all_d)
