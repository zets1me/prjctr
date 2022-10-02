# ### Practice
#
# **You have 100 cats.**
#
# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# 3. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# 4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.
#
# Optional: Make function that can calculate hat with any amount of rounds and cats.
#
# Here you should write an algorithm, after that, try to make pseudo code. Only after that start to work. Code is simple here, but you might struggle with algorithm. Therefore don`t try to write a code from the first attempt.

cats = int(input("How many cat's should be counted? "))
rounds = int(input("How many rounds should we walk through cats? "))
def cats_in_hats(cats, rounds):
    cats_in_hats = []
    for walk in range(1, rounds +1):
        for cat in range(1, cats +1):
            if cat % walk == 0:
                if cat in cats_in_hats:
                    cats_in_hats.remove(cat)
                else:
                    cats_in_hats.append(cat)
    return cats_in_hats
print(cats_in_hats(cats, rounds))
