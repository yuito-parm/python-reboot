scores = [90, 88, 98, 84, 77]

total = 0
for score in scores:
    total += score

average = total / len(scores)

print(f"合計点: {total}点")
print(f"平均点: {average:.1f}点")