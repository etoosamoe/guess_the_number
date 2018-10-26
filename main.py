import random
#Тестовая игра, программа загадывает число от 1 до 10, у пользователя есть три попытки, чтобы отгадать его

number=random.randint(1,10)

print(number) #debug
print("Я хочу сыграть с тобой в игру.\nЯ загадал число от 1 до 10.")

t = 1
while t < 4:
    #print('debug: ', number)
    user_num=input("Попробуй отгадать: ")
    if int(user_num) == int(number):
        print("Ты угадал, это и правда было число ", number, '.')
        break
    t=t+1
    print('Нет же, это другое число. Давай еще раз. У тебя осталось ',4-t,' попыток.')
else:
    print('Ну, ты не угадал. Это было число', number,'.')
