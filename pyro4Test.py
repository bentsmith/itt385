import Pyro4 as p4
import platform as plat

# @ is a decorator, decorator

@p4.expose
class myServ(object):

# self is the python equivalent of this. in java
    def sayHi(self):
        return "Hello There"


#
# -----------------------------------------------------
#

daemon = p4.Daemon(host=plat.node()) # avoid hardcoded IP address
ns     = p4.locateNS()

uri = daemon.register(myServ) # come up with an internal name

ns.register("Server.server", uri)

daemon.requestLoop()

