age = int(input("年齢を入力してください。"))

if age >= 20:
    print(f'あなたは{age}歳ですね。')
    print('大人ですね！')
elif age >= 13:
    print(f'あなたは{age}歳ですね。')
    print('ティーンですね！')
else:
    print(f'あなたは{age}歳ですね。')
    print('子どもですね！')