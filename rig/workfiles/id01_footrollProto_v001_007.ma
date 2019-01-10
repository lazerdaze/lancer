//Maya ASCII 2017ff04 scene
//Name: id01_footrollProto_v001_007.ma
//Last modified: Thu, Jan 18, 2018 10:57:01 PM
//Codeset: 1252
requires maya "2017ff04";
requires -nodeType "decomposeMatrix" -nodeType "composeMatrix" "matrixNodes" "1.0";
requires "stereoCamera" "10.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201702071345-1015190";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "5E1B0526-4CE8-950E-7536-339BF0539040";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -7.306689064992721 6.0155967972353395 14.54480540150009 ;
	setAttr ".r" -type "double3" -9.3383527294117386 -25.40000000000131 4.4011270048219741e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "4F383ED2-4EE7-0DD9-D579-0C8F43AD384E";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 14.472651404175476;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -2.4999999999999996 4 2.2159891280501309 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "0E31EE1C-4A75-E4B8-9C14-57A2D90788C3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "6BDBE115-4192-E4FA-0B72-478700714E66";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "5A7F0D20-41AC-014F-A83E-16AD1AF0A817";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.8180419804518524 2.0176894728408907 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "E0D006D9-40BA-945E-E790-42B92B3CA785";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 22.327767985899698;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "9BE6A7B5-4B9A-28AE-FAB2-0C9DFEC851B7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 3.1937708605175068 0.12054705389017878 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "A5360673-408D-5FDA-6005-DA8D8444B180";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 21.074503999168151;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "legGlobal_L_cmpnt";
	rename -uid "0E378926-444A-68FF-58B9-3F987790DD6A";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.059300009 0.5043 0.17050005 ;
createNode transform -n "input" -p "legGlobal_L_cmpnt";
	rename -uid "6195041D-49BC-6253-98B1-4BA978F47BFB";
	addAttr -ci true -sn "startMtx" -ln "startMtx" -at "matrix";
createNode transform -n "output" -p "legGlobal_L_cmpnt";
	rename -uid "AD423288-48DD-1660-FC35-3990B94570F5";
	addAttr -ci true -sn "limitedAnkle" -ln "limitedAnkle" -at "matrix";
	addAttr -ci true -sn "toeAngle" -ln "toeAngle" -at "doubleAngle";
createNode transform -n "control" -p "legGlobal_L_cmpnt";
	rename -uid "731D5B2F-477A-8093-C727-038F2AE35086";
createNode transform -n "animParameters" -p "|legGlobal_L_cmpnt|control";
	rename -uid "8EA7B613-4D2E-F0EE-E8F9-E3B2E4D1A044";
	addAttr -ci true -k true -sn "roll" -ln "roll" -smn -1.7 -smx 3.14 -at "doubleAngle";
	setAttr -k on ".roll";
createNode transform -n "configParameters" -p "|legGlobal_L_cmpnt|control";
	rename -uid "9E9BA6F1-4184-ABC8-6461-7DA220D98DAD";
	addAttr -ci true -k true -sn "toeRest" -ln "toeRest" -smn -1.7 -smx 3.14 -at "doubleAngle";
	addAttr -ci true -k true -sn "tarsirest" -ln "tarsirest" -smn -1.7 -smx 3.14 -at "doubleAngle";
	addAttr -ci true -k true -sn "toeLength" -ln "toeLength" -smn 0.01 -smx 10 -at "double";
	addAttr -ci true -k true -sn "tarsiLength" -ln "tarsiLength" -smn 0.01 -smx 10 -at "double";
	addAttr -ci true -sn "femurLength" -ln "femurLength" -dv 4 -min 0.01 -max 50 -at "double";
	addAttr -ci true -sn "tibiaLength" -ln "tibiaLength" -dv 4 -min 0.01 -max 50 -at "double";
	setAttr -k on ".toeRest" 10;
	setAttr -k on ".tarsirest" 20;
	setAttr -k on ".toeLength" 2;
	setAttr -k on ".tarsiLength" 4;
	setAttr -k on ".femurLength" 5;
	setAttr -k on ".tibiaLength" 5;
createNode transform -n "roll_mechanics" -p "|legGlobal_L_cmpnt|control";
	rename -uid "4CD0995C-49B8-C82B-8037-75B6CBFC5609";
createNode joint -n "legGlobal_L_roll_heel_srt" -p "roll_mechanics";
	rename -uid "3217ED01-4005-E9FD-10BA-33922256F19F";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "legGlobal_L_roll_tip_srt" -p "legGlobal_L_roll_heel_srt";
	rename -uid "7D7C5D2F-4DBD-564F-C264-ED8DB128BC64";
	setAttr ".t" -type "double3" -7 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60252962018639844;
createNode joint -n "legGlobal_L_roll_tarsi_srt" -p "legGlobal_L_roll_tip_srt";
	rename -uid "0641A02A-4304-F9E4-6ED4-E28631E02DDA";
	setAttr ".t" -type "double3" 2 0 -1.0755285551056204e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60252962018639844;
createNode joint -n "legGlobal_L_roll_tarsiEnd_srt" -p "legGlobal_L_roll_tarsi_srt";
	rename -uid "36A70538-4FC8-7127-9AC5-F1952F082250";
	setAttr ".t" -type "double3" 4 0 1.0755285551056204e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "legGlobal_L_roll_ankle_srt" -p "legGlobal_L_roll_tarsiEnd_srt";
	rename -uid "E0331096-439D-B72C-735A-D780195FCDC8";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr ".r" -type "double3" 0 0 -29.999999999999996 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
	setAttr ".nts" -type "string" "this is currently not connected to anything. Being the ankle we will want to compensate for the roll and make sure it remains world aligned, it should only be a matter of arithmetics on a few angles";
createNode transform -n "legGlobal_L_ankle_rest_srt" -p "roll_mechanics";
	rename -uid "05AC6C11-484A-B5FF-CE03-A3BF05F24D5C";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr ".t" -type "double3" -1.5662828788378289 2.3472963553338606 0 ;
	setAttr ".nts" -type "string" "right now the rest is manually placed and used as a static value to figure out the roll's ankle level offset from.\nTo make the component more dynamic and responsive to configuration this will need to eventually be the non-rolled default produced by the defaults";
createNode transform -n "legGlobal_L_worldAnkle_ctrl_srtBuffer" -p "|legGlobal_L_cmpnt|control";
	rename -uid "4DFF54C9-4976-E442-C936-34B4336A936D";
	setAttr ".t" -type "double3" 0 2.347 0 ;
createNode transform -n "legGlobal_L_worldAnkle_ctrl" -p "legGlobal_L_worldAnkle_ctrl_srtBuffer";
	rename -uid "F115B55D-4841-CBC6-1902-D1A4610C79D6";
createNode nurbsCurve -n "legGlobal_L_worldAnkle_ctrlShape" -p "legGlobal_L_worldAnkle_ctrl";
	rename -uid "5EE8CBF6-47C0-EAC7-4543-12802D3AB7CB";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "legGlobal_L_worldAnkle_rolled_srt" -p "legGlobal_L_worldAnkle_ctrl";
	rename -uid "09F3347C-4C46-4349-8B0C-23B97A38DC00";
	setAttr ".ove" yes;
createNode mesh -n "legGlobal_L_worldAnkle_rolled_srtShape" -p "legGlobal_L_worldAnkle_rolled_srt";
	rename -uid "96B5A13E-4492-A47B-F3F9-4A9A716C7B25";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 16 ".uvst[0].uvsp[0:15]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25 0.5 0.125 0.75 0.125;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 10 ".pt[0:9]" -type "float3"  0.13106491 0.088749178 -0.04643381 
		-0.046433534 0.088749178 -0.04643381 0.13106491 -0.088749111 -0.04643381 -0.046433534 
		-0.088749111 -0.04643381 0.13106494 -0.088749081 0.13106494 -0.046433534 -0.088749141 
		0.13106491 0.13106488 0.0887492 0.13106494 -0.046433534 0.088749178 0.13106494 0.042315558 
		-1.6764999e-009 0.34573501 0.34573501 -1.6764999e-009 0.042315558;
	setAttr -s 10 ".vt[0:9]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5 0 0 0.5 0.5 0 0;
	setAttr -s 20 ".ed[0:19]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0 0 8 1 8 3 1 2 8 1 8 1 1 1 9 1 9 5 1 3 9 1 9 7 1;
	setAttr -s 12 -ch 40 ".fc[0:11]" -type "polyFaces" 
		f 3 14 13 -2
		mu 0 3 2 14 3
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 3 18 17 -8
		mu 0 3 3 15 11
		f 4 10 4 6 8
		mu 0 4 12 0 2 13
		f 3 15 5 -14
		mu 0 3 14 1 3
		f 3 12 -15 -5
		mu 0 3 0 14 2
		f 3 0 -16 -13
		mu 0 3 0 1 14
		f 3 19 -10 -18
		mu 0 3 15 10 11
		f 3 16 -19 -6
		mu 0 3 1 15 3
		f 3 -12 -20 -17
		mu 0 3 1 10 15;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "legGlobal_L_limitedAnkle_srt" -p "|legGlobal_L_cmpnt|control";
	rename -uid "64FD68AC-4684-0D67-93B8-22AA58DDC9B1";
createNode ikHandle -n "leg_ankle_IKhdl" -p "legGlobal_L_limitedAnkle_srt";
	rename -uid "413E1648-4B65-BE66-F208-B6B7D86B55C4";
	setAttr ".s" -type "double3" 1 1 0.99999999999999967 ;
	setAttr ".pv" -type "double3" -1.2232799263357461e-009 0.056886406945122148 1.9991908204833468 ;
	setAttr ".roc" yes;
createNode transform -n "foot_M_cpmnt";
	rename -uid "E3F865EB-498D-5A0D-2C5F-18A87C4D0E0F";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.1814 0.29659995 0.5783 ;
	setAttr ".it" no;
createNode transform -n "input" -p "foot_M_cpmnt";
	rename -uid "6C1132A6-46EC-E323-85FC-6EB64FCDBD07";
	addAttr -ci true -sn "tarsiLength" -ln "tarsiLength" -dv 4 -min 0 -max 50 -at "double";
	addAttr -ci true -sn "startMtx" -ln "startMtx" -at "matrix";
	addAttr -ci true -sn "toeAngle" -ln "toeAngle" -at "doubleAngle";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".tarsiLength";
createNode transform -n "output" -p "foot_M_cpmnt";
	rename -uid "D9C6E67D-4010-24EF-C868-67B0DDD39FC4";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
createNode transform -n "control" -p "foot_M_cpmnt";
	rename -uid "66B07850-4C23-F05C-B849-C6B5847E9E2E";
	setAttr ".it" no;
createNode transform -n "foot_M_tarsii_ctrl_srtBuffer" -p "|foot_M_cpmnt|control";
	rename -uid "50F94EB5-42AA-6C61-1668-F393638190F8";
createNode transform -n "foot_M_tarsii_ctrl" -p "foot_M_tarsii_ctrl_srtBuffer";
	rename -uid "D888E2B2-4784-9C27-6ACA-C1986E0E6970";
createNode nurbsCurve -n "foot_M_tarsii_ctrlShape" -p "foot_M_tarsii_ctrl";
	rename -uid "01F34CB2-48FD-B823-FEDB-5FA035F53BBA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		-1.5892840977061378 0 0
		-1.059522731804095 1.5892840977061393 0
		1.059522731804095 1.5892840977061393 0
		1.5892840977061378 0 0
		-1.5892840977061378 0 0
		;
createNode joint -n "diagnostic_ankle" -p "foot_M_tarsii_ctrl";
	rename -uid "CBF7DBB2-4849-8D79-31E5-DAAC89E6E917";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode joint -n "diagnostic_tarsi" -p "diagnostic_ankle";
	rename -uid "4C3DFC2F-4EAE-86B6-D413-069D72C93699";
	setAttr ".t" -type "double3" 0 0 4 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode transform -n "foot_M_toes_ctrl_srtBuffer" -p "foot_M_tarsii_ctrl";
	rename -uid "E306CA04-4965-9C72-B977-67A77A3C61B8";
	setAttr ".t" -type "double3" 0 0 4 ;
createNode transform -n "foot_M_toes_ctrl" -p "foot_M_toes_ctrl_srtBuffer";
	rename -uid "DA5338BF-4B9F-0380-A369-23A3456591AA";
createNode nurbsCurve -n "foot_M_toes_ctrlShape" -p "foot_M_toes_ctrl";
	rename -uid "02AF3470-4071-51D4-9DF3-3F803C9A8EC9";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		-1.5892840977061378 0 0
		-1.059522731804095 1.5892840977061393 0
		1.059522731804095 1.5892840977061393 0
		1.5892840977061378 0 0
		-1.5892840977061378 0 0
		;
createNode joint -n "diagnostic_toes" -p "foot_M_toes_ctrl";
	rename -uid "E52B0F22-447C-E71B-8E15-6DB88DBCC0CB";
	setAttr ".t" -type "double3" 0 0 4.4408920985006262e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode joint -n "diagnostic_tip" -p "diagnostic_toes";
	rename -uid "2FDE15DE-4DEE-E2F3-B505-71B862062BD6";
	setAttr ".t" -type "double3" 0 0 2 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode transform -n "guide" -p "foot_M_cpmnt";
	rename -uid "4B3DDE1D-47FF-4987-F21A-2B81C3D4F3F3";
createNode transform -n "sketch";
	rename -uid "53E5FA5E-416F-367C-703E-298A9EE75E68";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0 0 ;
createNode joint -n "hip" -p "sketch";
	rename -uid "7C552281-4457-1EE2-A238-509D5A1AE933";
	setAttr ".r" -type "double3" -3.9068295599751845e-015 7.3592371185043848e-016 26.612268800366547 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999972 -21.682291613244935 -89.999999999999986 ;
	setAttr ".radi" 0.70798752597763914;
createNode joint -n "knee" -p "hip";
	rename -uid "91C9CB32-43F7-7765-590D-F39A606B8A91";
	setAttr ".t" -type "double3" 5 -6.6613381477509392e-016 1.1149064269357963e-015 ;
	setAttr ".r" -type "double3" 4.8382692192252413e-015 -1.64794110999739e-014 49.196875433166745 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 -6.2717258778555974e-015 -47.392245394056232 ;
	setAttr ".radi" 0.68063049658436803;
createNode joint -n "ankle_IK" -p "knee";
	rename -uid "868FFCE1-40C9-D29F-2649-03BD8BE79452";
	setAttr ".t" -type "double3" 5 -1.1102230246251565e-015 -4.9172525456397831e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 64.29004621918871 -89.999999999999943 0 ;
	setAttr ".radi" 0.66302611226386043;
createNode ikEffector -n "effector1" -p "knee";
	rename -uid "FA95316E-43CA-2DAF-41E1-EBB1122DF865";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "leg_buffer" -p "sketch";
	rename -uid "171E5048-4F5D-9FC7-C121-429C09D77117";
	setAttr ".t" -type "double3" 0 8.5727670206121154 0.084322298563176398 ;
	setAttr ".r" -type "double3" 91.092015353162168 25.736219219922926 -86.543619298111153 ;
	setAttr ".s" -type "double3" 1 0.99999999999999989 0.99999999999999989 ;
createNode transform -n "settings" -p "sketch";
	rename -uid "E62BED8E-43F2-71EA-1E95-9CA900A8FB4F";
	addAttr -ci true -sn "femurLength" -ln "femurLength" -min 0 -max 5 -at "double";
	addAttr -ci true -sn "tibiaLength" -ln "tibiaLength" -dv 5 -min 0 -max 5 -at "double";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr -k on ".femurLength" 5;
	setAttr -k on ".tibiaLength";
	setAttr ".nts" -type "string" "this is where guidable stuff comes from and it's still in the sketch, we'll need to supplant this with proper components parameters";
createNode locator -n "settingsShape" -p "settings";
	rename -uid "6535A3AE-47D8-8539-C546-36857DD50F42";
	setAttr -k off ".v";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "46BFE676-4995-07AF-EA84-9998347AF2F2";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "345FC65A-42B4-955A-0363-94BAB35DB0EA";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "95604379-4C0A-4A23-1BB6-E1B81347441B";
createNode displayLayerManager -n "layerManager";
	rename -uid "3B3EAE76-4328-4D1A-774E-2DBEA72DA376";
createNode displayLayer -n "defaultLayer";
	rename -uid "47B7C211-461A-819B-0D92-70A10B7C297F";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "048579CB-4440-BFA9-6A51-EFA56D35727C";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "60B4784F-4303-8975-139B-5DB969DA38AD";
	setAttr ".g" yes;
createNode ikRPsolver -n "ikRPsolver";
	rename -uid "B9E65A58-4653-C3C4-4144-6BA35C20A921";
createNode makeNurbCircle -n "makeNurbCircle1";
	rename -uid "E564EAD7-4510-6F81-8B5F-3393410C820D";
	setAttr ".nr" -type "double3" 0 1 0 ;
	setAttr ".r" 2;
	setAttr ".d" 1;
	setAttr ".s" 24;
createNode plusMinusAverage -n "legGlobal_L_hip2Ankle_displacement";
	rename -uid "39A26E34-49A1-7863-A6CC-90940ABDA672";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "legGlobal_L_limitedWorldAnkle_translate";
	rename -uid "BE42F8A2-4875-120E-6F0B-8B9FA8CECCDC";
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode addDoubleLinear -n "legGlobal_L_totalLength_fNode_add";
	rename -uid "24CF2356-4CB9-55BF-1F12-1EAD9E5AB312";
createNode vectorProduct -n "legGlobal_L_hip2ankle_direction_normal";
	rename -uid "050E5DA2-4B07-438D-24A7-D6A9A9779760";
	setAttr ".op" 0;
	setAttr ".no" yes;
createNode multiplyDivide -n "legGlobal_L_hip2Ankle_clamped_displacement";
	rename -uid "12AF279A-4014-A059-C248-A18F4D71A0AB";
createNode clamp -n "legGlobal_L_ankle2hip_clampedDistance";
	rename -uid "334F40F3-4D9A-EAFF-B1E1-7394A84D1984";
	setAttr ".mn" -type "float3" 3 3 3 ;
createNode distanceBetween -n "legGlobal_L_hip2ankle_distance";
	rename -uid "E7500AAA-428B-262E-6F0C-4D9EBFBFDB34";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "6D8108E1-4E25-54D3-01AD-F49859AB7A44";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n"
		+ "            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n"
		+ "            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n"
		+ "            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n"
		+ "            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1181\n            -height 1221\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n"
		+ "            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 0\n            -showAssets 1\n            -showContainedOnly 0\n            -showPublishedAsConnected 0\n            -showContainerContents 0\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n"
		+ "            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n"
		+ "            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 0\n            -showPublishedAsConnected 0\n            -showContainerContents 0\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n"
		+ "            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n"
		+ "                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -isSet 0\n                -isSetMember 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n"
		+ "                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                -selectionOrder \"display\" \n                -expandAttribute 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -clipTime \"on\" \n                -stackedCurves 0\n"
		+ "                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n"
		+ "                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n"
		+ "                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n"
		+ "                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n"
		+ "                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n"
		+ "                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n"
		+ "                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n"
		+ "                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n"
		+ "                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n"
		+ "                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 1\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 0\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 0\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 0\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n"
		+ "\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1181\\n    -height 1221\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1181\\n    -height 1221\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "5A55784D-4B1D-6C0F-66BC-E182D8E41028";
	setAttr ".b" -type "string" "playbackOptions -min -40 -max 120 -ast -40 -aet 200 ";
	setAttr ".st" 6;
createNode animCurveUA -n "legGlobal_L_roll_toe_fCurve";
	rename -uid "8C0A3869-4FD6-03D8-CB75-EBA484C47AFA";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  40 10 120 119.99999999999999;
createNode unitConversion -n "legGlobal_L_roll_UC";
	rename -uid "982BED6E-4A93-708A-9813-65966C2CD41C";
	setAttr ".cf" 57.295779513082323;
createNode animCurveUA -n "legGlobal_L_roll_tarsi_fCurve";
	rename -uid "EFF6015D-4515-1E59-B23B-BC9BDDF73B3D";
	setAttr ".tan" 2;
	setAttr -s 5 ".ktv[0:4]"  0 20 40 40 80 40 100 20 120 20;
	setAttr -s 5 ".kit[1:4]"  1 2 2 1;
	setAttr -s 5 ".kot[1:4]"  1 2 2 1;
	setAttr -s 5 ".kix[1:4]"  40 40 20 19.999999999999972;
	setAttr -s 5 ".kiy[1:4]"  0.3490658503988659 0 -0.3490658503988659 
		0;
	setAttr -s 5 ".kox[1:4]"  39.999999999999986 20 20 1;
	setAttr -s 5 ".koy[1:4]"  0 -0.3490658503988659 0 0;
createNode clamp -n "legGlobal_L_negativeOnlyRoll";
	rename -uid "7DFB4809-43F9-DC24-E2E9-E4BB9A48C420";
	setAttr ".mn" -type "float3" 0 0 -40 ;
createNode unitConversion -n "legGlobal_L_negativeOnlyRoll_UC";
	rename -uid "F43D9424-4F9F-44DB-85F2-9E86113E1EB0";
	setAttr ".cf" 0.017453292519943295;
createNode animCurveTA -n "animParameters_roll";
	rename -uid "AB41605F-4D7C-54D7-0A6E-2B8D317F2E41";
	setAttr ".tan" 2;
	setAttr -s 3 ".ktv[0:2]"  -40 -40 0 0 120 119.99999999999999;
createNode plusMinusAverage -n "legGlobal_L_ankle_offset_sub";
	rename -uid "BC1AC454-46A7-047F-71F1-BF856526D44F";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode decomposeMatrix -n "legGlobal_L_roll_tarsi_mtx2srt";
	rename -uid "05F8FCF5-4B4F-107E-6F19-4CA4AA2CC108";
	setAttr ".ot" -type "double3" -1.5662828788378289 2.3472963553338606 0 ;
	setAttr ".or" -type "double3" 0 0 29.999999999999996 ;
	setAttr ".os" -type "double3" 1 1 1 ;
	setAttr ".oqz" 0.25881904510252074;
	setAttr ".oqw" 0.96592582628906831;
createNode multDoubleLinear -n "legGlobal_L_ankle_offset_negation";
	rename -uid "687CD9E8-48E0-F2F0-E0F2-328B655A9729";
	setAttr ".i2" -1;
createNode decomposeMatrix -n "legGlobal_L_rolledAnkle_ctrl_world_mtx2srt";
	rename -uid "58574282-45A4-446A-9AA7-87A264FCAEE6";
	setAttr ".ot" -type "double3" 0 2.347 0 ;
	setAttr ".os" -type "double3" 1 1 1 ;
	setAttr ".oqw" 1;
createNode plusMinusAverage -n "legGlobal_L_tarsi_worldDirection_vec3";
	rename -uid "9A0CE03C-4235-00F8-AECA-76BF436A4D10";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode decomposeMatrix -n "legGlobal_L_roll_toes_world_mtx2srt";
	rename -uid "67237A7C-4832-8CC2-2473-FDA54AACD3D9";
	setAttr ".ot" -type "double3" -5.0303844939755837 0.34729635533386066 -1.0755285551056204e-015 ;
	setAttr ".or" -type "double3" 0 0 29.999999999999996 ;
	setAttr ".os" -type "double3" 1 1 1 ;
	setAttr ".oqz" 0.25881904510252074;
	setAttr ".oqw" 0.96592582628906831;
createNode angleBetween -n "legGlobal_L_tarsi_rolledAngle";
	rename -uid "FE18DCAE-4A64-B37F-BEB2-BFBE94A48267";
	setAttr ".v2" -type "double3" -1 0 0 ;
createNode animBlendNodeAdditiveDA -n "legGlobal_L_tarsi_rolledWorldAngle";
	rename -uid "AAD894B4-444A-550D-1485-9195D945911E";
	setAttr ".wb" -1;
	setAttr ".o" 29.999997258965475;
createNode animBlendNodeAdditiveDA -n "foot_M_toeAngle_negate";
	rename -uid "9BF000BB-4712-D397-2783-5F84EB60AC7B";
	setAttr ".wa" -1;
	setAttr ".o" -20;
createNode decomposeMatrix -n "foot_M_start_mtx2srt";
	rename -uid "1A530E00-4818-05F8-2026-98A898BD8DA5";
	setAttr ".ot" -type "double3" 0 2.3470001220703125 0 ;
	setAttr ".or" -type "double3" 29.999997258965475 0 0 ;
	setAttr ".os" -type "double3" 1 1 1 ;
	setAttr ".oqx" 0.25881902199753754;
	setAttr ".oqw" 0.96592583248002961;
createNode composeMatrix -n "legGlobal_L_limitedAnkle_mtx";
	rename -uid "A552ABB6-46AC-CE50-D917-D886195BFBA7";
	setAttr ".omat" -type "matrix" 1 0 0 0 0 0.86602542770447632 0.49999995856927709 0
		 0 -0.49999995856927709 0.86602542770447632 0 0 2.3470001220703125 0 1;
createNode multMatrix -n "multMatrix1";
	rename -uid "CFE21D16-40E1-1F71-2128-D29D64607362";
createNode composeMatrix -n "bodyComponent_outputEmulation";
	rename -uid "ED152837-4216-011D-6C0A-A5A4EB77E634";
	setAttr ".it" -type "double3" 0 9 0 ;
	setAttr ".omat" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 9 0 1;
createNode decomposeMatrix -n "legGlobal_L_start_mtx2srt";
	rename -uid "86E57754-43F1-CBD8-6835-4D83D17AEBAA";
	setAttr ".ot" -type "double3" 0 9 0 ;
	setAttr ".os" -type "double3" 1 1 1 ;
	setAttr ".oqw" 1;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "443D4995-4E31-8365-6638-EEB571236422";
	setAttr ".tgi[0].tn" -type "string" "wholeLeg";
	setAttr ".tgi[0].vl" -type "double2" -7941.1507513445194 -878.52682356538935 ;
	setAttr ".tgi[0].vh" -type "double2" -1795.5191538505046 1717.314582540291 ;
	setAttr -s 49 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -2434.28564453125;
	setAttr ".tgi[0].ni[0].y" 98.571426391601563;
	setAttr ".tgi[0].ni[0].nvs" 18312;
	setAttr ".tgi[0].ni[1].x" -2948.571533203125;
	setAttr ".tgi[0].ni[1].y" 612.85711669921875;
	setAttr ".tgi[0].ni[1].nvs" 18313;
	setAttr ".tgi[0].ni[2].x" -2434.28564453125;
	setAttr ".tgi[0].ni[2].y" 612.85711669921875;
	setAttr ".tgi[0].ni[2].nvs" 18312;
	setAttr ".tgi[0].ni[3].x" -6162.85693359375;
	setAttr ".tgi[0].ni[3].y" 612.85711669921875;
	setAttr ".tgi[0].ni[3].nvs" 18313;
	setAttr ".tgi[0].ni[4].x" -2691.428466796875;
	setAttr ".tgi[0].ni[4].y" 612.85711669921875;
	setAttr ".tgi[0].ni[4].nvs" 18312;
	setAttr ".tgi[0].ni[5].x" -6034.28564453125;
	setAttr ".tgi[0].ni[5].y" -72.857139587402344;
	setAttr ".tgi[0].ni[5].nvs" 18312;
	setAttr ".tgi[0].ni[6].x" -4705.71435546875;
	setAttr ".tgi[0].ni[6].y" 98.571426391601563;
	setAttr ".tgi[0].ni[6].nvs" 18312;
	setAttr ".tgi[0].ni[7].x" -2520;
	setAttr ".tgi[0].ni[7].y" 184.28572082519531;
	setAttr ".tgi[0].ni[7].nvs" 18312;
	setAttr ".tgi[0].ni[8].x" -2691.428466796875;
	setAttr ".tgi[0].ni[8].y" 484.28570556640625;
	setAttr ".tgi[0].ni[8].nvs" 18312;
	setAttr ".tgi[0].ni[9].x" -7611.4287109375;
	setAttr ".tgi[0].ni[9].y" 570;
	setAttr ".tgi[0].ni[9].nvs" 18312;
	setAttr ".tgi[0].ni[10].x" -5048.5712890625;
	setAttr ".tgi[0].ni[10].y" 355.71429443359375;
	setAttr ".tgi[0].ni[10].nvs" 18312;
	setAttr ".tgi[0].ni[11].x" -4362.85693359375;
	setAttr ".tgi[0].ni[11].y" 98.571426391601563;
	setAttr ".tgi[0].ni[11].nvs" 18313;
	setAttr ".tgi[0].ni[12].x" -4962.85693359375;
	setAttr ".tgi[0].ni[12].y" 141.42857360839844;
	setAttr ".tgi[0].ni[12].nvs" 18312;
	setAttr ".tgi[0].ni[13].x" -3848.571533203125;
	setAttr ".tgi[0].ni[13].y" 12.857142448425293;
	setAttr ".tgi[0].ni[13].nvs" 18312;
	setAttr ".tgi[0].ni[14].x" -4105.71435546875;
	setAttr ".tgi[0].ni[14].y" 55.714286804199219;
	setAttr ".tgi[0].ni[14].nvs" 18313;
	setAttr ".tgi[0].ni[15].x" -7825.71435546875;
	setAttr ".tgi[0].ni[15].y" 484.28570556640625;
	setAttr ".tgi[0].ni[15].nvs" 18312;
	setAttr ".tgi[0].ni[16].x" -4705.71435546875;
	setAttr ".tgi[0].ni[16].y" 12.857142448425293;
	setAttr ".tgi[0].ni[16].nvs" 18312;
	setAttr ".tgi[0].ni[17].x" -5862.85693359375;
	setAttr ".tgi[0].ni[17].y" 484.28570556640625;
	setAttr ".tgi[0].ni[17].nvs" 18312;
	setAttr ".tgi[0].ni[18].x" -5477.14306640625;
	setAttr ".tgi[0].ni[18].y" -72.857139587402344;
	setAttr ".tgi[0].ni[18].nvs" 18312;
	setAttr ".tgi[0].ni[19].x" -5562.85693359375;
	setAttr ".tgi[0].ni[19].y" 441.42855834960937;
	setAttr ".tgi[0].ni[19].nvs" 18312;
	setAttr ".tgi[0].ni[20].x" -5562.85693359375;
	setAttr ".tgi[0].ni[20].y" 227.14285278320312;
	setAttr ".tgi[0].ni[20].nvs" 18312;
	setAttr ".tgi[0].ni[21].x" -4962.85693359375;
	setAttr ".tgi[0].ni[21].y" -30;
	setAttr ".tgi[0].ni[21].nvs" 18312;
	setAttr ".tgi[0].ni[22].x" -5734.28564453125;
	setAttr ".tgi[0].ni[22].y" -72.857139587402344;
	setAttr ".tgi[0].ni[22].nvs" 18312;
	setAttr ".tgi[0].ni[23].x" -6454.28564453125;
	setAttr ".tgi[0].ni[23].y" 484.28570556640625;
	setAttr ".tgi[0].ni[23].nvs" 18312;
	setAttr ".tgi[0].ni[24].x" -6334.28564453125;
	setAttr ".tgi[0].ni[24].y" 314.28570556640625;
	setAttr ".tgi[0].ni[24].nvs" 18312;
	setAttr ".tgi[0].ni[25].x" -5820;
	setAttr ".tgi[0].ni[25].y" 142.85714721679687;
	setAttr ".tgi[0].ni[25].nvs" 18312;
	setAttr ".tgi[0].ni[26].x" -6582.85693359375;
	setAttr ".tgi[0].ni[26].y" 55.714286804199219;
	setAttr ".tgi[0].ni[26].nvs" 18312;
	setAttr ".tgi[0].ni[27].x" -6805.71435546875;
	setAttr ".tgi[0].ni[27].y" 312.85714721679687;
	setAttr ".tgi[0].ni[27].nvs" 18312;
	setAttr ".tgi[0].ni[28].x" -6720;
	setAttr ".tgi[0].ni[28].y" 228.57142639160156;
	setAttr ".tgi[0].ni[28].nvs" 18312;
	setAttr ".tgi[0].ni[29].x" -3591.428466796875;
	setAttr ".tgi[0].ni[29].y" 227.14285278320312;
	setAttr ".tgi[0].ni[29].nvs" 18312;
	setAttr ".tgi[0].ni[30].x" -5134.28564453125;
	setAttr ".tgi[0].ni[30].y" -244.28572082519531;
	setAttr ".tgi[0].ni[30].nvs" 18312;
	setAttr ".tgi[0].ni[31].x" -5048.5712890625;
	setAttr ".tgi[0].ni[31].y" -330;
	setAttr ".tgi[0].ni[31].nvs" 18312;
	setAttr ".tgi[0].ni[32].x" -2691.428466796875;
	setAttr ".tgi[0].ni[32].y" 355.71429443359375;
	setAttr ".tgi[0].ni[32].nvs" 18312;
	setAttr ".tgi[0].ni[33].x" -6077.14306640625;
	setAttr ".tgi[0].ni[33].y" 228.57142639160156;
	setAttr ".tgi[0].ni[33].nvs" 18312;
	setAttr ".tgi[0].ni[34].x" -6634.28564453125;
	setAttr ".tgi[0].ni[34].y" 142.85714721679687;
	setAttr ".tgi[0].ni[34].nvs" 18312;
	setAttr ".tgi[0].ni[35].x" -5562.85693359375;
	setAttr ".tgi[0].ni[35].y" 355.71429443359375;
	setAttr ".tgi[0].ni[35].nvs" 18312;
	setAttr ".tgi[0].ni[36].x" -6334.28564453125;
	setAttr ".tgi[0].ni[36].y" 142.85714721679687;
	setAttr ".tgi[0].ni[36].nvs" 18312;
	setAttr ".tgi[0].ni[37].x" -2605.71435546875;
	setAttr ".tgi[0].ni[37].y" 270;
	setAttr ".tgi[0].ni[37].nvs" 18312;
	setAttr ".tgi[0].ni[38].x" -7054.28564453125;
	setAttr ".tgi[0].ni[38].y" 312.85714721679687;
	setAttr ".tgi[0].ni[38].nvs" 18312;
	setAttr ".tgi[0].ni[39].x" -7011.4287109375;
	setAttr ".tgi[0].ni[39].y" 227.14285278320312;
	setAttr ".tgi[0].ni[39].nvs" 18312;
	setAttr ".tgi[0].ni[40].x" -7311.4287109375;
	setAttr ".tgi[0].ni[40].y" 312.85714721679687;
	setAttr ".tgi[0].ni[40].nvs" 18312;
	setAttr ".tgi[0].ni[41].x" -5305.71435546875;
	setAttr ".tgi[0].ni[41].y" 398.57144165039062;
	setAttr ".tgi[0].ni[41].nvs" 18312;
	setAttr ".tgi[0].ni[42].x" -7568.5712890625;
	setAttr ".tgi[0].ni[42].y" 484.28570556640625;
	setAttr ".tgi[0].ni[42].nvs" 18312;
	setAttr ".tgi[0].ni[43].x" -2434.28564453125;
	setAttr ".tgi[0].ni[43].y" 484.28570556640625;
	setAttr ".tgi[0].ni[43].nvs" 18312;
	setAttr ".tgi[0].ni[44].x" -5220;
	setAttr ".tgi[0].ni[44].y" -158.57142639160156;
	setAttr ".tgi[0].ni[44].nvs" 18312;
	setAttr ".tgi[0].ni[45].x" -3248.571533203125;
	setAttr ".tgi[0].ni[45].y" 612.85711669921875;
	setAttr ".tgi[0].ni[45].nvs" 18313;
	setAttr ".tgi[0].ni[46].x" -5262.85693359375;
	setAttr ".tgi[0].ni[46].y" 141.42857360839844;
	setAttr ".tgi[0].ni[46].nvs" 18312;
	setAttr ".tgi[0].ni[47].x" -5520;
	setAttr ".tgi[0].ni[47].y" 141.42857360839844;
	setAttr ".tgi[0].ni[47].nvs" 18312;
	setAttr ".tgi[0].ni[48].x" -5468.5712890625;
	setAttr ".tgi[0].ni[48].y" -244.28572082519531;
	setAttr ".tgi[0].ni[48].nvs" 18304;
select -ne :time1;
	setAttr ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 20 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "arnold";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "bodyComponent_outputEmulation.omat" "|legGlobal_L_cmpnt|input.startMtx"
		;
connectAttr "legGlobal_L_limitedAnkle_mtx.omat" "|legGlobal_L_cmpnt|output.limitedAnkle"
		;
connectAttr "legGlobal_L_roll_tarsi_srt.rz" "|legGlobal_L_cmpnt|output.toeAngle"
		;
connectAttr "animParameters_roll.o" "animParameters.roll";
connectAttr "legGlobal_L_negativeOnlyRoll_UC.o" "legGlobal_L_roll_heel_srt.rz";
connectAttr "legGlobal_L_roll_toe_fCurve.o" "legGlobal_L_roll_tip_srt.rz";
connectAttr "legGlobal_L_roll_tarsi_fCurve.o" "legGlobal_L_roll_tarsi_srt.rz";
connectAttr "configParameters.toeLength" "legGlobal_L_roll_tarsi_srt.tx";
connectAttr "configParameters.tarsiLength" "legGlobal_L_roll_tarsiEnd_srt.tx";
connectAttr "makeNurbCircle1.oc" "legGlobal_L_worldAnkle_ctrlShape.cr";
connectAttr "legGlobal_L_ankle_offset_sub.o3y" "legGlobal_L_worldAnkle_rolled_srt.ty"
		;
connectAttr "legGlobal_L_ankle_offset_negation.o" "legGlobal_L_worldAnkle_rolled_srt.tz"
		;
connectAttr "legGlobal_L_ankle_offset_sub.o3z" "legGlobal_L_worldAnkle_rolled_srt.tx"
		;
connectAttr "legGlobal_L_limitedWorldAnkle_translate.o3" "legGlobal_L_limitedAnkle_srt.t"
		;
connectAttr "hip.msg" "leg_ankle_IKhdl.hsj";
connectAttr "effector1.hp" "leg_ankle_IKhdl.hee";
connectAttr "ikRPsolver.msg" "leg_ankle_IKhdl.hsv";
connectAttr "|legGlobal_L_cmpnt|output.limitedAnkle" "|foot_M_cpmnt|input.startMtx"
		;
connectAttr "|legGlobal_L_cmpnt|output.toeAngle" "|foot_M_cpmnt|input.toeAngle";
connectAttr "foot_M_start_mtx2srt.or" "foot_M_tarsii_ctrl_srtBuffer.r";
connectAttr "foot_M_start_mtx2srt.ot" "foot_M_tarsii_ctrl_srtBuffer.t";
connectAttr "foot_M_toeAngle_negate.o" "foot_M_toes_ctrl_srtBuffer.rx";
connectAttr "legGlobal_L_start_mtx2srt.ot" "hip.t";
connectAttr "settings.femurLength" "knee.tx";
connectAttr "settings.tibiaLength" "ankle_IK.tx";
connectAttr "ankle_IK.tx" "effector1.tx";
connectAttr "ankle_IK.ty" "effector1.ty";
connectAttr "ankle_IK.tz" "effector1.tz";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "legGlobal_L_rolledAnkle_ctrl_world_mtx2srt.ot" "legGlobal_L_hip2Ankle_displacement.i3[0]"
		;
connectAttr "legGlobal_L_start_mtx2srt.ot" "legGlobal_L_hip2Ankle_displacement.i3[1]"
		;
connectAttr "legGlobal_L_hip2Ankle_clamped_displacement.o" "legGlobal_L_limitedWorldAnkle_translate.i3[0]"
		;
connectAttr "legGlobal_L_start_mtx2srt.ot" "legGlobal_L_limitedWorldAnkle_translate.i3[1]"
		;
connectAttr "configParameters.femurLength" "legGlobal_L_totalLength_fNode_add.i1"
		;
connectAttr "configParameters.tibiaLength" "legGlobal_L_totalLength_fNode_add.i2"
		;
connectAttr "legGlobal_L_hip2Ankle_displacement.o3" "legGlobal_L_hip2ankle_direction_normal.i1"
		;
connectAttr "legGlobal_L_hip2ankle_direction_normal.o" "legGlobal_L_hip2Ankle_clamped_displacement.i1"
		;
connectAttr "legGlobal_L_ankle2hip_clampedDistance.opr" "legGlobal_L_hip2Ankle_clamped_displacement.i2x"
		;
connectAttr "legGlobal_L_ankle2hip_clampedDistance.opr" "legGlobal_L_hip2Ankle_clamped_displacement.i2y"
		;
connectAttr "legGlobal_L_ankle2hip_clampedDistance.opr" "legGlobal_L_hip2Ankle_clamped_displacement.i2z"
		;
connectAttr "legGlobal_L_totalLength_fNode_add.o" "legGlobal_L_ankle2hip_clampedDistance.mxr"
		;
connectAttr "legGlobal_L_hip2ankle_distance.d" "legGlobal_L_ankle2hip_clampedDistance.ipr"
		;
connectAttr "legGlobal_L_start_mtx2srt.ot" "legGlobal_L_hip2ankle_distance.p1";
connectAttr "legGlobal_L_rolledAnkle_ctrl_world_mtx2srt.ot" "legGlobal_L_hip2ankle_distance.p2"
		;
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_roll_toe_fCurve.i";
connectAttr "animParameters.roll" "legGlobal_L_roll_UC.i";
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_roll_tarsi_fCurve.i";
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_negativeOnlyRoll.ipb";
connectAttr "legGlobal_L_negativeOnlyRoll.opb" "legGlobal_L_negativeOnlyRoll_UC.i"
		;
connectAttr "legGlobal_L_roll_tarsi_mtx2srt.ot" "legGlobal_L_ankle_offset_sub.i3[0]"
		;
connectAttr "legGlobal_L_ankle_rest_srt.t" "legGlobal_L_ankle_offset_sub.i3[1]";
connectAttr "legGlobal_L_roll_tarsiEnd_srt.wm" "legGlobal_L_roll_tarsi_mtx2srt.imat"
		;
connectAttr "legGlobal_L_ankle_offset_sub.o3x" "legGlobal_L_ankle_offset_negation.i1"
		;
connectAttr "legGlobal_L_worldAnkle_rolled_srt.wm" "legGlobal_L_rolledAnkle_ctrl_world_mtx2srt.imat"
		;
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.ot" "legGlobal_L_tarsi_worldDirection_vec3.i3[0]"
		;
connectAttr "legGlobal_L_roll_tarsi_mtx2srt.ot" "legGlobal_L_tarsi_worldDirection_vec3.i3[1]"
		;
connectAttr "legGlobal_L_roll_tarsi_srt.wm" "legGlobal_L_roll_toes_world_mtx2srt.imat"
		;
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.o3" "legGlobal_L_tarsi_rolledAngle.v1"
		;
connectAttr "legGlobal_L_tarsi_rolledAngle.euz" "legGlobal_L_tarsi_rolledWorldAngle.ib"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.rx" "legGlobal_L_tarsi_rolledWorldAngle.ia"
		;
connectAttr "|foot_M_cpmnt|input.toeAngle" "foot_M_toeAngle_negate.ia";
connectAttr "|foot_M_cpmnt|input.startMtx" "foot_M_start_mtx2srt.imat";
connectAttr "legGlobal_L_tarsi_rolledWorldAngle.o" "legGlobal_L_limitedAnkle_mtx.irx"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.ry" "legGlobal_L_limitedAnkle_mtx.iry";
connectAttr "legGlobal_L_worldAnkle_ctrl.rz" "legGlobal_L_limitedAnkle_mtx.irz";
connectAttr "legGlobal_L_limitedAnkle_srt.t" "legGlobal_L_limitedAnkle_mtx.it";
connectAttr "|legGlobal_L_cmpnt|input.startMtx" "legGlobal_L_start_mtx2srt.imat"
		;
connectAttr "diagnostic_tip.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "|foot_M_cpmnt|input.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "foot_M_tarsii_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn"
		;
connectAttr "legGlobal_L_roll_tarsi_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "foot_M_start_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "bodyComponent_outputEmulation.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "legGlobal_L_hip2ankle_direction_normal.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "diagnostic_toes.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn";
connectAttr "foot_M_toeAngle_negate.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "legGlobal_L_tarsi_rolledWorldAngle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "legGlobal_L_hip2Ankle_clamped_displacement.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "legGlobal_L_hip2Ankle_displacement.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "legGlobal_L_limitedAnkle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn"
		;
connectAttr "legGlobal_L_limitedWorldAnkle_translate.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn"
		;
connectAttr "animParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn";
connectAttr "legGlobal_L_ankle2hip_clampedDistance.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn"
		;
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn"
		;
connectAttr "legGlobal_L_start_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[18].dn"
		;
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[19].dn"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[20].dn"
		;
connectAttr "legGlobal_L_hip2ankle_distance.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[21].dn"
		;
connectAttr "|legGlobal_L_cmpnt|input.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[22].dn"
		;
connectAttr "legGlobal_L_roll_tarsi_fCurve.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[23].dn"
		;
connectAttr "legGlobal_L_ankle_rest_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[24].dn"
		;
connectAttr "legGlobal_L_ankle_offset_negation.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[25].dn"
		;
connectAttr "legGlobal_L_roll_ankle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[26].dn"
		;
connectAttr "legGlobal_L_roll_heel_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[27].dn"
		;
connectAttr "legGlobal_L_roll_tip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[28].dn"
		;
connectAttr "legGlobal_L_limitedAnkle_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[29].dn"
		;
connectAttr "knee.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[30].dn";
connectAttr "ankle_IK.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[31].dn";
connectAttr "diagnostic_ankle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[32].dn"
		;
connectAttr "legGlobal_L_ankle_offset_sub.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[33].dn"
		;
connectAttr "legGlobal_L_roll_tarsiEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[34].dn"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[35].dn"
		;
connectAttr "legGlobal_L_roll_tarsi_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[36].dn"
		;
connectAttr "diagnostic_tarsi.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[37].dn"
		;
connectAttr "legGlobal_L_negativeOnlyRoll_UC.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[38].dn"
		;
connectAttr "legGlobal_L_roll_toe_fCurve.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[39].dn"
		;
connectAttr "legGlobal_L_negativeOnlyRoll.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[40].dn"
		;
connectAttr "legGlobal_L_tarsi_rolledAngle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[41].dn"
		;
connectAttr "legGlobal_L_roll_UC.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[42].dn"
		;
connectAttr "foot_M_toes_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[43].dn"
		;
connectAttr "hip.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[44].dn";
connectAttr "|legGlobal_L_cmpnt|output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[45].dn"
		;
connectAttr "legGlobal_L_rolledAnkle_ctrl_world_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[46].dn"
		;
connectAttr "legGlobal_L_worldAnkle_rolled_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[47].dn"
		;
connectAttr "settings.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[48].dn";
connectAttr "legGlobal_L_hip2Ankle_displacement.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_limitedWorldAnkle_translate.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_totalLength_fNode_add.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_hip2ankle_direction_normal.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_hip2Ankle_clamped_displacement.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_ankle2hip_clampedDistance.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_hip2ankle_distance.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "legGlobal_L_negativeOnlyRoll.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_L_ankle_offset_sub.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_L_roll_tarsi_mtx2srt.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "legGlobal_L_ankle_offset_negation.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_rolledAnkle_ctrl_world_mtx2srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_tarsi_rolledAngle.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "foot_M_start_mtx2srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "legGlobal_L_limitedAnkle_mtx.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "multMatrix1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "bodyComponent_outputEmulation.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_L_start_mtx2srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "legGlobal_L_worldAnkle_rolled_srtShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
// End of id01_footrollProto_v001_007.ma
