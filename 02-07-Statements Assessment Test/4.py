# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
#What a Pepega English bruh, took me 10 min to figure out what the question meant LUL

for i in st.split():
    if len(i) % 2 == 0:
        print(f'{i} is an even number fam')