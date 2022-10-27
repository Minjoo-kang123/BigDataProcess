import sys

tmp = sys.argv


f_read = open(tmp[len(tmp)-2], "rt")
f_write = open(tmp[len(tmp)-1], "wt")
genre = dict()
for line in f_read:
#    line = "\'\'\'" + line +"\'\'\'"
    movie = line.split("::")
    gen = movie[len(movie) - 1].split("|")
    for g in gen:
        if g in genre:
            genre[g] += 1
        else:
            genre[g] = 1

g_name = list(genre.keys())
for k in g_name:
    f_write.write(k.strip() + " " + str(genre[k]) + "\n")

f_read.close()
f_write.close()
