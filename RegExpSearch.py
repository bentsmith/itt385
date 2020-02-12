# By Ben Smith
#   NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# This program assumes the proj-2-files folder is located within the current working directory of
# where the file is located. It also requires the directory entry to have "\" before and after the string
# Example: "\proj-2-files\"
#
# this program takes input from the user for a directory to search, and files and lines within the file to match with
# seperate reg expression keywords. The program traverses through the directories using a form of recursion while
# checking each entry for matches. It then adds the match to a valid list and prints it out.
# The program can handle both .zip and .tar archives.

# imports for RegExP, OS for directories, Tarfile for .tar file extraction, Zipfile for .zip file extraction
import re
import os
import tarfile
import zipfile

# user inputs
user_directory = input("Enter a directory to search                    :")
user_files = input("What files do you want to match (use RegExp) :")
user_lines = input("What lines do you want to match (use RegExp) :")

# regex patterns
patterns = {
    "files": r"" + user_files,
    "lines" : r"" + user_lines
}

def traverse(path):
    # entry is a thing inside a directory, could be file or another directory
    entries = os.listdir(path)
    # list to hold all of the matched entries
    found = []

    for entry in entries:
        entry_split = entry.split(".")  # determines if it is a files because files have a "."
        # if statement to go into the next directory
        if len(entry_split) == 1:  # the entry split is a directory because no "."
            # start the function to the next directory. recursion is a wonderful thing...
            found = found + traverse(path + entry + "\\")

            # file matches are found under here
        else:
            # the file type
            file_type = entry_split[-1]
            # the full path of the file
            full_path = path + entry

            # open files if they are a .zip
            if file_type == "zip":
                with zipfile.ZipFile(full_path) as zf:
                    # returns every file in the directory
                    for file in zf.namelist():
                        # get full file path
                        file_path = full_path + "\\" + file
                        # pattern search
                        if re.search(patterns["files"], file_path):
                            # zip file open
                            with zf.open(file, 'r') as f:
                                # search lines in zip file
                                found = found + [{"line": line, "path": file_path} for line in
                                                 valid_lines(f.readlines())]
            # open files if they are a .tar
            elif file_type == "tar":
                with tarfile.open(full_path) as tf:
                    for file in tf.getnames():
                        # get full file path
                        file_path = full_path + "\\" + file
                        # pattern search
                        if re.search(patterns["files"], file_path):
                            # tar file open
                            with tf.extractfile(file) as f:
                                # search lines in tar file
                                found = found + [{"line": line, "path": file_path} for line in
                                                 valid_lines(f.readlines())]

            else:
                # pattern search
                if re.search(patterns["files"], full_path):
                    with open(full_path, 'r', encoding="utf-8") as f:
                        # search lines in any other file
                        found = found + [{"line": line, "path": full_path} for line in valid_lines(f.readlines())]
    return found


def valid_lines(lines):
    # array for valid lines
    valid = []
    # for lines match and add
    for line in lines:
        # line match
        if re.search(patterns["lines"], str(line)):
            # add to valid array
            valid.append(str(line.decode("utf-8")))
    # return valid lines
    return valid


# start the function
for x in traverse(os.getcwd() + user_directory):
    # show found
    print(x["path"])
    print(x["line"])

# By Ben Smith
