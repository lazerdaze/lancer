//Maya ASCII 2018ff07 scene
//Name: legGlobal.ma
//Last modified: Sat, May 12, 2018 08:47:34 AM
//Codeset: 1252
requires maya "2018ff07";
requires -nodeType "decomposeMatrix" "matrixNodes" "1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201711281015-8e846c9074";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -n "legGlobal_L_cmpnt";
	rename -uid "0E378926-444A-68FF-58B9-3F987790DD6A";
	setAttr ".ove" yes;
	setAttr ".ovc" 19;
	setAttr ".ovrgb" -type "float3" 0.059300009 0.5043 0.17050005 ;
createNode transform -n "legGlobal_L_input" -p "legGlobal_L_cmpnt";
	rename -uid "6195041D-49BC-6253-98B1-4BA978F47BFB";
	addAttr -ci true -sn "endWorld" -ln "endWorld" -at "matrix";
	setAttr ".endWorld" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -5.5511151231257827e-15 -4.1078251911130792e-15 8.8817841970012523e-16 1;
createNode transform -n "legGlobal_L_output" -p "legGlobal_L_cmpnt";
	rename -uid "AD423288-48DD-1660-FC35-3990B94570F5";
	addAttr -ci true -sn "rolledAnkle" -ln "rolledAnkle" -nn "rolledAnkle" -at "matrix";
	addAttr -ci true -sn "toeAngle" -ln "toeAngle" -at "doubleAngle";
	addAttr -ci true -sn "tarsiAngle" -ln "tarsiAngle" -at "doubleAngle";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	addAttr -ci true -sn "upVectorWorld" -ln "upVectorWorld" -at "matrix";
	addAttr -ci true -sn "rawAnkleControl" -ln "rawAnkleControl" -at "matrix";
	setAttr ".nts" -type "string" "tarsi angle represents the angle betwaddAttr -ln \"chainEnd\" -at \"matrix\";een the world flat ankle and the tarsi vector (from ankle/beginning of tarsi to beginning of toes).\nToe angle is the following angle down, the one between toes and tarsi";
createNode transform -n "control" -p "legGlobal_L_cmpnt";
	rename -uid "731D5B2F-477A-8093-C727-038F2AE35086";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
createNode transform -n "legGlobal_L_animParameters" -p "|legGlobal_L_cmpnt|control";
	rename -uid "8EA7B613-4D2E-F0EE-E8F9-E3B2E4D1A044";
	addAttr -ci true -k true -sn "roll" -ln "roll" -smn -1.7 -smx 3.14 -at "doubleAngle";
	setAttr -k on ".roll";
createNode transform -n "roll_mechanics" -p "|legGlobal_L_cmpnt|control";
	rename -uid "4CD0995C-49B8-C82B-8037-75B6CBFC5609";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
createNode transform -n "legGlobal_L_ankle_rest_srt" -p "roll_mechanics";
	rename -uid "05AC6C11-484A-B5FF-CE03-A3BF05F24D5C";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr ".nts" -type "string" "right now the rest is manually placed and used as a static value to figure out the roll's ankle level offset from.\nTo make the component more dynamic and responsive to configuration this will need to eventually be the non-rolled default produced by the defaults";
createNode joint -n "legGlobal_L_ankle_rolled_srt" -p "legGlobal_L_ankle_rest_srt";
	rename -uid "E0331096-439D-B72C-735A-D780195FCDC8";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 84.553748547758588 9.5416640443905503e-15 180 ;
	setAttr ".radi" 0.5;
	setAttr ".nts" -type "string" "this is currently not connected to anything. Being the ankle we will want to compensate for the roll and make sure it remains world aligned, it should only be a matter of arithmetics on a few angles";
createNode transform -n "legGlobal_L_roll_world_srt" -p "roll_mechanics";
	rename -uid "0E959FFA-42A9-F097-0624-579669490C2B";
createNode joint -n "legGlobal_L_roll_heel_srt" -p "legGlobal_L_roll_world_srt";
	rename -uid "3217ED01-4005-E9FD-10BA-33922256F19F";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.1;
createNode joint -n "legGlobal_L_roll_tip_srt" -p "legGlobal_L_roll_heel_srt";
	rename -uid "7D7C5D2F-4DBD-564F-C264-ED8DB128BC64";
	setAttr ".r" -type "double3" -21.065155320812835 180 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.1;
createNode joint -n "legGlobal_L_roll_tarsi_srt" -p "legGlobal_L_roll_tip_srt";
	rename -uid "0641A02A-4304-F9E4-6ED4-E28631E02DDA";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.1;
createNode joint -n "legGlobal_L_roll_tarsiEnd_srt" -p "legGlobal_L_roll_tarsi_srt";
	rename -uid "36A70538-4FC8-7127-9AC5-F1952F082250";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.1;
createNode transform -n "legGlobal_L_worldAnkle_ctrl_srtBuffer" -p "|legGlobal_L_cmpnt|control";
	rename -uid "4DFF54C9-4976-E442-C936-34B4336A936D";
createNode transform -n "legGlobal_L_worldAnkle_ctrl" -p "legGlobal_L_worldAnkle_ctrl_srtBuffer";
	rename -uid "F115B55D-4841-CBC6-1902-D1A4610C79D6";
	setAttr -av ".tx";
	setAttr -av ".ty";
	setAttr -av ".tz";
createNode nurbsCurve -n "legGlobal_L_worldAnkle_ctrlShape" -p "legGlobal_L_worldAnkle_ctrl";
	rename -uid "5EE8CBF6-47C0-EAC7-4543-12802D3AB7CB";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 0.26105238444010315 0.52210476888020629 0.78315715332030944 1.0442095377604126
		 1.3052619222005157 1.5663143066406189 1.827366691080722 2.0884190755208252 2.3494714599609283
		 2.6105238444010315 2.8715762288411346 3.1326286132812378 3.3936809977213409 3.6547333821614441
		 3.9157857666015472 4.1768381510416503 4.4378905354817535 4.6989429199218566 4.9599953043619598
		 5.2210476888020629 5.4821000732421661 5.7431524576822692 6.0042048421223724 6.2652572265624755
		
		25
		1.2246467991473532e-16 1.2246467991473532e-16 -2
		-0.51763809020504137 1.1829179713786698e-16 -1.9318516525781366
		-0.99999999999999978 1.0605752387249069e-16 -1.7320508075688774
		-1.4142135623730949 8.6595605623549341e-17 -1.4142135623730951
		-1.7320508075688772 6.1232339957367673e-17 -1.0000000000000002
		-1.9318516525781364 3.1696191514317674e-17 -0.51763809020504192
		-2 3.4691420382247109e-32 -5.6655388976479796e-16
		-1.9318516525781368 -3.1696191514317612e-17 0.51763809020504092
		-1.7320508075688779 -6.1232339957367623e-17 0.99999999999999944
		-1.4142135623730958 -8.6595605623549304e-17 1.4142135623730947
		-1.0000000000000009 -1.0605752387249068e-16 1.7320508075688772
		-0.51763809020504259 -1.1829179713786698e-16 1.9318516525781366
		-1.0661542508461184e-15 -1.2246467991473535e-16 2.0000000000000004
		0.51763809020504059 -1.1829179713786703e-16 1.9318516525781373
		0.99999999999999922 -1.0605752387249075e-16 1.7320508075688783
		1.4142135623730947 -8.6595605623549403e-17 1.4142135623730963
		1.7320508075688772 -6.1232339957367747e-17 1.0000000000000013
		1.9318516525781368 -3.1696191514317742e-17 0.51763809020504303
		2.0000000000000009 -8.9076663320122757e-32 1.4547323094649232e-15
		1.931851652578138 3.1696191514317569e-17 -0.51763809020504026
		1.732050807568879 6.1232339957367611e-17 -0.99999999999999911
		1.4142135623730969 8.6595605623549304e-17 -1.4142135623730947
		1.000000000000002 1.0605752387249069e-16 -1.7320508075688774
		0.51763809020504359 1.1829179713786701e-16 -1.9318516525781371
		1.898821519314986e-15 1.2246467991473537e-16 -2.0000000000000009
		;
createNode transform -n "legGlobal_L_upVector_ctrl_srtBuffer" -p "|legGlobal_L_cmpnt|control";
	rename -uid "B24C6ADF-47FB-4CF1-D3C5-34BB75007AF4";
createNode transform -n "legGlobal_L_upVector_ctrl" -p "legGlobal_L_upVector_ctrl_srtBuffer";
	rename -uid "751C37B4-4A1E-FFB8-09FE-8B8CFAAAB421";
createNode nurbsCurve -n "legGlobal_L_upVector_ctrl" -p "|legGlobal_L_cmpnt|control|legGlobal_L_upVector_ctrl_srtBuffer|legGlobal_L_upVector_ctrl";
	rename -uid "30FFA44A-4AA6-E614-1708-E09534DD1A89";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		2.2204460492503131e-16 -1 -1
		0 0 -0.66395180606905013
		-2.2204460492503131e-16 1 -1
		0 0 0
		2.2204460492503131e-16 -1 -1
		;
createNode transform -n "legGlobal_L_configParameters" -p "|legGlobal_L_cmpnt|control";
	rename -uid "9E9BA6F1-4184-ABC8-6461-7DA220D98DAD";
	addAttr -ci true -k true -sn "toeRest" -ln "toeRest" -smn -1.7 -smx 3.14 -at "doubleAngle";
	addAttr -ci true -k true -sn "tarsirest" -ln "tarsirest" -smn -1.7 -smx 3.14 -at "doubleAngle";
	addAttr -ci true -k true -sn "toeLength" -ln "toeLength" -smn 0.01 -smx 10 -at "double";
	addAttr -ci true -k true -sn "tarsiLength" -ln "tarsiLength" -smn 0.01 -smx 10 -at "double";
	addAttr -ci true -sn "plantLength" -ln "plantLength" -min 0 -max 100 -at "double";
	addAttr -ci true -sn "ankleRest" -ln "ankleRest" -at "doubleAngle";
	addAttr -ci true -sn "ankleGlobalOffset" -ln "ankleGlobalOffset" -at "matrix";
	addAttr -ci true -sn "upVecGlobalOffset" -ln "upVecGlobalOffset" -at "matrix";
	setAttr -k on ".toeRest";
	setAttr -k on ".tarsirest";
	setAttr -k on ".toeLength";
	setAttr -k on ".tarsiLength";
	setAttr -k on ".plantLength";
createNode transform -n "legGlobal_L_worldAnkle_rolled_srt" -p "|legGlobal_L_cmpnt|control";
	rename -uid "D7EFCE8C-4FB2-A767-7420-D194093C348E";
createNode transform -n "guide" -p "legGlobal_L_cmpnt";
	rename -uid "9282F201-44BC-1498-A587-EBA4E678FEBE";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode transform -n "legGlobal_L_guide_global_ctrl" -p "|legGlobal_L_cmpnt|guide";
	rename -uid "8C6F2391-4B02-2F4E-551F-EB9BB3AA8A79";
	setAttr ".t" -type "double3" 3.2788051294853009 0.13294181866603688 0.013700291599500813 ;
createNode nurbsCurve -n "legGlobal_L_guide_global_ctrlShape" -p "legGlobal_L_guide_global_ctrl";
	rename -uid "BAB28D54-4DD2-FFFD-46A6-178032C820AF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 13 2 no 3
		14 0 1 2 3 4 5 6 7 8 9 10 11 12 13
		14
		0.50000000000000022 -6.106226635438361e-16 -0.5
		-0.50000000000000022 6.106226635438361e-16 0.5
		-0.50000000000000022 6.106226635438361e-16 2
		-1.0000000000000004 1.2212453270876722e-15 2
		0 0 3
		1.0000000000000004 -1.2212453270876722e-15 2
		0.50000000000000022 -6.106226635438361e-16 2
		0.50000000000000022 -6.106226635438361e-16 0.5
		2.0000000000000009 -2.4424906541753444e-15 0.5
		2.0000000000000009 -2.4424906541753444e-15 1
		3.0000000000000004 -3.1086244689504383e-15 0
		2.0000000000000009 -2.4424906541753444e-15 -1
		2.0000000000000009 -2.4424906541753444e-15 -0.5
		0.50000000000000022 -6.106226635438361e-16 -0.5
		;
createNode transform -n "legGlobal_L_guide_basisVector" -p "legGlobal_L_guide_global_ctrl";
	rename -uid "C5E8485C-4A0D-CE9B-EE44-3B88788296FF";
	setAttr ".t" -type "double3" 0 0 1 ;
createNode transform -n "legGlobal_L_guide_heel_ctrl" -p "legGlobal_L_guide_global_ctrl";
	rename -uid "E884B276-4D40-697F-6277-8AADBA434E8E";
	setAttr ".t" -type "double3" -3.3306690738754696e-16 0 -2.1093375553363201 ;
	setAttr ".ro" 2;
createNode nurbsCurve -n "legGlobal_L_guide_heel_ctrlShape" -p "legGlobal_L_guide_heel_ctrl";
	rename -uid "75699B71-48AA-23B2-FF88-58BC825854F3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 0.26105238444010315 0.52210476888020629 0.78315715332030944 1.0442095377604126
		 1.3052619222005157 1.5663143066406189 1.827366691080722 2.0884190755208252 2.3494714599609283
		 2.6105238444010315 2.8715762288411346 3.1326286132812378 3.3936809977213409 3.6547333821614441
		 3.9157857666015472 4.1768381510416503 4.4378905354817535 4.6989429199218566 4.9599953043619598
		 5.2210476888020629 5.4821000732421661 5.7431524576822692 6.0042048421223724 6.2652572265624755
		
		25
		2.2204460492503128e-16 0.42562035253973907 -1.5359963201678048e-16
		1.5265566588595902e-16 0.41111769071239207 0.11015865322053343
		3.0531133177191805e-16 0.36859803766710275 0.21281017626986951
		2.2204460492503131e-16 0.30095903749185859 0.30095903749185859
		1.6653345369377348e-16 0.21281017626986959 0.36859803766710281
		1.6653345369377348e-16 0.11015865322053366 0.41111769071239218
		1.1102230246251565e-16 2.4810633504451924e-16 0.42562035253973918
		5.5511151231257827e-17 -0.11015865322053335 0.41111769071239218
		5.5511151231257827e-17 -0.21281017626986939 0.36859803766710286
		-2.7755575615628914e-17 -0.30095903749185848 0.30095903749185871
		-1.6653345369377348e-16 -0.36859803766710275 0.21281017626986978
		-7.6327832942979512e-17 -0.41111769071239207 0.11015865322053375
		-2.2204460492503131e-16 -0.42562035253973918 9.9350572156140903e-17
		-1.5265566588595902e-16 -0.41111769071239229 -0.11015865322053336
		-1.6653345369377348e-16 -0.36859803766710303 -0.21281017626986945
		-1.9428902930940239e-16 -0.30095903749185871 -0.30095903749185848
		-1.1102230246251565e-16 -0.21281017626986989 -0.36859803766710286
		-1.6653345369377348e-16 -0.11015865322053379 -0.41111769071239218
		-1.3877787807814457e-16 -1.8204393730541235e-16 -0.42562035253973929
		-8.3266726846886741e-17 0.1101586532205333 -0.41111769071239246
		-2.7755575615628914e-17 0.21281017626986939 -0.36859803766710314
		2.7755575615628914e-17 0.30095903749185848 -0.30095903749185887
		1.8041124150158794e-16 0.36859803766710275 -0.21281017626987012
		1.7347234759768071e-16 0.41111769071239213 -0.11015865322053403
		2.2204460492503116e-16 0.4256203525397394 -5.3162644412773625e-16
		;
createNode transform -n "legGlobal_L_guide_tip_ctrl" -p "legGlobal_L_guide_heel_ctrl";
	rename -uid "3017BC2E-4C65-856B-1920-FA8F4E859E16";
	setAttr ".t" -type "double3" 0 0 5 ;
	setAttr -l on -k off ".ty";
	setAttr -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "legGlobal_L_guide_tip_ctrlShape" -p "legGlobal_L_guide_tip_ctrl";
	rename -uid "F101F6EF-4A4D-D5BE-8C13-FC90FC62CE0E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 0.26105238444010315 0.52210476888020629 0.78315715332030944 1.0442095377604126
		 1.3052619222005157 1.5663143066406189 1.827366691080722 2.0884190755208252 2.3494714599609283
		 2.6105238444010315 2.8715762288411346 3.1326286132812378 3.3936809977213409 3.6547333821614441
		 3.9157857666015472 4.1768381510416503 4.4378905354817535 4.6989429199218566 4.9599953043619598
		 5.2210476888020629 5.4821000732421661 5.7431524576822692 6.0042048421223724 6.2652572265624755
		
		25
		2.2204460492503128e-16 0.42562035253973907 -1.5359963201678048e-16
		1.5265566588595902e-16 0.41111769071239207 0.11015865322053343
		3.0531133177191805e-16 0.36859803766710275 0.21281017626986951
		2.2204460492503131e-16 0.30095903749185859 0.30095903749185859
		1.6653345369377348e-16 0.21281017626986959 0.36859803766710281
		1.6653345369377348e-16 0.11015865322053366 0.41111769071239218
		1.1102230246251565e-16 2.4810633504451924e-16 0.42562035253973918
		5.5511151231257827e-17 -0.11015865322053335 0.41111769071239218
		5.5511151231257827e-17 -0.21281017626986939 0.36859803766710286
		-2.7755575615628914e-17 -0.30095903749185848 0.30095903749185871
		-1.6653345369377348e-16 -0.36859803766710275 0.21281017626986978
		-7.6327832942979512e-17 -0.41111769071239207 0.11015865322053375
		-2.2204460492503131e-16 -0.42562035253973918 9.9350572156140903e-17
		-1.5265566588595902e-16 -0.41111769071239229 -0.11015865322053336
		-1.6653345369377348e-16 -0.36859803766710303 -0.21281017626986945
		-1.9428902930940239e-16 -0.30095903749185871 -0.30095903749185848
		-1.1102230246251565e-16 -0.21281017626986989 -0.36859803766710286
		-1.6653345369377348e-16 -0.11015865322053379 -0.41111769071239218
		-1.3877787807814457e-16 -1.8204393730541235e-16 -0.42562035253973929
		-8.3266726846886741e-17 0.1101586532205333 -0.41111769071239246
		-2.7755575615628914e-17 0.21281017626986939 -0.36859803766710314
		2.7755575615628914e-17 0.30095903749185848 -0.30095903749185887
		1.8041124150158794e-16 0.36859803766710275 -0.21281017626987012
		1.7347234759768071e-16 0.41111769071239213 -0.11015865322053403
		2.2204460492503116e-16 0.4256203525397394 -5.3162644412773625e-16
		;
createNode transform -n "legGlobal_L_guide_toe2Tarsi_ctrl" -p "legGlobal_L_guide_heel_ctrl";
	rename -uid "E00A0B26-43E9-7265-8152-0F88E4B3AEC2";
	setAttr ".t" -type "double3" 0 0.89346114646344565 2.6803418452449495 ;
	setAttr -k off ".tz";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" -1 0 -1 ;
	setAttr ".mtye" yes;
createNode nurbsCurve -n "legGlobal_L_guide_toe2Tarsi_ctrlShape" -p "legGlobal_L_guide_toe2Tarsi_ctrl";
	rename -uid "2AD36402-4244-976D-E4E0-92A035915C9B";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 0.26105238444010315 0.52210476888020629 0.78315715332030944 1.0442095377604126
		 1.3052619222005157 1.5663143066406189 1.827366691080722 2.0884190755208252 2.3494714599609283
		 2.6105238444010315 2.8715762288411346 3.1326286132812378 3.3936809977213409 3.6547333821614441
		 3.9157857666015472 4.1768381510416503 4.4378905354817535 4.6989429199218566 4.9599953043619598
		 5.2210476888020629 5.4821000732421661 5.7431524576822692 6.0042048421223724 6.2652572265624755
		
		25
		2.2204460492503128e-16 0.42562035253973907 -1.5359963201678048e-16
		1.5265566588595902e-16 0.41111769071239207 0.11015865322053343
		3.0531133177191805e-16 0.36859803766710275 0.21281017626986951
		2.2204460492503131e-16 0.30095903749185859 0.30095903749185859
		1.6653345369377348e-16 0.21281017626986959 0.36859803766710281
		1.6653345369377348e-16 0.11015865322053366 0.41111769071239218
		1.1102230246251565e-16 2.4810633504451924e-16 0.42562035253973918
		5.5511151231257827e-17 -0.11015865322053335 0.41111769071239218
		5.5511151231257827e-17 -0.21281017626986939 0.36859803766710286
		-2.7755575615628914e-17 -0.30095903749185848 0.30095903749185871
		-1.6653345369377348e-16 -0.36859803766710275 0.21281017626986978
		-7.6327832942979512e-17 -0.41111769071239207 0.11015865322053375
		-2.2204460492503131e-16 -0.42562035253973918 9.9350572156140903e-17
		-1.5265566588595902e-16 -0.41111769071239229 -0.11015865322053336
		-1.6653345369377348e-16 -0.36859803766710303 -0.21281017626986945
		-1.9428902930940239e-16 -0.30095903749185871 -0.30095903749185848
		-1.1102230246251565e-16 -0.21281017626986989 -0.36859803766710286
		-1.6653345369377348e-16 -0.11015865322053379 -0.41111769071239218
		-1.3877787807814457e-16 -1.8204393730541235e-16 -0.42562035253973929
		-8.3266726846886741e-17 0.1101586532205333 -0.41111769071239246
		-2.7755575615628914e-17 0.21281017626986939 -0.36859803766710314
		2.7755575615628914e-17 0.30095903749185848 -0.30095903749185887
		1.8041124150158794e-16 0.36859803766710275 -0.21281017626987012
		1.7347234759768071e-16 0.41111769071239213 -0.11015865322053403
		2.2204460492503116e-16 0.4256203525397394 -5.3162644412773625e-16
		;
createNode transform -n "legGlobal_L_guide_ankle_ctrl" -p "legGlobal_L_guide_heel_ctrl";
	rename -uid "05636397-4183-4E09-ADB5-439996EBDE7B";
	setAttr ".t" -type "double3" 0.026156666622707547 2.4115046272637359 1.5768095104276343 ;
	setAttr -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "legGlobal_L_guide_ankle_ctrlShape" -p "legGlobal_L_guide_ankle_ctrl";
	rename -uid "0E79BEA6-448C-1DD5-9EC6-EAB3EABA49AD";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 0.26105238444010315 0.52210476888020629 0.78315715332030944 1.0442095377604126
		 1.3052619222005157 1.5663143066406189 1.827366691080722 2.0884190755208252 2.3494714599609283
		 2.6105238444010315 2.8715762288411346 3.1326286132812378 3.3936809977213409 3.6547333821614441
		 3.9157857666015472 4.1768381510416503 4.4378905354817535 4.6989429199218566 4.9599953043619598
		 5.2210476888020629 5.4821000732421661 5.7431524576822692 6.0042048421223724 6.2652572265624755
		
		25
		2.2204460492503128e-16 0.42562035253973907 -1.5359963201678048e-16
		1.5265566588595902e-16 0.41111769071239207 0.11015865322053343
		3.0531133177191805e-16 0.36859803766710275 0.21281017626986951
		2.2204460492503131e-16 0.30095903749185859 0.30095903749185859
		1.6653345369377348e-16 0.21281017626986959 0.36859803766710281
		1.6653345369377348e-16 0.11015865322053366 0.41111769071239218
		1.1102230246251565e-16 2.4810633504451924e-16 0.42562035253973918
		5.5511151231257827e-17 -0.11015865322053335 0.41111769071239218
		5.5511151231257827e-17 -0.21281017626986939 0.36859803766710286
		-2.7755575615628914e-17 -0.30095903749185848 0.30095903749185871
		-1.6653345369377348e-16 -0.36859803766710275 0.21281017626986978
		-7.6327832942979512e-17 -0.41111769071239207 0.11015865322053375
		-2.2204460492503131e-16 -0.42562035253973918 9.9350572156140903e-17
		-1.5265566588595902e-16 -0.41111769071239229 -0.11015865322053336
		-1.6653345369377348e-16 -0.36859803766710303 -0.21281017626986945
		-1.9428902930940239e-16 -0.30095903749185871 -0.30095903749185848
		-1.1102230246251565e-16 -0.21281017626986989 -0.36859803766710286
		-1.6653345369377348e-16 -0.11015865322053379 -0.41111769071239218
		-1.3877787807814457e-16 -1.8204393730541235e-16 -0.42562035253973929
		-8.3266726846886741e-17 0.1101586532205333 -0.41111769071239246
		-2.7755575615628914e-17 0.21281017626986939 -0.36859803766710314
		2.7755575615628914e-17 0.30095903749185848 -0.30095903749185887
		1.8041124150158794e-16 0.36859803766710275 -0.21281017626987012
		1.7347234759768071e-16 0.41111769071239213 -0.11015865322053403
		2.2204460492503116e-16 0.4256203525397394 -5.3162644412773625e-16
		;
createNode transform -n "legGlobal_L_guide_upVector_ctrl_srtBuffer" -p "|legGlobal_L_cmpnt|guide";
	rename -uid "3E9304AA-4EB7-C6B4-146D-2681413FA73F";
createNode transform -n "legGlobal_L_guide_upVector_ctrl" -p "legGlobal_L_guide_upVector_ctrl_srtBuffer";
	rename -uid "04306C2A-41B2-DC00-86EA-15852E482FD9";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 4.7384588513953521 6.7561481902608396 -9.2158626204103253 ;
createNode nurbsCurve -n "legGlobal_L_guide_upVector_ctrlShape" -p "legGlobal_L_guide_upVector_ctrl";
	rename -uid "858A8A75-469A-5704-8F3B-0DA82BF1803A";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 0.26105238444010315 0.52210476888020629 0.78315715332030944 1.0442095377604126
		 1.3052619222005157 1.5663143066406189 1.827366691080722 2.0884190755208252 2.3494714599609283
		 2.6105238444010315 2.8715762288411346 3.1326286132812378 3.3936809977213409 3.6547333821614441
		 3.9157857666015472 4.1768381510416503 4.4378905354817535 4.6989429199218566 4.9599953043619598
		 5.2210476888020629 5.4821000732421661 5.7431524576822692 6.0042048421223724 6.2652572265624755
		
		25
		6.123233995736766e-17 6.123233995736766e-17 -1
		-0.25881904510252068 5.9145898568933492e-17 -0.96592582628906831
		-0.49999999999999989 5.3028761936245346e-17 -0.86602540378443871
		-0.70710678118654746 4.3297802811774664e-17 -0.70710678118654757
		-0.8660254037844386 3.0616169978683836e-17 -0.50000000000000011
		-0.9659258262890682 1.5848095757158837e-17 -0.25881904510252096
		-1 1.7345710191123555e-32 -2.8327694488239898e-16
		-0.96592582628906842 -1.5848095757158806e-17 0.25881904510252046
		-0.86602540378443893 -3.0616169978683812e-17 0.49999999999999972
		-0.70710678118654791 -4.3297802811774652e-17 0.70710678118654735
		-0.50000000000000044 -5.302876193624534e-17 0.8660254037844386
		-0.25881904510252129 -5.9145898568933492e-17 0.96592582628906831
		-5.330771254230592e-16 -6.1232339957367673e-17 1.0000000000000002
		0.2588190451025203 -5.9145898568933517e-17 0.96592582628906865
		0.49999999999999961 -5.3028761936245377e-17 0.86602540378443915
		0.70710678118654735 -4.3297802811774701e-17 0.70710678118654813
		0.8660254037844386 -3.0616169978683873e-17 0.50000000000000067
		0.96592582628906842 -1.5848095757158871e-17 0.25881904510252152
		1.0000000000000004 -4.4538331660061378e-32 7.273661547324616e-16
		0.96592582628906898 1.5848095757158785e-17 -0.25881904510252013
		0.86602540378443948 3.0616169978683806e-17 -0.49999999999999956
		0.70710678118654846 4.3297802811774652e-17 -0.70710678118654735
		0.500000000000001 5.3028761936245346e-17 -0.86602540378443871
		0.25881904510252179 5.9145898568933504e-17 -0.96592582628906853
		9.49410759657493e-16 6.1232339957367685e-17 -1.0000000000000004
		;
createNode transform -n "legGlobal_L_toolParameters" -p "|legGlobal_L_cmpnt|guide";
	rename -uid "135F304D-4145-8B82-4F30-BF8185355C55";
	addAttr -ci true -m -sn "toSwap" -ln "toSwap" -at "compound" -nc 2;
	addAttr -s false -ci true -sn "origin" -ln "origin" -at "message" -p "toSwap";
	addAttr -s false -ci true -sn "guided" -ln "guided" -at "message" -p "toSwap";
	addAttr -s false -ci true -m -sn "toDelete" -ln "toDelete" -at "message";
	setAttr -s 6 ".toSwap";
	setAttr -s 9 ".toDelete";
createNode angleBetween -n "legGlobal_L_guide_tarsi2Toe_rest_angle";
	rename -uid "2C140304-48AB-94EE-248F-11A698C1C301";
createNode angleBetween -n "legGlobal_L_guide_tarsi2World_rest_angle";
	rename -uid "B66299D2-4A72-1048-9B85-368EA388101A";
createNode angleBetween -n "legGlobal_L_guide_toe_rest_angle";
	rename -uid "DBBF67C9-43E3-DEE5-7F47-EEBF2925F82F";
createNode angleBetween -n "legGlobal_L_tarsi_rolledAngle";
	rename -uid "FE18DCAE-4A64-B37F-BEB2-BFBE94A48267";
createNode animBlendNodeAdditiveDA -n "legGlobal_L_guide_tarsi_rest_negate_angle";
	rename -uid "B666A5F1-43F0-A742-F1D7-DDAEEF9E45FF";
	setAttr ".wa" -1;
	setAttr ".o" -32.928389796476075;
createNode animBlendNodeAdditiveDA -n "legGlobal_L_tarsiRollOffset_angle";
	rename -uid "4976BE3E-4491-7F37-1C42-01B5DC91E4B0";
	setAttr ".wa" -1;
	setAttr ".o" -32.928389796476075;
createNode animBlendNodeAdditiveDA -n "legGlobal_L_toeRollOffset_angle";
	rename -uid "14366C82-4FEA-D2C9-0843-5095E74B4371";
	setAttr ".wa" -1;
	setAttr ".wb" -1;
	setAttr ".o" -21.065155320812835;
createNode animCurveUA -n "legGlobal_L_roll_tarsi_fCurve";
	rename -uid "EFF6015D-4515-1E59-B23B-BC9BDDF73B3D";
	setAttr ".tan" 2;
	setAttr -s 3 ".ktv[0:2]"  0 0 40 38 81 -20;
createNode animCurveUA -n "legGlobal_L_roll_toe_fCurve";
	rename -uid "8C0A3869-4FD6-03D8-CB75-EBA484C47AFA";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  40 0 140 140;
createNode clamp -n "legGlobal_L_heelBack_rollClamp";
	rename -uid "7DFB4809-43F9-DC24-E2E9-E4BB9A48C420";
	setAttr ".mn" -type "float3" 0 0 -40 ;
createNode decomposeMatrix -n "legGlobal_L_ankleFramed_tarsi_srt";
	rename -uid "D8D0DE40-484E-8CE6-2769-80AB795948E3";
createNode decomposeMatrix -n "legGlobal_L_ankleReparent_srt";
	rename -uid "A4E64472-487F-6017-861A-B6A06F00CAD0";
createNode decomposeMatrix -n "legGlobal_L_guide_ankle_world_srt";
	rename -uid "8D9675C6-4033-D98A-39BA-968890A595C2";
createNode decomposeMatrix -n "legGlobal_L_roll_tarsi_world_mtx";
	rename -uid "05F8FCF5-4B4F-107E-6F19-4CA4AA2CC108";
createNode decomposeMatrix -n "legGlobal_L_roll_toes_world_mtx2srt";
	rename -uid "67237A7C-4832-8CC2-2473-FDA54AACD3D9";
createNode decomposeMatrix -n "legGlobal_L_upVecReparent_srt";
	rename -uid "A0081B1F-484C-46F6-9AA5-9E93D881F122";
createNode decomposeMatrix -n "legGlobal_L_worldAnkle_ctrl_world_srt";
	rename -uid "15339721-4C64-F922-A7AF-23AE4AD5DDBD";
createNode distanceBetween -n "legGlobal_L_guide_tarsi_length";
	rename -uid "9B09A564-426C-A525-43FC-01A71E0F9CAE";
createNode distanceBetween -n "legGlobal_L_guide_toe_length";
	rename -uid "79AB0E96-41E2-8F6A-55B7-878B8316A6C4";
createNode multMatrix -n "legGlobal_L_ankleFramed_tarsi_mtx";
	rename -uid "12B84281-4004-9025-36F0-44BC86686BB9";
	setAttr -s 2 ".i";
createNode multMatrix -n "legGlobal_L_ankleReparent_mtxMult";
	rename -uid "A7696441-4AD1-1B6A-5C1A-988C94245A25";
	setAttr -s 2 ".i";
createNode multMatrix -n "legGlobal_L_upVecReparent_mtxMult";
	rename -uid "EAA42958-4DB4-C5B4-F73E-70B09258AB0E";
	setAttr -s 2 ".i";
createNode plusMinusAverage -n "legGlobal_L_guide_tarsi_direction_vec";
	rename -uid "0E469812-4503-35E2-5EEE-BBB80B88CBA0";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "legGlobal_L_guide_toe_direction_vec";
	rename -uid "D31DF879-4A3A-0197-5FF9-05A86D73C6F4";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "legGlobal_L_tarsi_worldDirection_vec3";
	rename -uid "9A0CE03C-4235-00F8-AECA-76BF436A4D10";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode pointMatrixMult -n "legGlobal_L_ankleFramed_rollOffset_srt";
	rename -uid "4C4EFD89-43A5-85FE-BDB6-97BB24962684";
createNode unitConversion -n "legGlobal_L_roll_UC";
	rename -uid "982BED6E-4A93-708A-9813-65966C2CD41C";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "legGlobal_L_heelback_roll_UC";
	rename -uid "F43D9424-4F9F-44DB-85F2-9E86113E1EB0";
	setAttr ".cf" 0.017453292519943295;
createNode container -n "legGlobal_L_container";
	rename -uid "887B4841-46B7-D3BA-EE11-438DF0B38BAF";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".isc" yes;
	setAttr -s 2 ".pni";
	setAttr ".ctor" -type "string" "Jaco";
	setAttr ".cdat" -type "string" "2018/02/16 08:10:51";
	setAttr ".aal" -type "attributeAlias" {"child","canBeChild[0]","parent","canBeParent[0]"
		,"legGlobal_L_worldAnkle_ctrl","publishedNodeInfo[0]","legGlobal_L_upVector_ctrl"
		,"publishedNodeInfo[1]"} ;
createNode hyperLayout -n "hyperLayout1";
	rename -uid "61DF42DE-44BD-4409-3BA0-1C942F7D9F83";
	setAttr ".ihi" 0;
	setAttr -s 65 ".hyp";
select -ne :time1;
	setAttr ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".etmr" no;
	setAttr ".tmr" 4096;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 108 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 6 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "legGlobal_L_worldAnkle_rolled_srt.wm" "legGlobal_L_output.rolledAnkle"
		;
connectAttr "|legGlobal_L_cmpnt|control|legGlobal_L_upVector_ctrl_srtBuffer|legGlobal_L_upVector_ctrl.wm" "legGlobal_L_output.upVectorWorld"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.wm" "legGlobal_L_output.rawAnkleControl"
		;
connectAttr "legGlobal_L_roll_tarsi_srt.rx" "legGlobal_L_output.toeAngle";
connectAttr "legGlobal_L_tarsi_rolledAngle.a" "legGlobal_L_output.tarsiAngle";
connectAttr "legGlobal_L_guide_ankle_world_srt.ot" "legGlobal_L_ankle_rest_srt.t"
		;
connectAttr "legGlobal_L_roll_world_srt.r" "legGlobal_L_ankle_rest_srt.r";
connectAttr "legGlobal_L_ankleFramed_tarsi_srt.or" "legGlobal_L_ankle_rolled_srt.r"
		;
connectAttr "legGlobal_L_ankleFramed_tarsi_srt.ot" "legGlobal_L_ankle_rolled_srt.t"
		;
connectAttr "legGlobal_L_guide_global_ctrl.r" "legGlobal_L_roll_world_srt.r";
connectAttr "legGlobal_L_guide_global_ctrl.s" "legGlobal_L_roll_world_srt.s";
connectAttr "legGlobal_L_guide_global_ctrl.t" "legGlobal_L_roll_world_srt.t";
connectAttr "legGlobal_L_heelback_roll_UC.o" "legGlobal_L_roll_heel_srt.rx";
connectAttr "legGlobal_L_guide_heel_ctrl.t" "legGlobal_L_roll_heel_srt.t";
connectAttr "legGlobal_L_toeRollOffset_angle.o" "legGlobal_L_roll_tip_srt.rx";
connectAttr "legGlobal_L_configParameters.plantLength" "legGlobal_L_roll_tip_srt.tz"
		;
connectAttr "legGlobal_L_tarsiRollOffset_angle.o" "legGlobal_L_roll_tarsi_srt.rx"
		;
connectAttr "legGlobal_L_configParameters.toeLength" "legGlobal_L_roll_tarsi_srt.tz"
		;
connectAttr "legGlobal_L_configParameters.tarsiLength" "legGlobal_L_roll_tarsiEnd_srt.tz"
		;
connectAttr "legGlobal_L_ankleReparent_srt.ot" "legGlobal_L_worldAnkle_ctrl_srtBuffer.t"
		;
connectAttr "legGlobal_L_ankleReparent_srt.or" "legGlobal_L_worldAnkle_ctrl_srtBuffer.r"
		;
connectAttr "legGlobal_L_upVecReparent_srt.or" "legGlobal_L_upVector_ctrl_srtBuffer.r"
		;
connectAttr "legGlobal_L_upVecReparent_srt.ot" "legGlobal_L_upVector_ctrl_srtBuffer.t"
		;
connectAttr "legGlobal_L_guide_tip_ctrl.tz" "legGlobal_L_configParameters.plantLength"
		;
connectAttr "legGlobal_L_guide_toe_length.d" "legGlobal_L_configParameters.toeLength"
		;
connectAttr "legGlobal_L_guide_tarsi_length.d" "legGlobal_L_configParameters.tarsiLength"
		;
connectAttr "legGlobal_L_guide_ankle_ctrl.wm" "legGlobal_L_configParameters.ankleGlobalOffset"
		;
connectAttr "legGlobal_L_guide_upVector_ctrl.m" "legGlobal_L_configParameters.upVecGlobalOffset"
		;
connectAttr "legGlobal_L_guide_toe_rest_angle.a" "legGlobal_L_configParameters.toeRest"
		;
connectAttr "legGlobal_L_guide_tarsi_rest_negate_angle.o" "legGlobal_L_configParameters.tarsirest"
		;
connectAttr "legGlobal_L_guide_tarsi2World_rest_angle.a" "legGlobal_L_configParameters.ankleRest"
		;
connectAttr "legGlobal_L_ankleFramed_rollOffset_srt.o" "legGlobal_L_worldAnkle_rolled_srt.t"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_world_srt.or" "legGlobal_L_worldAnkle_rolled_srt.r"
		;
connectAttr "legGlobal_L_configParameters.ankleGlobalOffset" "legGlobal_L_toolParameters.toSwap[0].guided"
		;
connectAttr "legGlobal_L_configParameters.plantLength" "legGlobal_L_toolParameters.toSwap[1].guided"
		;
connectAttr "legGlobal_L_configParameters.tarsiLength" "legGlobal_L_toolParameters.toSwap[2].guided"
		;
connectAttr "legGlobal_L_configParameters.tarsirest" "legGlobal_L_toolParameters.toSwap[3].guided"
		;
connectAttr "legGlobal_L_configParameters.toeLength" "legGlobal_L_toolParameters.toSwap[4].guided"
		;
connectAttr "legGlobal_L_configParameters.upVecGlobalOffset" "legGlobal_L_toolParameters.toSwap[5].guided"
		;
connectAttr "legGlobal_L_guide_tarsi2World_rest_angle.msg" "legGlobal_L_toolParameters.toDelete[0]"
		;
connectAttr "legGlobal_L_guide_tarsi2Toe_rest_angle.msg" "legGlobal_L_toolParameters.toDelete[1]"
		;
connectAttr "legGlobal_L_guide_tarsi_direction_vec.msg" "legGlobal_L_toolParameters.toDelete[2]"
		;
connectAttr "legGlobal_L_guide_toe_direction_vec.msg" "legGlobal_L_toolParameters.toDelete[3]"
		;
connectAttr "legGlobal_L_guide_ankle_world_srt.msg" "legGlobal_L_toolParameters.toDelete[4]"
		;
connectAttr "legGlobal_L_guide_toe_rest_angle.msg" "legGlobal_L_toolParameters.toDelete[5]"
		;
connectAttr "legGlobal_L_guide_tarsi_length.msg" "legGlobal_L_toolParameters.toDelete[6]"
		;
connectAttr "legGlobal_L_guide_toe_length.msg" "legGlobal_L_toolParameters.toDelete[7]"
		;
connectAttr "legGlobal_L_guide_tarsi_rest_negate_angle.msg" "legGlobal_L_toolParameters.toDelete[8]"
		;
connectAttr "legGlobal_L_guide_toe_direction_vec.o3" "legGlobal_L_guide_tarsi2Toe_rest_angle.v1"
		;
connectAttr "legGlobal_L_guide_tarsi_direction_vec.o3" "legGlobal_L_guide_tarsi2Toe_rest_angle.v2"
		;
connectAttr "legGlobal_L_guide_tarsi_direction_vec.o3" "legGlobal_L_guide_tarsi2World_rest_angle.v1"
		;
connectAttr "legGlobal_L_guide_basisVector.t" "legGlobal_L_guide_tarsi2World_rest_angle.v2"
		;
connectAttr "legGlobal_L_guide_toe_direction_vec.o3" "legGlobal_L_guide_toe_rest_angle.v1"
		;
connectAttr "legGlobal_L_guide_basisVector.t" "legGlobal_L_guide_toe_rest_angle.v2"
		;
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.o3" "legGlobal_L_tarsi_rolledAngle.v1"
		;
connectAttr "legGlobal_L_guide_tarsi2Toe_rest_angle.a" "legGlobal_L_guide_tarsi_rest_negate_angle.ia"
		;
connectAttr "legGlobal_L_configParameters.tarsirest" "legGlobal_L_tarsiRollOffset_angle.ib"
		;
connectAttr "legGlobal_L_roll_tarsi_fCurve.o" "legGlobal_L_tarsiRollOffset_angle.ia"
		;
connectAttr "legGlobal_L_configParameters.toeRest" "legGlobal_L_toeRollOffset_angle.ib"
		;
connectAttr "legGlobal_L_roll_toe_fCurve.o" "legGlobal_L_toeRollOffset_angle.ia"
		;
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_roll_tarsi_fCurve.i";
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_roll_toe_fCurve.i";
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_heelBack_rollClamp.ipb";
connectAttr "legGlobal_L_ankleFramed_tarsi_mtx.o" "legGlobal_L_ankleFramed_tarsi_srt.imat"
		;
connectAttr "legGlobal_L_ankleReparent_mtxMult.o" "legGlobal_L_ankleReparent_srt.imat"
		;
connectAttr "legGlobal_L_guide_ankle_ctrl.wm" "legGlobal_L_guide_ankle_world_srt.imat"
		;
connectAttr "legGlobal_L_roll_tarsiEnd_srt.wm" "legGlobal_L_roll_tarsi_world_mtx.imat"
		;
connectAttr "legGlobal_L_roll_tarsi_srt.wm" "legGlobal_L_roll_toes_world_mtx2srt.imat"
		;
connectAttr "legGlobal_L_upVecReparent_mtxMult.o" "legGlobal_L_upVecReparent_srt.imat"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.wm" "legGlobal_L_worldAnkle_ctrl_world_srt.imat"
		;
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.t" "legGlobal_L_guide_tarsi_length.p1"
		;
connectAttr "legGlobal_L_guide_ankle_ctrl.t" "legGlobal_L_guide_tarsi_length.p2"
		;
connectAttr "legGlobal_L_guide_tip_ctrl.t" "legGlobal_L_guide_toe_length.p1";
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.t" "legGlobal_L_guide_toe_length.p2"
		;
connectAttr "legGlobal_L_roll_tarsiEnd_srt.wm" "legGlobal_L_ankleFramed_tarsi_mtx.i[0]"
		;
connectAttr "legGlobal_L_ankle_rest_srt.wim" "legGlobal_L_ankleFramed_tarsi_mtx.i[1]"
		;
connectAttr "legGlobal_L_configParameters.ankleGlobalOffset" "legGlobal_L_ankleReparent_mtxMult.i[0]"
		;
connectAttr "legGlobal_L_input.endWorld" "legGlobal_L_ankleReparent_mtxMult.i[1]"
		;
connectAttr "legGlobal_L_configParameters.upVecGlobalOffset" "legGlobal_L_upVecReparent_mtxMult.i[0]"
		;
connectAttr "legGlobal_L_input.endWorld" "legGlobal_L_upVecReparent_mtxMult.i[1]"
		;
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.t" "legGlobal_L_guide_tarsi_direction_vec.i3[0]"
		;
connectAttr "legGlobal_L_guide_ankle_ctrl.t" "legGlobal_L_guide_tarsi_direction_vec.i3[1]"
		;
connectAttr "legGlobal_L_guide_tip_ctrl.t" "legGlobal_L_guide_toe_direction_vec.i3[0]"
		;
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.t" "legGlobal_L_guide_toe_direction_vec.i3[1]"
		;
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.ot" "legGlobal_L_tarsi_worldDirection_vec3.i3[0]"
		;
connectAttr "legGlobal_L_roll_tarsi_world_mtx.ot" "legGlobal_L_tarsi_worldDirection_vec3.i3[1]"
		;
connectAttr "legGlobal_L_ankle_rolled_srt.t" "legGlobal_L_ankleFramed_rollOffset_srt.ip"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.wm" "legGlobal_L_ankleFramed_rollOffset_srt.im"
		;
connectAttr "legGlobal_L_animParameters.roll" "legGlobal_L_roll_UC.i";
connectAttr "legGlobal_L_heelBack_rollClamp.opb" "legGlobal_L_heelback_roll_UC.i"
		;
connectAttr "hyperLayout1.msg" "legGlobal_L_container.hl";
connectAttr "legGlobal_L_cmpnt.msg" "legGlobal_L_container.cbp[0]";
connectAttr "legGlobal_L_cmpnt.msg" "legGlobal_L_container.cbc[0]";
connectAttr "legGlobal_L_worldAnkle_ctrl.msg" "legGlobal_L_container.pni[0].pnod"
		;
connectAttr "|legGlobal_L_cmpnt|control|legGlobal_L_upVector_ctrl_srtBuffer|legGlobal_L_upVector_ctrl.msg" "legGlobal_L_container.pni[1].pnod"
		;
connectAttr "legGlobal_L_cmpnt.msg" "hyperLayout1.hyp[0].dn";
connectAttr "legGlobal_L_input.msg" "hyperLayout1.hyp[1].dn";
connectAttr "legGlobal_L_output.msg" "hyperLayout1.hyp[2].dn";
connectAttr "|legGlobal_L_cmpnt|control.msg" "hyperLayout1.hyp[3].dn";
connectAttr "legGlobal_L_animParameters.msg" "hyperLayout1.hyp[4].dn";
connectAttr "roll_mechanics.msg" "hyperLayout1.hyp[5].dn";
connectAttr "legGlobal_L_ankle_rest_srt.msg" "hyperLayout1.hyp[6].dn";
connectAttr "legGlobal_L_ankle_rolled_srt.msg" "hyperLayout1.hyp[7].dn";
connectAttr "legGlobal_L_roll_world_srt.msg" "hyperLayout1.hyp[8].dn";
connectAttr "legGlobal_L_roll_heel_srt.msg" "hyperLayout1.hyp[9].dn";
connectAttr "legGlobal_L_roll_tip_srt.msg" "hyperLayout1.hyp[10].dn";
connectAttr "legGlobal_L_roll_tarsi_srt.msg" "hyperLayout1.hyp[11].dn";
connectAttr "legGlobal_L_roll_tarsiEnd_srt.msg" "hyperLayout1.hyp[12].dn";
connectAttr "legGlobal_L_worldAnkle_ctrl_srtBuffer.msg" "hyperLayout1.hyp[13].dn"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.msg" "hyperLayout1.hyp[14].dn";
connectAttr "legGlobal_L_upVector_ctrl_srtBuffer.msg" "hyperLayout1.hyp[17].dn";
connectAttr "|legGlobal_L_cmpnt|control|legGlobal_L_upVector_ctrl_srtBuffer|legGlobal_L_upVector_ctrl.msg" "hyperLayout1.hyp[18].dn"
		;
connectAttr "|legGlobal_L_cmpnt|guide.msg" "hyperLayout1.hyp[19].dn";
connectAttr "legGlobal_L_guide_global_ctrl.msg" "hyperLayout1.hyp[20].dn";
connectAttr "legGlobal_L_guide_basisVector.msg" "hyperLayout1.hyp[21].dn";
connectAttr "legGlobal_L_guide_heel_ctrl.msg" "hyperLayout1.hyp[22].dn";
connectAttr "legGlobal_L_guide_tip_ctrl.msg" "hyperLayout1.hyp[23].dn";
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.msg" "hyperLayout1.hyp[24].dn";
connectAttr "legGlobal_L_guide_ankle_ctrl.msg" "hyperLayout1.hyp[25].dn";
connectAttr "legGlobal_L_configParameters.msg" "hyperLayout1.hyp[26].dn";
connectAttr "legGlobal_L_guide_tarsi2Toe_rest_angle.msg" "hyperLayout1.hyp[28].dn"
		;
connectAttr "legGlobal_L_guide_tarsi2World_rest_angle.msg" "hyperLayout1.hyp[29].dn"
		;
connectAttr "legGlobal_L_guide_toe_rest_angle.msg" "hyperLayout1.hyp[30].dn";
connectAttr "legGlobal_L_tarsi_rolledAngle.msg" "hyperLayout1.hyp[31].dn";
connectAttr "legGlobal_L_guide_tarsi_rest_negate_angle.msg" "hyperLayout1.hyp[32].dn"
		;
connectAttr "legGlobal_L_tarsiRollOffset_angle.msg" "hyperLayout1.hyp[33].dn";
connectAttr "legGlobal_L_toeRollOffset_angle.msg" "hyperLayout1.hyp[34].dn";
connectAttr "legGlobal_L_roll_tarsi_fCurve.msg" "hyperLayout1.hyp[35].dn";
connectAttr "legGlobal_L_roll_toe_fCurve.msg" "hyperLayout1.hyp[36].dn";
connectAttr "legGlobal_L_heelBack_rollClamp.msg" "hyperLayout1.hyp[38].dn";
connectAttr "legGlobal_L_ankleFramed_tarsi_srt.msg" "hyperLayout1.hyp[41].dn";
connectAttr "legGlobal_L_ankleReparent_srt.msg" "hyperLayout1.hyp[42].dn";
connectAttr "legGlobal_L_guide_ankle_world_srt.msg" "hyperLayout1.hyp[43].dn";
connectAttr "legGlobal_L_roll_tarsi_world_mtx.msg" "hyperLayout1.hyp[44].dn";
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.msg" "hyperLayout1.hyp[45].dn";
connectAttr "legGlobal_L_upVecReparent_srt.msg" "hyperLayout1.hyp[48].dn";
connectAttr "legGlobal_L_worldAnkle_ctrl_world_srt.msg" "hyperLayout1.hyp[49].dn"
		;
connectAttr "legGlobal_L_guide_tarsi_length.msg" "hyperLayout1.hyp[50].dn";
connectAttr "legGlobal_L_guide_toe_length.msg" "hyperLayout1.hyp[51].dn";
connectAttr "legGlobal_L_ankleFramed_tarsi_mtx.msg" "hyperLayout1.hyp[54].dn";
connectAttr "legGlobal_L_ankleReparent_mtxMult.msg" "hyperLayout1.hyp[55].dn";
connectAttr "legGlobal_L_upVecReparent_mtxMult.msg" "hyperLayout1.hyp[56].dn";
connectAttr "legGlobal_L_guide_tarsi_direction_vec.msg" "hyperLayout1.hyp[58].dn"
		;
connectAttr "legGlobal_L_guide_toe_direction_vec.msg" "hyperLayout1.hyp[59].dn";
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.msg" "hyperLayout1.hyp[62].dn"
		;
connectAttr "legGlobal_L_ankleFramed_rollOffset_srt.msg" "hyperLayout1.hyp[63].dn"
		;
connectAttr "legGlobal_L_worldAnkle_ctrlShape.msg" "hyperLayout1.hyp[65].dn";
connectAttr "|legGlobal_L_cmpnt|control|legGlobal_L_upVector_ctrl_srtBuffer|legGlobal_L_upVector_ctrl|legGlobal_L_upVector_ctrl.msg" "hyperLayout1.hyp[67].dn"
		;
connectAttr "legGlobal_L_guide_global_ctrlShape.msg" "hyperLayout1.hyp[68].dn";
connectAttr "legGlobal_L_guide_heel_ctrlShape.msg" "hyperLayout1.hyp[69].dn";
connectAttr "legGlobal_L_guide_tip_ctrlShape.msg" "hyperLayout1.hyp[70].dn";
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrlShape.msg" "hyperLayout1.hyp[71].dn"
		;
connectAttr "legGlobal_L_guide_ankle_ctrlShape.msg" "hyperLayout1.hyp[72].dn";
connectAttr "legGlobal_L_roll_UC.msg" "hyperLayout1.hyp[73].dn";
connectAttr "legGlobal_L_heelback_roll_UC.msg" "hyperLayout1.hyp[74].dn";
connectAttr "legGlobal_L_toolParameters.msg" "hyperLayout1.hyp[75].dn";
connectAttr "legGlobal_L_guide_upVector_ctrl_srtBuffer.msg" "hyperLayout1.hyp[76].dn"
		;
connectAttr "legGlobal_L_guide_upVector_ctrl.msg" "hyperLayout1.hyp[77].dn";
connectAttr "legGlobal_L_guide_upVector_ctrlShape.msg" "hyperLayout1.hyp[78].dn"
		;
connectAttr "legGlobal_L_worldAnkle_rolled_srt.msg" "hyperLayout1.hyp[79].dn";
connectAttr "legGlobal_L_heelBack_rollClamp.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "legGlobal_L_roll_tarsi_world_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_tarsi_rolledAngle.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_L_guide_toe_length.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_L_guide_tarsi_length.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "legGlobal_L_guide_tarsi2Toe_rest_angle.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_guide_toe_direction_vec.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_guide_tarsi_direction_vec.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_guide_toe_rest_angle.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_guide_ankle_world_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_guide_tarsi2World_rest_angle.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_ankleFramed_tarsi_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_ankleFramed_tarsi_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_worldAnkle_ctrl_world_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_ankleReparent_mtxMult.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_ankleReparent_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_L_upVecReparent_mtxMult.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_upVecReparent_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
// End of legGlobal.ma
