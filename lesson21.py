import json
import random
from faker import Faker


fake = Faker()
students_list = []


for i in range(1, 101):
    student = {
        'id': i,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'status': random.choice([True, False])
    }
    students_list.append(student)


file_path = "students_data.json"

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(students_list, file, indent=4, ensure_ascii=False)

print(f"100 სტუდენტის მონაცემი წარმატებით ჩაიწერა ფაილში: {file_path}")