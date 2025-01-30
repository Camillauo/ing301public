file = open("/Users/camillaullestadolsen/Documents/Hvl/Datateknologi og programmering/ing301public/weeks/04/gpslogs/short.csv")
innhold = file.read()
print(type(innhold))
print(innhold)
linjer = innhold.split("/n")
print(type(linjer))


max_hoyde = 0
for linje in linjer:
    linje_delt = linje.split(",")
    print(linje_delt[3])
file.close()


