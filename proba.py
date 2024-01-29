# def test2(x, y, z):
#     return (x*2+y*2+z*2)
#
# res = test2(2,3,4)
# print('Результат:', res)

# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')
# name = input()
# # print('Java')
# # print('Ruby')
# # print('Scala')
# print('Python', end='+')  # print('C++')
# # print('GO')
# print('C#', end='=')  # print('C')
# print('awesome')
# # finish

num = int(input())
d3 = num % 10
d2 = (num // 10) % 10
d1 = num // 100
print(d1, d2, d3, sep='')
print(d1, d3, d2, sep='')
print(d2, d1, d3, sep='')
print(d2, d3, d1, sep='')
print(d3, d1, d2, sep='')
print(d3, d2, d1, sep='')
