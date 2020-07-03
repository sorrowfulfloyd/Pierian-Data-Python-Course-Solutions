# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

for i in st.split():
    if i[0] == 's':
        print(i)