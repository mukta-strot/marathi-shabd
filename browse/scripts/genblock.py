class GenBlock:
    def generate_block(self, row):  # generates a singular block for the markdown. row is a string parameter.
        word_block = ""

        # elements in row
        # 0 - en
        # 1 - mr
        # 2 - tags
        # 3 - context
        # 4 - mr-sentence
        # 5 - comment

        if row[1] != "":
            if row[3] != "":
                word_block += "### " + row[0] + " *(" + row[3] + ")* = " + row[1] + "\n\n"
            else:
                word_block += "### " + row[0] + " = " + row[1] + "\n\n"

        if row[4] != "":
            word_block += "**Sentence**: " + row[4] + "\n\n"

        if row[5] != "":
            word_block += "**Comment**: " + row[5] + "\n\n"

#       Temporarily disabled as displaying the tags doesn't give any information.
#       Can be enabled in future if the tags (topics) can be linked to their 
#       individual files
        # if row[2] != "":
        #     word_block += "###### Tags: " + row[2] + "\n\n"

        # add seperator line if context or sentence is present
        if row[4] != "" or row[5] != "":
            word_block += "---\n"

        return word_block

# use below line to test this function
#g = GenBlock()
#print(g.generate_block(["en","mr","tags","context","example","comment"]))
