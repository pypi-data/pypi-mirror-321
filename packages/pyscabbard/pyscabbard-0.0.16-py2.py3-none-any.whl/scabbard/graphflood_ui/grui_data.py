'''
WIP for graphflood universale interface
'''
import numpy as np
import scabbard as scb
import scipy.io as sio


class GFUI:

	def __init__(self, backend, grid):


		backend = backend.lower()
		# setting up the backend
		if(backend in ['gpu' , 'dagger' , 'cpu' , 'ttb' , 'topotoolbox']):
			self.backend = backend
		else:
			raise RuntimeError('Backend ' + backend + ' not recognised.')

		#########################
		# internal backend object
		#
		
		## graphflood OG from DAGGER (v1)
		### obj
		self._cpp_gf = None
		### graph
		self._cpp_graph = None
		### graph
		self._cpp_connector = None
		
		## Induced graph and v2
		self._cpp_env = None

		## lib-py-TopoToolBox
		# No object

		## GPU backend
		self._param = None
		self._rd = None


	def _init_riverdale_backend(self, grid):
		pass



		