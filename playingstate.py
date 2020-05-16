import musicservicestate as ms
import pausedstate as ps

class PlayingState(ms.MusicServiceState):

	def configureService(self,musicService):
		pass

	def playPressed(self,musicService):
		musicService.pause()
		self.changeState(musicService, ps.PausedState())

	def changeState(self,musicService, musicServiceState):
		musicService.setState(musicServiceState)
		