import maya.cmds as cmds
import maya.mel as mel


# Alt + W
def hotMove():
	moveQuery = cmds.manipMoveContext('Move', q=True, mode=True) + 2
	if moveQuery > 2:
		moveQuery = 0
	if moveQuery == 0:
		moveName = 'object'
	elif moveQuery == 2:
		moveName = 'world'
	cmds.manipMoveContext('Move', edit=True, mode=moveQuery)
	cmds.headsUpMessage('Move: ' + moveName)


# Alt + E
def hotRotate():
	rotateQuery = cmds.manipRotateContext('Rotate', q=True, mode=True) + 1
	if rotateQuery > 1:
		rotateQuery = 0
	if rotateQuery == 0:
		rotateName = 'object'
	elif rotateQuery == 1:
		rotateName = 'world'
	cmds.manipRotateContext('Rotate', edit=True, mode=rotateQuery)
	cmds.headsUpMessage('Rotate: ' + rotateName)


# Alt + 0
def zeroOut():
	selected = cmds.ls(sl=True)
	if selected:
		for obj in selected:
			for axis in ['x', 'y', 'z']:
				for attr in ['t', 'r', ]:
					try:
						cmds.setAttr('{}.{}{}'.format(obj, attr, axis), 0)
					except:
						print 'Zero out {}.{}{}. Skipped.'.format(obj, attr, axis)


# Alt + 0
def zeroAttrToDefaults():
	selected = cmds.ls(sl=True)
	if selected:
		for obj in selected:
			attributes = cmds.listAttr(obj, k=True)
			if attributes:
				for attr in attributes:
					default = cmds.attributeQuery(attr, node=obj, ld=True)[0]
					try:
						cmds.setAttr('{}.{}'.format(obj, attr), default)
					except:
						print 'Unable to zero out "{}.{}". Skipped.'.format(obj, attr)
	return


# Alt + S
def keyframeSpecial():
	mel.eval('performSetKeyframeArgList 1 {"0", "animationList"}; keyframe -time `currentTime -q` -tds 1;')


# Alt + G
def createNull():
	for x in cmds.ls(sl=True):
		name = '{0}_grp'.format(x)

		if cmds.objExists(name):
			name = '{0}_grp#'.format(x)

		par = cmds.listRelatives(x, parent=True)
		grp = cmds.group(n=name, em=True)
		cmds.delete(cmds.parentConstraint(x, grp))

		if par:
			cmds.parent(grp, par)

		cmds.parent(x, grp)


# Ctl + Alt + S
def incrementalSave():
	mel.eval('''
global proc incrementalSave () {
    int $DEBUG = 0; // make this 1 for debugging only

    // get the current filename	
    string $fname = `file -q -sn`; 
    if ($DEBUG) print ($fname + "\n");

    // make sure filename ends with .ma or .mb 
    int $len = `size $fname`;
    if ($DEBUG) print ($len + "\n");
    string $suffix = `substring $fname ($len-2) $len`;
    if ($DEBUG) print ($suffix + "\n");
    if (! ($suffix == ".ma" || $suffix == ".mb")) {
	error ("filename doesn't end with .ma or .mb\n");
    }

    // extract the main part of the filename, before the suffix
    string $suffixless = `substring $fname 1 ($len - 3)`;
    if ($DEBUG) print ($suffixless + "\n");

    // extract any digits at the end of the filename
    string $digits = `match "[0-9]*$" $suffixless`; 
    if ($DEBUG) print ("digits: " + $digits + "\n");

    // if there are no digits, tack on "000" and go around again.
    if ($digits == "") {
	string $newname = $suffixless + "000" + $suffix;
	if ($DEBUG) print ("no digits at end of name, renaming to " + $newname + "\n");
	file -rn $newname;
	incrementalSave;
    } else {

    // if there are serial number digits, calculate the new serial number
	int $n = (int) $digits;
	int $nextn = $n + 1;
	string $newdigits = (string) $nextn;

	// pad the serial number with "0" on the left as needed 
	int $ndigits = `size $digits`;
	int $nnewdigits = `size $newdigits`;
	if ($DEBUG) print ($newdigits + "\n");
	while ($ndigits > $nnewdigits) {
	    $newdigits = "0" + $newdigits;
	    $nnewdigits++;
	}
	if ($DEBUG) print ($newdigits + "\n");

	// put the new filename together, rename, and save
	int $lengthwithoutdigits = `size $suffixless` - `size $digits`;
	string $stringwithoutdigits = `substring $suffixless 1 $lengthwithoutdigits`;
	string $newname = $stringwithoutdigits + $newdigits + $suffix;
	if ($DEBUG) print ($newname + "\n");
	file -rn $newname;
	file -save;
    }
}

incrementalSave;
	''')


# Alt + (Num 1 - 9)
def cupSet(setIndex=1):
	name = 'teaCupSelectSet_{}'.format(setIndex)

	if 0 > setIndex > 9:
		raise ValueError('Index must be greater than 0 and less than 10')
		return
	else:
		if cmds.objExists(name):
			cmds.select(name)
			return
		else:
			selected = cmds.ls(sl=True)
			if not selected:
				cmds.warning('Nothing selected.')
				return
			else:
				cmds.sets(selected, name=name)
	return
