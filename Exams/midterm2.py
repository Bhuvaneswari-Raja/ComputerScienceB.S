def question_nine(x):
   if x % 2 == 0:
       return x + 1
   else:
       return 2 * x
  
'''
print(question_nine(15))

a_map = {"squirrel": 15, "bear": 31, "turnip": 71, "broccoli": 45}
print(a_map["broccoli"])
print(a_map['turnip'] + a_map['bear'])
a_map['chocolate'] = 5
print(len(a_map))


names = {"Eric":1, "Pooja": 2, "Amrithya": 3}
print("Eric" in names and "George" not in names)

words = {
    "veritable": 15,
    "art": 3,
    "fifteen": 14,
    "gold": 83,
    "orbit": 55
}
print(words.get("art", 0))
print(words.get("seven", 0))


a_list = [[2, 4, 6], [1, 2, 8], [3, 11, 17]]
for x in range(5, 7):
	print(a_list[x % 3][(2 * x + 2) % 3])


def get_even_count(num_list):
    even_count_list = []
    for row in num_list:
        count = 0
        for col in range(len(row)):
            if row[col] % 2 == 0:
                 count += 1
        even_count_list.append(count)
    return even_count_list

print(get_even_count([[1,2], [5,6]]))
print(get_even_count([[1,2,3,4], [5,6,7,8], [8,10,12,12]]))

'''

def average_lists(num_list):
    if len(num_list) == 0:
        return 0
    else:
        sum_of_num = 0
        total = 0
        for sub in num_list:
            for num in range(len(sub)):
                total += 1
                sum_of_num += sub[num]
        if total == 0:
            return 0
        else:
            return sum_of_num / total


print(average_lists([1,2,3], [2,3,4]))
print(average_lists([[1,2], [3,4], [5,8,6,7], [12,11,10,9]]))

                

            
