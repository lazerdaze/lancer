# Project Modules

# Python Modules

# Maya Modules
from maya import cmds


# ======================================================================================================================
#
#
# Global
#
#
# ======================================================================================================================

# ======================================================================================================================
#
#
# Function
#
#
# ======================================================================================================================

def get_selected_anim_curve(*args, **kwargs):
	return cmds.keyframe(q=True, sl=True, name=True)


def get_raw_anim_curves(*args, **kwargs):
	result_curves = {}
	anim_curves = cmds.keyframe(q=True, sl=True, name=True)
	if anim_curves is None:
		return None
	for anim_curve in anim_curves:
		anim_keys = cmds.keyframe(q=True, sl=True, timeChange=True)
		start, end = int(anim_keys[0]), int(anim_keys[len(anim_keys) - 1])
		anim_dict = {}
		for i in range(start, end + 1):
			anim_dict[i] = cmds.keyframe(anim_curve, q=True, time=(i, i), ev=True)[0]
		result_curves[anim_curve] = anim_dict
	return result_curves


def get_selected(kind='dag', *args, **kwargs):
	return


# ======================================================================================================================
#
#
# Class
#
#
# ======================================================================================================================


# ======================================================================================================================
#
#
# Execute
#
#
# ======================================================================================================================

if __name__ == '__main__':
	pass
