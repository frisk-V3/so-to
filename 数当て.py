import random

def guess_number_game():
    target = random.randint(1, 100)
    attempts = 0
  # 無理だけどwww 
  print("1から100の間で数字を当ててみてね！")

    while True:
        try:
            guess = int(input("予想を入力してください: "))
            attempts += 1
            if guess < target:
                print("もっと大きいよ！")
            elif guess > target:
                print("もっと小さいよ！")
            else:
                print(f"正解！ {attempts}回目で当てました！")
                break
        except ValueError:
            print("有効な数字を入力してね。")

guess_number_game()
