# LANCER.LANCERNODE
#
#
#
#
#

# Python Modules
import sys

# Maya Modules
from maya import cmds, mel, OpenMaya, OpenMayaMPx

NODENAME = 'lancerNode'
NODEID = OpenMaya.MTypeId(0x100fff)


class lancerNode(OpenMayaMPx.MPxNode):
	input = OpenMaya.MObject()
	output = OpenMaya.MObject()

	def __init__(self):
		OpenMayaMPx.MPxNode.__init__(self)

	def compute(self, plug, dataBlock):
		if plug == lancerNode.output:
			dataInput = dataBlock.inputValue(lancerNode.input)
			inputVal = dataInput.asFloat()
			output = inputVal * 2.0

			dataOutput = dataBlock.outputValue(lancerNode.output)

			dataOutput.setFloat(output)
			dataBlock.setClean(plug)
		else:
			return OpenMaya.kUnknownParameter


def nodeCreator():
	return OpenMayaMPx.asMPxPtr(lancerNode())


def nodeInitializer():
	# Function Set for Numeric Attributes
	mFnAttr = OpenMaya.MFnNumericAttribute()

	# Create Attributes (longName, shortName, type, value)
	lancerNode.input = mFnAttr.create('input', 'input', OpenMaya.MFnNumericData.kFloat, 0.0)
	mFnAttr.setReadable(True)
	mFnAttr.setWritable(True)
	mFnAttr.setStorable(True)
	mFnAttr.setKeyable(True)

	lancerNode.output = mFnAttr.create('output', 'output', OpenMaya.MFnNumericData.kFloat)
	mFnAttr.setReadable(True)
	mFnAttr.setWritable(False)
	mFnAttr.setStorable(False)
	mFnAttr.setKeyable(False)

	# Attach Attributes
	lancerNode.addAttribute(lancerNode.input)
	lancerNode.addAttribute(lancerNode.output)

	# Design Circuitry
	lancerNode.attributeAffects(lancerNode.input, lancerNode.output)
	return


def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerNode(NODENAME, NODEID, nodeCreator, nodeInitializer)
	except:
		sys.stderr.write("Failed to register command: {}.".format(NODENAME))


def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand(NODENAME)
	except:
		sys.stderr.write("Failed to unregister command: {}.".format(NODENAME))
