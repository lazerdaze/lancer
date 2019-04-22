'''
Control UI Picker - CUP
'''

import os
import maya.cmds as cmds
import maya.mel as mel
from functools import partial


class cup():

	def __init__(self):

		# Dir Var--
		DIRPATH = os.path.dirname(os.path.abspath(__file__))
		PREFFILE = os.path.join(DIRPATH, 'jt_cup_pref.py')

		self.defaultDir = PREFFILE

		if not os.path.exists(self.defaultDir):
			self.makeDefaultDir()

		# UI Var--

		self.win = 'CUP'
		self.pWin = '%s_addPickerWinUI' % self.win
		self.colSuffix = '%s_columnLayout' % self.win
		self.ctlSuffix = '%s_buttonControl' % self.win
		self.mar = 10
		self.col = 60
		self.cel = 80

		# Global Color Var--

		self.color = self.colorList()

		# Functions--

		self.ui()
		self.loadData(filePath=self.defaultDir)

	# Functions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def makeDefaultDir(self):
		file = open(self.defaultDir, 'w')
		file.write('{None}')
		file.close()

	def test(self, var, *args):
		print var

	def colorList(self, *args):
		indexColor = []

		indexColor.append([0.35, 0.35, 0.35])

		for x in range(1, 32, 1):
			c = []

			for y in cmds.colorIndex(x, q=True):
				c.append(round(y, 2))

			indexColor.append(c)

		return indexColor

	def loadData(self, filePath, debug=False, *args):

		# Load Dict from PY

		importFile = open(filePath, 'r')
		data = eval(importFile.read())
		importFile.close()

		if debug:
			print filePath
			print data
			print type(data)

		if None not in data:
			self.updateData(data)

	def updateData(self, data, *args):

		# From Dict

		for lay in data:

			# Create Tab

			layoutLabel = lay.split('_')[0]

			cmds.gridLayout(lay, cellWidthHeight=(self.cel, self.cel), ag=True, cr=True, p=self.tab)
			cmds.setParent('..')

			cmds.shelfTabLayout(self.tab, e=True, tabLabel=(lay, layoutLabel))

			for ctl in data[lay]:
				# Create Object

				annot = data[lay][ctl]['annotation']
				bgc = data[lay][ctl]['color']

				buttonCtl = cmds.button(ctl, l=ctl.split('_')[0], rs=True, p=lay, annotation=annot,
				                        c=partial(self.selectObjects, annot), bgc=bgc)

				self.pickerPopupMenu(buttonCtl)

	def saveData(self, filePath, debug=True, *args):

		data = {}

		if debug:
			print ''
			print ''
			print 'Cup File Save Data +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			print 'Tab: %s' % self.tab

		# Layout

		layoutData = {}
		queryTabCA = cmds.tabLayout(self.tab, q=True, ca=True)

		if queryTabCA:
			for lay in queryTabCA:

				if debug:
					print '\t\tLayout: %s' % lay

				# Button / Control

				ctlList = cmds.layout(lay, q=True, ca=True)

				if ctlList:

					controlAttrData = {}

					for ctl in ctlList:
						if ctl:

							# Get Button / Control Data

							label = cmds.button(ctl, q=True, l=True)
							annot = cmds.button(ctl, q=True, annotation=True)
							bgc = cmds.button(ctl, q=True, bgc=True)

							controlAttrData[ctl] = {'annotation': str(annot), 'color': bgc}

							if debug:
								print '\t\t\tButton: %s | Label: %s | Annotation: %s | HasBackgroundColor: %s | Color: %s' % (
								ctl, label, annot, bgc)
								print '\t\t\t%s' % controlAttrData

					layoutData[lay] = controlAttrData

			data = layoutData

		else:
			data = '{None}'

		if debug:
			print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			print ''
			print ''

		# Write To File

		if debug:

			print data

		else:

			# PY Export

			exportFile = open(filePath, 'w')
			exportFile.write(str(data))
			exportFile.close()

	def frame(self, l='', cl=False, cll=False, *args):
		cmds.frameLayout(l=l, bgs=True, mh=self.mar, mw=self.mar, cll=cll, cl=cl)

	def end(self):
		cmds.setParent('..')

	def formRow(self,
	            items=[],
	            exclude=[],
	            special=[],
	            specialColor=[1, 0, 0],
	            roundOff=1,
	            command=[],
	            *args):

		form = cmds.formLayout(nd=100)

		length = float(len(items))
		step = 100 / length

		masterList = []

		i = 0
		for v in items:

			if type(v) == float or type(v) == int:
				label = int(v * roundOff)

			elif type(v) == str:
				label = v.capitalize()

			if v in exclude:
				x = cmds.text(l=label, enable=False)

			else:
				x = cmds.button(l=label, c=partial(command, v), )

			if special:
				if v in special:
					cmds.button(x, e=True, bgc=specialColor)

			masterList.append(x)

			if i == 0:
				cmds.formLayout(form, edit=True,
				                attachForm=[(x, 'left', 0), (x, 'top', 0), (x, 'bottom', 0), ],
				                attachPosition=[(x, 'right', 1, step), ],
				                )

			else:
				cmds.formLayout(form, edit=True,
				                attachForm=[(x, 'top', 0), (x, 'bottom', 0), ],
				                attachControl=[(x, 'left', 2, masterList[i - 1]), ],
				                attachPosition=[(x, 'right', 1, step), ]
				                )

			step += 100 / length
			i += 1

		cmds.setParent('..')

	def nameInput(self, layout, title='Name', message='Enter Name: ', *args):

		layoutList = cmds.layout(layout, q=True, ca=True)

		prompt = cmds.promptDialog(title=title, message=message, button=['OK', 'Cancel'], defaultButton='OK',
		                           cancelButton='Cancel', dismissString='Cancel')

		if prompt == 'OK':

			inputName = cmds.promptDialog(query=True, text=True)

			if inputName:
				if layoutList:
					for x in layoutList:
						if inputName.lower() == x.split('_')[0].lower():
							var = False
							cmds.warning('CUP: Object already exists.')
							return None
						else:
							var = True

				else:
					var = True

				if var:
					return inputName



			else:
				cmds.warning('CUP: No name specified.')
				return None

	def pickerPrompt(self, t='Add Picker', tx='', c='', *args):

		if cmds.tabLayout(self.tab, q=True, ca=True):

			if cmds.window(self.pWin, exists=True):
				cmds.deleteUI(self.pWin, window=True)

			cmds.window(self.pWin, title=t, rtf=True)

			cmds.columnLayout(adj=True, )
			cmds.frameLayout(lv=False, mh=self.mar, mw=self.mar)
			self.promptName = cmds.textFieldGrp(l='Name: ', tx=tx, cw=[1, self.col], ad2=2)
			self.promptColor = cmds.colorIndexSliderGrp(l='Color: ', min=1, max=32, value=1,
			                                            cw=[[1, self.col], [2, self.col]])

			self.promptTab = cmds.optionMenuGrp(l='Tab: ', cw=[1, self.col], ad2=2)

			for x in cmds.tabLayout(self.tab, q=True, tl=True):
				cmds.menuItem(l=x)

			cmds.optionMenuGrp(self.promptTab, e=True, v=cmds.tabLayout(self.tab, q=True, st=True).split('_')[0])

			cmds.setParent('..')
			self.formRow(items=['ok', 'cancel'], command=c)
			cmds.setParent('..')

			cmds.showWindow(self.pWin)

	# WIP
	def pickerCommand(self, typ, *args):

		# Add Picker -------------------------------------------------------------------------------------------------------------------

		if typ == 'add':

			# Get Objects

			selected = cmds.ls(sl=True)

			# Get Layout

			tabPar = cmds.layout('%s_%s' % (str(cmds.optionMenuGrp(self.promptTab, q=True, v=True)), self.colSuffix),
			                     q=True, fpn=True)




		# Edit Picker -------------------------------------------------------------------------------------------------------------------

		elif typ == 'edit':
			pass

	def addPickerCommand(self, typ, *args):

		# Get Selected Objects

		selected = cmds.ls(sl=True)

		# Get Layout

		tabPar = cmds.layout('%s_%s' % (str(cmds.optionMenuGrp(self.promptTab, q=True, v=True)), self.colSuffix),
		                     q=True, fpn=True)
		layoutList = cmds.layout(tabPar, q=True, ca=True)

		if typ == 'ok':

			if selected:

				# Get / Check Name

				inputName = cmds.textFieldGrp(self.promptName, q=True, tx=True)
				inputColor = cmds.colorIndexSliderGrp(self.promptColor, q=True, v=True) - 1

				if inputName:
					if layoutList:
						for x in layoutList:
							if inputName.lower() == x.split('_')[0].lower():
								var = False
								cmds.warning('CUP: Picker already exists.')

							else:
								var = True
					else:
						var = True

					if var:
						# Create Picker

						buttonName = '%s_%s' % (inputName, self.ctlSuffix)
						buttonCtl = cmds.button(buttonName, l=inputName, rs=True, p=tabPar, annotation=str(selected),
						                        bgc=self.color[inputColor], c=partial(self.selectObjects, selected))
						self.pickerPopupMenu(buttonCtl)

						# Clean Up

						self.removeUI(self.pWin, typ='window')
						self.autoSave()

				else:
					cmds.warning('CUP: No name specified.')


			else:
				cmds.warning('CUP: Nothing selected.')



		elif typ == 'cancel':
			self.removeUI(self.pWin, typ='window')

	def autoSave(self, *args):
		self.saveData(debug=False, filePath=self.defaultDir)

	def pickerPopupMenu(self, par, *args):

		popUp = cmds.popupMenu(p=par)
		cmds.menuItem(l='Edit Picker', c=lambda *_: self.editPickerPrompt(ctl=par, menu=popUp))
		cmds.menuItem(d=True)
		cmds.menuItem(l='Add Selected', c=lambda *_: self.addObjectToPicker(ctl=par))
		cmds.menuItem(l='Remove Selected', c=lambda *_: self.removeObjectFromPicker(ctl=par))
		cmds.menuItem(d=True)
		cmds.menuItem(l='Delete Picker', c=lambda *_: self.removeUI(par, typ='control'))

	def addObjectToPicker(self, ctl, *args):

		newObjList = []
		selected = cmds.ls(sl=True)
		buttonObjs = cmds.button(ctl, q=True, annotation=True).replace('[', '').replace(']', '').replace("u'",
		                                                                                                 '').replace(
			"'", '').replace(' ', '').split(',')

		if selected:
			for x in selected:
				newObjList.append(x)

			for x in buttonObjs:
				newObjList.append(x)

			cmds.button(ctl, e=True, annotation=str(newObjList), c=partial(self.selectObjects, newObjList))
			cmds.select(newObjList)

			self.autoSave()

	def removeObjectFromPicker(self, ctl, *args):

		newObjList = []
		selected = cmds.ls(sl=True)
		buttonObjs = cmds.button(ctl, q=True, annotation=True).replace('[', '').replace(']', '').replace("u'",
		                                                                                                 '').replace(
			"'", '').replace(' ', '').split(',')

		if selected:
			for x in buttonObjs:
				if x not in selected:
					newObjList.append(x)

			cmds.button(ctl, e=True, annotation=str(newObjList), c=partial(self.selectObjects, newObjList))
			cmds.select(newObjList)

			self.autoSave()

	def editPickerPrompt(self, ctl, menu, *args):

		# Var

		self.editCtl = ctl
		self.editMenu = menu
		self.editLayout = self.getCurrentTab()

		# Prompt Window

		self.pickerPrompt(t='Edit Picker', c=self.editPickerCommand)

		# Update Prompt Window

		cmds.textFieldGrp(self.promptName, e=True, tx=cmds.button(ctl, q=True, l=True))
		cmds.colorIndexSliderGrp(self.promptColor, e=True, v=self.queryColor(ctl))

	def queryColor(self, ctl, *args):

		ctlColor = cmds.button(ctl, q=True, bgc=True)
		queryColor = []

		for x in ctlColor:
			queryColor.append(round(x, 2))

		if queryColor in self.color:
			return self.color.index(queryColor) + 1

		else:
			return 1

	def editPickerCommand(self, typ, *args):

		layoutPath = self.getCurrentTab()
		layoutList = cmds.layout(layoutPath, q=True, ca=True)

		tabPar = cmds.layout('%s_%s' % (str(cmds.optionMenuGrp(self.promptTab, q=True, v=True)), self.colSuffix),
		                     q=True, fpn=True)

		if typ == 'ok':

			# Rename

			inputName = cmds.textFieldGrp(self.promptName, q=True, tx=True)
			inputColor = cmds.colorIndexSliderGrp(self.promptColor, q=True, v=True) - 1

			if inputName:
				if layoutList:
					for x in layoutList:
						if inputName == x.split('_')[0]:
							var = False
						# cmds.warning('CUP: Picker already exists.')

						else:
							var = True
				else:
					var = True

				if var:

					if inputName != cmds.button(self.editCtl, q=True, l=True):
						# Get Name

						buttonName = '%s_%s' % (inputName, self.ctlSuffix)

						# Rename Button

						cmds.button(self.editCtl, e=True, l=inputName)
						self.editCtl = cmds.renameUI(self.editCtl, buttonName)

						# Replace PopupMenu

						self.removeUI(self.editMenu)
						self.pickerPopupMenu(self.editCtl)

			# Edit Layout

			if tabPar != layoutPath:
				self.orderLayout(self.editCtl, origin=layoutPath, destination=tabPar)

			# Edit Color

			if inputColor != cmds.button(self.editCtl, q=True, bgc=True):
				cmds.button(self.editCtl, e=True, bgc=self.color[inputColor])

			# Clean up

			self.removeUI(self.pWin, typ='window')
			self.autoSave()

		elif typ == 'cancel':
			self.removeUI(self.pWin, typ='window')

	def removeUI(self, item, typ='', *args):

		if typ == 'control':
			prompt = cmds.confirmDialog(title='Remove Picker?',
			                            message='Remove picker and all data asscoiated with it?', button=['Yes', 'No'],
			                            defaultButton='No', cancelButton='No', dismissString='No', icn='warning')

			if prompt == 'Yes':
				cmds.evalDeferred(lambda *_: cmds.deleteUI(item, control=True))

		elif typ == 'layout':
			prompt = cmds.confirmDialog(title='Remove Tab?', message='Remove tab and all data asscoiated with it?',
			                            button=['Yes', 'No'], defaultButton='No', cancelButton='No', dismissString='No',
			                            icn='warning')

			if prompt == 'Yes':
				cmds.evalDeferred(lambda *_: cmds.deleteUI(item, layout=True))

		elif typ == 'window':
			cmds.evalDeferred(lambda *_: cmds.deleteUI(item, window=True))

		else:
			cmds.evalDeferred(lambda *_: cmds.deleteUI(item))

	def createTab(self, *args):

		name = self.nameInput(layout=self.tab, title='Create Tab')

		if name:
			layoutName = '%s_%s' % (name, self.colSuffix)

			# cmds.columnLayout(layoutName, adj=True, )
			cmds.gridLayout(layoutName, cellWidthHeight=(self.cel, self.cel), ag=True, cr=True, p=self.tab, aec=False)
			cmds.setParent('..')

			cmds.shelfTabLayout(self.tab, e=True, tabLabel=(layoutName, name))

	def renameTab(self, *args):

		if cmds.layout(self.tab, q=True, ca=True):

			layoutPath = self.getCurrentTab()
			current = layoutPath.split('|')[-1]

			if layoutPath:

				name = self.nameInput(layout=layoutPath, title='Rename Tab')

				if name:
					layoutName = '%s_%s' % (name, self.colSuffix)

					cmds.renameUI(layoutPath, layoutName)
					cmds.tabLayout(self.tab, e=True, tli=[cmds.tabLayout(self.tab, q=True, sti=True), name])

					self.autoSave()

	def removeTab(self, *args):

		if cmds.layout(self.tab, q=True, ca=True):

			current = cmds.tabLayout(self.tab, q=True, st=True)
			layoutPath = cmds.layout(current, q=True, fpn=True)

			if layoutPath:
				prompt = cmds.confirmDialog(title='Remove Tab?', message='Remove tab and all data asscoiated with it?',
				                            button=['Yes', 'No'], defaultButton='No', cancelButton='No',
				                            dismissString='No', icn='warning')

				if prompt == 'Yes':
					cmds.evalDeferred(lambda *_: cmds.deleteUI(current, lay=True))

					self.autoSave()

	def getCurrentTab(self, *args):
		return cmds.layout(cmds.shelfTabLayout(self.tab, q=True, st=True), q=True, fpn=True)

	def selectObjects(self, items=[], *args):

		if type(items) == type('str'):
			items = items.replace('[', '').replace(']', '').replace("u'", '').replace("'", '').replace(' ', '').replace(
				'"', '').split(',')

		if items:
			# Check items in scene:

			found = []
			notFound = []

			for obj in items:

				if cmds.objExists(obj):
					var = True

				elif cmds.objExists(obj.split(':')[-1]):
					obj = obj.split(':')[-1]
					var = True

				elif cmds.objExists('*:%s' % obj.split(':')[-1]):
					obj = '*:%s' % obj.split(':')[-1]
					var = True

				else:
					var = False

				if var:
					found.append(obj)

				else:
					notFound.append(obj)

			if notFound:
				print '''CUP: '%s' doesn't exists in current scene.''' % notFound

			if found:
				modifiers = cmds.getModifiers()
				shift = bool((modifiers & 1) > 0)

				cmds.select(found, add=shift)

	def isShiftPressed(self, *args):

		modifiers = cmds.getModifiers()
		shift = bool((modifiers & 1) > 0)

		return shift

	def compareStr(par, child, *args):

		if child.lower() == par.lower():
			return True

		else:
			return False

	def orderLayout(self, item, origin, destination, *args):

		# --
		originList = cmds.layout(origin, q=True, ca=True)
		destinList = cmds.layout(destination, q=True, ca=True)

		if originList:
			for y1 in originList:
				cmds.control(y1, e=True, parent=self.tempLayout1)

		if destinList:
			for y2 in destinList:
				cmds.control(y2, e=True, parent=self.tempLayout2)

		# --

		cmds.control(item, e=True, parent=self.tempLayout2)

		# --

		tempList1 = cmds.layout(self.tempLayout1, q=True, ca=True)
		tempList2 = cmds.layout(self.tempLayout2, q=True, ca=True)

		if tempList1:
			for x1 in tempList1:
				cmds.control(x1, e=True, parent=origin)

		if tempList2:
			for x2 in tempList2:
				cmds.control(x2, e=True, parent=destination)

	def dragUI(self, dragControl, x, y, modifiers, *args):
		debug = False

		if debug:
			print 'DRAG CONTROL'
			print '-------------'
			print dragControl.split('|')[-1]
			print ''

	def dropUI(self, dragControl, dropControl, messages, x, y, dragType, *args):
		debug = False

		if debug:
			print 'DROP CONTROL'
			print '-------------'
			print dragControl
			print dropControl
			print ''

		if dragControl == dropControl:
			pass

		else:
			pass
		# Drop to other tab

	def pickerMenuItems(self, *args):
		cmds.menuItem(l='Add Picker', c=lambda *_: self.pickerPrompt(t='Add Picker', c=self.addPickerCommand))

	def tabMenuItems(self, *args):

		cmds.menuItem(l='Add Tab', c=self.createTab)
		cmds.menuItem(l='Rename Tab', c=self.renameTab)
		cmds.menuItem(d=True)
		cmds.menuItem(l='Remove Tab', c=self.removeTab)

	# Build UI +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def ui(self):

		if cmds.window(self.win, exists=True):
			cmds.deleteUI(self.win, window=True)

		if cmds.window(self.pWin, exists=True):
			cmds.deleteUI(self.pWin, window=True)

		cmds.window(self.win, title=self.win + ' - CONTROL UI PICKER')

		# Menu +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		cmds.menuBarLayout()
		cmds.menu(l='File')
		cmds.menuItem(l='Save', c=lambda *_: self.saveData(debug=False, filePath=self.defaultDir))
		cmds.menuItem(d=True)
		cmds.menuItem(l='Debug', c=lambda *_: self.saveData(debug=True))
		cmds.menu(l='Picker')
		self.pickerMenuItems()
		cmds.menu(l='Tab')
		self.tabMenuItems()
		cmds.setParent('..')

		form = cmds.formLayout()
		self.tab = cmds.shelfTabLayout(snt=True, scr=False, ntc=self.createTab, cr=True)

		# Popup Menu +++++++++++++++++++++++++++++++++++++++++++++++++++

		cmds.popupMenu()
		self.pickerMenuItems()
		cmds.menuItem(d=True)
		self.tabMenuItems()

		# Main UI ++++++++++++++++++++++++++++++++++++++++++++++++++++++

		# End UI ++++++++++++++++++++++++++++++++++++++++++++++++++++++

		cmds.setParent('..')
		cmds.setParent('..')

		self.tempLayout1 = cmds.columnLayout(bgc=[1, 0, 0], m=False)
		cmds.setParent('..')

		self.tempLayout2 = cmds.columnLayout(bgc=[0, 1, 0], m=False)
		cmds.setParent('..')

		cmds.formLayout(form, e=True,
		                attachForm=[(self.tab, 'left', 0), (self.tab, 'top', 0), (self.tab, 'bottom', 0),
		                            (self.tab, 'right', 0), ],
		                )

		cmds.showWindow(self.win)
