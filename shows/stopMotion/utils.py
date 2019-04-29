# Python Modules
import random
import time
from functools import wraps, partial
import _ctypes

# Maya Modules
from maya import cmds, mel
from maya.api import OpenMaya, OpenMayaAnim


# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================


def undo(func):
	""" Puts the wrapped `func` into a single Maya Undo action, then
		undoes it when the function enters the finally: block """
	
	@wraps(func)
	def _undofunc(*args, **kwargs):
		try:
			# start an undo chunk
			cmds.undoInfo(ock=True)
			cmds.cycleCheck(e=False)
			return func(*args, **kwargs)
		finally:
			# after calling the func, end the undo chunk and undo
			cmds.undoInfo(cck=True)
			cmds.cycleCheck(e=True)
	
	return _undofunc


def viewportOff(func):
	"""
	Decorator - turn off Maya display while func is running.
	if func will fail, the error will be raised after.
	"""
	
	@wraps(func)
	def wrap(*args, **kwargs):
		
		# mel.eval("paneLayout -e -manage false $gMainPane")
		cmds.refresh(suspend=True)
		
		try:
			return func(*args, **kwargs)
		except Exception:
			raise
		finally:
			# mel.eval("paneLayout -e -manage true $gMainPane")
			cmds.refresh(suspend=False)
	
	return wrap


# FIXME: Need to solely depend on animation curves. Dag selection is not reliable.
def max_value_change(frame, randomness, nodes):
	values = []
	
	if not isinstance(nodes, (list, dict, tuple)):
		nodes = [nodes]
	
	for node in nodes:
		chList = cmds.listAttr(node, keyable=True)
		
		for ch in chList:
			if not cmds.keyframe(node + '.' + ch, q=True, n=True):
				continue
			
			val2 = cmds.keyframe(node, query=True, attribute=ch, eval=True, t=(frame + 1, frame + 1))
			val1 = cmds.keyframe(node, query=True, attribute=ch, eval=True, t=(frame, frame))
			
			valChng = float(val2[0]) - float(val1[0])
			
			cmds.setKeyframe(node, attribute=ch, v=val1[0] + (randomness * (valChng * random.random())), t=frame)
			
			if ch in ('rotateX', 'rotateY', 'rotateZ'):
				valChng = valChng / 100
			
			values.append(abs(valChng))
	return max(values)


def max_anim_curve_change(curves, frame, randomness, layer='BaseAnimation'):
	values = []
	
	if not isinstance(curves, (list, dict, tuple)):
		curves = [curves]
	
	for curve in curves:
		value2 = cmds.keyframe(curve, query=True, eval=True, t=(frame + 1, frame + 1))
		value1 = cmds.keyframe(curve, query=True, eval=True, t=(frame, frame))
		
		value_change = float(value2[0]) - float(value1[0])
		cmds.setKeyframe(curve, v=value1[0] + (randomness * (value_change * random.random())), t=frame,
		                 animLayer=layer)
		
		value_change = value_change / 100
		
		values.append(abs(value_change))
	return max(values)


@viewportOff
def generate_stop_motion(nodes, ratio=0.5, randomness=0.0, start=1001, end=1200, layer=None):
	key = 0
	remove = 0
	step = 0
	
	if not isinstance(nodes, (list, dict, tuple)):
		nodes = [nodes]
	
	targets = []
	
	for node in nodes:
		if cmds.keyframe(node, q=True, name=True):
			targets.append(node)
	
	if targets:
		
		# Get anim curves based on layer
		if layer:
			targets_curves = get_curves_from_anim_layer(layer)
		else:
			targets_curves = targets
		
		# Get Counter
		autoCounter = []
		for frame in range(start, end):
			if layer:
				autoCounter.append(max_anim_curve_change(curves=targets_curves,
				                                         frame=frame,
				                                         randomness=randomness,
				                                         layer=layer))
			else:
				autoCounter.append(max_value_change(frame, randomness, targets))
		
		autoCounterSorted = sorted(autoCounter)
		
		# Threshold
		threshold = autoCounterSorted[0] + ((autoCounterSorted[-1] - autoCounterSorted[0]) * ratio)
		
		for frame in range(start, end - 1):
			if key == 1:
				key = 0
				cmds.cutKey(targets_curves, time=(frame, frame))
				remove = remove + 1
			elif key == 0:
				valChange = autoCounter[frame - start]
				if valChange == 0:
					key = 1
					cmds.cutKey(targets_curves, time=(frame, frame))
					remove = remove + 1
				if valChange < threshold:
					key = 1
					cmds.keyTangent(targets_curves, t=(frame, frame), ott='step')
					step = step + 1
				elif valChange > threshold:
					key = 0
					cmds.keyTangent(targets_curves, t=(frame, frame), ott='step')
					step = step + 1
	return


def set_curve_to_step(curves, *args, **kwargs):
	return cmds.keyTangent(curves, outTangentType='step')


def curves_value_change(curves, start, end, *args, **kwargs):
	result = []
	query = {}
	
	# Remove Static From Calc
	for curve in curves:
		is_static = False
		values = [curves[curve][frame] for frame in curves[curve]]
		
		if len(values) == 1:
			is_static = True
		
		if all(x == values[0] for x in values):
			is_static = True
		
		if not is_static:
			query[curve] = curves[curve]
	
	# Get Max Values
	for frame in range(start, end):
		values = []
		
		for curve in query:
			value2 = float(query[curve][frame + 1])
			value1 = float(query[curve][frame])
			
			value_change = (value2 - value1) / 100.0
			values.append(abs(value_change))
		
		result.append(max(values))
	return result


def generate_stop_motion_curves(curves, ratio=0.5, start=1001, end=1200):
	start = int(start)
	end = int(end)
	
	# Get Counter
	counter = curves_value_change(curves, start, end)
	counter_sorted = sorted(counter)
	
	# Threshold
	threshold = counter_sorted[0] + ((counter_sorted[-1] - counter_sorted[0]) * ratio)
	
	key = 0
	remove = 0
	step = 0
	
	remove_list = []
	add_list = []
	
	for frame in range(start, end):
		if key == 1:
			key = 0
			
			# Remove
			remove_list.append(frame)
			remove = remove + 1
		
		elif key == 0:
			value_change = counter[frame - start]
			
			if value_change == 0:
				key = 1
				
				# Remove
				remove_list.append(frame)
				remove = remove + 1
			
			if value_change < threshold:
				key = 1
				
				# Add
				add_list.append(frame)
				
				step = step + 1
			
			elif value_change > threshold:
				key = 0
				
				# Add
				add_list.append(frame)
				step = step + 1
	
	processed_curves = {}
	
	for curve in curves:
		save_keys = {}
		set_curve_to_step(curve)
		
		for frame in curves[curve]:
			if frame not in remove_list:
				save_keys[frame] = curves[curve][frame]
		
		processed_curves[curve] = save_keys
	
	# Convert To Step
	
	return processed_curves


def get_time_range(*args, **kwargs):
	start = cmds.playbackOptions(query=True, min=True)
	end = cmds.playbackOptions(query=True, max=True)
	return int(start), int(end)


# FIXME: Bake to layer is a bit slow. Could just copy keys?
@viewportOff
def bake_to_layer(nodes, layer, *args, **kwargs):
	cmds.bakeResults(nodes,
	                 simulation=True,
	                 time=get_time_range(),
	                 sampleBy=1,
	                 disableImplicitControl=True,
	                 preserveOutsideKeys=True,
	                 sparseAnimCurveBake=False,
	                 removeBakedAttributeFromLayer=False,
	                 removeBakedAnimFromLayer=False,
	                 bakeOnOverrideLayer=False,
	                 minimizeRotation=True,
	                 controlPoints=False,
	                 shape=False,
	                 destinationLayer=layer,
	                 attribute=['tx', 'ty', 'tz', 'rx', 'ry', 'rz']
	                 )
	return


def bake_keys(nodes, *args, **kwargs):
	cmds.bakeResults(nodes,
	                 simulation=True,
	                 time=get_time_range(),
	                 sampleBy=1,
	                 disableImplicitControl=True,
	                 preserveOutsideKeys=True,
	                 sparseAnimCurveBake=False,
	                 removeBakedAttributeFromLayer=False,
	                 removeBakedAnimFromLayer=False,
	                 bakeOnOverrideLayer=False,
	                 minimizeRotation=True,
	                 controlPoints=False,
	                 shape=False,
	                 )
	return


def get_all_assemblies(*args, **kwargs):
	return cmds.ls(assemblies=True)


def attribute_exist(node, attribute, *args, **kwargs):
	return cmds.attributeQuery(attribute, node=node, ex=True)


def set_current_time(value, *args, **kwargs):
	return cmds.currentTime(value)


def delete_keys(dag_nodes, *args, **kwargs):
	if not isinstance(dag_nodes, (dict, tuple, list)):
		dag_nodes = [dag_nodes]
	
	for dag in dag_nodes:
		for attr in ['t', 'r']:
			for axis in ['x', 'y', 'z']:
				for typ in ['TU', 'TL', 'TA']:
					con = cmds.listConnections('{}.{}{}'.format(dag, attr, axis),
					                           s=True,
					                           type='animCurve{}'.format(typ),
					                           scn=True
					                           )
					if con:
						try:
							cmds.delete(con)
						except RuntimeError:
							print 'Delete skipped: {}'.format(con)
	return


def create_anim_layer(name, override=True, *args, **kwargs):
	return cmds.animLayer(name, override=override)


def anim_layer_add(name, nodes, *args, **kwargs):
	if not isinstance(nodes, (list, dict, tuple)):
		nodes = [nodes]
	
	for node in nodes:
		for attr in ['t', 'r']:
			for axis in ['x', 'y', 'z']:
				attribute = '{}.{}{}'.format(node, attr, axis)
				if not cmds.getAttr(attribute, lock=True):
					cmds.animLayer(name, edit=True, attribute=attribute)
					transfer_anim(node, '{}{}'.format(attr, axis), name)
	return


def transfer_anim(node, attribute, layer):
	time_range = get_time_range()
	can_paste = False
	
	try:
		cmds.copyKey(node, attribute=attribute, time=time_range, animLayer='BaseAnimation')
		can_paste = True
	except RuntimeError:
		try:
			cmds.copyKey(node, attribute=attribute, time=time_range)
			can_paste = True
		except RuntimeError:
			pass
	
	# Fixme: Attributes with no animation connections
	if can_paste:
		try:
			cmds.pasteKey(node, attribute=attribute, option="replace", animLayer=layer)
		except:
			pass
	return


def get_top_anim_layer(*args, **kwargs):
	index_dict = {}
	index_list = []
	
	anim_layers = cmds.treeView('AnimLayerTabanimLayerEditor', q=True, children=True)
	
	if anim_layers:
		for layer in anim_layers:
			index = cmds.treeView('AnimLayerTabanimLayerEditor', q=True, idx=layer)
			index_list.append(index)
			index_dict[index] = layer
		
		return index_dict[max(index_list)]
	return


def get_all_anim_layers(*args, **kwargs):
	return cmds.ls(type='animLayer')


def get_selected_anim_layer(*args, **kwargs):
	return cmds.treeView('AnimLayerTabanimLayerEditor', q=True, si=True)


def scene_has_anim_layers(*args, **kwargs):
	query = get_all_anim_layers()
	return True if query else False


def clean_anim_layers(*args, **kwargs):
	query = get_all_anim_layers()
	
	if len(query) == 1:
		cmds.delete('BaseAnimation')
	return


def remove_from_anim_layer(node, layer, *args, **kwargs):
	attributes = cmds.listAttr(node, keyable=True, locked=False)
	
	if attributes:
		for attribute in attributes:
			try:
				cmds.animLayer(layer, edit=True, removeAttribute='{}.{}'.format(node, attribute))
			except RuntimeError:
				pass
	return


def get_curves_from_anim_layer(layer, *args, **kwargs):
	query = cmds.animLayer(layer, q=True, animCurves=True)
	return query if query else None


def get_raw_curves(nodes):
	"""
	:param nodes:
	:return: dict   {curve: {frame:value}}
	"""
	
	result_curves = {}
	anim_curves = cmds.keyframe(nodes, q=True, name=True)
	
	if anim_curves is None:
		return None
	
	for anim_curve in anim_curves:
		anim_keys = cmds.keyframe(nodes, q=True, timeChange=True)
		start, end = int(min(anim_keys)), int(max(anim_keys))
		anim_dict = {}
		
		for frame in range(start, end + 1):
			anim_dict[frame] = cmds.keyframe(anim_curve, q=True, time=(frame, frame), ev=True)[0]
		
		result_curves[anim_curve] = anim_dict
	
	return result_curves


def copy_original_curves(nodes):
	"""
	Copy selected animation curves to clipboard and return the names with start and end frames
	so we can paste them back later

	:return: list of anim curve names, start frame, end frame
	:rtype: list, float, float
	"""
	anim_curves = cmds.keyframe(nodes, q=True, name=True)
	
	if anim_curves is None:
		return None, None, None
	
	anim_keys = cmds.keyframe(nodes, q=True, timeChange=True)
	start, end = int(min(anim_keys)), int(max(anim_keys))
	
	cmds.copyKey(anim_curves, t=(start, end))
	return anim_curves, start, end


def paste_clipboard_curves(anim_curves, start, end):
	# type: (list, float, float) -> None
	"""
	Paste original anim curves we stored when the preview button was pressed

	:param anim_curves: list of animation curves
	:param start: start frame
	:param end: end frame
	:return: None
	"""
	return cmds.pasteKey(anim_curves, t=(start, end), o="replace")


def add_keys(anim_curve, key_dict):
	# type: (unicode, dict) -> None
	"""
	Add keyframes to animation curve

	:param anim_curve: animation curve name
	:param key_dict: dictionary of keyframes in {frame_number (float): value (float)} format
	:return: None
	"""
	
	unit = OpenMaya.MTime.uiUnit()
	nodeNattr = cmds.listConnections(anim_curve, d=True, s=False, p=True)[0]
	selList = OpenMaya.MSelectionList()
	selList.add(nodeNattr)
	mplug = selList.getPlug(0)
	dArrTimes = OpenMaya.MTimeArray()
	dArrVals = OpenMaya.MDoubleArray()
	
	if 'rotate' in nodeNattr:
		for i in key_dict.keys():
			dArrTimes.append(OpenMaya.MTime(float(i), unit))
			dArrVals.append(OpenMaya.MAngle.uiToInternal(key_dict[i]))
	else:
		for i in key_dict.keys():
			dArrTimes.append(OpenMaya.MTime(float(i), unit))
			dArrVals.append(key_dict[i])
	
	crvFnc = OpenMayaAnim.MFnAnimCurve(mplug)
	crvFnc.addKeys(dArrTimes, dArrVals, crvFnc.kTangentAuto, crvFnc.kTangentStep)
	return


def apply_curves(original_curves, processed_curves=None, start=1001, end=1200):
	for curve in original_curves.keys():
		try:
			cmds.cutKey(curve, time=(start + 0.001, end - 0.001), option="keys", cl=True)
			
			if processed_curves is not None:
				add_keys(curve, processed_curves[curve])
			else:
				add_keys(curve, original_curves[curve])
		except:
			continue
	return


def curve_generator(curve, start, end):
	for frame in range(start, end + 1):
		yield cmds.keyframe(curve, q=True, time=(frame, frame), eval=True)[0]
	return


def remove_generateor_indexs(generator, indexs):
	index = 0
	for item in generator:
		if index not in indexs:
			yield item
		index += 1
	return


def divide_chunks(items, num_chunks):
	len_items = len(items)
	size = int(round(float(len_items) / float(num_chunks)))
	
	for i in range(0, len(items), size):
		yield items[i:i + num_chunks]


def merge_dicts(*args):
	result = {}
	
	for arg in args:
		if isinstance(arg, (list, tuple)):
			for item in arg:
				if isinstance(item, dict):
					result.update(item)
		elif isinstance(arg, dict):
			result.update(arg)
	
	return result


def time_range_to_zero(start, end):
	start = int(start)
	end = int(end)
	
	new_start = 0
	new_end = 0
	offset = 0
	
	if start == 0:
		return start, end
	
	elif start < 0:
		offset = start * -1
		new_end = end + offset
	else:
		offset = 0 - start
		new_end = end + offset
	
	return new_start, new_end



# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================

class Apex_Name(object):
	WTSR = 'wattson'
	EAOR = 'octane'
	ECIR = 'bangalore'
	ECCR = 'crypto'
	EAGR = 'gibraltar'
	ECMR = 'mirage'


class Apex_Rig(object):
	def __init__(self,
	             parent=None,
	             name=None,
	             assembly=None,
	             namespace=None,
	             index=0,
	             visibility=True,
	             proxy=False,
	             controls=True,
	             reference=None,
	             state=None,
	             loaded=True,
	             filepath=None,
	             sets=None,
	             ):
		
		self.parent = parent
		self.name = name
		self.reference = reference
		self.assembly = assembly
		self.namespace = namespace
		self.index = index
		self.visibility = visibility
		self.proxy = proxy
		self.controls = controls
		self.state = state
		self.loaded = loaded
		self.filepath = filepath
		self.sets = sets
		
		self.all_controls = []
		self.main_controls = []
		self.face_controls = []
		self.dyn_joints = []
		self.dyn_controls = []
		
		self.dyn_antenna_attr = 'C_antenna_dynamic'
		self.dyn_antenna_blend_attr = 'C_antenna_dyn_blend'
		self.dyn_antenna_attract_attr = 'C_antenna_inputAttract'
		self.dyn_hair_attr = 'hair_dynamic'
		self.dyn_hair_blend_attr = 'hair_dyn_blend'
		self.dyn_hair_attract_attr = 'hair_inputAttract'
		self.dyn_mapper = {
			'C_hairA_01_BONE'  : 'C_hairA_1_FK_CTRL',
			'C_hairA_02_BONE'  : 'C_hairA_2_FK_CTRL',
			'C_hairA_03_BONE'  : 'C_hairA_3_FK_CTRL',
			'C_hairA_04_JNT'   : 'C_hairA_4_FK_CTRL',
			'C_hairB_01_BONE'  : 'C_hairB_1_FK_CTRL',
			'C_hairB_02_BONE'  : 'C_hairB_2_FK_CTRL',
			'C_hairB_03_BONE'  : 'C_hairB_3_FK_CTRL',
			'C_hairB_04_BONE'  : 'C_hairB_4_FK_CTRL',
			'C_hairB_04_JNT'   : 'C_hairB_4_FK_CTRL',
			'C_hairB_05_JNT'   : 'C_hairB_5_FK_CTRL',
			'C_hairC_01_BONE'  : 'C_hairC_1_FK_CTRL',
			'C_hairC_02_BONE'  : 'C_hairC_2_FK_CTRL',
			'C_hairC_03_BONE'  : 'C_hairC_3_FK_CTRL',
			'C_hairC_04_JNT'   : 'C_hairC_4_FK_CTRL',
			'C_antena_01_BONE' : 'C_antenna_1_FK_CTRL',
			'C_antena_02_BONE' : 'C_antenna_2_FK_CTRL',
			'C_antena_03_BONE' : 'C_antenna_3_FK_CTRL',
			'C_antena_04_BONE' : 'C_antenna_4_FK_CTRL',
			'C_antena_05_BONE' : 'C_antenna_5_FK_CTRL',
			'C_antena_06_JNT'  : 'C_antenna_6_FK_CTRL',
			'C_hairA_root_CTRL': None,
			'C_hairB_root_CTRL': None,
			'C_hairC_root_CTRL': None,
		}
		
		self.find_assemblies()
		self.find_rig_controls()
	
	def __str__(self):
		value = ''
		for x in vars(self).iterkeys():
			value += '{}: {}\n'.format(x, vars(self)[x])
		return value
	
	def find_assemblies(self, *args, **kwargs):
		if self.namespace:
			self.assembly = [x for x in get_all_assemblies() if x.split(':')[0] == self.namespace]
		return
	
	def find_rig_controls(self, *args, **kwargs):
		control_set = 'CONTROLS'
		face_set = 'FACE_SLDR'
		dyn_set = 'DYN_JOINTS'
		
		if self.namespace:
			body_name = '{}:{}'.format(self.namespace, control_set)
			face_name = '{}:{}'.format(self.namespace, face_set)
			dyn_name = '{}:{}'.format(self.namespace, dyn_set)
			
			if cmds.objExists(body_name):
				self.all_controls = cmds.sets(body_name, q=True)
				self.main_controls = [x for x in cmds.sets(body_name, q=True) if cmds.objectType(x) != 'objectSet']
			
			if cmds.objExists(face_name):
				self.face_controls = cmds.sets(face_name, q=True)
			
			if cmds.objExists(dyn_name):
				self.dyn_joints = cmds.sets(dyn_name, q=True)
			
			self.dyn_controls = []
			
			for item in self.dyn_mapper.keys():
				dyn_control = '{}:{}'.format(self.namespace, self.dyn_mapper[item])
				
				if cmds.objExists(dyn_control):
					self.dyn_controls.append(dyn_control)
		
		return
	
	def set_dyn(self, value):
		self.set_dyn_hair(value)
		self.set_dyn_antenna(value)
		return
	
	def set_dyn_hair(self, value):
		if self.assembly:
			for node in self.assembly:
				if attribute_exist(node, self.dyn_hair_attr):
					cmds.setAttr('{}.{}'.format(node, self.dyn_hair_attr), value)
				
				if attribute_exist(node, self.dyn_hair_blend_attr):
					cmds.setAttr('{}.{}'.format(node, self.dyn_hair_blend_attr), int(not value))
				
				if attribute_exist(node, self.dyn_hair_attract_attr):
					cmds.setAttr('{}.{}'.format(node, self.dyn_hair_attract_attr), int(not value))
		return
	
	def set_dyn_antenna(self, value):
		if self.assembly:
			for node in self.assembly:
				if attribute_exist(node, self.dyn_antenna_attr):
					cmds.setAttr('{}.{}'.format(node, self.dyn_antenna_attr), value)
				
				if attribute_exist(node, self.dyn_antenna_attract_attr):
					cmds.setAttr('{}.{}'.format(node, self.dyn_antenna_attract_attr), value)
				
				if attribute_exist(node, self.dyn_antenna_blend_attr):
					blend_value = 0.75 if value else 1.0
					cmds.setAttr('{}.{}'.format(node, self.dyn_antenna_blend_attr), blend_value)
		return
	
	def transfer_dyn_to_controls(self, *args, **kwargs):
		nulls = []
		destinations = []
		
		if self.dyn_joints:
			for source in self.dyn_joints:
				destination = None
				
				if self.namespace:
					name = source.split(':')[-1]
				else:
					name = source
				
				if name in self.dyn_mapper:
					destination = self.dyn_mapper[name]
					
					if self.namespace:
						destination = '{}:{}'.format(self.namespace, destination)
				
				if destination:
					delete_keys(source)
					null = cmds.group(empty=True)
					cmds.parentConstraint(source, null, mo=False)
					nulls.append(null)
					destinations.append(destination)
			
			if nulls and destinations:
				set_current_time(get_time_range()[0])
				self.set_dyn(1)
				
				# Bake Nulls
				bake_keys(nulls)
				self.set_dyn(0)
				
				for null in nulls:
					index = nulls.index(null)
					cmds.parentConstraint(null, destinations[index])
				
				# Bake Destinations
				bake_keys(destinations)
				
				# Cleanup
				cmds.delete(nulls)
		return
