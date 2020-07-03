# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

justalistbro = [x[0] for x in st.split()]
print(justalistbro)