import Pyro4 as p4

server = p4.Proxy("PYRONAME:Server.server")

s = server.sayHi()
print(s)

sum = server.calc(10,20,30)
print(sum)
