with open("scores.csv", "r") as f:
    next(f)
    print("CSVファイルから読み込んだデータ(上位3人):")
    people = []
    for line in f:
        name, total, average = line.strip().split(",")
        people.append({
            "name": name,
            "total": int(total),
            "average": float(average)
        })

sorted_people = sorted(people, key=lambda p: p["average"])
for person in sorted_people[:3]:
    print(f"{person['name']}さん: 合計{person['total']}点、平均{person['average']}")
