import glob
#Enter directory name for files which to be searched
directory = 'C:/Users/7000033087/PycharmProjects/Python-learnings/Python-tasks'

file_pattern = '*.py'   #give the file pattern
files = glob.glob(f"{directory}/{file_pattern}")

#loop through the files to print the list of patterns
for file in files:
    print(file)