from sort import Sort

s = Sort()

element_list = s.sort("db.csv")

with open("markdown.md", "w", encoding="utf-8") as f:
    for i in range(0, len(element_list[0])):
        if element_list[1][i] == "":
            f.write("## " + element_list[0][i] + " = NULL\n\n")
        else:
            f.write("## " + element_list[0][i] + " = " + element_list[1][i] + "\n\n")

        if element_list[3][i] == "":
            f.write("|NULL|\n")
        else:
            f.write("|" + element_list[3][i] + "|\n")
        f.write("|---|\n")

        if element_list[4][i] == "":
            f.write("|NULL|\n")
        else:
            f.write("|" + element_list[4][i] + "|\n\n")
        f.write("---\n")


