import musicservicestate as ms
import playingstate as ps

class InitializeState(ms.MusicServiceState):

	def configureService(self, musicService):
		musicService.startService()
		self.playPressed(musicService)

	def playPressed(self,musicService):
		musicService.play()
		self.changeState(musicService,ps.PlayingState())

	def changeState(self,musicService, musicServiceState):
		musicService.setState(musicServiceState)
		