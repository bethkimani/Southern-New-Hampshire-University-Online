while True:
    user_text = input().split()  # Line 2, where the error occurred
    if len(user_text) < 2:
        if user_text and user_text[0] == 'quit':
            break
        continue
    word = user_text[0]
    if word == 'quit':
        break
    number = user_text[1]
    print('Eating {} {} a day keeps the doctor away.'.format(number, word))