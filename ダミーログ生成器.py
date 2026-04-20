import datetime
import time

def generate_logs(count=10):
    levels = ["INFO", "WARNING", "ERROR"]
    with open("app.log", "w", encoding="utf-8") as f:
        for i in range(count):
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            lv = levels[i % 3]
            msg = f"[{now}] {lv}: ダミーメッセージ {i+1} を出力しました。\n"
            f.write(msg)
            print(msg.strip())
            time.sleep(0.1)

print("ログファイルを生成中...")
generate_logs(15)
print("app.log に保存されました。")
