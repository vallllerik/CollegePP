mode = input()
while True:
  i = 3
  if mode == "game":
    while i > 0:
      num = int(input())
      if num == 5:
        print("Вы выиграли билет на концерт!")
        break
      else:
        print("Ответ неверен! Попробуй ещё раз!")
        i -= 1
    else:
      print("Вы исчерпали количество попыток!")
  elif mode == "off":
    break
