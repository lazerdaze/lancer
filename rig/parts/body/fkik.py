# Lancer Modules
from rig.utils import *
from rigBase import RIGBASE

# Maya Moudles
from maya import cmds

class FKIK(RIGBASE):
	def __init__(self,
	             start,
	             mid,
	             end,
	             name='fkik',
	             ):
		RIGBASE.__init__(self,
		                 items=[start, mid, end],
		                 name=name,
		                 )

		self.createFKIKChain(self.items)
		self.createNetwork(typ='fkik')
		self.createNetworkConnections()