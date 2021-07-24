from filterdb import Filter
from genblock import GenBlock


def gen_out(csv, filter=None, sub_filter=None):
    f = Filter()  # filter class object
    g = GenBlock()  # block class object
    with open("out.md", "w", encoding="UTF-8") as md_file:
        f.filter_db(csv, filter, sub_filter)
        row_list = f.gen_row_list("filtered.csv")
        for row in row_list:
            md_block = g.generate_block(row)
            md_file.write(md_block)

# test code below
gen_out("C:\\Users\\aaroh\\OneDrive\\Documents\\GitHub\\marathi-shabd\\database\\db.csv")
