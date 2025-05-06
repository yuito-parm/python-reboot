def average_add_list(nums):
    add = 0
    for num in nums:
        add += num
    
    average = add / len(nums)
    return add, average

list1 = [80, 90, 70, 60]
list2 = [100, 95, 85]
[add1, average1] = average_add_list(list1)
print(f"{list1}の合計は {add1}点 です。")
print(f"{list1}の平均は {average1:.1f}点 です。")
[add2, average2] = average_add_list(list2)
print(f"{list2}の合計は {add2}点 です。")
print(f"{list2}の平均は {average2:.1f}点 です。")