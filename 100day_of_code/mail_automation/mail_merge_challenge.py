with open("mail_names.txt") as name_list:
    content = name_list.read()

sorted_names = []
for line in content.splitlines():
    name = line.strip()
    if name:
        sorted_names.append(name)

print(sorted_names)
number = 0
while number < (len(sorted_names)):
    anschrift = sorted_names[number]
    with open(f"{anschrift}.txt", mode="w") as new_letter:
        new_letter.write(f"Dear {anschrift}, this is a test letter!")
    number += 1
