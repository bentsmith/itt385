# program that prompts the user for a specific directory to search
# along with a regular expression to match a full filename, also including file path
# the file should be able to handle both tar or zip

# imports for regular expressions, tar and zip files
import re
import os
import tarfile
import zipfile

# ask user for inputs

# directory = str(input("Enter the directory to search: "))  # remember to swap over to directory
# regex_file = str(input("What files do you want to match? (RegEx)"))
# regex_line = str(input("What lines do you want to match? (RegEx)"))

raw_files = [][]
path = "c:\\proj-2-files\\"  # aka the directory. we gonna use path for now to save time

for x in range(0,len(os.listdir(path))):
    raw_files = os.listdir(path)
    if os.listdir(path + raw_files[x]) is not None:
        for y in range(0, len(os.listdir(path + raw_files[x] ) ) ) :
            raw_files[x][y] = os.listdir(path + raw_files[x])
            print raw_files[x][y]

# re.search & re.match for reg exp searching or re.findall(pattern, string)