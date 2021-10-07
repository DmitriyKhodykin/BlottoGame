"""
Module with the implementation of Blotto Game theory.
"""
x = [20, 19, 22, 19, 20]  # Gamer
y = [20, 19, 21, 20, 20]  # AI

print("X:", sum(x))
print("Y:", sum(x))

res = 0
for i in range(len(x)):
    r = x[i] - y[i]
    if r < 0:
        res = res + 1

print("RES:", res)

if res > 2:
    print("You are lose")
elif res == 0:
    print("Draw game")
else:
    print("You are win")
