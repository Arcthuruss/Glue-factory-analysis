import csv

input_file = "./datasets/19860105-20210731_race_result.csv"
output_file = "./clean_datasets/filtered_race_result.csv"

# Ligne qui va être supprimée (pas de nom de colonne car le header est en japonais et prendrais trop de temps)
positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 36, 40, 41, 43, 47, 49, 52, 53, 54, 57, 60, 61, 62, 63, 64, 65]

with open(input_file, newline='', encoding='utf-8') as infile, \
    open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        filtered_row = [col for i, col in enumerate(row) if i not in positions]
        if all(filtered_row): 
            writer.writerow(filtered_row)

# Remplace le header par le header en anglais
with open(output_file, 'r', newline='', encoding='utf-8') as infile:
    lines = infile.readlines()
header = "Turf and Dirt Category,Clockwise And Anti-clockwise and Straight Course Category,Distance(m),Weather,Track Condition1,Final Position,Bracket Number,Post Position,Horse Name,Age,Jockey,Total Time(1/10s),Position 3rd Corner,Position 4th Corner,Win Odds(100Yen),Win Fav"
lines[0] = header + "\n"
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    outfile.writelines(lines)
