import csv
import sys

print(sys.argv)
if len(sys.argv) < 4 :
    print("Usage: Python prog2.py <src> <dst> <change1> <change2> ...")
    sys.exit()

old_file = sys.argv[1]
new_file = sys.argv[2]
changes = sys.argv[3:]

#print(old_file, new_file, changes)

with open("old.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    #for line in csv_reader:
     #   print(line)
    old_data = list(csv_reader)
    print(old_data)
    print(old_data[0][0])
    old_data[0][0] = "piano"
    old_data[1][3] = "mug"
    old_data[2][1] = 17
    old_data[3][3] = 0
    print(old_data)
with open("new.csv", "w", newline="") as new_csv_file:
    csv_writer = csv.writer( new_csv_file)

    for line in old_data:
        csv_writer.writerow(line)



   