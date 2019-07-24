ten_things = 'Apple Oranges Crows Telephone Light Sugar'

print('잠깐 아직 목록에 10개가 들어 있지 않으나 함 번 고쳐봅시다')
stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee',
              'Corn', 'Banana', 'Girl','Boy']
while len(stuff) != 10 :
    next_one = more_stuff.pop()
    print('Adding : ', next_one)
    stuff.append(next_one)
    '-'.join(stuff)
    print(f'이제 {len(stuff)}항목이 있습니다')
print('한번 볼까용?', stuff)

'-'.join(stuff)