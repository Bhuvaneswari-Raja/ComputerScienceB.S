word = input("Enter a string: ")

word = word.lower().strip().split()
word = "".join(word)

someword = ""
num = 0
winner = False

while winner == False:
    for k in range(1,len(word)):
        word = word[k:] + word[:k]
        print("word =",word)
    if someword == word:
        winner = True
    
if num > 0:        
    print(word,"is a rotation with offset",num)
else:
    print("There are no rotations of the string")