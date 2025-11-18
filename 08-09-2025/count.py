names = ["Anu", "meena", "Rani", "Anand"]

count_a = 0

for name in names:
    count_a += name.lower().count("a")

print("Number of 'a' characters: ",count_a)
