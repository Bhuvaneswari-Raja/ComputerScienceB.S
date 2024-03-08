"""
PRICES = {5:["burger","sandwich"],
        3:"fries",
        2.5:["coke","sprite","mountain dew"],
        8.5:[["burger","sandwich"],"fries",["coke","sprite","mountain dew"]],
        4:"anything else"}

for x in PRICES:
    print(f"{PRICES[x]}:{x}")

    sample = {"pizza":4,}

    

extra = [["burger" for i in range(4)], ["fries" for i in range(2)],["drink" for i in range(1)]]
print(extra)

word = "abcdba"

print(word[-1:2:-1])"""

extras = ["burger"] * (2) + ["fries"] * (3) + ["coke"] * (5)

print(extras)

extras.append("combo" * 4)
print(extras)