try:
  file = open('mytext.txt', 'a')
  file.write('Hello\n')
# Error type isnt mandatory, but you can use except conditionally
except IOError:
  print("Error: File not found!")
# else/ finally. However, finally will be excecuted even if and error happened.
finally:
  file.close()
  print('Success')
  