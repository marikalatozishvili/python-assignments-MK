import string

print("--- დავალება 1 ---")
text1 = input("შეიყვანეთ ტექსტი: ")
encoded_text = text1.encode("utf-8")
print("UTF-8 დაშიფრული ვერსია:", encoded_text)
print("-" * 20)


print("--- დავალება 2 ---")
text2 = input("შეიყვანეთ ტექსტი: ")
# ვშლით ზედმეტ ინტერვალებს
text2 = text2.strip()
# გადაგვყავს პატარა ასოებში
text2 = text2.lower()
# თუ არის სიტყვა "python", ვანაცვლებთ "Python"-ით
text2 = text2.replace("python", "Python")
# ვუმატებთ ქვესტრიქონს 'Python'
text2 = text2 + " Python"
print("შედეგი:", text2)
print("-" * 20)


print("--- დავალება 3 ---")
text3 = input("შეიყვანეთ ტექსტი: ")
# ვიგებთ სიგრძის ნახევარს (ვიყენებთ // რათა მივიღოთ მთელი რიცხვი)
half_length = len(text3) // 2
first_half = text3[:half_length]
print("პირველი ნახევარი:", first_half)
print("-" * 20)


print("--- დავალება 4 ---")
text4 = input("შეიყვანეთ ტექსტი: ")

has_letter = False
has_digit = False
has_special_char = False

for char in text4:
    # ვამოწმებთ არის თუ არა ასო
    if char in string.ascii_letters:
        has_letter = True
    # ვამოწმებთ არის თუ არა ციფრი
    if char in string.digits:
        has_digit = True
    # ვამოწმებთ არის თუ არა დამატებითი სიმბოლო (!, ~, #, $ და ა.შ.)
    if char in string.punctuation:
        has_special_char = True

# ვალიდურია, თუ აქვს ასოც, ციფრიც და არ აქვს სპეციალური სიმბოლო
if has_letter == True and has_digit == True and has_special_char == False:
    print("სტრიქონი ვალიდურია")
else:
    print("სტრიქონი არ არის ვალიდური")
print("-" * 20)


print("--- დავალება 5 ---")
text5 = input("შეიყვანეთ ტექსტი: ")
# გადაგვყავს ბაიტებში და ვბეჭდავთ
bytes_text = text5.encode("utf-8")
print("ბაიტებში:", bytes_text)

# გადაგვყავს უკან სტრიქონში და ვბეჭდავთ
string_text = bytes_text.decode("utf-8")
print("სტრიქონში:", string_text)


# ვქმნით ცარიელ სიას
my_list = []

while True:
    action = input("შეიყვანეთ ბრძანება (a, r, e): ")

    if action == "a":
        number = int(input("შეიყვანეთ რიცხვი დასამატებლად: "))
        my_list.append(number)
        print("მიმდინარე სია:", my_list)

    elif action == "r":
        number = int(input("შეიყვანეთ რიცხვი წასაშლელად: "))
        if number in my_list:
            my_list.remove(number)
        else:
            print("ეს რიცხვი სიაში არ არის.")
        print("მიმდინარე სია:", my_list)

    elif action == "e":
        print("პროგრამამ დაასრულა მუშაობა.")
        print("საბოლოო სია:", my_list)
        break

    else:
        print("არასწორი ბრძანება, სცადეთ თავიდან.")

        my_list_1 = [43, "22", 12, 66, 210, ["hi"]]

# a. დაბეჭდავს 210-ის ინდექსს
print("210-ის ინდექსია:", my_list_1.index(210))

# b. დაამატებს ბოლო ელემენტში ტექსტს "hello"
# ბოლო ელემენტი არის სია ["hi"], ამიტომ მასზე ვიძახებთ append-ს
my_list_1[-1].append("hello")

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას
my_list_1.pop(2)
print("მე-2 ინდექსის წაშლის შემდეგ:", my_list_1)

# d. ახალი სია my_list_2
# ვიყენებთ .copy()-ს, რომ ორივე სია ერთმანეთზე არ იყოს გადაბმული
my_list_2 = my_list_1.copy()
my_list_2.clear()

print("my_list_1 მნიშნველობა:", my_list_1)
print("my_list_2 მნიშნველობა გასუფთავების შემდეგ:", my_list_2)

import re

phone_number = input("შეიყვანეთ ტელეფონის ნომერი: ")

# (123) 456-789 ფორმატის შემოწმება
# \d ნიშნავს ციფრს, {3} ნიშნავს 3 ცალს
pattern = r"\(\d{3}\) \d{3}-\d{3}"

if re.fullmatch(pattern, phone_number):
    print(phone_number)
else:
    print("Invalid format")
