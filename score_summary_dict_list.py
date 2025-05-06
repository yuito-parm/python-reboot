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

people = [
            {"name": "Yuito", "scores":[80, 90, 70, 60]}, 
            {"name": "Hanako", "scores":[100, 95, 85]}
]

for person in people:
    name = person["name"]
    scores = person["scores"]
    add = list_add(scores)
    average = list_average(scores)
    print(f"{name}さんの合計は{add}、平均は{average:.1f}点です。")