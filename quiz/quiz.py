import csv
import time

with open("quiz.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    ques_counter = 0
    score = 0
    for row in csv_reader:
        if len(row) != 6:
            continue
        print("Q-"+str(ques_counter+1)+': '+row[0].strip())
        print(f"  1-{row[1].strip()}")
        print(f"  2-{row[2].strip()}")
        print(f"  3-{row[3].strip()}")
        print(f"  4-{row[4].strip()}")
        ans = input()
        if(int(ans) == row.index(row[5])):
            score += 1
        ques_counter += 1
    print(f"You scored {score}/{ques_counter}")
