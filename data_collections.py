# A daļa saraksti
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
for i in saraksts:
    total += i
    count += 1
if count > 0:
    average = total / count
    print(f"Vidējā vērtība: {average}")
print(f"Summa: {total}")