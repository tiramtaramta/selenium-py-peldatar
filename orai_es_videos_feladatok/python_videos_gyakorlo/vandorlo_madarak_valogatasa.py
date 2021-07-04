# melyik a leggyakoribb típus, amit megfigyeltek

birds = [2, 3, 4, 4, 5, 4, 2, 4]

counts = {}  # az adott típushoz tartozó értékekhez felveszünk egy dictionary-t

for birds_type in birds:
    counts[birds_type] = counts.get(birds_type, 0) + 1  # csak így működik, mert először bele kell tenni a nullát
print(counts)  # {2: 2, 3: 1, 4: 4, 5: 1}

print(max(counts, key=counts.get))
# legnagyobb elemet keressük ki a counts dictionary-ben
# a kulcsot hogyan értelmezze... counts.get lekérést használja mellé (ez kicsit homályosan volt megfogalmazva)