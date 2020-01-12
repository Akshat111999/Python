import string
def string_processing(string_list):
  
  z=string_list.lower()
  p=''.join([x for x in z if not x in string.punctuation])
  return p
  
st=string_processing("Hello, world!")
print(st)
