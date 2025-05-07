def average_fanc(scores):
    class_total = 0
    for score in scores:
        class_total += score
    class_average = class_total / len(scores)
    return class_average
    



with open("scores.csv", "r") as f:
    next(f)
    people = []
    total_list = []
    for line in f:
        name, total, average = line.strip().split(",")
        total = int(total)
        people.append({
            "name": name,
            "total": total,
            "average": float(average)
        })
        total_list.append(total)


sorted_people = sorted(people, key=lambda p: p["average"])
for person in sorted_people[:3]:
    print(f"{person['name']}さん: 合計{person['total']}点、平均{person['average']:.1f}")

class_average = average_fanc(total_list)
print(f"クラス全体の平均点は{class_average:.1f}点です。")