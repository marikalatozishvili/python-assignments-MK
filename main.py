import json

# 1. მისამართის კლასი ჩაშენებული ველებისთვის
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __repr__(self):
        return f"{self.city}, {self.street}"


# 2. მთავარი სტუდენტის კლასი
class Student:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address  # აქ გადმოეცემა Address კლასის ეგზემპლარი

    def __repr__(self):
        return f"Student(სახელი: {self.name}, ტელეფონი: {self.phone}, მისამართი: [{self.address}])"


# 3. დესერიალიზაცია და ეგზემპლარების შექმნა
def load_students(file_path):
    # ვკითხულობთ ფაილს (აუცილებლად utf-8 ენკოდინგით, რადგან ქართული შრიფტია)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    students_list = []
    
    # გადავუყვებით json-დან მიღებულ სიას
    for item in data:
        # ჯერ ვქმნით მისამართის ეგზემპლარს
        address_info = item.get('address', {})
        address_obj = Address(
            city=address_info.get('city'), 
            street=address_info.get('street')
        )
        
        # შემდეგ ვქმნით სტუდენტის ეგზემპლარს და გადავცემთ მისამართის ობიექტს
        student_obj = Student(
            name=item.get('name'),
            phone=item.get('phone'),
            address=address_obj
        )
        
        students_list.append(student_obj)
        
    return students_list

# კოდის გაშვება
if __name__ == "__main__":
    # დარწმუნდი, რომ ფაილს ზუსტად "students.json" ჰქვია
    file_name = 'data.json' 
    
    # ვინახავთ შექმნილ ეგზემპლარებს ცვლადში
    student_instances = load_students(file_name)
    
    # ვბეჭდავთ თითოეულ ეგზემპლარს
    for student in student_instances:
        print(student)