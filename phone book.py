book = {}
while True:
 user=input()
 if user=='add':
  name=input('name')
  tele=input('tele')
  book[name]=tele
 if user=='del':
  name=input('имя')
  if name in book:
   del book[name]
   print('спешно удаленно')
  else:
   print('ошибка')

 if user=='print':
  print(book)
 if user=='poisk':
  name=input('name')
  if  name in book:
   print(book[name])
  else:
   print('ошибка')

# TODO: Заметки
## Date: 25.05.2024
