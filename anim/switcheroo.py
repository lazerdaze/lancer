# Switcheroo
# Instructions: switcheroo.show()
#
#
#
#

# Maya Modules
from maya import cmds, mel

########################################################################################################################
#
#
#	GLOBAL VARIABLES
#
#
########################################################################################################################

WINNAME = 'switcherooWindowUI'
ROTATIONORDER = ["xyz", "yzx", "zxy", "xzy", "yxz ", "zyx"]
WINTITLE = 'Switcheroo'

COLUMNWIDTH = 60
MARGIN = 10
SPACING = 5


########################################################################################################################
#
#
#	UTILITIES
#
#
########################################################################################################################

def getSelected():
    return cmds.ls(sl=True)


def zooChangeRoo(order):
    mel.eval('''
global proc zooChangeRoo( string $newRoo ) {
	string $selObjs[] = `ls -sl`;
	string $staticObjs[];
	string $animatedObjs[];
	string $rotateOrders[] = { "xyz","yzx","zxy","xzy","yxz ","zyx" };
	float $keyTimeList[];
	float $initialTime = `currentTime -q`;

	//source all dependencies
	//string $deps[] = `zooChangeRooDependencies -scripts`;
	//for( $script in $deps ) if( `exists $script` ) eval( "source " + $script );

	for( $obj in $selObjs ) if( size(`keyframe -q -tc $obj`)) $animatedObjs[( `size $animatedObjs` )] = $obj;
		else $staticObjs[( `size $staticObjs` )] = $obj;

	$keyTimeList = `keyframe -q -tc $animatedObjs`;
	$keyTimeList = `sort $keyTimeList`;
	$keyTimeList = `zooUtilsRemoveDupeArrayItems_float $keyTimeList`;
	for( $n = 0; $n <= `size $keyTimeList`; $n++ ) {
		int $t = $keyTimeList[$n];
		currentTime $t;
		for( $i = 0; $i < `size $animatedObjs`; $i++ ) {
			string $obj = $animatedObjs[$i];
			int $oldRooAttr = `getAttr ( $obj + ".rotateOrder" )`;
			string $oldRoo = $rotateOrders[$oldRooAttr];

			//make sure both the target object exist AND the object's source has a key on this frame
			if( `keyframe -t $t -q -kc $obj` ) {
				xform -p 1 -roo $newRoo $obj;
				xform -p 0 -roo $oldRoo $obj;
				}
			}
		}

	xform -p 1 -roo $newRoo $staticObjs;
	xform -p 0 -roo $newRoo $animatedObjs;

	currentTime $initialTime;
	}


global proc float[] zooChangeRooRemoveDuplicateTimes( float $array[] ) {
	float $returnArray[];
	float $prevVal = $array[0];

	$returnArray[0] = $array[0];
	for( $n = 1; $n < `size $array`; $n++ ) {
		if( $prevVal != $array[$n] ) $returnArray[( `size $returnArray` )] = $array[$n];
		$prevVal = $array[$n];
		}

	return $returnArray;
	}

global proc float[] zooUtilsRemoveDupeArrayItems_float( float $array[] ) {
	float $returnArray[];
	float $prevVal = $array[0];

	$returnArray[0] = $array[0];
	for( $n = 1; $n < `size $array`; $n++ ) {
		if( $prevVal != $array[$n] ) $returnArray[( `size $returnArray` )] = $array[$n];
		$prevVal = $array[$n];
		}

	return $returnArray;
	}

''')
    mel.eval('zooChangeRoo {};'.format(order))
    return


def optionMenuCallback(func, value, *args):
    return func(value)


########################################################################################################################
#
#
#	UI
#
#
########################################################################################################################

def ui():
    cmds.frameLayout(label='Rotation Order', bgs=True, mw=MARGIN, mh=MARGIN)
    cmds.columnLayout(adj=True)
    optionUI = cmds.optionMenu(cc=lambda *x: optionMenuCallback(func=zooChangeRoo,
                                                                value=cmds.optionMenu(optionUI, q=True, v=True)
                                                                ))
    for item in ROTATIONORDER:
        cmds.menuItem(label=item)
    cmds.setParent('..')
    cmds.setParent('..')
    return


def show(name=WINNAME, title=WINTITLE):
    if cmds.window(name, exists=True):
        cmds.deleteUI(name, window=True)

    window = cmds.window(name, title=title)
    cmds.columnLayout(adj=True)
    ui()
    cmds.setParent('..')

    cmds.showWindow(window)
    return
