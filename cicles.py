i = 5
while i < 15:
    print(i)
    i = i + 2

for i in 'hello world':
    print(i * 2, end='')

for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')

for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')

for i in 'hello world':
    if i == 'a':
        break
else:
    print('Буквы a в строке нет')