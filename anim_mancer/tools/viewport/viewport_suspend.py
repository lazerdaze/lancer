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
'''
def suspendViewportToggle(o_O_l_1____1__1):
    o_O_____o = o_O_l_1____1__1.o_0__o__l__1_____l_____l_1____o_o_0_____1___1____O___O_o_O.isChecked()
    if o_O_____o:
        if not cmds.headsUpDisplay(o_O_l_1____1__1.o_____1____l_____O_o____1____O_____0__1__o___0_o____o___O_____o__1__o_____O, exists=True):
            try:
                cmds.hudButton(o_O_l_1____1__1.o_____1____l_____O_o____1____O_____0__1__o___0_o____o___O_____o__1__o_____O, allowOverlap=True, section=7, block=5, blockSize='large', visible=True, label='Viewport Suspended (Click Here to Unlock)', buttonWidth=300, buttonShape='roundRectangle', releaseCommand=lambda *args: o_O_l_1____1__1.setSuspendViewport(False))
            except RuntimeError:
                pass

    else:
        if cmds.headsUpDisplay(o_O_l_1____1__1.o_____1____l_____O_o____1____O_____0__1__o___0_o____o___O_____o__1__o_____O, exists=True):
            cmds.headsUpDisplay(o_O_l_1____1__1.o_____1____l_____O_o____1____O_____0__1__o___0_o____o___O_____o__1__o_____O, remove=True)
    cmds.refresh(suspend=o_O_____o)
    if not o_O_____o:
        o_____1_O__0_____o__O_____0().o_____0____1_____O___1()
        
def __doSuspendViewport(o_O_l_1____1__1):
    if o_____1_O__0_____o__O_____0().o___0____o___0__o__l____0_O:
        cmds.refresh(suspend=True)
        
def __o_1_l___l___o__0__O____o_____o__o(o_O_l_1____1__1):
    CORE.callbackBot.o_____0_____l_O_____1_____o_____1_____1(CORE.suspendViewport.o____o__l_o_____o____0)
    if o_O_l_1____1__1.suspendViewportState():
        return
    cmds.refresh(suspend=False)

'''


def suspend_viewport(value=True, *args, **kwargs):
	return

def suspend_viewport_toggle(*args, **kwargs):
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
