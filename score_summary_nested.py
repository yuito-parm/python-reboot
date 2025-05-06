def list_add(nums):
    add = 0
    for num in nums:
        add += num
    
    return add

def list_average(nums):
    result = 0
    for num in nums:
        result += num
    
    average = result / len(nums)
    return average

def show_summary(scores):
    add1 = list_add(scores)
    average1 = list_average(scores)
    print(f"{scores}の合計は {add1}点、平均は{average1:.1f} 点です。")

list1 = [80, 90, 70, 60]
list2 = [100, 95, 85]

show_summary(list1)
show_summary(list2)