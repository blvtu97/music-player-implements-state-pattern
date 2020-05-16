from abc import ABC, abstractmethod

class MusicServiceState(ABC):

	@abstractmethod
	def configureService(self,musicService):
		pass

	def playPressed(self,musicService):
		pass

	def changeState(self,musicService, musicServiceState):
		pass



