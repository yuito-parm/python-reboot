def list_add(nums):
    result = 0
    for num in nums:
        result += num
    
    return result

list1 = [80, 90, 70, 60]
list2 = [100, 95, 85]
add1 = list_add(list1)
print(f"{list1}の合計は {add1}点 です。")
add2 = list_add(list2)
print(f"{list2}の合計は {add2}点 です。")