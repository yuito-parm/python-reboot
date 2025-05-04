scores = {
    "国語": 93,
    "数学": 78,
    "英語": 91,
    "理科": 74,
    "社会": 88
}

total = 0
for subject, score in scores.items():
    print(f"{subject}: {score}点")
    total += score

average = total / len(scores)
print(f"合計点: {total}点")
print(f"平均点: {average:.1f}点")
