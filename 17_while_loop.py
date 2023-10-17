for i in range(10):
    print(i)

# for ciklusváltozó szekvencia(feltétel, kezdőérték, léptetés):
#     ciklusmag

i = 0
while i < 10:
    print(i)
    i += 1

my_list = [1, 2, 3, 4, 5]

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

num = 34
counter = 0
while True:
    tipp = input('Gondoltam egy számra 1 és 100 között, add meg a tipped: ')
    counter += 1
    # "error handling"
    if tipp.isdigit():
        tipp = int(tipp)
    else:
        print('1 és 100 közötti tippet adj meg!')
        continue

    if tipp > num:
        print('Kissebb számra gondoltam')
    elif tipp < num:
        print('Nagyobb számra gondoltam')
    elif tipp == num:
        print(f'Eltaláltad {counter} lépésből!')
        break

number = 5
i = 2
while i <= number // 2:
    if number % i == 0:
        print(f'{number} in not prime')
        break
    i += 1
else:
    print(f'{number} is prime')
