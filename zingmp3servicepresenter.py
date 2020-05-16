from abc import ABC, abstractmethod

class MusicServicePresenter(ABC):

	@abstractmethod
	def play(self):
		pass

	def pause(self):
		pass
		
	def unpause(self):
		pass

	def loadPlaylist(self):
		pass