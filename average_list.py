def average_list(nums):
    result = 0
    for num in nums:
        result += num
    
    return result / len(nums)

list1 = [80, 90, 70, 60]
list2 = [100, 95, 85]
avr1 = average_list(list1)
print(f"{list1}の平均は {avr1:.1f}点 です。")
avr2 = average_list(list2)
print(f"{list2}の平均は {avr2:.1f}点 です。")