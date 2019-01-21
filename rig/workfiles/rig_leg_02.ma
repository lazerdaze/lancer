//Maya ASCII 2018 scene
//Name: rig_leg_02.ma
//Last modified: Sun, Jan 13, 2019 09:47:46 PM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	rename -uid "0E3E5F85-4752-044E-1BF7-B490F9C80EB9";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 12.703967546958886 3.5399557672496296 1.2984478026483486 ;
	setAttr ".r" -type "double3" -9.9383527292086011 82.599999999999739 -1.2347295893567371e-14 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "5362DD8A-44E8-1815-1D25-0A812F9AE34A";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 13.287441526907456;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "01609549-48E1-0A68-9E40-CCA248FC0B02";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "C7E85206-4F4F-9866-7585-B3BC65E7CAEC";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "C0C427E7-44C4-D786-2F8C-11A0DFCAEA40";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "19E74150-4D20-4135-2842-C787F60D9C4E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "86684065-41B4-61B8-0931-529C9143FFF7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 2.4922533718701212 0.85205213122557022 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "89E99911-4BFE-67F8-04DA-36A97D943B89";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 14.965775118671118;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "character_group";
	rename -uid "3ECE6E64-4C78-2DF7-CA9F-2489DEDB0568";
createNode transform -n "joint_group" -p "character_group";
	rename -uid "D6C5D471-4D38-4562-D2B9-CEAFB1F8EC04";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode joint -n "root_C_0_joint" -p "joint_group";
	rename -uid "827A6657-41F7-3D01-E06D-09B9B64D8A6C";
	setAttr ".t" -type "double3" 1.1840306323599276e-16 4 -1.0664799829382838 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".ssc" no;
	setAttr ".typ" 2;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_hip_0_joint" -p "root_C_0_joint";
	rename -uid "6B21B72E-40A7-E7F8-A4F1-3FB7B7C172EB";
	setAttr ".t" -type "double3" 1.0664800405502319 0 3.5520919566172163e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.9959671327898901e-15 -1.4124500153760508e-30 -45 ;
	setAttr ".ssc" no;
	setAttr ".typ" 2;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_hip_1_joint" -p "leg_C_hip_0_joint";
	rename -uid "2D3248BD-43AD-EDE8-3E1A-CDB2306A207B";
	setAttr ".t" -type "double3" 0.080211792340957322 3.3242300988012887e-17 -5.1432520967045226e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9083328088781107e-14 0 0 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_hip_2_joint" -p "leg_C_hip_0_joint";
	rename -uid "464BE4CE-41EF-0260-583D-D9860A5871B9";
	setAttr ".t" -type "double3" 1.5 5.1052896728689359e-17 9.2673276898598736e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -90.000000000000014 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_knee_0_joint" -p "leg_C_hip_0_joint";
	rename -uid "7E0F7693-4644-BC5F-7C9D-11BF6E88FA4F";
	setAttr ".t" -type "double3" 2.8284270763397217 -2.2204460492503131e-16 3.1401848636255743e-16 ;
	setAttr ".r" -type "double3" -1.109335173705636e-30 1.0207704879981805e-27 1.9984005899718748e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -90.000000000000014 ;
	setAttr ".ssc" no;
	setAttr ".typ" 3;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_knee_1_joint" -p "leg_C_knee_0_joint";
	rename -uid "6A374FBA-4507-EB9F-D18C-32A109FDE27F";
	setAttr ".t" -type "double3" 1.5 0 -8.4952118724667019e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_knee_2_joint" -p "leg_C_knee_0_joint";
	rename -uid "D663BD08-4469-2BA6-DAC3-47B83CC1F35B";
	setAttr ".t" -type "double3" 2.7724068471577121 3.3306690738754696e-16 -2.2006825536204082e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_foot_0_joint" -p "leg_C_knee_0_joint";
	rename -uid "B8294725-4B41-C856-6ACC-22AB19507873";
	setAttr ".t" -type "double3" 2.8284270763397217 -4.078274779151998e-16 1.5700924318127877e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_toe_0_joint" -p "leg_C_foot_0_joint";
	rename -uid "D455D460-48C2-4D7B-87D1-74BE534C56FE";
	setAttr ".t" -type "double3" 1.5427947862008293 6.0797965605060666e-16 1.5659073121546644e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.59457381679721677;
createNode transform -n "control_group" -p "character_group";
	rename -uid "F94B3447-4B54-5D63-FABB-22A9D794F8E1";
createNode transform -n "rig_global_control_position" -p "control_group";
	rename -uid "07F67260-450E-6484-151F-ABB3A2188210";
createNode transform -n "rig_global_control" -p "rig_global_control_position";
	rename -uid "E56D0C97-430A-35F4-6582-5C90E7F56FB3";
	addAttr -ci true -sn "jointVisibility" -ln "jointVisibility" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "FKIK" -ln "FKIK" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "globalScale" -ln "globalScale" -dv 1 -at "double";
	addAttr -ci true -k true -m -sn "slideLeaf" -ln "slideLeaf" -at "double";
	addAttr -ci true -k true -m -sn "slide" -ln "slide" -at "double";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".jointVisibility" yes;
	setAttr -k on ".FKIK";
	setAttr -k on ".globalScale";
	setAttr -k on ".slideLeaf";
	setAttr -k on ".slideLeaf";
	setAttr -k on ".slideLeaf[0]";
	setAttr -k on ".slideLeaf[1]";
	setAttr -k on ".slideLeaf[2]";
	setAttr -k on ".slideLeaf[3]";
createNode nurbsCurve -n "rig_global_controlShape" -p "rig_global_control";
	rename -uid "C92DED41-42B4-E5F6-8587-E894414B260C";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "leg_C_0_FKControl_group" -p "rig_global_control";
	rename -uid "47495DB2-4D5A-D260-CB09-44813185C9D7";
createNode transform -n "leg_C_hip_0_FKControl_position" -p "leg_C_0_FKControl_group";
	rename -uid "BDD521F1-4886-2035-D685-28BDC88CE726";
	setAttr ".t" -type "double3" 0 4 0 ;
	setAttr ".r" -type "double3" 90 -45 -90 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
createNode transform -n "leg_C_hip_0_FKControl" -p "leg_C_hip_0_FKControl_position";
	rename -uid "8122EEC7-4418-0725-5CF2-648A22BD0BCC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "leg_C_hip_0_FKControlShape" -p "leg_C_hip_0_FKControl";
	rename -uid "7ECE6DF9-416C-A24D-CD20-6A8D55FC0BA6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.2197910707351852e-16 -0.78361162489122449 -0.7836116248912246
		6.7857323231109134e-17 -6.7857323231109109e-17 -1.1081941875543877
		-1.2601436025374905e-16 0.78361162489122449 -0.78361162489122438
		-2.4606854055573016e-16 1.1081941875543881 -5.7448982375248304e-17
		-2.2197910707351852e-16 0.78361162489122449 0.78361162489122449
		-6.7857323231109196e-17 1.1100856969603224e-16 1.1081941875543884
		1.2601436025374905e-16 -0.78361162489122449 0.78361162489122438
		2.4606854055573016e-16 -1.1081941875543881 1.511240500779959e-16
		2.2197910707351852e-16 -0.78361162489122449 -0.7836116248912246
		6.7857323231109134e-17 -6.7857323231109109e-17 -1.1081941875543877
		-1.2601436025374905e-16 0.78361162489122449 -0.78361162489122438
		;
createNode transform -n "leg_C_knee_0_FKControl_position" -p "leg_C_hip_0_FKControl";
	rename -uid "EE74617E-449A-BA41-60AC-35984416BBF4";
	setAttr ".t" -type "double3" 2.8284271247461894 0 0 ;
	setAttr ".r" -type "double3" 0 0 -90.000000000000014 ;
	setAttr ".s" -type "double3" 1 1 0.99999999999999978 ;
createNode transform -n "leg_C_knee_0_FKControl" -p "leg_C_knee_0_FKControl_position";
	rename -uid "A2CCA1C0-4C2E-8A75-7E5F-3EA536D5AB5F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 4.4408920985006262e-16 -9.8607613152626476e-32 0 ;
	setAttr ".sp" -type "double3" 4.4408920985006262e-16 -9.8607613152626476e-32 0 ;
createNode nurbsCurve -n "leg_C_knee_0_FKControlShape" -p "leg_C_knee_0_FKControl";
	rename -uid "6A357242-4A76-A463-04F4-84A018A334F8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.2197910707351852e-16 -0.78361162489122449 -0.7836116248912246
		6.7857323231109134e-17 -6.7857323231109109e-17 -1.1081941875543877
		-1.2601436025374905e-16 0.78361162489122449 -0.78361162489122438
		-2.4606854055573016e-16 1.1081941875543881 -5.7448982375248304e-17
		-2.2197910707351852e-16 0.78361162489122449 0.78361162489122449
		-6.7857323231109196e-17 1.1100856969603224e-16 1.1081941875543884
		1.2601436025374905e-16 -0.78361162489122449 0.78361162489122438
		2.4606854055573016e-16 -1.1081941875543881 1.511240500779959e-16
		2.2197910707351852e-16 -0.78361162489122449 -0.7836116248912246
		6.7857323231109134e-17 -6.7857323231109109e-17 -1.1081941875543877
		-1.2601436025374905e-16 0.78361162489122449 -0.78361162489122438
		;
createNode transform -n "leg_C_foot_0_FKControl_position" -p "leg_C_knee_0_FKControl";
	rename -uid "B70C96EE-49C1-BEEB-C803-1AA475C26929";
	setAttr ".t" -type "double3" 2.8284271247461903 6.5035359056653816e-17 -9.4205547521026475e-16 ;
createNode transform -n "leg_C_foot_0_FKControl" -p "leg_C_foot_0_FKControl_position";
	rename -uid "FF65F915-4788-9D38-D62C-9E83127CB3F9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "leg_C_foot_0_FKControlShape" -p "leg_C_foot_0_FKControl";
	rename -uid "5733E2B6-4ABB-8900-58D6-63AB715EE621";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.2197910707351852e-16 -0.78361162489122449 -0.7836116248912246
		6.7857323231109134e-17 -6.7857323231109109e-17 -1.1081941875543877
		-1.2601436025374905e-16 0.78361162489122449 -0.78361162489122438
		-2.4606854055573016e-16 1.1081941875543881 -5.7448982375248304e-17
		-2.2197910707351852e-16 0.78361162489122449 0.78361162489122449
		-6.7857323231109196e-17 1.1100856969603224e-16 1.1081941875543884
		1.2601436025374905e-16 -0.78361162489122449 0.78361162489122438
		2.4606854055573016e-16 -1.1081941875543881 1.511240500779959e-16
		2.2197910707351852e-16 -0.78361162489122449 -0.7836116248912246
		6.7857323231109134e-17 -6.7857323231109109e-17 -1.1081941875543877
		-1.2601436025374905e-16 0.78361162489122449 -0.78361162489122438
		;
createNode transform -n "leg_C_0_IKControl_group" -p "rig_global_control";
	rename -uid "1D08BA25-4D50-1475-7C89-60807E048152";
	setAttr ".t" -type "double3" 1.1840306323599276e-16 4 -1.0664799829382838 ;
	setAttr ".r" -type "double3" 0 -89.999999999999986 0 ;
createNode transform -n "leg_C_knee_0_IKControl_position" -p "leg_C_0_IKControl_group";
	rename -uid "DE4647AF-4E0C-937C-1713-7D973D77E041";
	setAttr ".t" -type "double3" 6.0664799829382838 -1.9999999999999996 1.4654322143331347e-15 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
createNode transform -n "leg_C_knee_0_IKControl" -p "leg_C_knee_0_IKControl_position";
	rename -uid "E7BC11A5-4B43-5879-1FD8-54B1C90ECC10";
	setAttr -l on -k off ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 4.4408920985006262e-16 -1.9721522630525295e-31 1.9721522630525295e-31 ;
	setAttr ".sp" -type "double3" 4.4408920985006262e-16 -1.9721522630525295e-31 1.9721522630525295e-31 ;
createNode nurbsCurve -n "leg_C_knee_0_IKControlShape" -p "leg_C_knee_0_IKControl";
	rename -uid "7DF2A44C-42AA-1BC9-00D8-80982B6738C8";
	setAttr -k off ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.5627577924682713e-16 -0.66261185642447384 -0.66261185642447396
		1.2595239191646901e-16 -5.7379275000421612e-17 -0.93707467394470467
		-3.7982996510000622e-17 0.66261185642447384 -0.66261185642447384
		-1.3949925884525721e-16 0.93707467394470512 -4.8578116572280648e-17
		-1.1912954541473239e-16 0.66261185642447384 0.66261185642447384
		1.1193841915625697e-17 9.3867410983756124e-17 0.93707467394470523
		1.7512923034209536e-16 -0.66261185642447384 0.66261185642447384
		2.7664549267735195e-16 -0.93707467394470512 1.2778854242554949e-16
		2.5627577924682713e-16 -0.66261185642447384 -0.66261185642447396
		1.2595239191646901e-16 -5.7379275000421612e-17 -0.93707467394470467
		-3.7982996510000622e-17 0.66261185642447384 -0.66261185642447384
		;
createNode transform -n "leg_C_foot_0_IKControl_position" -p "leg_C_0_IKControl_group";
	rename -uid "134298CE-4F5E-FA38-A856-A5801EB900E5";
	setAttr ".t" -type "double3" 1.0664799829382834 -3.9999999999999991 -2.7282779376553173e-16 ;
	setAttr ".r" -type "double3" 0 0 -135.00000000000003 ;
	setAttr ".s" -type "double3" 1 1.0000000000000004 1 ;
createNode transform -n "leg_C_foot_0_IKControl" -p "leg_C_foot_0_IKControl_position";
	rename -uid "FCBBFC3B-4C1C-16DE-79F8-5CBFD21BCF69";
	setAttr -l on -k off ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 2.1895288505075267e-47 -9.8607613152626476e-32 0 ;
	setAttr ".sp" -type "double3" 2.1895288505075267e-47 -9.8607613152626476e-32 0 ;
createNode nurbsCurve -n "leg_C_foot_0_IKControlShape" -p "leg_C_foot_0_IKControl";
	rename -uid "EC044C93-4A9A-3687-ABAA-10BD0E31824B";
	setAttr -k off ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.8770266233077976e-16 -0.66261185642447384 -0.66261185642447396
		5.7379275000421624e-17 -5.7379275000421599e-17 -0.93707467394470467
		-1.0655611342604799e-16 0.66261185642447384 -0.66261185642447384
		-2.0807237576130458e-16 0.93707467394470512 -4.8578116572280648e-17
		-1.8770266233077976e-16 0.66261185642447384 0.66261185642447384
		-5.7379275000421673e-17 9.3867410983756136e-17 0.93707467394470523
		1.0655611342604799e-16 -0.66261185642447384 0.66261185642447384
		2.0807237576130458e-16 -0.93707467394470512 1.2778854242554949e-16
		1.8770266233077976e-16 -0.66261185642447384 -0.66261185642447396
		5.7379275000421624e-17 -5.7379275000421599e-17 -0.93707467394470467
		-1.0655611342604799e-16 0.66261185642447384 -0.66261185642447384
		;
createNode ikHandle -n "leg_C_0_ikHandle" -p "leg_C_foot_0_IKControl";
	rename -uid "2FBFFE8F-4606-59B9-24FB-FB99C23D6BB3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.5700924586837747e-16 7.8504622934188736e-16 1.4130832128153975e-15 ;
	setAttr ".r" -type "double3" -135.00000000000003 90 0 ;
	setAttr ".s" -type "double3" 1 1 0.99999999999999989 ;
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "ikHandle1_poleVectorConstraint1" -p "leg_C_0_ikHandle";
	rename -uid "59517D16-4FAA-580D-1A25-75985CC2F0BD";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "leg_C_knee_0_IKControlW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
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
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" -2.4651903288156619e-31 -2 1.9999999999999993 ;
	setAttr -k on ".w0";
createNode transform -n "leg_C_0_IKJoint_position" -p "leg_C_0_IKControl_group";
	rename -uid "126AC0A6-4AF7-90EC-3910-6EA22105619F";
createNode joint -n "leg_C_0_IKJoint" -p "leg_C_0_IKJoint_position";
	rename -uid "3F6AAE2E-4EC0-BC2E-ECE0-DFBAE0528986";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.9959671327898901e-15 -1.4124500153760508e-30 -45 ;
	setAttr ".ssc" no;
	setAttr ".typ" 2;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_1_IKJoint" -p "leg_C_0_IKJoint";
	rename -uid "20913079-41DE-9A16-2358-4E985266E48D";
	setAttr ".t" -type "double3" 2.8284271247461898 -2.2204460492503131e-16 3.1401849173675498e-16 ;
	setAttr ".r" -type "double3" -1.1093352118797366e-30 1.0207705072793618e-27 1.9984006587403382e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -90.000000000000014 ;
	setAttr ".ssc" no;
	setAttr ".typ" 3;
	setAttr ".radi" 0.59457381679721677;
createNode joint -n "leg_C_2_IKJoint" -p "leg_C_1_IKJoint";
	rename -uid "D0E00D93-45E0-BC31-1ED7-D883944A2E7C";
	setAttr ".t" -type "double3" 2.8284271247461903 -2.2204460492503131e-16 1.5700924586837764e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.59457381679721677;
createNode ikEffector -n "effector1" -p "leg_C_1_IKJoint";
	rename -uid "C2CFDAAA-426D-67BB-FD22-DF8B25E43DC5";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "leg_C_hip_0_IKControl_position" -p "leg_C_0_IKControl_group";
	rename -uid "BC93FC0B-4CA7-FBAC-1F45-888CCA06A549";
	setAttr ".t" -type "double3" 1.0659999847412109 0 9.8607613152626476e-32 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode transform -n "leg_C_hip_0_IKControl" -p "leg_C_hip_0_IKControl_position";
	rename -uid "BF35A452-46BB-7AB6-F67A-46A894BE2904";
	setAttr -l on -k off ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0.00047999819707278781 0 3.5520918970797795e-16 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "leg_C_hip_0_IKControlShape" -p "leg_C_hip_0_IKControl";
	rename -uid "75590240-429F-C984-C47B-C3859576F08D";
	setAttr -k off ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.8770266233077976e-16 -0.66261185642447384 -0.66261185642447396
		5.7379275000421624e-17 -5.7379275000421599e-17 -0.93707467394470467
		-1.0655611342604799e-16 0.66261185642447384 -0.66261185642447384
		-2.0807237576130458e-16 0.93707467394470512 -4.8578116572280648e-17
		-1.8770266233077976e-16 0.66261185642447384 0.66261185642447384
		-5.7379275000421673e-17 9.3867410983756136e-17 0.93707467394470523
		1.0655611342604799e-16 -0.66261185642447384 0.66261185642447384
		2.0807237576130458e-16 -0.93707467394470512 1.2778854242554949e-16
		1.8770266233077976e-16 -0.66261185642447384 -0.66261185642447396
		5.7379275000421624e-17 -5.7379275000421599e-17 -0.93707467394470467
		-1.0655611342604799e-16 0.66261185642447384 -0.66261185642447384
		;
createNode transform -n "mesh_group" -p "character_group";
	rename -uid "ED56ED06-4777-3F09-7A29-78B311AACD01";
createNode transform -n "leg_C_0_group";
	rename -uid "E6E77E51-4409-26C8-CE26-348CAE92A614";
	setAttr ".t" -type "double3" 1.1840306323599276e-16 4 -1.0664799829382838 ;
	setAttr ".r" -type "double3" 0 -89.999999999999986 0 ;
createNode transform -n "leg_C_hip_0_rigJoint_position" -p "leg_C_0_group";
	rename -uid "DBD8E1E3-493F-30C0-A6F2-6188AAFB8866";
	setAttr ".t" -type "double3" 1.0664800405502319 0 3.5520919566172163e-16 ;
	setAttr ".r" -type "double3" 0 0 -45.000000000000007 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode transform -n "leg_C_hip_0_rigJoint_connection" -p "leg_C_hip_0_rigJoint_position";
	rename -uid "D674B9BA-4B60-6FEB-2FBA-DABDFBD80A98";
	setAttr ".t" -type "double3" 0 0 -2.4651903288156619e-32 ;
createNode joint -n "leg_C_hip_0_rigJoint" -p "leg_C_hip_0_rigJoint_connection";
	rename -uid "D03887DA-4454-5D31-5083-16B6D5F6FEF0";
	setAttr ".t" -type "double3" 0 0 -2.4651903288156619e-32 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 2;
	setAttr ".radi" 0.25;
createNode transform -n "leg_C_0_detailControl_position" -p "leg_C_hip_0_rigJoint";
	rename -uid "D0A44DF7-4406-D2B4-B2D4-2B9DE8485B7F";
	setAttr ".t" -type "double3" 0.0802117923409571 -4.4408920985006262e-16 -5.1432520967045257e-17 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode transform -n "leg_C_0_detailControl_connection" -p "leg_C_0_detailControl_position";
	rename -uid "5E929E9E-4A40-D36C-505F-B19484DACBE3";
	setAttr ".t" -type "double3" 0 -4.4408920985006262e-16 0 ;
createNode transform -n "leg_C_0_detailControl" -p "leg_C_0_detailControl_connection";
	rename -uid "60B13CF6-434C-B611-836F-CB8975E06ABA";
createNode nurbsCurve -n "leg_C_0_detailControlShape" -p "leg_C_0_detailControl";
	rename -uid "E3EF5ACD-46DE-8DC0-D09F-C287EE01CF60";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1.1102230246251565e-16 -0.5 0.5
		-1.1102230246251565e-16 -0.5 -0.5
		1.1102230246251565e-16 0.5 -0.5
		1.1102230246251565e-16 0.5 0.5
		-1.1102230246251565e-16 -0.5 0.5
		;
createNode joint -n "leg_C_hip_1_rigJoint" -p "leg_C_0_detailControl";
	rename -uid "AAE257D7-4D7B-5CAA-1A30-82A9BF0AE1DB";
	setAttr ".t" -type "double3" -0.00021179234095658472 8.8817841970012523e-16 5.1432520967045226e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.25;
createNode transform -n "leg_C_1_detailControl_position" -p "leg_C_hip_0_rigJoint";
	rename -uid "EC115B84-49A4-D2CE-20AD-F6B0AF8F01A9";
	setAttr ".t" -type "double3" 1.4999999757376425 4.3555897555336287e-08 9.267328647019823e-17 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode transform -n "leg_C_1_detailControl_connection" -p "leg_C_1_detailControl_position";
	rename -uid "EEFCB941-4416-8155-C386-149E7012AF13";
	setAttr ".t" -type "double3" 0 -4.4408920985006262e-16 4.9303806576313238e-32 ;
createNode transform -n "leg_C_1_detailControl" -p "leg_C_1_detailControl_connection";
	rename -uid "DFBD2786-489D-FDBB-C8AE-12A3B2B5C0D0";
	setAttr ".t" -type "double3" 0 0 4.9303806576313238e-32 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode nurbsCurve -n "leg_C_1_detailControlShape" -p "leg_C_1_detailControl";
	rename -uid "B7C34064-4943-EBE1-B85C-29890E016208";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1.1102230246251565e-16 -0.5 0.5
		-1.1102230246251565e-16 -0.5 -0.5
		1.1102230246251565e-16 0.5 -0.5
		1.1102230246251565e-16 0.5 0.5
		-1.1102230246251565e-16 -0.5 0.5
		;
createNode joint -n "leg_C_hip_2_rigJoint" -p "leg_C_1_detailControl";
	rename -uid "EE17F525-44F2-A2ED-3CA3-4D87DED89CB6";
	setAttr ".t" -type "double3" 2.426235679031663e-08 -4.3555897555336287e-08 -9.2673286470198243e-17 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.25;
createNode transform -n "leg_C_2_detailControl_position" -p "leg_C_hip_0_rigJoint";
	rename -uid "4DDCDEA7-4637-10B3-E1B5-DFB389118669";
	setAttr ".t" -type "double3" 2.8038594977279421 -1.3322676295501878e-15 2.2501253159249665e-16 ;
createNode transform -n "leg_C_2_detailControl_connection" -p "leg_C_2_detailControl_position";
	rename -uid "6997D813-4A2F-AFFA-31EE-E0B67F091B4F";
	setAttr ".t" -type "double3" 0 -4.4408920985006262e-16 4.9303806576313238e-32 ;
createNode transform -n "leg_C_2_detailControl" -p "leg_C_2_detailControl_connection";
	rename -uid "0CAA4649-4391-5601-C20C-D0B79222CDF3";
	setAttr ".t" -type "double3" 0 0 4.9303806576313238e-32 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode nurbsCurve -n "leg_C_2_detailControlShape" -p "leg_C_2_detailControl";
	rename -uid "41504CFE-47BB-3110-B544-FC9B6ACA1FA2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1.1102230246251565e-16 -0.5 0.5
		-1.1102230246251565e-16 -0.5 -0.5
		1.1102230246251565e-16 0.5 -0.5
		1.1102230246251565e-16 0.5 0.5
		-1.1102230246251565e-16 -0.5 0.5
		;
createNode joint -n "leg_C_hip_3_rigJoint" -p "leg_C_2_detailControl";
	rename -uid "7A107782-417B-CF9F-C644-E2B51E9F085A";
	setAttr ".t" -type "double3" 0.00014050227205730792 1.7763568394002505e-15 -2.2501253159249665e-16 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.25;
createNode transform -n "leg_C_knee_0_rigJoint_position" -p "leg_C_hip_0_rigJoint";
	rename -uid "A4722D29-4645-A6B7-B90D-A8A913CF3910";
	setAttr ".t" -type "double3" 2.8190687859580681 -1.7763568394002505e-15 3.1254914824711629e-16 ;
	setAttr ".r" -type "double3" 0 0 -89.999999999999986 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000004 1 ;
createNode transform -n "leg_C_knee_0_rigJoint_connection" -p "leg_C_knee_0_rigJoint_position";
	rename -uid "003AF6D3-4074-3D20-2311-33B037B90B2B";
	setAttr ".t" -type "double3" -4.4408920985006262e-16 -6.7480743215497796e-16 0 ;
	setAttr ".s" -type "double3" 0.99999999999999967 0.99999999999999956 0.99999999999999978 ;
createNode joint -n "leg_C_knee_0_rigJoint" -p "leg_C_knee_0_rigJoint_connection";
	rename -uid "A9D4BB83-4E19-0D45-3050-8CB06DF1A5EA";
	setAttr ".t" -type "double3" -4.4408920985006262e-16 2.203098814490545e-16 4.9303806576313238e-32 ;
	setAttr ".r" -type "double3" -1.109335173705636e-30 1.0207704879981805e-27 1.9984005899718748e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 3;
	setAttr ".radi" 0.25;
createNode transform -n "leg_C_3_detailControl_position" -p "leg_C_knee_0_rigJoint";
	rename -uid "FE1781BC-4283-5871-C70C-0FB0DF7CAD46";
	setAttr ".t" -type "double3" 1.5 0 -8.4952118724667007e-17 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
createNode transform -n "leg_C_3_detailControl_connection" -p "leg_C_3_detailControl_position";
	rename -uid "7AD6AA73-4698-3958-B424-9B81FFC557B2";
	setAttr ".t" -type "double3" 0 -1.6543612251060553e-24 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
createNode transform -n "leg_C_3_detailControl" -p "leg_C_3_detailControl_connection";
	rename -uid "4F59B49B-4B97-2EA9-2256-56B5BF25AE71";
	setAttr ".t" -type "double3" 0 -1.1102230742559933e-16 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 1 ;
createNode nurbsCurve -n "leg_C_3_detailControlShape" -p "leg_C_3_detailControl";
	rename -uid "D303B9B6-4EC1-5E01-964E-7D893EEF4D42";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1.1102230246251565e-16 -0.5 0.5
		-1.1102230246251565e-16 -0.5 -0.5
		1.1102230246251565e-16 0.5 -0.5
		1.1102230246251565e-16 0.5 0.5
		-1.1102230246251565e-16 -0.5 0.5
		;
createNode joint -n "leg_C_knee_1_rigJoint" -p "leg_C_3_detailControl";
	rename -uid "17F9336B-4613-7FB3-77D9-0387EB73BE3E";
	setAttr ".t" -type "double3" 0 1.0928757898653885e-16 8.4952118724667007e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.25;
createNode transform -n "leg_C_4_detailControl_position" -p "leg_C_knee_0_rigJoint";
	rename -uid "9A69F9CF-49D9-55E6-D9B0-8EA12F58BCC9";
	setAttr ".t" -type "double3" 2.7724068467512977 -2.3386396638680473e-10 -2.2006926764805497e-18 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
createNode transform -n "leg_C_4_detailControl_connection" -p "leg_C_4_detailControl_position";
	rename -uid "3175844A-4662-996C-AD9E-95B5874BBC78";
	setAttr ".t" -type "double3" 0 3.4694452975923891e-18 -4.9303806576313238e-32 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
createNode transform -n "leg_C_4_detailControl" -p "leg_C_4_detailControl_connection";
	rename -uid "CBE659CA-410E-C01D-DBBD-7687A67E26CF";
	setAttr ".t" -type "double3" 6.9388939039072284e-18 -6.9388988669909037e-18 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 1 ;
createNode nurbsCurve -n "leg_C_4_detailControlShape" -p "leg_C_4_detailControl";
	rename -uid "639AFB20-475E-36C3-24BD-E0A722282CD0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1.1102230246251565e-16 -0.5 0.5
		-1.1102230246251565e-16 -0.5 -0.5
		1.1102230246251565e-16 0.5 -0.5
		1.1102230246251565e-16 0.5 0.5
		-1.1102230246251565e-16 -0.5 0.5
		;
createNode joint -n "leg_C_knee_2_rigJoint" -p "leg_C_4_detailControl";
	rename -uid "C3F75A97-4170-9E7C-DD9E-23A596943A89";
	setAttr ".t" -type "double3" -0.00040684675129797759 2.3386402363267944e-10 2.2006926764805497e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.25;
createNode transform -n "leg_C_foot_0_rigJoint_position" -p "leg_C_knee_0_rigJoint";
	rename -uid "71BB2CE7-4CD2-5EE2-52BD-DA9016253D4F";
	setAttr ".t" -type "double3" 2.8284270763397226 -8.795048023202412e-16 1.5700924318127872e-16 ;
	setAttr ".r" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
createNode transform -n "leg_C_foot_0_rigJoint_connection" -p "leg_C_foot_0_rigJoint_position";
	rename -uid "63DC8BFA-4143-999A-B4AD-D08699939BD9";
	setAttr ".t" -type "double3" 0 0 1.9721522630525295e-31 ;
	setAttr ".s" -type "double3" 1 0.99999999999999978 1.0000000000000002 ;
createNode joint -n "leg_C_foot_0_rigJoint" -p "leg_C_foot_0_rigJoint_connection";
	rename -uid "D841DCE5-41CD-D062-E1D0-FF832F972B9B";
	setAttr ".t" -type "double3" 6.2970462177958098e-16 9.4195488716007565e-16 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -1.5902773407317587e-14 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.25;
createNode joint -n "leg_C_toe_0_rigJoint" -p "leg_C_foot_0_rigJoint";
	rename -uid "FDEA48CB-4B12-ED09-FB65-AEA74847B0E1";
	setAttr ".t" -type "double3" 1.5427947862008293 6.0797965605060666e-16 1.5659073121546644e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".typ" 4;
	setAttr ".radi" 0.25;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "24B55B63-4035-83C8-5DED-5AAFB9A89643";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "453ABE80-496A-3414-2E18-998B0B3C5B12";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "108C50E7-4643-172F-2F8C-87973AE45E1E";
createNode displayLayerManager -n "layerManager";
	rename -uid "1368DD3D-4634-99DF-1236-DC998CA0A621";
	setAttr ".cdl" 1;
	setAttr ".dli[1]"  1;
	setAttr -s 2 ".dli";
createNode displayLayer -n "defaultLayer";
	rename -uid "1A005273-4A9B-9443-FCC8-21B1246EE88C";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "191C8750-42B7-74AB-F7CD-0AA0B1C89320";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "9191CD39-44CE-810F-AACC-5A805313A331";
	setAttr ".g" yes;
createNode ikRPsolver -n "ikRPsolver";
	rename -uid "A3F5B41B-4655-6F0F-0A11-A3B3C0896895";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "6ECFE7DC-4B86-F929-1E0B-B3A7185922A3";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n"
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1067\n            -height 737\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n"
		+ "            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 0\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 0\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n"
		+ "            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 0\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 0\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n"
		+ "            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n"
		+ "                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -isSet 0\n                -isSetMember 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n"
		+ "                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"selected\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                -selectionOrder \"display\" \n                -expandAttribute 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"on\" \n                -smoothness \"fine\" \n                -resultSamples 1\n"
		+ "                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -clipTime \"on\" \n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n"
		+ "                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n"
		+ "                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n"
		+ "                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n"
		+ "                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n"
		+ "                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n"
		+ "                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n"
		+ "                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -highlightConnections 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n"
		+ "                -showNamespace 1\n                -showShapes 0\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 2\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1067\\n    -height 737\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1067\\n    -height 737\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 1 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "B467B9B6-4F27-2C42-3E06-48AF1940375F";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode makeNurbCircle -n "makeNurbCircle1";
	rename -uid "75D6D498-4A73-A43B-A61B-16AD99C3114D";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode transformGeometry -n "transformGeometry1";
	rename -uid "5A7C383B-487D-D3F3-AB78-F49F5A9389A9";
	setAttr ".txf" -type "matrix" 5 0 0 0 0 5 0 0 0 0 5 0 0 0 0 1;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "535A73A0-4E9A-87ED-9BEE-D89E00E8E8A6";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -328.57141551517361 -285.71427436102056 ;
	setAttr ".tgi[0].vh" -type "double2" -57.142854872204104 322.61903479931902 ;
createNode blendColors -n "blendColors1";
	rename -uid "4C3670AF-4659-0BE7-357A-D08B88F0CA41";
createNode blendColors -n "blendColors2";
	rename -uid "38E177FE-4463-F329-FBB6-DC874CF3DBEF";
createNode unitConversion -n "unitConversion1";
	rename -uid "37B0F9F7-4DFE-DF17-5529-A3A2BDF2B5B5";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion2";
	rename -uid "A8D220DF-4740-67D4-40F5-36B8B0DC3521";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion3";
	rename -uid "CF46B37E-40B0-F8D9-8C6D-4B8E412400C2";
	setAttr ".cf" 0.017453292519943295;
createNode blendColors -n "blendColors3";
	rename -uid "F9D5922E-4701-7BBE-4F25-3092199CA079";
createNode blendColors -n "blendColors4";
	rename -uid "7A7F6CD8-4E2B-37AD-8DA1-9896FD6B5372";
createNode addDoubleLinear -n "addDoubleLinear3";
	rename -uid "98619E75-499D-67A1-17AC-3C8D9DC785E8";
	setAttr ".i2" 2.828;
createNode blendColors -n "blendColors5";
	rename -uid "71449917-4C3D-43DC-CB5C-87B52943101A";
createNode blendColors -n "blendColors6";
	rename -uid "199ABB40-4B32-EB7D-E75F-50A36C3A79E3";
createNode unitConversion -n "unitConversion4";
	rename -uid "21DFC0AC-4222-1F7E-7F10-1183D4C991B4";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion5";
	rename -uid "8F2C3A0A-4594-896C-D848-A2B4065BE1A4";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion6";
	rename -uid "EB9A30EC-4228-34D7-A6D1-668593476979";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion7";
	rename -uid "794DB26F-42B8-620A-5D71-50BB793639B9";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion8";
	rename -uid "147394EA-482A-B95D-E37F-4A9D0167440B";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion9";
	rename -uid "E586B8C8-453B-E07E-D528-4D9ED9B68317";
	setAttr ".cf" 0.017453292519943295;
createNode reverse -n "reverse1";
	rename -uid "868C314D-43D9-97A3-9E48-8BAC522C5491";
createNode addDoubleLinear -n "addDoubleLinear2";
	rename -uid "F5F918EE-4B34-1F68-2B34-07B53ED4506F";
	setAttr ".i2" 2.828;
createNode addDoubleLinear -n "addDoubleLinear4";
	rename -uid "D4578F6A-462D-582A-BDE4-0B826787CA06";
	setAttr ".i2" 1.066;
createNode addDoubleLinear -n "addDoubleLinear5";
	rename -uid "FC8EC21D-4F32-DC92-C01A-C7AB2A67F015";
	setAttr ".i2" 1.066;
createNode displayLayer -n "layer1";
	rename -uid "6C04EF78-45C1-4BF2-D23B-BD86FDC45404";
	setAttr ".v" no;
	setAttr ".do" 1;
createNode addDoubleLinear -n "addDoubleLinear7";
	rename -uid "BD4B1991-442A-8600-D099-CFB6DA9822D9";
	setAttr ".i2" 1.5;
createNode addDoubleLinear -n "addDoubleLinear8";
	rename -uid "91B2A374-4F67-5694-1DA3-36A7837027C0";
	setAttr ".i2" 2.804;
createNode addDoubleLinear -n "addDoubleLinear9";
	rename -uid "952A7E98-4494-91A2-85D5-33A70A92C207";
	setAttr ".i2" 1.5;
createNode addDoubleLinear -n "addDoubleLinear10";
	rename -uid "8295BC0B-4111-53F5-AE78-FC9D95B31F4F";
	setAttr ".i2" 2.772;
createNode addDoubleLinear -n "addDoubleLinear6";
	rename -uid "569162AB-4E03-76B5-8699-28981557E626";
	setAttr ".i2" 0.08;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "EF3C9ED7-4ED9-D0F4-C831-B88234EE2A87";
	setAttr -s 3 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "fkik";
	setAttr ".tgi[0].vl" -type "double2" -2569.2287424741921 -1172.284226805871 ;
	setAttr ".tgi[0].vh" -type "double2" 2022.3422627830184 1378.2302852436048 ;
	setAttr -s 36 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -1187.142822265625;
	setAttr ".tgi[0].ni[0].y" -545.71429443359375;
	setAttr ".tgi[0].ni[0].nvs" 18314;
	setAttr ".tgi[0].ni[1].x" -572.85711669921875;
	setAttr ".tgi[0].ni[1].y" 745.71429443359375;
	setAttr ".tgi[0].ni[1].nvs" 18314;
	setAttr ".tgi[0].ni[2].x" -265.71429443359375;
	setAttr ".tgi[0].ni[2].y" 984.28570556640625;
	setAttr ".tgi[0].ni[2].nvs" 18314;
	setAttr ".tgi[0].ni[3].x" -1187.142822265625;
	setAttr ".tgi[0].ni[3].y" -31.428571701049805;
	setAttr ".tgi[0].ni[3].nvs" 18314;
	setAttr ".tgi[0].ni[4].x" -572.85711669921875;
	setAttr ".tgi[0].ni[4].y" 75.714286804199219;
	setAttr ".tgi[0].ni[4].nvs" 18314;
	setAttr ".tgi[0].ni[5].x" -572.85711669921875;
	setAttr ".tgi[0].ni[5].y" -100;
	setAttr ".tgi[0].ni[5].nvs" 18314;
	setAttr ".tgi[0].ni[6].x" 41.428569793701172;
	setAttr ".tgi[0].ni[6].y" 1371.4285888671875;
	setAttr ".tgi[0].ni[6].nvs" 18314;
	setAttr ".tgi[0].ni[7].x" -880;
	setAttr ".tgi[0].ni[7].y" -555.71429443359375;
	setAttr ".tgi[0].ni[7].nvs" 18312;
	setAttr ".tgi[0].ni[8].x" -265.71429443359375;
	setAttr ".tgi[0].ni[8].y" 325.71429443359375;
	setAttr ".tgi[0].ni[8].nvs" 18314;
	setAttr ".tgi[0].ni[9].x" -880;
	setAttr ".tgi[0].ni[9].y" 1357.142822265625;
	setAttr ".tgi[0].ni[9].nvs" 18312;
	setAttr ".tgi[0].ni[10].x" -265.71429443359375;
	setAttr ".tgi[0].ni[10].y" -241.42857360839844;
	setAttr ".tgi[0].ni[10].nvs" 18312;
	setAttr ".tgi[0].ni[11].x" 325.38363647460938;
	setAttr ".tgi[0].ni[11].y" 876.63458251953125;
	setAttr ".tgi[0].ni[11].nvs" 18314;
	setAttr ".tgi[0].ni[12].x" -265.71429443359375;
	setAttr ".tgi[0].ni[12].y" 1085.7142333984375;
	setAttr ".tgi[0].ni[12].nvs" 18312;
	setAttr ".tgi[0].ni[13].x" -1187.142822265625;
	setAttr ".tgi[0].ni[13].y" -1014.2857055664063;
	setAttr ".tgi[0].ni[13].nvs" 18314;
	setAttr ".tgi[0].ni[14].x" 313.70285034179688;
	setAttr ".tgi[0].ni[14].y" 354.95480346679688;
	setAttr ".tgi[0].ni[14].nvs" 18314;
	setAttr ".tgi[0].ni[15].x" -265.71429443359375;
	setAttr ".tgi[0].ni[15].y" 427.14285278320313;
	setAttr ".tgi[0].ni[15].nvs" 18312;
	setAttr ".tgi[0].ni[16].x" -1187.142822265625;
	setAttr ".tgi[0].ni[16].y" 437.14285278320313;
	setAttr ".tgi[0].ni[16].nvs" 18314;
	setAttr ".tgi[0].ni[17].x" -1350;
	setAttr ".tgi[0].ni[17].y" 1768.5714111328125;
	setAttr ".tgi[0].ni[17].nvs" 18304;
	setAttr ".tgi[0].ni[18].x" -572.85711669921875;
	setAttr ".tgi[0].ni[18].y" 570;
	setAttr ".tgi[0].ni[18].nvs" 18314;
	setAttr ".tgi[0].ni[19].x" -572.85711669921875;
	setAttr ".tgi[0].ni[19].y" -677.14288330078125;
	setAttr ".tgi[0].ni[19].nvs" 18314;
	setAttr ".tgi[0].ni[20].x" -880;
	setAttr ".tgi[0].ni[20].y" 1027.142822265625;
	setAttr ".tgi[0].ni[20].nvs" 18314;
	setAttr ".tgi[0].ni[21].x" -880;
	setAttr ".tgi[0].ni[21].y" -392.85714721679688;
	setAttr ".tgi[0].ni[21].nvs" 18312;
	setAttr ".tgi[0].ni[22].x" -265.71429443359375;
	setAttr ".tgi[0].ni[22].y" -342.85714721679688;
	setAttr ".tgi[0].ni[22].nvs" 18314;
	setAttr ".tgi[0].ni[23].x" -880;
	setAttr ".tgi[0].ni[23].y" 1458.5714111328125;
	setAttr ".tgi[0].ni[23].nvs" 18312;
	setAttr ".tgi[0].ni[24].x" 41.428569793701172;
	setAttr ".tgi[0].ni[24].y" 1817.142822265625;
	setAttr ".tgi[0].ni[24].nvs" 18314;
	setAttr ".tgi[0].ni[25].x" -1538.5714111328125;
	setAttr ".tgi[0].ni[25].y" 1192.857177734375;
	setAttr ".tgi[0].ni[25].nvs" 18304;
	setAttr ".tgi[0].ni[26].x" 1195.7142333984375;
	setAttr ".tgi[0].ni[26].y" -564.28570556640625;
	setAttr ".tgi[0].ni[26].nvs" 18304;
	setAttr ".tgi[0].ni[27].x" -265.71429443359375;
	setAttr ".tgi[0].ni[27].y" 1418.5714111328125;
	setAttr ".tgi[0].ni[27].nvs" 18314;
	setAttr ".tgi[0].ni[28].x" -1871.301513671875;
	setAttr ".tgi[0].ni[28].y" 1518.31005859375;
	setAttr ".tgi[0].ni[28].nvs" 18314;
	setAttr ".tgi[0].ni[29].x" -1187.142822265625;
	setAttr ".tgi[0].ni[29].y" 951.4285888671875;
	setAttr ".tgi[0].ni[29].nvs" 18314;
	setAttr ".tgi[0].ni[30].x" -880;
	setAttr ".tgi[0].ni[30].y" 297.14285278320313;
	setAttr ".tgi[0].ni[30].nvs" 18312;
	setAttr ".tgi[0].ni[31].x" -572.85711669921875;
	setAttr ".tgi[0].ni[31].y" 1472.857177734375;
	setAttr ".tgi[0].ni[31].nvs" 18314;
	setAttr ".tgi[0].ni[32].x" -880;
	setAttr ".tgi[0].ni[32].y" 398.57144165039063;
	setAttr ".tgi[0].ni[32].nvs" 18312;
	setAttr ".tgi[0].ni[33].x" 274.28570556640625;
	setAttr ".tgi[0].ni[33].y" -330;
	setAttr ".tgi[0].ni[33].nvs" 18306;
	setAttr ".tgi[0].ni[34].x" -1206.6383056640625;
	setAttr ".tgi[0].ni[34].y" 1548.800048828125;
	setAttr ".tgi[0].ni[34].nvs" 18314;
	setAttr ".tgi[0].ni[35].x" 313.70285034179688;
	setAttr ".tgi[0].ni[35].y" -194.49436950683594;
	setAttr ".tgi[0].ni[35].nvs" 18314;
	setAttr ".tgi[1].tn" -type "string" "Untitled_1";
	setAttr ".tgi[1].vl" -type "double2" -2904.4687458314756 -1558.5841266556276 ;
	setAttr ".tgi[1].vh" -type "double2" 1265.8127292448548 757.9135185588226 ;
	setAttr -s 27 ".tgi[1].ni";
	setAttr ".tgi[1].ni[0].x" -2085.71435546875;
	setAttr ".tgi[1].ni[0].y" -671.4285888671875;
	setAttr ".tgi[1].ni[0].nvs" 18304;
	setAttr ".tgi[1].ni[1].x" -2085.71435546875;
	setAttr ".tgi[1].ni[1].y" -541.4285888671875;
	setAttr ".tgi[1].ni[1].nvs" 18304;
	setAttr ".tgi[1].ni[2].x" -2085.71435546875;
	setAttr ".tgi[1].ni[2].y" -411.42855834960938;
	setAttr ".tgi[1].ni[2].nvs" 18304;
	setAttr ".tgi[1].ni[3].x" -978.78887939453125;
	setAttr ".tgi[1].ni[3].y" -436.43960571289063;
	setAttr ".tgi[1].ni[3].nvs" 18314;
	setAttr ".tgi[1].ni[4].x" -2851.428466796875;
	setAttr ".tgi[1].ni[4].y" -365.71429443359375;
	setAttr ".tgi[1].ni[4].nvs" 18304;
	setAttr ".tgi[1].ni[5].x" -2085.71435546875;
	setAttr ".tgi[1].ni[5].y" -281.42855834960938;
	setAttr ".tgi[1].ni[5].nvs" 18304;
	setAttr ".tgi[1].ni[6].x" -2811.428466796875;
	setAttr ".tgi[1].ni[6].y" -625.71429443359375;
	setAttr ".tgi[1].ni[6].nvs" 18304;
	setAttr ".tgi[1].ni[7].x" -2085.71435546875;
	setAttr ".tgi[1].ni[7].y" -21.428571701049805;
	setAttr ".tgi[1].ni[7].nvs" 18304;
	setAttr ".tgi[1].ni[8].x" -2085.71435546875;
	setAttr ".tgi[1].ni[8].y" 108.57142639160156;
	setAttr ".tgi[1].ni[8].nvs" 18304;
	setAttr ".tgi[1].ni[9].x" -427.14285278320313;
	setAttr ".tgi[1].ni[9].y" -292.85714721679688;
	setAttr ".tgi[1].ni[9].nvs" 18304;
	setAttr ".tgi[1].ni[10].x" -2838.571533203125;
	setAttr ".tgi[1].ni[10].y" -495.71429443359375;
	setAttr ".tgi[1].ni[10].nvs" 18304;
	setAttr ".tgi[1].ni[11].x" -2085.71435546875;
	setAttr ".tgi[1].ni[11].y" 238.57142639160156;
	setAttr ".tgi[1].ni[11].nvs" 18304;
	setAttr ".tgi[1].ni[12].x" -2085.71435546875;
	setAttr ".tgi[1].ni[12].y" 368.57144165039063;
	setAttr ".tgi[1].ni[12].nvs" 18304;
	setAttr ".tgi[1].ni[13].x" -2278.571533203125;
	setAttr ".tgi[1].ni[13].y" -1184.2857666015625;
	setAttr ".tgi[1].ni[13].nvs" 18304;
	setAttr ".tgi[1].ni[14].x" -1554.105224609375;
	setAttr ".tgi[1].ni[14].y" 393.61212158203125;
	setAttr ".tgi[1].ni[14].nvs" 18314;
	setAttr ".tgi[1].ni[15].x" 60;
	setAttr ".tgi[1].ni[15].y" -422.85714721679688;
	setAttr ".tgi[1].ni[15].nvs" 18304;
	setAttr ".tgi[1].ni[16].x" 61.724109649658203;
	setAttr ".tgi[1].ni[16].y" -294.58123779296875;
	setAttr ".tgi[1].ni[16].nvs" 18304;
	setAttr ".tgi[1].ni[17].x" 60;
	setAttr ".tgi[1].ni[17].y" 487.14285278320313;
	setAttr ".tgi[1].ni[17].nvs" 18304;
	setAttr ".tgi[1].ni[18].x" -247.14285278320313;
	setAttr ".tgi[1].ni[18].y" 487.14285278320313;
	setAttr ".tgi[1].ni[18].nvs" 18304;
	setAttr ".tgi[1].ni[19].x" 60;
	setAttr ".tgi[1].ni[19].y" -162.85714721679688;
	setAttr ".tgi[1].ni[19].nvs" 18304;
	setAttr ".tgi[1].ni[20].x" 60;
	setAttr ".tgi[1].ni[20].y" -32.857143402099609;
	setAttr ".tgi[1].ni[20].nvs" 18304;
	setAttr ".tgi[1].ni[21].x" 60;
	setAttr ".tgi[1].ni[21].y" 97.142860412597656;
	setAttr ".tgi[1].ni[21].nvs" 18304;
	setAttr ".tgi[1].ni[22].x" 60;
	setAttr ".tgi[1].ni[22].y" 227.14285278320313;
	setAttr ".tgi[1].ni[22].nvs" 18304;
	setAttr ".tgi[1].ni[23].x" -957.21734619140625;
	setAttr ".tgi[1].ni[23].y" -967.094970703125;
	setAttr ".tgi[1].ni[23].nvs" 18314;
	setAttr ".tgi[1].ni[24].x" -980.67510986328125;
	setAttr ".tgi[1].ni[24].y" 589.0294189453125;
	setAttr ".tgi[1].ni[24].nvs" 18314;
	setAttr ".tgi[1].ni[25].x" -970.708984375;
	setAttr ".tgi[1].ni[25].y" 65.755126953125;
	setAttr ".tgi[1].ni[25].nvs" 18314;
	setAttr ".tgi[1].ni[26].x" 60;
	setAttr ".tgi[1].ni[26].y" 357.14285278320313;
	setAttr ".tgi[1].ni[26].nvs" 18304;
	setAttr ".tgi[2].tn" -type "string" "Untitled_2";
	setAttr ".tgi[2].vl" -type "double2" -3152.748238762108 -2946.2421023557495 ;
	setAttr ".tgi[2].vh" -type "double2" 2826.7182977638768 375.21718864990237 ;
	setAttr -s 20 ".tgi[2].ni";
	setAttr ".tgi[2].ni[0].x" -1998.5714111328125;
	setAttr ".tgi[2].ni[0].y" -1257.142822265625;
	setAttr ".tgi[2].ni[0].nvs" 18304;
	setAttr ".tgi[2].ni[1].x" 1441.4285888671875;
	setAttr ".tgi[2].ni[1].y" -1257.142822265625;
	setAttr ".tgi[2].ni[1].nvs" 18304;
	setAttr ".tgi[2].ni[2].x" -266.12490844726563;
	setAttr ".tgi[2].ni[2].y" -308.60943603515625;
	setAttr ".tgi[2].ni[2].nvs" 18314;
	setAttr ".tgi[2].ni[3].x" -598.3193359375;
	setAttr ".tgi[2].ni[3].y" 236.8907470703125;
	setAttr ".tgi[2].ni[3].nvs" 18314;
	setAttr ".tgi[2].ni[4].x" 25.6302490234375;
	setAttr ".tgi[2].ni[4].y" 243.19326782226563;
	setAttr ".tgi[2].ni[4].nvs" 18314;
	setAttr ".tgi[2].ni[5].x" -289.95095825195313;
	setAttr ".tgi[2].ni[5].y" 299.71987915039063;
	setAttr ".tgi[2].ni[5].nvs" 18314;
	setAttr ".tgi[2].ni[6].x" -596.37908935546875;
	setAttr ".tgi[2].ni[6].y" -385.82833862304688;
	setAttr ".tgi[2].ni[6].nvs" 18314;
	setAttr ".tgi[2].ni[7].x" 45.311447143554688;
	setAttr ".tgi[2].ni[7].y" -388.71463012695313;
	setAttr ".tgi[2].ni[7].nvs" 18314;
	setAttr ".tgi[2].ni[8].x" -253.09605407714844;
	setAttr ".tgi[2].ni[8].y" -2119.188232421875;
	setAttr ".tgi[2].ni[8].nvs" 18314;
	setAttr ".tgi[2].ni[9].x" 46.071212768554688;
	setAttr ".tgi[2].ni[9].y" -2197.232666015625;
	setAttr ".tgi[2].ni[9].nvs" 18314;
	setAttr ".tgi[2].ni[10].x" -265.12777709960938;
	setAttr ".tgi[2].ni[10].y" -912.0853271484375;
	setAttr ".tgi[2].ni[10].nvs" 18314;
	setAttr ".tgi[2].ni[11].x" 76.082405090332031;
	setAttr ".tgi[2].ni[11].y" -1000.99755859375;
	setAttr ".tgi[2].ni[11].nvs" 18314;
	setAttr ".tgi[2].ni[12].x" -579.81591796875;
	setAttr ".tgi[2].ni[12].y" -2208.14990234375;
	setAttr ".tgi[2].ni[12].nvs" 18314;
	setAttr ".tgi[2].ni[13].x" 69.714546203613281;
	setAttr ".tgi[2].ni[13].y" -1611.4580078125;
	setAttr ".tgi[2].ni[13].nvs" 18314;
	setAttr ".tgi[2].ni[14].x" -602.0052490234375;
	setAttr ".tgi[2].ni[14].y" -1611.2286376953125;
	setAttr ".tgi[2].ni[14].nvs" 18314;
	setAttr ".tgi[2].ni[15].x" -607.65838623046875;
	setAttr ".tgi[2].ni[15].y" -1001.3015747070313;
	setAttr ".tgi[2].ni[15].nvs" 18314;
	setAttr ".tgi[2].ni[16].x" -267.40631103515625;
	setAttr ".tgi[2].ni[16].y" -1543.5535888671875;
	setAttr ".tgi[2].ni[16].nvs" 18314;
	setAttr ".tgi[2].ni[17].x" 1430;
	setAttr ".tgi[2].ni[17].y" -2110;
	setAttr ".tgi[2].ni[17].nvs" 18304;
	setAttr ".tgi[2].ni[18].x" 1424.2857666015625;
	setAttr ".tgi[2].ni[18].y" -404.28570556640625;
	setAttr ".tgi[2].ni[18].nvs" 18304;
	setAttr ".tgi[2].ni[19].x" -2007.142822265625;
	setAttr ".tgi[2].ni[19].y" -2110;
	setAttr ".tgi[2].ni[19].nvs" 18304;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
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
	setAttr -s 16 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "mayaHardware2";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "rig_global_control.t" "joint_group.t";
connectAttr "rig_global_control.r" "joint_group.r";
connectAttr "rig_global_control.s" "joint_group.s";
connectAttr "rig_global_control.jointVisibility" "joint_group.v";
connectAttr "layer1.di" "joint_group.do";
connectAttr "rig_global_control.globalScale" "rig_global_control.sx" -l on;
connectAttr "rig_global_control.globalScale" "rig_global_control.sy" -l on;
connectAttr "rig_global_control.globalScale" "rig_global_control.sz" -l on;
connectAttr "transformGeometry1.og" "rig_global_controlShape.cr";
connectAttr "reverse1.ox" "leg_C_0_FKControl_group.v";
connectAttr "layer1.di" "leg_C_0_FKControl_group.do";
connectAttr "rig_global_control.FKIK" "leg_C_0_IKControl_group.v";
connectAttr "layer1.di" "leg_C_0_IKControl_group.do";
connectAttr "leg_C_0_IKJoint.msg" "leg_C_0_ikHandle.hsj";
connectAttr "effector1.hp" "leg_C_0_ikHandle.hee";
connectAttr "ikRPsolver.msg" "leg_C_0_ikHandle.hsv";
connectAttr "ikHandle1_poleVectorConstraint1.ctx" "leg_C_0_ikHandle.pvx";
connectAttr "ikHandle1_poleVectorConstraint1.cty" "leg_C_0_ikHandle.pvy";
connectAttr "ikHandle1_poleVectorConstraint1.ctz" "leg_C_0_ikHandle.pvz";
connectAttr "leg_C_0_ikHandle.pim" "ikHandle1_poleVectorConstraint1.cpim";
connectAttr "leg_C_0_IKJoint.pm" "ikHandle1_poleVectorConstraint1.ps";
connectAttr "leg_C_0_IKJoint.t" "ikHandle1_poleVectorConstraint1.crp";
connectAttr "leg_C_knee_0_IKControl.t" "ikHandle1_poleVectorConstraint1.tg[0].tt"
		;
connectAttr "leg_C_knee_0_IKControl.rp" "ikHandle1_poleVectorConstraint1.tg[0].trp"
		;
connectAttr "leg_C_knee_0_IKControl.rpt" "ikHandle1_poleVectorConstraint1.tg[0].trt"
		;
connectAttr "leg_C_knee_0_IKControl.pm" "ikHandle1_poleVectorConstraint1.tg[0].tpm"
		;
connectAttr "ikHandle1_poleVectorConstraint1.w0" "ikHandle1_poleVectorConstraint1.tg[0].tw"
		;
connectAttr "addDoubleLinear5.o" "leg_C_0_IKJoint.tx";
connectAttr "leg_C_hip_0_IKControl.ty" "leg_C_0_IKJoint.ty";
connectAttr "leg_C_hip_0_IKControl.tz" "leg_C_0_IKJoint.tz";
connectAttr "leg_C_2_IKJoint.tx" "effector1.tx";
connectAttr "leg_C_2_IKJoint.ty" "effector1.ty";
connectAttr "leg_C_2_IKJoint.tz" "effector1.tz";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "makeNurbCircle1.oc" "transformGeometry1.ig";
connectAttr "rig_global_control.FKIK" "blendColors1.b";
connectAttr "leg_C_0_IKJoint.t" "blendColors1.c1";
connectAttr "leg_C_hip_0_FKControl.ty" "blendColors1.c2g";
connectAttr "leg_C_hip_0_FKControl.tz" "blendColors1.c2b";
connectAttr "addDoubleLinear4.o" "blendColors1.c2r";
connectAttr "rig_global_control.FKIK" "blendColors2.b";
connectAttr "unitConversion1.o" "blendColors2.c1";
connectAttr "unitConversion2.o" "blendColors2.c2";
connectAttr "leg_C_0_IKJoint.r" "unitConversion1.i";
connectAttr "leg_C_hip_0_FKControl.r" "unitConversion2.i";
connectAttr "blendColors2.op" "unitConversion3.i";
connectAttr "rig_global_control.FKIK" "blendColors3.b";
connectAttr "unitConversion4.o" "blendColors3.c1";
connectAttr "unitConversion6.o" "blendColors3.c2";
connectAttr "rig_global_control.FKIK" "blendColors4.b";
connectAttr "leg_C_1_IKJoint.t" "blendColors4.c1";
connectAttr "leg_C_knee_0_FKControl.ty" "blendColors4.c2g";
connectAttr "leg_C_knee_0_FKControl.tz" "blendColors4.c2b";
connectAttr "addDoubleLinear2.o" "blendColors4.c2r";
connectAttr "leg_C_foot_0_FKControl.tx" "addDoubleLinear3.i1";
connectAttr "rig_global_control.FKIK" "blendColors5.b";
connectAttr "leg_C_2_IKJoint.t" "blendColors5.c1";
connectAttr "leg_C_foot_0_FKControl.ty" "blendColors5.c2g";
connectAttr "leg_C_foot_0_FKControl.tz" "blendColors5.c2b";
connectAttr "addDoubleLinear3.o" "blendColors5.c2r";
connectAttr "rig_global_control.FKIK" "blendColors6.b";
connectAttr "unitConversion5.o" "blendColors6.c1";
connectAttr "unitConversion8.o" "blendColors6.c2";
connectAttr "leg_C_1_IKJoint.r" "unitConversion4.i";
connectAttr "leg_C_2_IKJoint.r" "unitConversion5.i";
connectAttr "leg_C_knee_0_FKControl.r" "unitConversion6.i";
connectAttr "blendColors3.op" "unitConversion7.i";
connectAttr "leg_C_foot_0_FKControl.r" "unitConversion8.i";
connectAttr "blendColors6.op" "unitConversion9.i";
connectAttr "rig_global_control.FKIK" "reverse1.ix";
connectAttr "leg_C_knee_0_FKControl.tx" "addDoubleLinear2.i1";
connectAttr "leg_C_hip_0_FKControl.tx" "addDoubleLinear4.i1";
connectAttr "leg_C_hip_0_IKControl.tx" "addDoubleLinear5.i1";
connectAttr "layerManager.dli[1]" "layer1.id";
connectAttr "leg_C_1_detailControl.tx" "addDoubleLinear7.i1";
connectAttr "leg_C_2_detailControl.tx" "addDoubleLinear8.i1";
connectAttr "leg_C_3_detailControl.tx" "addDoubleLinear9.i1";
connectAttr "leg_C_4_detailControl.tx" "addDoubleLinear10.i1";
connectAttr "leg_C_0_detailControl.tx" "addDoubleLinear6.i1";
connectAttr "leg_C_2_IKJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "addDoubleLinear4.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "blendColors1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "leg_C_knee_0_FKControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "addDoubleLinear2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "blendColors6.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn";
connectAttr "leg_C_0_FKControl_group.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "unitConversion8.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn";
connectAttr "blendColors4.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn";
connectAttr "unitConversion2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn";
connectAttr "unitConversion9.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "leg_C_hip_0_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "unitConversion3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "leg_C_foot_0_FKControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn"
		;
connectAttr "leg_C_knee_0_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn"
		;
connectAttr "unitConversion7.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn"
		;
connectAttr "leg_C_1_IKJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn"
		;
connectAttr "leg_C_hip_2_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn"
		;
connectAttr "blendColors3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[18].dn";
connectAttr "addDoubleLinear3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[19].dn"
		;
connectAttr "rig_global_control.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[20].dn"
		;
connectAttr "unitConversion5.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[21].dn"
		;
connectAttr "blendColors5.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[22].dn";
connectAttr "unitConversion1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[23].dn"
		;
connectAttr "leg_C_0_IKControl_group.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[24].dn"
		;
connectAttr "leg_C_knee_2_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[25].dn"
		;
connectAttr "layer1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[26].dn";
connectAttr "reverse1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[27].dn";
connectAttr "leg_C_hip_0_IKControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[28].dn"
		;
connectAttr "leg_C_hip_0_FKControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[29].dn"
		;
connectAttr "unitConversion6.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[30].dn"
		;
connectAttr "blendColors2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[31].dn";
connectAttr "unitConversion4.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[32].dn"
		;
connectAttr "addDoubleLinear5.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[33].dn"
		;
connectAttr "leg_C_0_IKJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[34].dn"
		;
connectAttr "leg_C_foot_0_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[35].dn"
		;
connectAttr "leg_C_knee_2_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[0].dn"
		;
connectAttr "leg_C_foot_0_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[1].dn"
		;
connectAttr "leg_C_toe_0_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[2].dn"
		;
connectAttr "leg_C_3_detailControl_connection.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[3].dn"
		;
connectAttr "leg_C_2_detailControl_connection.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[4].dn"
		;
connectAttr "leg_C_hip_0_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[5].dn"
		;
connectAttr "leg_C_2_detailControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[6].dn"
		;
connectAttr "leg_C_knee_0_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[7].dn"
		;
connectAttr "leg_C_hip_1_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[8].dn"
		;
connectAttr "leg_C_0_group.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[9].dn";
connectAttr "leg_C_2_detailControl_position.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[10].dn"
		;
connectAttr "leg_C_knee_1_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[11].dn"
		;
connectAttr "leg_C_hip_2_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[12].dn"
		;
connectAttr "leg_C_hip_3_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[13].dn"
		;
connectAttr "rig_global_control.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[14].dn"
		;
connectAttr "leg_C_knee_1_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[15].dn"
		;
connectAttr "leg_C_knee_2_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[16].dn"
		;
connectAttr "leg_C_toe_0_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[17].dn"
		;
connectAttr "leg_C_foot_0_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[18].dn"
		;
connectAttr "leg_C_knee_0_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[19].dn"
		;
connectAttr "leg_C_hip_2_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[20].dn"
		;
connectAttr "leg_C_hip_0_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[21].dn"
		;
connectAttr "root_C_0_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[22].dn";
connectAttr "leg_C_4_detailControl_connection.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[23].dn"
		;
connectAttr "leg_C_0_detailControl_connection.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[24].dn"
		;
connectAttr "leg_C_1_detailControl_connection.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[25].dn"
		;
connectAttr "leg_C_hip_1_joint.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[26].dn"
		;
connectAttr "leg_C_foot_0_rigJoint_connection.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[0].dn"
		;
connectAttr "leg_C_knee_0_rigJoint_connection.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[1].dn"
		;
connectAttr "addDoubleLinear7.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[2].dn"
		;
connectAttr "leg_C_0_detailControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[3].dn"
		;
connectAttr "leg_C_hip_1_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[4].dn"
		;
connectAttr "addDoubleLinear6.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[5].dn"
		;
connectAttr "leg_C_1_detailControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[6].dn"
		;
connectAttr "leg_C_hip_2_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[7].dn"
		;
connectAttr "addDoubleLinear10.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[8].dn"
		;
connectAttr "leg_C_knee_2_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[9].dn"
		;
connectAttr "addDoubleLinear8.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[10].dn"
		;
connectAttr "leg_C_hip_3_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[11].dn"
		;
connectAttr "leg_C_4_detailControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[12].dn"
		;
connectAttr "leg_C_knee_1_rigJoint.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[13].dn"
		;
connectAttr "leg_C_3_detailControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[14].dn"
		;
connectAttr "leg_C_2_detailControl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[15].dn"
		;
connectAttr "addDoubleLinear9.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[16].dn"
		;
connectAttr "leg_C_hip_0_rigJoint_position.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[17].dn"
		;
connectAttr "leg_C_knee_0_rigJoint_position.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[18].dn"
		;
connectAttr "leg_C_foot_0_rigJoint_position.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[19].dn"
		;
connectAttr "blendColors1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "blendColors2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "blendColors3.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "blendColors4.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear3.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "blendColors5.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "blendColors6.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "reverse1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear4.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear5.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear6.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear7.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear8.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear9.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear10.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
// End of rig_leg_02.ma
