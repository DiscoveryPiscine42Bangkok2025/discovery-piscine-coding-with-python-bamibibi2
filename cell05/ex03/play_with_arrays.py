original = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for i in original:
    if i > 5:
        new_set.add(i + 2)

print(original)
print(new_set)
