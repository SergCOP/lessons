import random
a = random.randint(0, 100)
b = 0
for i in range (1, 9):
    print(f'Попытка № {i}')
    b = int(input())
    if a == b:
        print ('Вы победили!')
        break
    elif a <= b:
        print ('Не правильно! Загаданное число меньше!') 
    elif a >= b:
        print ('Не правильно! Загаданное число больше!')    
else:    
    print ('Вы проиграли!')
    

    
