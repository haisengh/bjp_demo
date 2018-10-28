class moyin(object):
	def __init__(self,mofa=0):
		self._attack = 6
		self.mofa = mofa

	def chenyin(self):
		self.mofa += 1
	@property
	def attack(self):
		return self._attack + self.mofa*2

class dao(object):
	def __init__(self,feiyonog=-2):
		self.attack = 1
		self.feiyong = -2

class cigu(object):
	def __init__(self,feiyong=-2):
		self.attack = 4
		self.feiyong = -2

class tongji(object):
	def __init__(self.feiyong=-4):
		self.attack = 3
		
	