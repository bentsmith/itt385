import re
#
#pattern = input("Enter a pattern: ")
#teststr = input("Enter a string to test: ")
#
#two step method
#p = re.compile(pattern)
#m = p.search(teststr)
#
#
#one step
#m = re.search(pattern, teststr)
#
#if m is None:
#    print("No match")
#else:
#    print("Match. String:")
#    print(m.group(0))
teststr = input("Enter a string to test: ")
pattern = "((U\.?S\.?M\.?)|(U\s+ of Southern Maine))"

newstr = re.sub(pattern, "University of Maine at Portland", teststr, flags=re.IGNORECASE|re.MULTILINE)

print(newstr)

# read, check, and write files if they need a name change
#fname = input("Enter a filename: ")
#f = open(fname)
#s = f.read()
#f.close()
#teststr = input("Enter a string to test: ")
#pattern = "((U\.?S\.?M\.?)|(U\s+ of Southern Maine))"
#
#newstr = re.sub(pattern, "University of Maine at Portland", teststr, flags=re.IGNORECASE)
#
#if(s == newstr):
#    print("No Change ness")
#else:
#    print("creating new version")
#    f = open(fname + ".new", "w")
#    f.writable(newstr)
#    f.close()