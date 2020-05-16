import zingmp3servicepresenter as zsp
import tkinter as tkr
import pygame


class ZingMp3Service(zsp.MusicServicePresenter):

	def __init__(self):
		self.service = pygame
		self._state = None

	def setView(self,app):
		self._appMusic = app

	def setState(self,state):
		self._state = state
		self._state.configureService(self)

	def setPlaylist(self,playlist):
		self.playlist = playlist

	def startService(self):
		self.service.init()
		self.service.mixer.init()

	def play(self):
		self.service.mixer.music.load(self.playlist.get(tkr.ACTIVE))
		self.service.mixer.music.play()
		self._appMusic.onPlay()

	def pause(self):
		self.service.mixer.music.pause()
		self._appMusic.onPause()

	def unpause(self):
		self.service.mixer.music.unpause()
		self._appMusic.onUnpause()

	def loadPlaylist(self):
		self._appMusic.onPlaylist()


