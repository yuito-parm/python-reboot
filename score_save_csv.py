def list_add(scores):
    result = 0
    for num in scores:
        result += num
    
    return result

def list_average(scores):
    result = 0
    for score in scores:
        result += score
    
    average = result / len(scores)
    return average

people = []
while True:
    person = {}
    scores = []
    person["name"] = input("名前を入力してください：")
    if person["name"] == "exit":
        break
    while True:
        try:
            sbj = int(input("何教科ありますか？"))
            break
        except:
            print("数字を入力してください！")
    for i in range(sbj):
        while True:
            try:
                scores.append(int(input(f"{i + 1}つめの点数を入力してください。")))
                break
            except:
                print("数字を入力してください！")
    person["scores"] = scores
    people.append(person)
    print(person)

class_score = []
for person in people:
    add = list_add(person["scores"])
    average = list_average(person["scores"])
    class_score.append(add)
    person["add"] = add
    person["average"] = average

sorted_people = sorted(people, key=lambda p: p["average"])

print("合計点上位3人だけ表示します。")
for person in sorted_people[:3]:
    print(f"{person['name']}さんの合計は{person['add']}点、平均は{person['average']:.1f}点です。")

class_average = list_average(class_score)
print(f"クラスの平均点は{class_average:.1f}点です")

with open("scores.csv", "w") as f:
    f.write("name,total,average\n")
    for person in sorted_people:
        f.write(f"{person['name']},{person['add']},{person['average']}\n")