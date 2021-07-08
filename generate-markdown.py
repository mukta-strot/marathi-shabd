

def generate_block(row):  # generates a singular block for the markdown. row is a string parameter.
    word_block = ""
    element_list = row.split(",")
    if element_list[1] == "":
        word_block += "## " + element_list[0] + " = NULL\n\n"
    else:
        word_block += "## " + element_list[0] + " = " + element_list[1] + "\n\n"

    if element_list[3] == "":
        word_block += "|NULL|\n"
    else:
        word_block += "|" + element_list[3] + "|\n"
    word_block += "|---|\n"
    if element_list[4] == "":
        word_block += "|NULL|\n\n"
    else:
        word_block += "|" + element_list[4] + "|\n\n"
    word_block += "---\n"

    return word_block


print(generate_block("experience,अनुभव,daily,I have experience in this.,मला यात अनुभव आहे."))

