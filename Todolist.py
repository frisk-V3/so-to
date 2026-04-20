todo_list = []

def show_menu():
    print("\n--- TODOアプリ ---")
    print("1. タスク追加 / 2. 一覧表示 / 3. 削除 / 4. 終了")

while True:
    show_menu()
    choice = input("番号を選んでください: ")
    if choice == "1":
        task = input("タスク名: ")
        todo_list.append(task)
    elif choice == "2":
        for i, t in enumerate(todo_list):
            print(f"{i+1}: {t}")
    elif choice == "3":
        idx = int(input("消去する番号: ")) - 1
        if 0 <= idx < len(todo_list):
            todo_list.pop(idx)
    elif choice == "4":
        break
