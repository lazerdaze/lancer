# LANCER.LANCERNODE
#
#
#
#
#

# Lancer Modules
from library import mathUtils
from rig import utils

# Python Modules
import sys

# Maya Modules
from maya import cmds, mel, OpenMaya, OpenMayaMPx

# TODO: Center of Gravity Node

'''
cmds.loadPlugin('I:\\lancer\\plugins\\lancerNode.py')
cmds.createNode('lancer')


# #Function Set for Numeric Attributes
# mFnAttr = OpenMaya.MFnNumericAttribute()
#
# # Create Attributes (longName, shortName, type, value)
# LancerNode.input = mFnAttr.create('input', 'input', OpenMaya.MFnNumericData.kFloat, 0.0)
# mFnAttr.setReadable(True)
# mFnAttr.setWritable(True)
# mFnAttr.setStorable(True)
# mFnAttr.setKeyable(True)
#
# LancerNode.output = mFnAttr.create('output', 'output', OpenMaya.MFnNumericData.kFloat)
# mFnAttr.setReadable(True)
# mFnAttr.setWritable(False)
# mFnAttr.setStorable(False)
# mFnAttr.setKeyable(False)
#
# # Attach Attributes
# LancerNode.addAttribute(LancerNode.input)
# LancerNode.addAttribute(LancerNode.output)
#
# # Design Circuitry
# LancerNode.attributeAffects(LancerNode.input, LancerNode.output)
'''


########################################################################################################################
#
#
#	Utilities
#
#
########################################################################################################################

def getApiNode(name):
	m_selectionList = OpenMaya.MSelectionList()
	m_node = OpenMaya.MObject()
	m_node_fn = OpenMaya.MFnDependencyNode()

	try:
		m_selectionList.add(name)
	except utils.NodeExistsError:
		raise utils.NodeExistsError('Api Node "{}" does not exist.'.format(name))

	m_selectionList.getDependNode(0, m_node)
	m_node_fn.setObject(m_node)
	return m_node_fn


def nameToNode(name):
	selectionList = OpenMaya.MSelectionList()
	selectionList.add(name)
	node = OpenMaya.MObject()
	selectionList.getDependNode(0, node)
	return node


def nameToNodePlug(attrName, nodeObject):
	depNodeFn = OpenMaya.MFnDependencyNode(nodeObject)
	attrObject = depNodeFn.attribute(attrName)
	plug = OpenMaya.MPlug(nodeObject, attrObject)
	return plug


########################################################################################################################
#
#
#	SDK Class
#
#
########################################################################################################################


def addExtraAttrToNode(name):
	'''
	Add custom extra attributes to the API node.

	:param name:    Node name
	:return bool:
	:usage:         addExtraAttrToNode('lambert1')
	'''

	m_node_fn = getApiNode(name)

	fAttr = OpenMaya.MFnNumericAttribute()
	aSampleFloat = fAttr.create("sampleFloat", "sf",
	                            OpenMaya.MFnNumericData.kFloat, 0.0)
	fAttr.setKeyable(True)
	fAttr.setStorable(True)
	fAttr.setDefault(1.0)

	# string attribute
	fAttr = OpenMaya.MFnTypedAttribute()
	aSampleTxt = fAttr.create("sampleTXT", "st",
	                          OpenMaya.MFnData.kString)
	fAttr.setKeyable(True)
	fAttr.setWritable(True)
	fAttr.setReadable(True)
	fAttr.setStorable(True)

	# boolean attribute
	fAttr = OpenMaya.MFnNumericAttribute()
	aSampleBool = fAttr.create("sampleBOOL", "sb",
	                           OpenMaya.MFnNumericData.kBoolean, True)
	fAttr.setKeyable(True)
	fAttr.setStorable(True)
	fAttr.setReadable(True)
	fAttr.setWritable(True)

	# multi compound attribute
	fAttr = OpenMaya.MFnCompoundAttribute()
	aCompound = fAttr.create("sampleCompound", "sc")
	fAttr.addChild(aSampleBool)  # child 0
	fAttr.addChild(aSampleTxt)  # child 1
	fAttr.addChild(aSampleFloat)  # child 2
	fAttr.setArray(True)  # create 'multi' attr
	fAttr.setKeyable(True)
	fAttr.setWritable(True)
	fAttr.setReadable(True)
	fAttr.setStorable(True)
	try:
		# try to add attributes using function set
		m_node_fn.addAttribute(aCompound)
	except:
		return False
	return True


def setExtraAttrValues(m_node_name, m_index, m_tuple):
	'''
	:param m_node_name:     node name
	:param m_index:         index of item where you want to write
	:param m_tuple:         ( True , 'Test', 4.2 )
						    m_tuple[0] - True
						    m_tuple[1] - 'Test'
						    m_tuple[2] - 4.2
	:return bool:
	:usage:                 setExtraAttrValues( 'lambert1', 1, ( False , 'Test', 4.2 )  )
	'''
	m_selectionList = OpenMaya.MSelectionList()
	m_node = OpenMaya.MObject()
	m_node_fn = OpenMaya.MFnDependencyNode()

	try:
		m_selectionList.add(m_node_name)
		m_selectionList.getDependNode(0, m_node)
		m_node_fn.setObject(m_node)
		m_attr = m_node_fn.attribute('sampleCompound')
		m_attr_plug = OpenMaya.MPlug(m_node, m_attr)

		# convert m_index to integer
		m_index = int(m_index)

		# write data stored in tuple to the node
		m_attr_plug.elementByLogicalIndex(m_index).child(0).setBool(m_tuple[0])
		m_attr_plug.elementByLogicalIndex(m_index).child(1).setString(m_tuple[1])
		m_attr_plug.elementByLogicalIndex(m_index).child(2).setFloat(m_tuple[2])

	except:
		return False
	return True


def printExtraAttrData(m_node_name):
	m_selectionList = OpenMaya.MSelectionList()  # create selection list
	m_node = OpenMaya.MObject()  # create MObject
	m_node_fn = OpenMaya.MFnDependencyNode()  # create a function set
	try:
		# add node with name 'lambert2'
		m_selectionList.add(m_node_name)
	except:
		return False
	# get first element in the selection list and connect with MObject
	m_selectionList.getDependNode(0, m_node)
	# connect MObject with function set
	m_node_fn.setObject(m_node)
	# find attribute by name using function set class
	#
	m_attr = m_node_fn.attribute('sampleCompound')
	# create MPlug object fo work with attribute
	# A plug is a point on a dependency node where a
	# particular attribute can be connected
	m_attr_plug = OpenMaya.MPlug(m_node, m_attr)
	# create int array fo storing indexes of available items
	#
	m_ind = OpenMaya.MIntArray()
	m_attr_plug.getExistingArrayAttributeIndices(m_ind)
	try:
		for i in m_ind:
			print("IND %s BOOL %s STR %s FLOAT %s"
			      % (i,
			         m_attr_plug.elementByLogicalIndex(i).child(0).asBool(),
			         m_attr_plug.elementByLogicalIndex(i).child(1).asString(),
			         m_attr_plug.elementByLogicalIndex(i).child(2).asFloat()))
	except:
		return False
	return True


def addSDK(parent, children=None, name='test', minValue=0, value=0, maxValue=1, *args, **kwargs):
	# API Node
	parent = getApiNode(parent)

	# Input Attr
	cmpAttr = OpenMaya.MFnCompoundAttribute()
	inputAttr = cmpAttr.create('input', 'input')
	cmpAttr.setArray(True)
	cmpAttr.setReadable(True)
	cmpAttr.setWritable(True)
	cmpAttr.setStorable(True)
	cmpAttr.setKeyable(True)
	cmpAttr.setUsesArrayDataBuilder(True)

	# Num Attr
	num = OpenMaya.MFnNumericAttribute()

	# Value
	valueAttr = num.create('value', 'value', OpenMaya.MFnNumericData.kFloat, float(value))
	num.setReadable(False)
	num.setWritable(True)
	num.setStorable(False)
	num.setKeyable(True)
	num.setMin(0.0)
	num.setMax(1.0)
	num.setDefault(0.0)
	cmpAttr.addChild(valueAttr)

	# Min
	minAttr = num.create('minValue', 'minValue', OpenMaya.MFnNumericData.kFloat, float(minValue))
	num.setReadable(False)
	num.setWritable(True)
	num.setStorable(True)
	num.setKeyable(False)
	cmpAttr.addChild(minAttr)

	# Max
	maxAttr = num.create('maxValue', 'maxValue', OpenMaya.MFnNumericData.kFloat, float(maxValue))
	num.setReadable(False)
	num.setWritable(True)
	num.setStorable(True)
	num.setKeyable(False)
	cmpAttr.addChild(maxAttr)

	# Attach Attributes
	parent.addAttribute(inputAttr)

	# Design Circuitry
	# parent.attributeAffects(getattr(parent, name), LancerNode.output)

	return


########################################################################################################################
#
#
#	Lancer Class
#
#
########################################################################################################################

'''
UserDefinedAttr

Input[0]
	- value
	- minTranslateX
	- minTranslateY
	- minTranslateZ
	- min...
	- maxTranslateX
	- maxTranslateY
	- maxTranslateZ
	- max...
	- index
		- index[0]
		- index[1]


Output is based on index. Have to remember the index in relation user defined output.

Output[0]
	- translateX
	- translateY
	- translateZ
	- rotateX
	- rotateY
	- rotateZ
	- scaleX
	- scaleY
	- scaleZ
'''


# TODO: SDK - Dealing with blending of values
# TODO: SDK - Dealing with mutiple objects

class LancerNode(OpenMayaMPx.MPxNode):
	name = 'lancer'
	id = OpenMaya.MTypeId(0x100fff)

	pose = OpenMaya.MObject()
	output = OpenMaya.MObject()

	def __init__(self):
		OpenMayaMPx.MPxNode.__init__(self)

	@staticmethod
	def creator():
		return OpenMayaMPx.asMPxPtr(LancerNode())

	@staticmethod
	def initialize():
		# Input Attr
		poseMFN = OpenMaya.MFnCompoundAttribute()
		poseAttr = poseMFN.create('pose', 'pose')
		poseMFN.setArray(True)
		poseMFN.setReadable(True)
		poseMFN.setWritable(True)
		poseMFN.setStorable(True)
		poseMFN.setKeyable(True)
		poseMFN.setUsesArrayDataBuilder(True)

		# Index
		indexMFN = OpenMaya.MFnTypedAttribute()
		indexAttr = indexMFN.create('index', 'index', OpenMaya.MFnData.kString)
		indexMFN.setWritable(True)
		indexMFN.setReadable(False)
		indexMFN.setStorable(True)
		indexMFN.setKeyable(False)
		LancerNode.addAttribute(indexAttr)
		poseMFN.addChild(indexAttr)

		# Driver
		diverMFN = OpenMaya.MFnNumericAttribute()
		driverAttr = diverMFN.create('driver', 'driver', OpenMaya.MFnNumericData.kFloat, 0.0)
		diverMFN.setReadable(False)
		diverMFN.setWritable(True)
		diverMFN.setStorable(True)
		diverMFN.setKeyable(True)
		diverMFN.setMin(0.0)
		diverMFN.setMax(1.0)
		diverMFN.setDefault(0.0)
		poseMFN.addChild(driverAttr)

		# Default, Min, Max
		unitMFN = OpenMaya.MFnNumericAttribute()

		for inputName in ['default', 'min', 'max']:
			for attr in ['translate', 'rotate', 'scale']:
				attrName = utils.camelCase(inputName, attr, capitalize=False)
				shortName = utils.camelCase(inputName, attr[0])
				unitAttr = unitMFN.createPoint(attrName, shortName)
				unitMFN.setWritable(True)
				unitMFN.setReadable(False)
				unitMFN.setStorable(True)
				unitMFN.setKeyable(False)
				poseMFN.addChild(unitAttr)

		# Add Input Attr
		LancerNode.pose = poseAttr
		LancerNode.addAttribute(poseAttr)

		# Output Attribute
		outputMFN = OpenMaya.MFnCompoundAttribute()

		outputAttr = outputMFN.create('output', 'output')
		outputMFN.setArray(True)
		outputMFN.setReadable(True)
		outputMFN.setWritable(False)
		outputMFN.setStorable(True)
		outputMFN.setKeyable(False)
		outputMFN.setUsesArrayDataBuilder(True)

		# Translate, Rotate, Scale
		for attribute in ['translate', 'rotate', 'scale']:
			if attribute == 'rotate':
				outputUnitMFN = OpenMaya.MFnUnitAttribute()
				dataType = OpenMaya.MFnUnitAttribute.kAngle
			else:
				outputUnitMFN = OpenMaya.MFnNumericAttribute()
				dataType = OpenMaya.MFnNumericData.kFloat

			for axis in ['x', 'y', 'z']:
				attrName = utils.camelCase(attribute, axis, capitalize=False)
				shortName = '{}{}'.format(attribute[0], axis)

				attr = outputUnitMFN.create(attrName, shortName, dataType, 0.0)
				outputUnitMFN.setReadable(True)
				outputUnitMFN.setWritable(False)
				outputUnitMFN.setStorable(False)
				outputUnitMFN.setKeyable(False)
				outputMFN.addChild(attr)

		# Add Output Attr
		LancerNode.output = outputAttr
		LancerNode.addAttribute(outputAttr)

		# Connect Attributes
		LancerNode.attributeAffects(poseAttr, outputAttr)
		return

	def _setDependentsDirty(self, plugBeingDirtied, affectedPlugs):
		thisNode = self.thisMObject()
		fnThisNode = OpenMaya.MFnDependencyNode(thisNode)

		if plugBeingDirtied.partialName() == 'A':
			pB = OpenMaya.MPlug(fnThisNode.findPlug('B'))
			affectedPlugs.append(pB)
			print 'Dirtying...'
		return

	def _postConstructor(self, *args):
		'''
	    MStatus status = MStatus::kSuccess;
	    // Get the datablock outside the compute with MPxNode::forceCache
	    MDataBlock block = this->forceCache();

	    // The remaining part is the same as compute
	    unsigned i, j;
	    MObject thisNode = thisMObject();
	    MPlug wPlug(thisNode, aWeights);

	    // Write into aWeightList
	    for( i = 0; i < 3; i++) {
	        status = wPlug.selectAncestorLogicalIndex( i, aWeightsList );
	        MDataHandle wHandle = wPlug.constructHandle(block);
	        MArrayDataHandle arrayHandle(wHandle, &status);
	        //McheckErr(status, "arrayHandle construction failed\n");
	        MArrayDataBuilder arrayBuilder = arrayHandle.builder(&status);

	        for( j = 0; j < i+2; j++) {
	            MDataHandle handle = arrayBuilder.addElement(j,&status);
	            float val = (float)(1.0f*(i+j));
	            handle.set(val);
	        }
	        status = arrayHandle.set(arrayBuilder);

	        wPlug.setValue(wHandle);
	        wPlug.destructHandle(wHandle);
		'''

		# dataBlock = OpenMaya.MDataBlock(self._forceCache())
		return

	def _compute(self, plug, dataBlock):
		'''
		thisNode = self.thisMObject()

		print 'computing'

		if plug == LancerNode.output:
			inputVal = dataBlock.inputValue(LancerNode.input).asFloat()

			# Calculations
			result = inputVal * 2.0

			# Output Values
			dataOutput = dataBlock.outputValue(LancerNode.output)
			dataOutput.setFloat(result)

			# Clean Up
			dataBlock.setClean(plug)
		else:
			return OpenMaya.kUnknownParameter


		dataHandle = dataBlock.inputArrayValue(LancerNode.pose)
		index = dataHandle.elementCount()

		print 'Input Index Count {}'.format(index)

		inputData = []
		for i in range(index):
			# Go to the first child in the array
			dataHandle.jumpToElement(i)

			# First Input entry: input[0]
			inputDataHandle = dataHandle.inputValue().child(LancerNode.pose)
			childHandle = OpenMaya.MArrayDataHandle(inputDataHandle)

			# Child Arrays
			childIndex = childHandle.elementCount()

			data = []
			for c in range(childIndex):
				childHandle.jumpToElement(c)
				value = childHandle.inputValue().asFloat()
				data.append(value)
				print 'Input[{}][{}]:{}'.format(i, c, value)

			inputData.append(data)
		'''

		return


########################################################################################################################
#
#
#	Initialize Plugin
#
#
########################################################################################################################


def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject, 'Justin Tirado', '1.0.0', 'Any')
	try:
		mplugin.registerNode(LancerNode.name, LancerNode.id, LancerNode.creator, LancerNode.initialize)
	except:
		sys.stderr.write("Failed to register command: {}.".format(LancerNode.name))
		raise
	# evalAETemplate()
	return


def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand(LancerNode.name)
	except:
		sys.stderr.write("Failed to unregister command: {}.".format(LancerNode.name))
		raise
	return


def evalAETemplate():
	mel.eval('''
    global proc AEprRemapValueTemplate(string $nodeName)
    {
        editorTemplate -beginScrollLayout;
            editorTemplate -beginLayout "prRemapValue Attributes" -collapse 0;
                editorTemplate -label "sampleMethod" -addControl "sampleMethod";
                editorTemplate -label "inputValue" -addControl "inputValue";
                editorTemplate -label "counter" -addControl "counter";
                AEaddRampControl ($nodeName+".value");
                AEaddRampControl ($nodeName+".color");
            editorTemplate -endLayout;
            editorTemplate -beginLayout "Input and Output Ranges";
                editorTemplate -label "inputMin" -addControl "inputMin";
                editorTemplate -label "inputMax" -addControl "inputMax";
                editorTemplate -label "outputMin" -addControl "outputMin";
                editorTemplate -label "outputMax" -addControl "outputMax";
            editorTemplate -endLayout;
            AEdependNodeTemplate $nodeName;
            editorTemplate -addExtraControls;
        editorTemplate -endScrollLayout;
    };
    ''')
