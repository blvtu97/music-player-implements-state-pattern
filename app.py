from abc import ABC, abstractmethod

import initializestate as it
import playingstate as pl 
import zingmp3service as zs

import tkinter as tkr
import tkinter.messagebox as mbox

from tkinter.filedialog import askdirectory
from tkinter.filedialog import Open

from PIL import Image, ImageTk

import pygame
import os

import zingmp3servicepresenter as zmsp

import pathlib


class AppView(ABC):

	@abstractmethod
	def onPlay(self):
		pass

	def onPause(self):
		pass
		
	def onUnpause(self):
		pass

	def onPlayList(self):
		pass
		
class App(AppView):

	def __init__(self):
		self.initUI()

	def setMusicService(self, musicService):
		self.musicService = musicService
		self.musicService.setView(self)

	def initUI(self):
		'''Create a window'''
		self.player = tkr.Tk()
		self.player.title('Zing Mp3')
		self.player.geometry('350x440')

		'''Create a menubar'''
		self.menuBar = tkr.Menu(self.player)
		self.player.config(menu = self.menuBar)

		self.fileMenu = tkr.Menu(self.menuBar)
		self.fileMenu.add_command(label="Open Playlist", command = self.openPlaylist)
		self.menuBar.add_cascade(label="File", menu = self.fileMenu)

		'''Register widget'''
		self.savePath = os.getcwd()
		img = ImageTk.PhotoImage(Image.open(self.savePath + "/play.png"))
		self.btnPlay = tkr.Button(self.player, image = img, command = self.onButtonClicked)
		self.btnPlay.image = img 
		self.btnPlay.pack()

	def updateUI(self):
		self.playlist = tkr.Listbox(self.player,highlightcolor = 'green',selectmode = tkr.SINGLE)
		self.playlist.bind("<<ListboxSelect>>", self.onSelectSong)
		for item in self.songList:
			self.playlist.insert(tkr.END,item)
		self.playlist.pack(fill = "both",expand = "yes")

		self.var = tkr.StringVar()
		self.songtitle = tkr.Label(self.player,textvariable = self.var)
		self.songtitle.pack()

	def show(self):
		self.player.mainloop()

	def onButtonClicked(self):
		if self.musicService._state == None:
			mbox.showerror("Error","Please select a playlist!")
			return
		self.musicService._state.playPressed(self.musicService)

	def onSelectSong(self,val):
		index = val.widget.curselection()
		value = val.widget.get(index)
		self.playlist.activate(index)
		self.var.set(value)

		self.musicService.setState(it.InitializeState())

	def openPlaylist(self):
		self.musicService.loadPlaylist()

	def onPlay(self):
		#img = ImageTk.PhotoImage(Image.open("D:/PythonProject/ProgramData/nhom13/pause.png")) 
		img = ImageTk.PhotoImage(Image.open(self.savePath + "/pause.png"))
		self.btnPlay.config(text = 0)
		self.btnPlay.config(image = img)
		self.btnPlay.image = img 

	def onPause(self):
		img = ImageTk.PhotoImage(Image.open(self.savePath + "/play.png"))
		self.btnPlay.config(text = 0)
		self.btnPlay.config(image = img)
		self.btnPlay.image = img 

	def onUnpause(self):
		img = ImageTk.PhotoImage(Image.open(self.savePath + "/pause.png"))
		self.btnPlay.config(text = 0)
		self.btnPlay.config(image = img)
		self.btnPlay.image = img 

	def onPlaylist(self):
		directory = askdirectory()
		os.chdir(directory)
		self.songList = os.listdir()
		self.updateUI()

		self.musicService.setPlaylist(self.playlist)
		self.musicService.setState(it.InitializeState())


def main():
	zingMp3 = App()
	zingMp3.setMusicService(zs.ZingMp3Service())
	zingMp3.show()

main()










