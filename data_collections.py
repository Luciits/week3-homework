# A daļa saraksti
print("-----Saraksti-----/")
saraksts = [1, 2, 3, 4, 5]
print(saraksts)
saraksts.append(11)
saraksts.append(12)
saraksts.append(13)
saraksts.append(14)
print(saraksts)
saraksts.pop()
print(saraksts)
total = 0
count = 0
para_saraksts = []
for i in saraksts:
    total += i
    count += 1
    if i % 2 == 0:
        para_saraksts.append(i)
if count > 0:
    average = total / count
    print(f"Vidējā vērtība: {average} Summa: {total}")
    print(f"Pāra skaitļi: {para_saraksts}")
    print(f"Pirmie 3 skaitļi: {saraksts[:3]} pēdējie 2 skaitļi: {saraksts[-2:]} katrs otrais skaitlis: {saraksts[1:9:2]}")

# B daļa vārdnīcas
print("\n-----Vārdnīca-----/")
vardnica = {"Anna": 85, "Jānis": 72, "Līga": 95, "Pēteris": 68}
vardnica["Marta"] = 90
for name, grade in vardnica.items():
    print(f"{name}: {grade}")
for name, grade in vardnica.items():
    if grade == max(vardnica.values()):
        print(f"{name} ir labākais students ar {grade} punktiem")
# C daļa kombinācija
print ("n/-----Studenti ar atzīmi >= 80-----/")
student_grades = [{"name": "Anna", "grade": 85}, {"name": "Jānis", "grade": 72}, {"name": "Līga", "grade": 95}, {"name": "Pēteris", "grade": 68}, {"name": "Marta", "grade": 90}]
top_students = [t for t in student_grades if t["grade"] >= 80]
for i, student in enumerate(top_students, start=1):
    print (f"{i}. {student['name']} - {student['grade']}")