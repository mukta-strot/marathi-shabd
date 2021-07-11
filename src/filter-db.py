# purpose - to filter the input csv data as per the provided arguments

# ### filter types ###
# - invalid data
# - all words
# - specific topic
# - specific alphabet (which will be initial of the english word)
# - TBD (more can be added)

# ### about invalid data filter ###
# the invalid data filter is to be run always before running any other filter,
# as it eliminates those data elements which have insufficient or invalid data
# insufficient data - any of the english or marathi word is missing
# invalid data - if english word contains non english characters (this can be
# thought of later, and is low priority right now), same for marathi word.

# IMP - make separate functions for each filter type
# as per the passed argument of the "filter type" call the relavant function

# steps
# 1. take passed csv data and filter type as argument
# 2. generate a truncated csv data structure as per the target filter
#    - call the specific filter function here
# 3. return this truncated data to the calling function
