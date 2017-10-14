import ui
import qrcode
import imgUtil
import dialogs

class Scout (object):
	def __init__(self):
		self.gameData = {'teamName':'', 'mode':'', 'total cones':0, 'average cones mbg':0, 'spire':0, 'ground':0, 'mbg time':0, 'cone time':0, 'mbg20':0, 'mbg10':0, 'mbg5':0, 'preload':True}
		self.autoData = {}
		self.driverData = {}
		self.teamnum = ''
		self.l = {'total cones':'coneTxt', 'average cones mbg':'mbgTxt', 'spire':'spireTxt', 'ground':'gTxt', 'mbg time':'mbgTimeTxt', 'cone time':'coneTimeTxt', 'mbg20':'20Txt', 'mbg10':'10Txt', 'mbg5':'5Txt'}
		self.e = {'preload':'pswitch'}
		self.v = ui.load_view('Zone')
		self.display(self.v)
	
	def tapBtn(self,sender):
		'@type sender: ui.Button'
		t = sender.title
		n = sender.name 
		global qrImg
		
		if t == 'Team':
			sender.superview['teamTxt'].text = self.teamnum = dialogs.input_alert('Team Number')
		
		if t == 'Share':
			dialogs.share_image(qrImg)
			
		if (t == 'Autonomous'):
			mV = ui.load_view('Scout')
			mV.name = 'Autonomous' 
			if self.autoData == {}:
				self.autoData = self.gameData
			self.fillValues(mV,self.autoData)
			self.display(mV)
			mV.wait_modal() # this is great magic
			if self.gameData != {'teamName':'', 'mode':'', 'total cones':0, 'average cones mbg':0, 'spire':0, 'ground':0, 'mbg time':0, 'cone time':0, 'mbg20':0, 'mbg10':0, 'mbg5':0, 'preload':True}:
				self.autoData = self.gameData
			self.autoData['mode'] = 'auto'
			self.autoData['teamName'] = self.teamnum
			self.gameData = {'teamName':'', 'mode':'', 'total cones':0, 'average cones mbg':0, 'spire':0, 'ground':0, 'mbg time':0, 'cone time':0, 'mbg20':0, 'mbg10':0, 'mbg5':0, 'preload':True}
			sender.superview['qRView'].image = qrImg = imgUtil.pil2ui(qrcode.make((str(self.autoData)+str(self.driverData))))
			
		if (t == 'Driver Control'):
			mV = ui.load_view('Scout')
			mV.name = 'Driver Control' 
			if self.driverData == {}:
				self.driverData = self.gameData
			self.fillValues(mV,self.driverData)
			self.display(mV)
			mV.wait_modal() # this is great magic
			if self.gameData != {'teamName':'', 'mode':'', 'total cones':0, 'average cones mbg':0, 'spire':0, 'ground':0, 'mbg time':0, 'cone time':0, 'mbg20':0, 'mbg10':0, 'mbg5':0, 'preload':True}:
				self.driverData = self.gameData
			self.driverData['mode'] = 'driver'
			self.driverData['teamName'] = self.teamnum
			self.gameData = {'teamName':'', 'mode':'', 'total cones':0, 'average cones mbg':0, 'spire':0, 'ground':0, 'mbg time':0, 'cone time':0, 'mbg20':0, 'mbg10':0, 'mbg5':0, 'preload':True}
			sender.superview['qRView'].image = qrImg = imgUtil.pil2ui(qrcode.make((str(self.autoData)+str(self.driverData))))
			
		if len(n) > 0:
			if n == 'tcm' and self.gameData['total cones'] > 0:
				self.gameData['total cones']-=1
			if n == 'tcp':
				self.gameData['total cones']+=1
			if n == 'cmm' and self.gameData['average cones mbg'] > 0:
				self.gameData['average cones mbg']-=1
			if n == 'cmp':
				self.gameData['average cones mbg']+=1
			if n == 'hsm' and self.gameData['spire'] > 0:
				self.gameData['spire']-=1
			if n == 'hsp':
				self.gameData['spire']+=1
			if n == 'hgm' and self.gameData['ground'] > 0:
				self.gameData['ground']-=1
			if n == 'hgp':
				self.gameData['ground']+=1
			if n == 'm20m' and self.gameData['mbg20'] > 0:
				self.gameData['mbg20']-=1
			if n == 'm20p':
				self.gameData['mbg20']+=1
			if n == 'm10m' and self.gameData['mbg10'] > 0:
				self.gameData['mbg10']-=1
			if n == 'm10p':
				self.gameData['mbg10']+=1
			if n == 'm5m' and self.gameData['mbg5'] > 0:
				self.gameData['mbg5']-=1
			if n == 'm5p':
				self.gameData['mbg5']+=1
				
			sender.superview[self.l['total cones']].text = str(self.gameData['total cones'])
			sender.superview[self.l['average cones mbg']].text = str(self.gameData['average cones mbg'])
			sender.superview[self.l['spire']].text = str(self.gameData['spire'])
			sender.superview[self.l['ground']].text = str(self.gameData['ground'])
			sender.superview[self.l['mbg20']].text = str(self.gameData['mbg20'])
			sender.superview[self.l['mbg10']].text = str(self.gameData['mbg10'])
			sender.superview[self.l['mbg5']].text = str(self.gameData['mbg5'])
		
	def slide(self,sender):
		'@type sender: ui.Slider'
		t = sender.name
		if(t=='mbgSlider'):
			self.gameData['mbg time'] = int(sender.value * 20)
			sender.superview['mbgTimeTxt'].text = str(self.gameData['mbg time'])
		if(t=='coneSlider'):
			self.gameData['cone time'] = int(sender.value * 12)
			sender.superview['coneTimeTxt'].text = str(self.gameData['cone time'])
			
	def switch(self,sender):
		'@type sender: ui.Switch'
		self.gameData['preload'] = sender.value
		
	def display(self,mV):
		if min(ui.get_screen_size()) >= 768: # iPad
			mV.present('sheet')
		else: # iPhone
			mV.present(orientations=['portrait'])
	
	def fillValues(self,view,values):
		for key,value in self.l.items():
			view[value].text = str(values[key])
		for key,value in self.e.items():
			view[value].value = values[key]
	
Scout()
