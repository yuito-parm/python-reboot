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
for i in range(2):
    person = {}
    scores = []
    person["name"] = input("名前を入力してください：")
    for i in range(3):
        scores.append(int(input(f"{i + 1}つめの点数を入力してください。")))
    person["scores"] = scores
    people.append(person)
    print(person)

for person in people:
    add = list_add(person["scores"])
    average = list_average(person["scores"])
    print(f"{person['name']}さんの合計は{add}点、平均は{average:.1f}点です。")