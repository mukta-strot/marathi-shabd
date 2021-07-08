from sort import Sort

s = Sort()


def generate_block(i, file_name):  # generates a singular block for the markdown
    element_list = s.sort(file_name)
    with open("markdown.md", "w", encoding="utf-8") as f:
            if element_list[1][i] == "":
                f.write("## " + element_list[0][i] + " = NULL\n\n")
            else:
                f.write("## " + element_list[0][i] + " = " + element_list[1][i] + "\n\n")
            if element_list[1][i] == "":
                f.write("|NULL|\n")
            else:
                f.write("|" + element_list[3][i] + "|\n")
            f.write("|---|\n")
            if element_list[1][i] == "":
                f.write("|NULL|\n\n")
            else:
                f.write("|" + element_list[4][i] + "|\n\n")
            f.write("---\n")


