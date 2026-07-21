# 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).
input_seq1 = input("1. შეიტანეთ მიმდევრობა (გამოყავით ჰარით): ")
my_set = set(input_seq1.split())
print("Set:", my_set)
print("-" * 30)

# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ ... (frozenset).
input_seq2 = input("2. შეიტანეთ მიმდევრობა (გამოყავით ჰარით): ")
my_frozenset = frozenset(input_seq2.split())
print("Frozenset:", my_frozenset)
print("-" * 30)

# 3. აიღეთ set ტიპის ორი მონაცემი... დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).
set1 = {1, 2, 3, "Python"}
set2 = {3, 4, 5, "Backend"}
union_set = set1.union(set2)
result_tuple = tuple(union_set)
print("3. გაერთიანებული Tuple:", result_tuple)
print("-" * 30)

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი... დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).
input_seq4 = input("4. შეიტანეთ რიცხვების მიმდევრობა (გამოყავით ჰარით): ")
my_tuple = tuple(input_seq4.split())
unique_list = list(set(my_tuple))
print("Unique list:", unique_list)
print("-" * 30)

# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს... დაბეჭდეთ შემდეგი ფორმატით.
people = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
print("5. დაბეჭდილი სია:")
for name, age in people:
    print(f"Name: {name}, Age: {age}")
print("-" * 30)

# 6. მოცემულია მომხმარებლების სია... დავბეჭდოთ თანხვედრა.
list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

# თანხვედრის (გადაკვეთის) საპოვნელად გადაგვყავს set-ში
intersection = set(list1).intersection(set(list2))
print("6. თანხვედრა სიებს შორის:", intersection)