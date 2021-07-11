# purpose - to generate a markdown formatted file of the database as per the
# passed filter type

# input arguments -
# database (csv) data
# output file name
# filter type

# usage example --
# for all words         - gen-out(dbHandler,"all.md","all")
# for specific topic    - gen-out(dbHandler,"science.md","science")
# for s initialed words - gen-out(dbHandler,"s.md","alpha","s")



# steps
# 1. read csv file in a local handler and create a blank output md file
# 2. filter rows from the csv as per the filter argument (call filter function)
# 3. extract a single row of the csv
# 4. call the gen-block function to generate a md block
# 5. append the output md file with the above returned block
# 6. repeat 3-5 till entire csv is parsed
# 7. save the resultant md file (in its correct path) with the name passed in 
#    the argument initially
