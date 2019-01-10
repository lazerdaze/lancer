//Maya ASCII 2018ff07 scene
//Name: leg_v004.ma
//Last modified: Sat, May 12, 2018 10:19:36 PM
//Codeset: 1252
requires maya "2018ff07";
requires -nodeType "floatCondition" "lookdevKit" "1.0";
requires -nodeType "decomposeMatrix" -nodeType "composeMatrix" -nodeType "inverseMatrix"
		 "matrixNodes" "1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201711281015-8e846c9074";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -n "leg_R_cmpnt";
	rename -uid "8DF6D34B-49A3-9B94-DA5A-459CC10B315C";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
createNode transform -n "leg_R_input" -p "leg_R_cmpnt";
	rename -uid "AB171627-4004-6546-C8D5-A0B2C214BF1D";
	addAttr -ci true -sn "endWorld" -ln "endWorld" -at "matrix";
	addAttr -ci true -sn "rolledAnkle" -ln "rolledAnkle" -nn "rolledAnkle" -at "matrix";
	addAttr -ci true -sn "upVectorFrame" -ln "upVectorFrame" -at "matrix";
	addAttr -ci true -sn "rawAnkleControl" -ln "rawAnkleControl" -at "matrix";
	setAttr ".endWorld" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -1.6653345369377348e-14 11.841588736937647 -2.2621914758103046e-11 1;
	setAttr ".rolledAnkle" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.2790000000000057 2.5447593967200013 -0.51870724801412282 1;
	setAttr ".upVectorFrame" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -4.7380000000000058 6.7561481902608351 -9.2158626204103236 1;
	setAttr ".rawAnkleControl" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.2528433333772986 2.5444464459297689 -0.51882775330918385 1;
createNode transform -n "leg_R_output" -p "leg_R_cmpnt";
	rename -uid "C0BAD8DC-41A8-0626-5551-ACA0FD06D13E";
	addAttr -ci true -sn "chainEnd" -ln "chainEnd" -at "matrix";
createNode transform -n "control" -p "leg_R_cmpnt";
	rename -uid "4814D932-4432-BDBA-CB62-6DBB455573D0";
createNode transform -n "leg_R_animParameters" -p "|leg_R_cmpnt|control";
	rename -uid "C84B4495-4C7F-DD4E-8DDC-80A03FBE1DA9";
	addAttr -ci true -sn "FKIK_blend" -ln "FKIK_blend" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".FKIK_blend";
createNode transform -n "leg_R_IK_srtBuffer" -p "|leg_R_cmpnt|control";
	rename -uid "A33CA758-4D06-DC7C-6EAA-3BA57733C92F";
createNode transform -n "leg_R_hip_srt" -p "leg_R_IK_srtBuffer";
	rename -uid "678F4001-4C81-2F8F-8F86-B99B6E8DC46D";
createNode mesh -n "diagnosticCube_geoShape" -p "leg_R_hip_srt";
	rename -uid "B840A353-4F0C-2821-3359-49843D355DE6";
	setAttr -k off ".v";
	setAttr -s 3 ".iog";
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
	setAttr -s 10 ".pt[0:9]" -type "float3"  0.31097692 0.31127802 -0.16441351 
		-0.31299272 0.31127802 -0.16441351 0.31097692 -0.31269172 -0.16441351 -0.31299272 
		-0.31269172 -0.16441351 0.31097692 -0.31269172 0.45955637 -0.31299272 -0.31269172 
		0.45955637 0.31097692 0.31127802 0.45955637 -0.31299272 0.31127802 0.45955637 -0.001007581 
		-0.00070697814 0.014877097 -0.13370168 -0.00070697814 0.1475714;
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
createNode transform -n "leg_R_femurEnd_srt" -p "leg_R_hip_srt";
	rename -uid "74CFB8F9-4E82-B1C5-D9B9-EE8951436612";
createNode transform -n "leg_R_tibiaStart_srt" -p "leg_R_femurEnd_srt";
	rename -uid "72485456-4657-0620-1DA1-2D859B8BE7BA";
createNode transform -n "leg_R_tibiaEnd_srt" -p "leg_R_tibiaStart_srt";
	rename -uid "A1184C98-45E1-E60B-8C5E-8B99E45905EB";
createNode transform -n "leg_R_FK_hrc" -p "|leg_R_cmpnt|control";
	rename -uid "74DB9858-447A-FC25-AFAA-BB8F281DFD5B";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "leg_R_fk_handedness" -p "leg_R_FK_hrc";
	rename -uid "D8AE6B7C-436F-1F21-CD00-96AF59D4D624";
createNode transform -n "leg_R_fk01_ctrl_srtBuffer" -p "leg_R_fk_handedness";
	rename -uid "4A4E4B8F-4ACB-EFA6-E591-0E8D3C83C127";
	setAttr ".t" -type "double3" 2.1100000000000163 8.2979359030074455 0.11647361508212915 ;
	setAttr ".ro" 5;
createNode transform -n "leg_R_fk01_ctrl" -p "leg_R_fk01_ctrl_srtBuffer";
	rename -uid "D4C7B340-4BBB-6006-F7F9-1E863BFCCB5E";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.96589994 ;
createNode nurbsCurve -n "leg_R_fk01_ctrlShape" -p "leg_R_fk01_ctrl";
	rename -uid "04D30784-42A8-C6A5-7268-089BB332EBC0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0 0
		0 1 0
		1 0 0
		0 0 0
		0 0 3.7889897830403605
		;
createNode transform -n "leg_R_fk02_ctrl_srtBuffer" -p "leg_R_fk01_ctrl";
	rename -uid "AB925908-4251-434F-B995-5FA173EBB90D";
createNode transform -n "leg_R_fk02_ctrl" -p "leg_R_fk02_ctrl_srtBuffer";
	rename -uid "44D83984-4E58-0B57-5F3E-2A88A86D703E";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.96589994 ;
createNode nurbsCurve -n "leg_R_fk02_ctrlShape" -p "leg_R_fk02_ctrl";
	rename -uid "51D22E19-4096-A05A-1E5C-FD856FEA4236";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0 0
		0 1 0
		1 0 0
		0 0 0
		0 0 3.8063396303648802
		;
createNode transform -n "leg_R_fk03_ctrl_srtBuffer" -p "leg_R_fk02_ctrl";
	rename -uid "3C686519-4BD4-5389-0EA7-BF9C6EA7CAC4";
	setAttr ".ro" 4;
	setAttr ".s" -type "double3" -1 0.99999999999999956 -1 ;
createNode transform -n "leg_R_fk03_ctrl" -p "leg_R_fk03_ctrl_srtBuffer";
	rename -uid "D1C6DF71-4FCC-709A-409F-74AC239A83A0";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.96589994 ;
createNode nurbsCurve -n "leg_R_fk03_ctrlShape" -p "leg_R_fk03_ctrl";
	rename -uid "C85F7C9A-43FD-524F-F758-D18B2A26D2CB";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0 0
		0 1 0
		1 0 0
		0 0 0
		4.4408920985006262e-16 0 1.2678614721477759
		;
createNode transform -n "leg_R_limitedAnkle_srt" -p "|leg_R_cmpnt|control";
	rename -uid "CA6F7E9F-4EEC-82EC-56C0-1183BCD1220F";
createNode transform -n "leg_R_configParameters" -p "|leg_R_cmpnt|control";
	rename -uid "C33E54CE-4F63-9CCC-EF5A-3CAFEEBE5F9E";
	addAttr -ci true -sn "femurLength" -ln "femurLength" -min 0 -max 5 -at "double";
	addAttr -ci true -sn "tibiaLength" -ln "tibiaLength" -dv 5 -min 0 -max 5 -at "double";
	addAttr -ci true -sn "hipOffsetIK" -ln "hipOffsetIK" -at "matrix";
	addAttr -ci true -sn "hipOffsetFK" -ln "hipOffsetFK" -at "matrix";
	addAttr -ci true -sn "invertedHandedness" -ln "invertedHandedness" -min 0 -max 1 
		-at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".femurLength";
	setAttr -k on ".tibiaLength";
	setAttr -k on ".invertedHandedness" yes;
createNode transform -n "deform" -p "leg_R_cmpnt";
	rename -uid "1DCB4390-477B-AA4A-CC60-4DBCA4211BC8";
createNode joint -n "leg_R_j01_srt" -p "|leg_R_cmpnt|deform";
	rename -uid "D96223FC-4310-AF9D-384F-8895F7903E8E";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.7068965517241379;
createNode joint -n "leg_R_j02_srt" -p "leg_R_j01_srt";
	rename -uid "6B3C8086-433B-05A7-7655-CC91C47CC11B";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.7068965517241379;
createNode joint -n "leg_R_j03_srt" -p "leg_R_j02_srt";
	rename -uid "EE5F7D3C-4CED-3575-0ACE-3884E42E8DE8";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.7068965517241379;
createNode transform -n "guide" -p "leg_R_cmpnt";
	rename -uid "7296DC69-42E9-234F-886C-A89373392CD2";
createNode transform -n "leg_R_toolParameters" -p "|leg_R_cmpnt|guide";
	rename -uid "8F45D60F-4387-9351-2F1B-F1B482BE1815";
	addAttr -ci true -m -sn "toSwap" -ln "toSwap" -at "compound" -nc 2;
	addAttr -s false -ci true -sn "origin" -ln "origin" -at "message" -p "toSwap";
	addAttr -s false -ci true -sn "guided" -ln "guided" -at "message" -p "toSwap";
	addAttr -s false -ci true -m -sn "toDelete" -ln "toDelete" -at "message";
	setAttr -s 8 ".toSwap";
	setAttr -s 12 ".toDelete";
createNode transform -n "leg_R_guide_hipPos_ctrl_srtBuffer" -p "|leg_R_cmpnt|guide";
	rename -uid "AB2889D2-4944-8A33-14AC-85BD3F502982";
createNode transform -n "leg_R_guide_hipPos_ctrl" -p "leg_R_guide_hipPos_ctrl_srtBuffer";
	rename -uid "5D70FC91-4BFC-89BF-3252-D19543F880AC";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" -2.11 -3.5436528339302011 0.11647361510475107 ;
createNode nurbsCurve -n "leg_R_guide_hipPos_ctrlShape" -p "leg_R_guide_hipPos_ctrl";
	rename -uid "2995B93E-421D-6DB9-598A-1BAA5664B193";
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
createNode transform -n "leg_R_guide_kneePos_ctrl_srtBuffer" -p "leg_R_guide_hipPos_ctrl";
	rename -uid "EE02C2BF-44E3-60A9-B994-BAB03BFE1632";
createNode transform -n "leg_R_guide_kneePos_ctrl" -p "leg_R_guide_kneePos_ctrl_srtBuffer";
	rename -uid "842F6B95-4275-215B-04F4-C287E29807C9";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 0 -2.3856530387133725 2.9436547275218761 ;
	setAttr -l on ".tx";
createNode nurbsCurve -n "leg_R_guide_kneePos_ctrlShape" -p "leg_R_guide_kneePos_ctrl";
	rename -uid "9FBD12D7-46B6-8BE2-E9B0-71A6CE262D17";
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
createNode aimConstraint -n "leg_R_guide_kneeUpV_aim_cns" -p "leg_R_guide_kneePos_ctrl_srtBuffer";
	rename -uid "574673A8-477F-EB58-D996-6DA1D5A51785";
	addAttr -dcb 0 -ci true -sn "w0" -ln "legGlobal_L_worldAnkle_ctrlW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" -8.8817841970012523e-16 -2.3592239273284576e-16 1.7763568394002505e-15 ;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" -108.78803859417859 42.08439514048581 142.51117437558833 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999967 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".a" -type "double3" 0 0 1 ;
	setAttr -k on ".w0";
parent -s -nc -r -add "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|diagnosticCube_geoShape" "leg_R_tibiaStart_srt" ;
parent -s -nc -r -add "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|diagnosticCube_geoShape" "leg_R_tibiaEnd_srt" ;
createNode angleBetween -n "leg_R_IK_tension_rot";
	rename -uid "BB76840C-477D-D0A8-B9B8-888A4CA3DF98";
	setAttr ".v1" -type "double3" 0 -1 0 ;
createNode angleBetween -n "leg_R_IK_upVectoringAngle";
	rename -uid "BBD0E200-4D66-AE54-F2CC-2083D24B580F";
	setAttr ".v1" -type "double3" 0 0 -1 ;
createNode animBlendNodeAdditiveF -n "leg_R_fkik_blend_complement";
	rename -uid "EA9D3569-41CD-D1A5-EC7E-B9B62C43115E";
	setAttr ".wb" -1;
	setAttr ".ia" 1;
	setAttr ".o" 1;
createNode animBlendNodeAdditiveRotation -n "leg_R_fkik_j02_blended_rot";
	rename -uid "C69C3700-490F-D448-4540-F9A3B8054B9C";
	setAttr ".o" -type "double3" 44.769504766427154 -13.97399045812613 170.0571149534901 ;
createNode animBlendNodeAdditiveRotation -n "leg_R_fkik_j01_blended_rot";
	rename -uid "FF117057-4B49-E9C5-D856-41A7F04932D0";
	setAttr ".o" -type "double3" 57.285987229634486 13.97399045812613 -9.9428850465099092 ;
createNode decomposeMatrix -n "leg_R_fk01_ctrl_world_mtx";
	rename -uid "75A2E388-4823-3B4E-65E1-70A5CA2AEE7F";
	setAttr ".imat" -type "matrix" 0.955830310499581 -0.16755640722170154 -0.24148140286413355 0
		 0.29344252320070213 0.49724691784750119 0.81647840649264336 0 -0.016730305074326119 -0.8512757209565629 0.52445185079471712 0
		 -2.1100000000000163 8.2979359030074455 0.11647361508212915 1;
createNode decomposeMatrix -n "leg_R_fk02reframed01_rot";
	rename -uid "71E51702-47A3-2943-52C3-6F98C4DD94F0";
createNode decomposeMatrix -n "leg_R_hip_rot";
	rename -uid "1263FA50-4810-B242-4767-EFBE4BFA6F18";
createNode decomposeMatrix -n "leg_R_hipWorld_srt";
	rename -uid "895B010E-482C-E316-8609-96B22C16D12D";
createNode decomposeMatrix -n "leg_R_IK_upVector_hipYProjected_srt";
	rename -uid "B385D5E7-49D4-1DD7-E832-0C969EC64FFE";
createNode decomposeMatrix -n "leg_R_limitedAnkleWorld_srt";
	rename -uid "15D38715-4D15-2B5D-6366-94848F2064C6";
createNode expression -n "leg_R_IK_solver_xpr";
	rename -uid "5515A358-4460-5825-AFBA-478A4FF79E9E";
	setAttr -k on ".nds";
	setAttr -s 3 ".in";
	setAttr -s 3 ".in";
	setAttr -s 2 ".out";
	setAttr ".ixp" -type "string" "float $a = .I[0];\nfloat $b = .I[1];\nfloat $c = .I[2];\n\nfloat $sqA = pow($a, 2);\nfloat $sqB = pow($b, 2);\nfloat $sqC = pow($c, 2);\n\n.O[0] = (deg_to_rad(180.0) - acos(($sqA + $sqB - $sqC)/(2.0 * $a * $b)));\n.O[1] = deg_to_rad(90.0) + (-acos(($sqC + $sqA - $sqB)/(2.0 * $c * $a)));";
	setAttr ".uno" 1;
createNode multMatrix -n "leg_R_fk02reframed01_mtx";
	rename -uid "043EE944-4E7A-D4D3-DCD7-C0BD5C16AEA6";
createNode multMatrix -n "leg_R_IK_upVector_hipFramed_mtx";
	rename -uid "4AEF1C88-4AAB-94C6-ECC2-629AAD061274";
	setAttr -s 2 ".i";
createNode plusMinusAverage -n "leg_R_IK_ankleDisplacement_vec";
	rename -uid "7F42091A-480F-4DD8-D7D7-6AAA2DDD1415";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode decomposeMatrix -n "leg_R_rolledAnkle_ctrl_world_mtx2srt";
	rename -uid "44E53A54-4D29-CE84-1A2A-AFACE0704B81";
createNode addDoubleLinear -n "leg_R_totalLength_fNode_add";
	rename -uid "5D59A0E7-4FBA-D0DB-3275-41BA540A8529";
createNode plusMinusAverage -n "leg_R_limitedWorldAnkle_translate";
	rename -uid "B9435728-41ED-CE22-78D8-6A82C9CA30BE";
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode multDoubleLinear -n "leg_R_lengthLimit_fNode";
	rename -uid "09ED9E05-417D-E142-78E2-C8B2ADBC8688";
	setAttr ".i2" 0.992;
createNode clamp -n "leg_R_ankle2hip_clampedDistance";
	rename -uid "66366550-4613-A541-91AB-6699D2D6A862";
	setAttr ".mn" -type "float3" 3 3 3 ;
createNode multiplyDivide -n "leg_R_hip2Ankle_clamped_displacement";
	rename -uid "5BBC4C9E-4277-ECAF-ED56-1C8CABC675BD";
createNode distanceBetween -n "leg_R_hip2ankle_distance";
	rename -uid "10BFD1A8-4892-26D3-DC3B-EBB30205E300";
createNode plusMinusAverage -n "leg_R_hip2Ankle_displacement";
	rename -uid "D62B04DF-4010-A646-06CC-299987F60083";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode vectorProduct -n "leg_R_hip2ankle_direction_normal";
	rename -uid "9DABF4AA-4607-8B32-26F0-1E99EFA1ADE5";
	setAttr ".op" 0;
	setAttr ".no" yes;
createNode decomposeMatrix -n "leg_R_rolledAnkle_frame_srt";
	rename -uid "389AB29F-45F4-74F7-5373-4B9BE8371D38";
createNode multMatrix -n "leg_R_hipWorld_mtx";
	rename -uid "9EEA7D13-4284-FB9E-651C-D585768EE194";
	setAttr -s 2 ".i";
createNode distanceBetween -n "leg_R_guide_femurLength";
	rename -uid "FD044778-44F4-5742-A7EF-D5974893EE22";
createNode distanceBetween -n "leg_R_guide_tibiaLength";
	rename -uid "A3FF7D37-4362-7E7E-85D6-2ABE533E0A86";
createNode decomposeMatrix -n "leg_R_FK_start_srt";
	rename -uid "6500E1E8-42B6-1B61-B7F4-45B0ED46E7C3";
	setAttr ".ro" 5;
createNode decomposeMatrix -n "leg_R_guide_upVector_srt";
	rename -uid "E60A7044-4C6D-3FC5-98EE-008F1B58F759";
createNode decomposeMatrix -n "leg_R_guide_knee_world_srt";
	rename -uid "BFE26CE5-4B75-4B9A-F6FF-67A4DC3319F1";
createNode decomposeMatrix -n "leg_R_guide_hipInput_srt";
	rename -uid "F770B47B-41BD-DB6A-7908-EBAE36AD8433";
createNode decomposeMatrix -n "leg_R_guide_hip_world_srt";
	rename -uid "385012F3-4A24-2BCA-149A-FCB487F73F5A";
createNode decomposeMatrix -n "leg_R_guide_ankle_world_srt";
	rename -uid "B8D3491A-4377-CAA9-A8E9-3987642EC07F";
createNode plusMinusAverage -n "leg_R_guide_hip2UpV_vec";
	rename -uid "B48437A9-4F8D-C7D0-C1E3-ACA565098E1F";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode decomposeMatrix -n "leg_R_guide_globalAnkleInfk02Space_srt";
	rename -uid "E0C862E6-46F0-F17F-FC8F-FE8FC828EE55";
	setAttr ".ro" 4;
createNode multMatrix -n "leg_R_guide_globalAnkleInfk02Space";
	rename -uid "6D652101-48AC-F95B-6342-12A1A381B586";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "leg_R_globalAnkle_srt";
	rename -uid "C5EF69D0-4754-BAFC-F174-0D839108152E";
createNode multMatrix -n "leg_R_guide_ikHip_local_mtx";
	rename -uid "3D88E326-4D8B-A566-BFBC-70A4E14E8DE7";
	setAttr -s 2 ".i";
createNode inverseMatrix -n "leg_R_guide_endWorldInverse_mtx";
	rename -uid "6D511D45-4B5F-0F51-4110-3DBFEFAAC315";
	setAttr ".omat" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 1.6653345369377348e-14 -11.841588736937647 2.2621914758103049e-11 1;
createNode composeMatrix -n "leg_R_ankle_blend_mtx";
	rename -uid "D24019D5-4C9C-52A4-0FF3-5DBBC22B23F7";
	setAttr ".omat" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -0.41875307185034405 3.9117831557928815 5.2757283082146866 1;
createNode decomposeMatrix -n "leg_R_j03_worldMtx";
	rename -uid "66EEECA4-48FD-C6FC-0005-62ACB8B5F09A";
createNode animBlendNodeAdditiveRotation -n "leg_R_ankle_rotBlend";
	rename -uid "A3972A5A-4EBE-8F62-29BA-AA93850B3A87";
	setAttr ".o" -type "double3" -3.1805546814635183e-15 -3.1805546814635168e-15 6.3611093629270335e-15 ;
createNode decomposeMatrix -n "leg_R_fk03_worldMtx";
	rename -uid "FDBD2D5C-4F98-7E28-DA2F-959C7314EB2C";
	setAttr ".imat" -type "matrix" 1 1.1102230246251565e-16 5.5511151231257827e-17 0
		 -1.6653345369377348e-16 0.99999999999999956 -5.5511151231257827e-17 0 -8.3266726846886741e-17 0 1.0000000000000002 0
		 -3.2790000000000061 2.5447593967200017 -0.51870724801412305 1;
createNode multMatrix -n "leg_R_FK_start_mtx";
	rename -uid "F82AA626-4100-D2A1-D482-04883AF33621";
	setAttr -s 2 ".i";
createNode animBlendNodeAdditiveDA -n "animBlendNodeAdditiveDA2";
	rename -uid "B484D72F-43F9-F915-0A4E-05B208642555";
	setAttr ".o" 0.95862059441954717;
createNode animBlendNodeAdditiveDA -n "animBlendNodeAdditiveDA1";
	rename -uid "F22BF4EC-4E36-4170-2CA7-58A3727FDDDD";
	setAttr ".o" 17.066629620449635;
createNode floatCondition -n "leg_R_handedNessSign";
	rename -uid "55E8FF85-44F6-A090-A9E0-3DBD0FA86892";
	setAttr "._fa" -1;
createNode container -n "leg_R_container";
	rename -uid "FA802CF1-4EE7-E98A-2E73-8EB4CF08767E";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".isc" yes;
	setAttr -s 2 ".pni";
	setAttr ".ctor" -type "string" "Jaco";
	setAttr ".cdat" -type "string" "2018/02/16 08:27:10";
	setAttr ".aal" -type "attributeAlias" {"child","canBeChild[0]","parent","canBeParent[0]"
		,"leg_L_fk01_ctrl","publishedNodeInfo[0]","leg_L_fk02_ctrl","publishedNodeInfo[1]"
		} ;
createNode hyperLayout -n "hyperLayout5";
	rename -uid "379B5494-4D0D-5609-38FE-F0B879B11576";
	setAttr ".ihi" 0;
	setAttr -s 84 ".hyp";
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
	setAttr -s 133 ".u";
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
connectAttr "leg_R_ankle_blend_mtx.omat" "leg_R_output.chainEnd";
connectAttr "leg_R_hipWorld_srt.ot" "leg_R_IK_srtBuffer.t";
connectAttr "leg_R_IK_tension_rot.eux" "leg_R_IK_srtBuffer.rx";
connectAttr "leg_R_IK_tension_rot.euy" "leg_R_IK_srtBuffer.ry";
connectAttr "leg_R_IK_tension_rot.euz" "leg_R_IK_srtBuffer.rz";
connectAttr "leg_R_hipWorld_srt.os" "leg_R_IK_srtBuffer.s";
connectAttr "leg_R_IK_solver_xpr.out[1]" "leg_R_hip_srt.rx";
connectAttr "leg_R_IK_upVectoringAngle.euy" "leg_R_hip_srt.ry";
connectAttr "leg_R_configParameters.femurLength" "leg_R_femurEnd_srt.tz";
connectAttr "leg_R_IK_solver_xpr.out[0]" "leg_R_tibiaStart_srt.rx";
connectAttr "leg_R_configParameters.tibiaLength" "leg_R_tibiaEnd_srt.tz";
connectAttr "leg_R_handedNessSign.of" "leg_R_fk_handedness.sx";
connectAttr "leg_R_FK_start_srt.oty" "leg_R_fk01_ctrl_srtBuffer.ty";
connectAttr "leg_R_FK_start_srt.otz" "leg_R_fk01_ctrl_srtBuffer.tz";
connectAttr "animBlendNodeAdditiveDA2.o" "leg_R_fk01_ctrl_srtBuffer.ry";
connectAttr "animBlendNodeAdditiveDA1.o" "leg_R_fk01_ctrl_srtBuffer.rz";
connectAttr "leg_R_FK_start_srt.orx" "leg_R_fk01_ctrl_srtBuffer.rx";
connectAttr "leg_R_configParameters.femurLength" "leg_R_fk01_ctrlShape.cp[4].zv"
		;
connectAttr "leg_R_configParameters.femurLength" "leg_R_fk02_ctrl_srtBuffer.tz";
connectAttr "leg_R_tibiaStart_srt.rx" "leg_R_fk02_ctrl_srtBuffer.rx";
connectAttr "leg_R_configParameters.tibiaLength" "leg_R_fk02_ctrlShape.cp[4].zv"
		;
connectAttr "leg_R_guide_globalAnkleInfk02Space_srt.ot" "leg_R_fk03_ctrl_srtBuffer.t"
		;
connectAttr "leg_R_guide_globalAnkleInfk02Space_srt.or" "leg_R_fk03_ctrl_srtBuffer.r"
		;
connectAttr "leg_R_limitedWorldAnkle_translate.o3" "leg_R_limitedAnkle_srt.t";
connectAttr "leg_R_rolledAnkle_frame_srt.or" "leg_R_limitedAnkle_srt.r";
connectAttr "leg_R_guide_femurLength.d" "leg_R_configParameters.femurLength";
connectAttr "leg_R_guide_tibiaLength.d" "leg_R_configParameters.tibiaLength";
connectAttr "leg_R_guide_hipPos_ctrl.m" "leg_R_configParameters.hipOffsetIK";
connectAttr "leg_R_guide_ikHip_local_mtx.o" "leg_R_configParameters.hipOffsetFK"
		;
connectAttr "leg_R_fkik_j01_blended_rot.o" "leg_R_j01_srt.r";
connectAttr "leg_R_hipWorld_srt.ot" "leg_R_j01_srt.t";
connectAttr "leg_R_configParameters.femurLength" "leg_R_j02_srt.tz";
connectAttr "leg_R_fkik_j02_blended_rot.o" "leg_R_j02_srt.r";
connectAttr "leg_R_configParameters.tibiaLength" "leg_R_j03_srt.tz";
connectAttr "leg_R_configParameters.femurLength" "leg_R_toolParameters.toSwap[0].guided"
		;
connectAttr "leg_R_configParameters.tibiaLength" "leg_R_toolParameters.toSwap[1].guided"
		;
connectAttr "leg_R_fk01_ctrlShape.cp[4].zv" "leg_R_toolParameters.toSwap[2].guided"
		;
connectAttr "leg_R_fk02_ctrlShape.cp[4].zv" "leg_R_toolParameters.toSwap[3].guided"
		;
connectAttr "leg_R_fk02_ctrl_srtBuffer.rx" "leg_R_toolParameters.toSwap[4].guided"
		;
connectAttr "leg_R_fk03_ctrl_srtBuffer.t" "leg_R_toolParameters.toSwap[7].guided"
		;
connectAttr "leg_R_fk03_ctrl_srtBuffer.r" "leg_R_toolParameters.toSwap[8].guided"
		;
connectAttr "leg_R_configParameters.hipOffsetFK" "leg_R_toolParameters.toSwap[9].guided"
		;
connectAttr "leg_R_guide_hipInput_srt.msg" "leg_R_toolParameters.toDelete[0]";
connectAttr "leg_R_guide_hip_world_srt.msg" "leg_R_toolParameters.toDelete[1]";
connectAttr "leg_R_guide_hipPos_ctrl.msg" "leg_R_toolParameters.toDelete[2]";
connectAttr "leg_R_guide_ankle_world_srt.msg" "leg_R_toolParameters.toDelete[3]"
		;
connectAttr "leg_R_guide_femurLength.msg" "leg_R_toolParameters.toDelete[4]";
connectAttr "leg_R_guide_tibiaLength.msg" "leg_R_toolParameters.toDelete[5]";
connectAttr "leg_R_guide_knee_world_srt.msg" "leg_R_toolParameters.toDelete[6]";
connectAttr "leg_R_guide_hip2UpV_vec.msg" "leg_R_toolParameters.toDelete[7]";
connectAttr "leg_R_guide_globalAnkleInfk02Space_srt.msg" "leg_R_toolParameters.toDelete[8]"
		;
connectAttr "leg_R_guide_globalAnkleInfk02Space.msg" "leg_R_toolParameters.toDelete[9]"
		;
connectAttr "leg_R_guide_ikHip_local_mtx.msg" "leg_R_toolParameters.toDelete[11]"
		;
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" "leg_R_toolParameters.toDelete[12]"
		;
connectAttr "leg_R_guide_hipInput_srt.or" "leg_R_guide_hipPos_ctrl_srtBuffer.r";
connectAttr "leg_R_guide_hipInput_srt.os" "leg_R_guide_hipPos_ctrl_srtBuffer.s";
connectAttr "leg_R_guide_hipInput_srt.ot" "leg_R_guide_hipPos_ctrl_srtBuffer.t";
connectAttr "leg_R_guide_kneeUpV_aim_cns.cr" "leg_R_guide_kneePos_ctrl_srtBuffer.r"
		;
connectAttr "leg_R_guide_hipPos_ctrl.wim" "leg_R_guide_kneeUpV_aim_cns.cpim";
connectAttr "leg_R_input.rawAnkleControl" "leg_R_guide_kneeUpV_aim_cns.tg[0].tpm"
		;
connectAttr "leg_R_guide_hip2UpV_vec.o3" "leg_R_guide_kneeUpV_aim_cns.wu";
connectAttr "leg_R_IK_ankleDisplacement_vec.o3" "leg_R_IK_tension_rot.v2";
connectAttr "leg_R_IK_upVector_hipYProjected_srt.otz" "leg_R_IK_upVectoringAngle.v2z"
		;
connectAttr "leg_R_IK_upVector_hipYProjected_srt.otx" "leg_R_IK_upVectoringAngle.v2x"
		;
connectAttr "leg_R_animParameters.FKIK_blend" "leg_R_fkik_blend_complement.ib";
connectAttr "leg_R_fk02reframed01_rot.or" "leg_R_fkik_j02_blended_rot.ia";
connectAttr "leg_R_tibiaStart_srt.rx" "leg_R_fkik_j02_blended_rot.ibx";
connectAttr "leg_R_animParameters.FKIK_blend" "leg_R_fkik_j02_blended_rot.wb";
connectAttr "leg_R_fkik_blend_complement.o" "leg_R_fkik_j02_blended_rot.wa";
connectAttr "leg_R_fk01_ctrl_world_mtx.or" "leg_R_fkik_j01_blended_rot.ia";
connectAttr "leg_R_hip_rot.or" "leg_R_fkik_j01_blended_rot.ib";
connectAttr "leg_R_animParameters.FKIK_blend" "leg_R_fkik_j01_blended_rot.wb";
connectAttr "leg_R_fkik_blend_complement.o" "leg_R_fkik_j01_blended_rot.wa";
connectAttr "leg_R_fk02reframed01_mtx.o" "leg_R_fk02reframed01_rot.imat";
connectAttr "leg_R_hip_srt.wm" "leg_R_hip_rot.imat";
connectAttr "leg_R_hipWorld_mtx.o" "leg_R_hipWorld_srt.imat";
connectAttr "leg_R_IK_upVector_hipFramed_mtx.o" "leg_R_IK_upVector_hipYProjected_srt.imat"
		;
connectAttr "leg_R_limitedAnkle_srt.wm" "leg_R_limitedAnkleWorld_srt.imat";
connectAttr "leg_R_configParameters.femurLength" "leg_R_IK_solver_xpr.in[0]";
connectAttr "leg_R_configParameters.tibiaLength" "leg_R_IK_solver_xpr.in[1]";
connectAttr "leg_R_ankle2hip_clampedDistance.opr" "leg_R_IK_solver_xpr.in[2]";
connectAttr ":time1.o" "leg_R_IK_solver_xpr.tim";
connectAttr "leg_R_fk02_ctrl.wm" "leg_R_fk02reframed01_mtx.i[1]";
connectAttr "leg_R_input.upVectorFrame" "leg_R_IK_upVector_hipFramed_mtx.i[0]";
connectAttr "leg_R_IK_srtBuffer.wim" "leg_R_IK_upVector_hipFramed_mtx.i[1]";
connectAttr "leg_R_limitedAnkleWorld_srt.ot" "leg_R_IK_ankleDisplacement_vec.i3[0]"
		;
connectAttr "leg_R_hipWorld_srt.ot" "leg_R_IK_ankleDisplacement_vec.i3[1]";
connectAttr "leg_R_input.rolledAnkle" "leg_R_rolledAnkle_ctrl_world_mtx2srt.imat"
		;
connectAttr "leg_R_configParameters.tibiaLength" "leg_R_totalLength_fNode_add.i2"
		;
connectAttr "leg_R_configParameters.femurLength" "leg_R_totalLength_fNode_add.i1"
		;
connectAttr "leg_R_hip2Ankle_clamped_displacement.o" "leg_R_limitedWorldAnkle_translate.i3[0]"
		;
connectAttr "leg_R_hipWorld_srt.ot" "leg_R_limitedWorldAnkle_translate.i3[1]";
connectAttr "leg_R_totalLength_fNode_add.o" "leg_R_lengthLimit_fNode.i1";
connectAttr "leg_R_lengthLimit_fNode.o" "leg_R_ankle2hip_clampedDistance.mxr";
connectAttr "leg_R_hip2ankle_distance.d" "leg_R_ankle2hip_clampedDistance.ipr";
connectAttr "leg_R_hip2ankle_direction_normal.o" "leg_R_hip2Ankle_clamped_displacement.i1"
		;
connectAttr "leg_R_ankle2hip_clampedDistance.opr" "leg_R_hip2Ankle_clamped_displacement.i2x"
		;
connectAttr "leg_R_ankle2hip_clampedDistance.opr" "leg_R_hip2Ankle_clamped_displacement.i2y"
		;
connectAttr "leg_R_ankle2hip_clampedDistance.opr" "leg_R_hip2Ankle_clamped_displacement.i2z"
		;
connectAttr "leg_R_rolledAnkle_ctrl_world_mtx2srt.ot" "leg_R_hip2ankle_distance.p1"
		;
connectAttr "leg_R_hipWorld_srt.ot" "leg_R_hip2ankle_distance.p2";
connectAttr "leg_R_rolledAnkle_ctrl_world_mtx2srt.ot" "leg_R_hip2Ankle_displacement.i3[0]"
		;
connectAttr "leg_R_hipWorld_srt.ot" "leg_R_hip2Ankle_displacement.i3[1]";
connectAttr "leg_R_hip2Ankle_displacement.o3" "leg_R_hip2ankle_direction_normal.i1"
		;
connectAttr "leg_R_input.rolledAnkle" "leg_R_rolledAnkle_frame_srt.imat";
connectAttr "leg_R_configParameters.hipOffsetIK" "leg_R_hipWorld_mtx.i[1]";
connectAttr "leg_R_input.endWorld" "leg_R_hipWorld_mtx.i[2]";
connectAttr "leg_R_guide_knee_world_srt.ot" "leg_R_guide_femurLength.p2";
connectAttr "leg_R_guide_hip_world_srt.ot" "leg_R_guide_femurLength.p1";
connectAttr "leg_R_guide_knee_world_srt.ot" "leg_R_guide_tibiaLength.p2";
connectAttr "leg_R_guide_ankle_world_srt.ot" "leg_R_guide_tibiaLength.p1";
connectAttr "leg_R_FK_start_mtx.o" "leg_R_FK_start_srt.imat";
connectAttr "leg_R_input.upVectorFrame" "leg_R_guide_upVector_srt.imat";
connectAttr "leg_R_guide_kneePos_ctrl.wm" "leg_R_guide_knee_world_srt.imat";
connectAttr "leg_R_input.endWorld" "leg_R_guide_hipInput_srt.imat";
connectAttr "leg_R_guide_hipPos_ctrl.wm" "leg_R_guide_hip_world_srt.imat";
connectAttr "leg_R_input.rolledAnkle" "leg_R_guide_ankle_world_srt.imat";
connectAttr "leg_R_guide_upVector_srt.ot" "leg_R_guide_hip2UpV_vec.i3[0]";
connectAttr "leg_R_guide_hip_world_srt.ot" "leg_R_guide_hip2UpV_vec.i3[1]";
connectAttr "leg_R_guide_globalAnkleInfk02Space.o" "leg_R_guide_globalAnkleInfk02Space_srt.imat"
		;
connectAttr "leg_R_input.rolledAnkle" "leg_R_guide_globalAnkleInfk02Space.i[0]";
connectAttr "leg_R_fk02_ctrl.wim" "leg_R_guide_globalAnkleInfk02Space.i[1]";
connectAttr "leg_R_input.rawAnkleControl" "leg_R_globalAnkle_srt.imat";
connectAttr "leg_R_hip_srt.wm" "leg_R_guide_ikHip_local_mtx.i[0]";
connectAttr "leg_R_guide_endWorldInverse_mtx.omat" "leg_R_guide_ikHip_local_mtx.i[1]"
		;
connectAttr "leg_R_input.endWorld" "leg_R_guide_endWorldInverse_mtx.imat";
connectAttr "leg_R_ankle_rotBlend.o" "leg_R_ankle_blend_mtx.ir";
connectAttr "leg_R_j03_worldMtx.ot" "leg_R_ankle_blend_mtx.it";
connectAttr "leg_R_j03_srt.wm" "leg_R_j03_worldMtx.imat";
connectAttr "leg_R_fk03_worldMtx.or" "leg_R_ankle_rotBlend.ia";
connectAttr "leg_R_fkik_blend_complement.o" "leg_R_ankle_rotBlend.wa";
connectAttr "leg_R_animParameters.FKIK_blend" "leg_R_ankle_rotBlend.wb";
connectAttr "leg_R_globalAnkle_srt.or" "leg_R_ankle_rotBlend.ib";
connectAttr "leg_R_configParameters.hipOffsetFK" "leg_R_FK_start_mtx.i[0]";
connectAttr "leg_R_input.endWorld" "leg_R_FK_start_mtx.i[1]";
connectAttr "leg_R_FK_start_srt.ory" "animBlendNodeAdditiveDA2.ib";
connectAttr "leg_R_handedNessSign.of" "animBlendNodeAdditiveDA2.wb";
connectAttr "leg_R_FK_start_srt.orz" "animBlendNodeAdditiveDA1.ib";
connectAttr "leg_R_handedNessSign.of" "animBlendNodeAdditiveDA1.wb";
connectAttr "leg_R_configParameters.invertedHandedness" "leg_R_handedNessSign._cnd"
		;
connectAttr "hyperLayout5.msg" "leg_R_container.hl";
connectAttr "leg_R_cmpnt.msg" "leg_R_container.cbp[0]";
connectAttr "leg_R_cmpnt.msg" "leg_R_container.cbc[0]";
connectAttr "leg_R_fk01_ctrl.msg" "leg_R_container.pni[0].pnod";
connectAttr "leg_R_fk02_ctrl.msg" "leg_R_container.pni[1].pnod";
connectAttr "leg_R_cmpnt.msg" "hyperLayout5.hyp[0].dn";
connectAttr "leg_R_input.msg" "hyperLayout5.hyp[1].dn";
connectAttr "leg_R_output.msg" "hyperLayout5.hyp[2].dn";
connectAttr "|leg_R_cmpnt|control.msg" "hyperLayout5.hyp[3].dn";
connectAttr "leg_R_animParameters.msg" "hyperLayout5.hyp[4].dn";
connectAttr "leg_R_IK_srtBuffer.msg" "hyperLayout5.hyp[5].dn";
connectAttr "leg_R_hip_srt.msg" "hyperLayout5.hyp[6].dn";
connectAttr "leg_R_femurEnd_srt.msg" "hyperLayout5.hyp[7].dn";
connectAttr "leg_R_tibiaStart_srt.msg" "hyperLayout5.hyp[8].dn";
connectAttr "leg_R_tibiaEnd_srt.msg" "hyperLayout5.hyp[9].dn";
connectAttr "leg_R_FK_hrc.msg" "hyperLayout5.hyp[10].dn";
connectAttr "leg_R_fk01_ctrl_srtBuffer.msg" "hyperLayout5.hyp[11].dn";
connectAttr "leg_R_fk01_ctrl.msg" "hyperLayout5.hyp[12].dn";
connectAttr "leg_R_fk02_ctrl_srtBuffer.msg" "hyperLayout5.hyp[13].dn";
connectAttr "leg_R_fk02_ctrl.msg" "hyperLayout5.hyp[14].dn";
connectAttr "|leg_R_cmpnt|deform.msg" "hyperLayout5.hyp[15].dn";
connectAttr "leg_R_j01_srt.msg" "hyperLayout5.hyp[16].dn";
connectAttr "leg_R_j02_srt.msg" "hyperLayout5.hyp[17].dn";
connectAttr "leg_R_j03_srt.msg" "hyperLayout5.hyp[18].dn";
connectAttr "|leg_R_cmpnt|guide.msg" "hyperLayout5.hyp[19].dn";
connectAttr "leg_R_configParameters.msg" "hyperLayout5.hyp[20].dn";
connectAttr "leg_R_IK_tension_rot.msg" "hyperLayout5.hyp[21].dn";
connectAttr "leg_R_IK_upVectoringAngle.msg" "hyperLayout5.hyp[22].dn";
connectAttr "leg_R_fkik_blend_complement.msg" "hyperLayout5.hyp[23].dn";
connectAttr "leg_R_fkik_j02_blended_rot.msg" "hyperLayout5.hyp[24].dn";
connectAttr "leg_R_fkik_j01_blended_rot.msg" "hyperLayout5.hyp[25].dn";
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" "hyperLayout5.hyp[26].dn";
connectAttr "leg_R_fk02reframed01_rot.msg" "hyperLayout5.hyp[27].dn";
connectAttr "leg_R_hip_rot.msg" "hyperLayout5.hyp[29].dn";
connectAttr "leg_R_hipWorld_srt.msg" "hyperLayout5.hyp[30].dn";
connectAttr "leg_R_IK_upVector_hipYProjected_srt.msg" "hyperLayout5.hyp[31].dn";
connectAttr "leg_R_limitedAnkleWorld_srt.msg" "hyperLayout5.hyp[32].dn";
connectAttr "leg_R_IK_solver_xpr.msg" "hyperLayout5.hyp[34].dn";
connectAttr "leg_R_fk02reframed01_mtx.msg" "hyperLayout5.hyp[35].dn";
connectAttr "leg_R_IK_upVector_hipFramed_mtx.msg" "hyperLayout5.hyp[36].dn";
connectAttr "leg_R_IK_ankleDisplacement_vec.msg" "hyperLayout5.hyp[37].dn";
connectAttr "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|diagnosticCube_geoShape.msg" "hyperLayout5.hyp[38].dn"
		;
connectAttr "leg_R_fk01_ctrlShape.msg" "hyperLayout5.hyp[39].dn";
connectAttr "leg_R_fk02_ctrlShape.msg" "hyperLayout5.hyp[40].dn";
connectAttr "leg_R_toolParameters.msg" "hyperLayout5.hyp[41].dn";
connectAttr "leg_R_rolledAnkle_ctrl_world_mtx2srt.msg" "hyperLayout5.hyp[42].dn"
		;
connectAttr "leg_R_totalLength_fNode_add.msg" "hyperLayout5.hyp[43].dn";
connectAttr "leg_R_limitedWorldAnkle_translate.msg" "hyperLayout5.hyp[44].dn";
connectAttr "leg_R_lengthLimit_fNode.msg" "hyperLayout5.hyp[45].dn";
connectAttr "leg_R_ankle2hip_clampedDistance.msg" "hyperLayout5.hyp[46].dn";
connectAttr "leg_R_hip2Ankle_clamped_displacement.msg" "hyperLayout5.hyp[47].dn"
		;
connectAttr "leg_R_hip2ankle_distance.msg" "hyperLayout5.hyp[48].dn";
connectAttr "leg_R_hip2Ankle_displacement.msg" "hyperLayout5.hyp[50].dn";
connectAttr "leg_R_hip2ankle_direction_normal.msg" "hyperLayout5.hyp[51].dn";
connectAttr "leg_R_limitedAnkle_srt.msg" "hyperLayout5.hyp[52].dn";
connectAttr "leg_R_rolledAnkle_frame_srt.msg" "hyperLayout5.hyp[53].dn";
connectAttr "leg_R_hipWorld_mtx.msg" "hyperLayout5.hyp[55].dn";
connectAttr "leg_R_guide_femurLength.msg" "hyperLayout5.hyp[56].dn";
connectAttr "leg_R_guide_tibiaLength.msg" "hyperLayout5.hyp[57].dn";
connectAttr "leg_R_FK_start_srt.msg" "hyperLayout5.hyp[58].dn";
connectAttr "leg_R_guide_upVector_srt.msg" "hyperLayout5.hyp[59].dn";
connectAttr "leg_R_guide_knee_world_srt.msg" "hyperLayout5.hyp[60].dn";
connectAttr "leg_R_guide_hipInput_srt.msg" "hyperLayout5.hyp[61].dn";
connectAttr "leg_R_guide_hip_world_srt.msg" "hyperLayout5.hyp[62].dn";
connectAttr "leg_R_guide_ankle_world_srt.msg" "hyperLayout5.hyp[63].dn";
connectAttr "leg_R_guide_hipPos_ctrl_srtBuffer.msg" "hyperLayout5.hyp[64].dn";
connectAttr "leg_R_guide_hipPos_ctrl.msg" "hyperLayout5.hyp[65].dn";
connectAttr "leg_R_guide_hipPos_ctrlShape.msg" "hyperLayout5.hyp[66].dn";
connectAttr "leg_R_guide_kneePos_ctrl_srtBuffer.msg" "hyperLayout5.hyp[67].dn";
connectAttr "leg_R_guide_kneePos_ctrl.msg" "hyperLayout5.hyp[68].dn";
connectAttr "leg_R_guide_kneePos_ctrlShape.msg" "hyperLayout5.hyp[69].dn";
connectAttr "leg_R_guide_kneeUpV_aim_cns.msg" "hyperLayout5.hyp[70].dn";
connectAttr "leg_R_guide_hip2UpV_vec.msg" "hyperLayout5.hyp[71].dn";
connectAttr "leg_R_guide_globalAnkleInfk02Space_srt.msg" "hyperLayout5.hyp[72].dn"
		;
connectAttr "leg_R_guide_globalAnkleInfk02Space.msg" "hyperLayout5.hyp[73].dn";
connectAttr "leg_R_fk03_ctrl_srtBuffer.msg" "hyperLayout5.hyp[74].dn";
connectAttr "leg_R_fk03_ctrl.msg" "hyperLayout5.hyp[75].dn";
connectAttr "leg_R_fk03_ctrlShape.msg" "hyperLayout5.hyp[76].dn";
connectAttr "leg_R_globalAnkle_srt.msg" "hyperLayout5.hyp[77].dn";
connectAttr "leg_R_guide_ikHip_local_mtx.msg" "hyperLayout5.hyp[78].dn";
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" "hyperLayout5.hyp[79].dn";
connectAttr "leg_R_ankle_blend_mtx.msg" "hyperLayout5.hyp[80].dn";
connectAttr "leg_R_j03_worldMtx.msg" "hyperLayout5.hyp[81].dn";
connectAttr "leg_R_ankle_rotBlend.msg" "hyperLayout5.hyp[82].dn";
connectAttr "leg_R_fk03_worldMtx.msg" "hyperLayout5.hyp[83].dn";
connectAttr "leg_R_FK_start_mtx.msg" "hyperLayout5.hyp[84].dn";
connectAttr "animBlendNodeAdditiveDA2.msg" "hyperLayout5.hyp[85].dn";
connectAttr "animBlendNodeAdditiveDA1.msg" "hyperLayout5.hyp[86].dn";
connectAttr "leg_R_handedNessSign.msg" "hyperLayout5.hyp[87].dn";
connectAttr "leg_R_hip2Ankle_displacement.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_R_limitedWorldAnkle_translate.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_totalLength_fNode_add.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_R_hip2ankle_direction_normal.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_hip2Ankle_clamped_displacement.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_ankle2hip_clampedDistance.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_hip2ankle_distance.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_rolledAnkle_ctrl_world_mtx2srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_hipWorld_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_IK_tension_rot.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_IK_ankleDisplacement_vec.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "leg_R_IK_upVector_hipFramed_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_IK_upVector_hipYProjected_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_IK_upVectoringAngle.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_lengthLimit_fNode.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_hipWorld_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_limitedAnkleWorld_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_R_hip_rot.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_fk02reframed01_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_fk02reframed01_rot.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_FK_start_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_rolledAnkle_frame_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_R_guide_hipInput_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_guide_femurLength.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_guide_ankle_world_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_R_guide_knee_world_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_guide_tibiaLength.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_guide_hip_world_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_guide_upVector_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_guide_hip2UpV_vec.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_guide_globalAnkleInfk02Space.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_guide_globalAnkleInfk02Space_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_guide_ikHip_local_mtx.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_R_FK_start_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_fk03_worldMtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_j03_worldMtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_ankle_blend_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_globalAnkle_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_handedNessSign.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|leg_R_femurEnd_srt|leg_R_tibiaStart_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|leg_R_femurEnd_srt|leg_R_tibiaStart_srt|leg_R_tibiaEnd_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
// End of leg_v004.ma
