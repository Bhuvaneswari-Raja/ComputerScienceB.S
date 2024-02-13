'''
my_int = 32
while my_int:
    print(my_int)
    my_int //=5


def count_down(n):
    if n == 0:
        print("Surprise")
        return 0
    else:
        print(n)
        return n + count_down(n-1)
    
def down_count(n):
    if n == 0:
        print("Surprise")
    else:
        print(n)
        down_count(n-1)
    
print(count_down(5))

print("-------------------------------------------")
print(count_down(5))
print("-------------------------------------------")
down_count(5)
'''

def palindrome(word):
    if len(word) == 0:
        return True
    else:
        