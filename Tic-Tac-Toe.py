player1 = input('Please write the name of the first player(X): ')
player2 = input('Please write the name of the second player(O): ')
print(f'We will Start with {player1}')
axis=[[1,2,3],
      [4,5,6],
      [7,8,9]]
array_length = len(axis)
for i in range(array_length):
    print(axis[i])
