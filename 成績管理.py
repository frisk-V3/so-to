students = [
    {"name": "田中", "score": 85},
    {"name": "佐藤", "score": 92},
    {"name": "鈴木", "score": 68},
    {"name": "高橋", "score": 77}
]

def analyze_scores(data):
    total = sum(s["score"] for s in data)
    avg = total / len(data)
    highest = max(data, key=lambda x: x["score"])
    
    print("--- 成績レポート ---")
    for s in data:
        status = "合格" if s["score"] >= 70 else "再試験"
        print(f"{s['name']}: {s['score']}点 ({status})")
    print(f"平均点: {avg:.1f}")
    print(f"最高点: {highest['name']}さんの{highest['score']}点")

analyze_scores(students)
