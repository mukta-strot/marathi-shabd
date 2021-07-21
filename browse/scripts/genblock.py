class GenBlock:
    def generate_block(self, row):  # generates a singular block for the markdown. row is a string parameter.
        word_block = ""
        if row[1] == "":
            word_block += "## " + row[0] + " = NULL\n\n"
        else:
            word_block += "## " + row[0] + " = " + row[1] + "\n\n"

        if row[3] == "":
            word_block += "|NULL|\n"
        else:
            word_block += "|" + row[3] + "|\n"
        word_block += "|---|\n"
        if row[4] == "":
            word_block += "|NULL|\n\n"
        else:
            word_block += "|" + row[4] + "|\n\n"
        word_block += "---\n"

        return word_block

# use below line to test this function
# print(generate_block("experience,अनुभव,daily,I have experience in this.,मला यात अनुभव आहे."))
