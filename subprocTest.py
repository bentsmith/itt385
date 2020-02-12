import subprocess

# stdin
# Linux/Windows
# >
# >>
#
# |

# stderr

# proc = subprocess.run(["dir","c:\\Windows"], shell=True, stdout=subprocess.PIPE)
proc = subprocess.Popen(["dir","c://Windows"], shell=True, stdout=subprocess.PIPE)

for s in proc.stdout:
    s = s.decode('utf-8')
    s = s.rstrip()

    print(">>>", s)