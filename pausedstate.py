import musicservicestate as ms
import playingstate as ps

class PausedState(ms.MusicServiceState):

	def configureService(self,musicService):
		pass

	def playPressed(self,musicService):
		musicService.unpause()
		self.changeState(musicService, ps.PlayingState())

	def changeState(self,musicService, musicServiceState):
		musicService.setState(musicServiceState)
		