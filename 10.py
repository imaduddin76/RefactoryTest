import json

with open('file.json') as f:
  data = json.load(f)

no = 0
for row in data:
    no += 1
    print("id: " + str(row["id"]))
    print("nama: " + row['name'])
    print("umur: " + str(row["age"]))

    if (row["age"]) < 21:
        print(row)
    else:
        print("")

    print()
