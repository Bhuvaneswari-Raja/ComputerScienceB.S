"""
Spring 2023

animals = ["peacock", "lemur", "parrot", "dog", "cat", "zebra"]

print(animals[len(animals)//2])

animals.append("sugar glider")
print(len(animals))

animals.remove("ferret")
print(len(animals))

chance_rain = 1
umbrella = True
rain_coat = True
if chance_rain > 0.01 and umbrella and rain_coat:
    print("True")}

x = 21
y = 12

if ((x > 20) and not (y > 12)) or ((y > 12) and not (x > 20)):
    print("True")


x = 4
print((5+x) ** 2)
print(5 ** 2+x **2)
print((5+x) ** 2>5 ** 2+x **2 )



print(3%2 == 0 or "he" in "hello")


print(2 in [1,2,5,6] and "xy" in "x and y")


double = 0
while double < 50:
    print(double)
    double *=2

for i in range(5,27,3):
    print(i) 

s = "hello"
n =15
if n == 20 and s == "hello":
    print("both are true")
elif n == 15:
    print ("15 is equal to 3 times 5")
elif s == "hello":
    print (" Well Hello There ")
else:
    print (" Obi Wan Kenobi , You ’re my only hope ")

"""
"""
def get_two_max_values(L):
    max_list = []
    if L:
        print("so far so good")
        if len(L) <= 1:
            max_list.append(str(L[-1]))
            max_list.append(str(-1))
        else:
            max_list.append(str(max(L)))
            L.remove(max(L))
            max_list.append(str(max(L)))

    else:
        print("it's empty")
        max_list.append(str(-1))
        max_list.append(str(-1))
        
    print("Max values:", ", ".join(max_list))
    return max_list

get_two_max_values([4])


def distance_three_match(s,c):
    if c in s:
        for x in range(len(s)):
            if s[x] == c:
                if s[x+3] == c:
                    return True
                else:
                    return False
    else:
        return False




print(distance_three_match("abca","a"))
print(distance_three_match("adabdc","a"))
print(distance_three_match("adabdc","d"))
"""


animals = ["peacock", "lemur", "parrot", "dog", "cat", "zebra"]
print(animals["peacock"])