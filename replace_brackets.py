import sys

path = sys.argv[1].strip()

# Read in the file
with open(path, 'r') as file :
  filedata = file.read()

# Replace the brackets in ZH-CN with brackets in EN
filedata = filedata.replace('（', '(')
filedata = filedata.replace('）', ')')

# Write the file out again
with open(path, 'w') as file:
  file.write(filedata)