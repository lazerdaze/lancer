# Lancer Modules
from rig.utils import *
from bodyBase import BASE

# Maya Moudles
from maya import cmds

class FKIK(BASE):
	def __init__(self,
	             start,
	             mid,
	             end,
	             name='fkik',
	             ):
		BASE.__init__(self,
		              objects=[start, mid, end],
		              name=name,
		              )

		self.createFKIKChain(self.objects)
		self.createNetwork(typ='fkik')
		self.createNetworkConnections()