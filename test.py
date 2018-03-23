# class A(object):
#     __a = "12"
#
#
# print(A.__dict__)
# print(A.__dir__(A))


# list1 = []
#
# for i in range(10):
#     list1.append(str(i))
#
# print(list1)
#
# print(','.join(list1))

dict1 = {'aa':12}

a_key = ''
a_value = ''

for key,value in dict1.items():
    a_key = key

    if isinstance(value , int):
        a_value = str(value)
    else:
        pass

print( a)