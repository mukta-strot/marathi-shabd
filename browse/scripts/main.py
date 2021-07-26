from genOut import GenFiles
from topicsParser import TopicsParser

f = GenFiles() # GenFiles object

# code to generate output markdown files

# all words
f.gen_out("../../database/db.csv", "../all.md", "all_words")

# alphabets
f.gen_out("../../database/db.csv", "../alpha/a.md", "alphabet", "a")
f.gen_out("../../database/db.csv", "../alpha/b.md", "alphabet", "b")
f.gen_out("../../database/db.csv", "../alpha/c.md", "alphabet", "c")
f.gen_out("../../database/db.csv", "../alpha/d.md", "alphabet", "d")
f.gen_out("../../database/db.csv", "../alpha/e.md", "alphabet", "e")
f.gen_out("../../database/db.csv", "../alpha/f.md", "alphabet", "f")
f.gen_out("../../database/db.csv", "../alpha/g.md", "alphabet", "g")
f.gen_out("../../database/db.csv", "../alpha/h.md", "alphabet", "h")
f.gen_out("../../database/db.csv", "../alpha/i.md", "alphabet", "i")
f.gen_out("../../database/db.csv", "../alpha/j.md", "alphabet", "j")
f.gen_out("../../database/db.csv", "../alpha/k.md", "alphabet", "k")
f.gen_out("../../database/db.csv", "../alpha/l.md", "alphabet", "l")
f.gen_out("../../database/db.csv", "../alpha/m.md", "alphabet", "m")
f.gen_out("../../database/db.csv", "../alpha/n.md", "alphabet", "n")
f.gen_out("../../database/db.csv", "../alpha/o.md", "alphabet", "o")
f.gen_out("../../database/db.csv", "../alpha/p.md", "alphabet", "p")
f.gen_out("../../database/db.csv", "../alpha/q.md", "alphabet", "q")
f.gen_out("../../database/db.csv", "../alpha/r.md", "alphabet", "r")
f.gen_out("../../database/db.csv", "../alpha/s.md", "alphabet", "s")
f.gen_out("../../database/db.csv", "../alpha/t.md", "alphabet", "t")
f.gen_out("../../database/db.csv", "../alpha/u.md", "alphabet", "u")
f.gen_out("../../database/db.csv", "../alpha/v.md", "alphabet", "v")
f.gen_out("../../database/db.csv", "../alpha/w.md", "alphabet", "w")
f.gen_out("../../database/db.csv", "../alpha/x.md", "alphabet", "x")
f.gen_out("../../database/db.csv", "../alpha/y.md", "alphabet", "y")
f.gen_out("../../database/db.csv", "../alpha/z.md", "alphabet", "z")

# topics
tp = TopicsParser()
topics = tp.gen_topics("../../database/db.csv")
for topic in topics:
    f.gen_out("../../database/db.csv", '../topics/{}.md'.format(topic), "topic", "{}".format(topic))

# TODO (topics markdown generator)
# the topics section above can be improved by using the topicsparser.py script,
# wherein the code can be something like below -
# ----
# topicslist = output from topicsparser.py
# for currentTopic from topicslist 
#   f.gen_out("../../database/db.csv", "../topics/<currentTopic>.md", "topic", "<currentTopic>")
# end for
# ----
# basically instead of hardcoded topics used to generate the markdown files, use
# the parser to get a list of avaialble topics and generate all markdown files as
# per that list.
