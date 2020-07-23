character = input('>>enter a character: ')
num = int(input('>>enter a positive number (> 5):'))

for i in range(1, num + 1):
  text = ' '
  for j in range(i):
    text += character

  print(text)