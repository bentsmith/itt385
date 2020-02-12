
# This program is designed to check two filesystems of the user's choice and filter it by a file prefix.
# The program will read through the filesystems, formatting the file data for easier processing and then compare
# the two systems against each other for differences

# Ask user for inputs
user_input = [str(input("Enter the filename for the first system: ")),
              str(input("Enter the filename for the second system: "))]

# Prefix input so we only get the directory name without the slashes
prefix = str(input("Prefix path:")).replace("/", "")

# list to hold the raw file
raw_systems = []

# loop through the two systems and open files
for file_name in user_input:

    path = "c:\\files\\" + file_name

    with open(path, encoding="utf-8", errors="ignore") as file:
        # add full line to the raw systems list
        raw_systems.append(file.readlines())

# systems array used to store the system<k,v> or <md5 sum, path>
systems = []
for raw_system in raw_systems:

    system = {}

    for raw_line in raw_system:
        # eliminate new lines in the raw line and split the raw line into (md5sum, path) by the format of two spaces
        line = raw_line.replace("\n", "").split("  ")

        # split the full file path by "/"
        full_path = line[1].split("/")

        # check if file begins with the prefix, then add to sys list
        if full_path[1] == prefix:
            system[line[0]] = line[1]

    # add md5 sums and paths to systems list
    systems.append(system)

# scan through and find differences
for x in range(0, 2):

    if x == 0:
        compare = 1
    else:
        compare = 0
# run through systems list and compare for differences
    for system0_sum, system0_path in systems[x].items():

        found = False

        for system1_sum, system1_path in systems[compare].items():
            if system0_path == system1_path and system0_sum == system1_sum and not found:
                found = True
            # check for same file path but different md5 sum
            elif system0_path == system1_path and system0_sum != system1_sum and not found:
                found = True
                print("%s is the same path, different md5 sums: %s md5: %s " % (system0_path, system0_sum, system1_sum))
        # missing file on either system, compare + 1 to change from sys 0 and 1 to sys 1 and 2
        if not found:
            print("%s is not on system %s " % (system0_path, compare + 1))

