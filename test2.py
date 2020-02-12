import cgitb
import cgi
DEBUG = 1

if DEBUG > 0:
	cgitb.enable()

# cgi needs a content type and a blank line, then it can do html
print("Content-Type: text/html")
print("")

print("""
<html>
	<head>
		<title> Welcome</title>
	</head>
	<body>
		<h1>Welcome to my web page</h1>
	</body>
</html>

""")

if DEBUG > 0:
	form = cgi.FieldStorage()
	print("<br />")
	print("Fields Info", <br \>
	
	for key in form.keys():
		print(key, " = ", form, getvalue(key), "<br /")
	