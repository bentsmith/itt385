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
