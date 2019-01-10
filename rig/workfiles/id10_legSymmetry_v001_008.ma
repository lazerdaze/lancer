//Maya ASCII 2018ff07 scene
//Name: id10_legSymmetry_v001_008.ma
//Last modified: Sat, May 12, 2018 10:20:19 PM
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
createNode transform -s -n "persp";
	rename -uid "5E1B0526-4CE8-950E-7536-339BF0539040";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -55.788659273392682 31.58692065741177 41.542017907130045 ;
	setAttr ".r" -type "double3" -21.33835285749565 -773.39999999994973 0 ;
	setAttr ".rp" -type "double3" 1.1990408665951691e-14 -3.5527136788005009e-15 0 ;
	setAttr ".rpt" -type "double3" -1.626461965996476e-14 -4.0459907989498604e-15 -2.860328035193607e-14 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "4F383ED2-4EE7-0DD9-D579-0C8F43AD384E";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 71.346402246376556;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -1.9315832609027803 6.9380022659105736 1.5157087146627681 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
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
createNode transform -s -n "front";
	rename -uid "5A7F0D20-41AC-014F-A83E-16AD1AF0A817";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.1235253881359206 6.8806552364090967 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "E0D006D9-40BA-945E-E790-42B92B3CA785";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 8.980614471741438;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "9BE6A7B5-4B9A-28AE-FAB2-0C9DFEC851B7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 7.1935677669416842 -1.7936038521310333 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "A5360673-408D-5FDA-6005-DA8D8444B180";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 24.174883914042663;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "leg_L_cmpnt";
	rename -uid "EF70FC04-42AC-7247-A669-D8811F53F740";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
createNode transform -n "leg_L_input" -p "leg_L_cmpnt";
	rename -uid "DCF5B81F-44C2-6A8F-8E51-A981F1615A24";
	addAttr -ci true -sn "endWorld" -ln "endWorld" -at "matrix";
	addAttr -ci true -sn "rolledAnkle" -ln "rolledAnkle" -nn "rolledAnkle" -at "matrix";
	addAttr -ci true -sn "upVectorFrame" -ln "upVectorFrame" -at "matrix";
	addAttr -ci true -sn "rawAnkleControl" -ln "rawAnkleControl" -at "matrix";
createNode transform -n "leg_L_output" -p "leg_L_cmpnt";
	rename -uid "94B311FA-43FC-6926-BCFD-A8B02F936E7D";
	addAttr -ci true -sn "chainEnd" -ln "chainEnd" -at "matrix";
createNode transform -n "control" -p "leg_L_cmpnt";
	rename -uid "E232BFAC-4537-7AB4-ECB2-16A18E64DBD3";
createNode transform -n "leg_L_IK_srtBuffer" -p "|leg_L_cmpnt|control";
	rename -uid "925DBA39-4196-51E6-DDE9-259F899240E8";
createNode transform -n "leg_L_hip_srt" -p "leg_L_IK_srtBuffer";
	rename -uid "0E8FEB9E-48F0-CC5A-D4CC-7796530B065E";
createNode mesh -n "diagnosticCube_geoShape" -p "leg_L_hip_srt";
	rename -uid "96B5A13E-4492-A47B-F3F9-4A9A716C7B25";
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
	setAttr -s 10 ".pt[0:9]" -type "float3"  0.31209025 0.31198502 -0.16323061 
		-0.31187969 0.31198502 -0.16323061 0.31209025 -0.31198472 -0.16323061 -0.31187969 
		-0.31198472 -0.16323061 0.31209025 -0.31198472 0.46073928 -0.31187969 -0.31198472 
		0.46073928 0.31209025 0.31198502 0.46073928 -0.31187969 0.31198502 0.46073928 0.00010524935 
		2.3499554e-08 0.016059995 -0.13258834 2.3499554e-08 0.1487543;
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
createNode transform -n "leg_L_femurEnd_srt" -p "leg_L_hip_srt";
	rename -uid "E97D311D-4E94-28E0-F58C-1182452C9B84";
createNode transform -n "leg_L_tibiaStart_srt" -p "leg_L_femurEnd_srt";
	rename -uid "85821FC2-4039-C386-362F-E5A18FD64187";
createNode transform -n "leg_L_tibiaEnd_srt" -p "leg_L_tibiaStart_srt";
	rename -uid "93270C2D-4672-75B5-51C9-FA8A97E1522A";
createNode transform -n "leg_L_animParameters" -p "|leg_L_cmpnt|control";
	rename -uid "51EABCBA-4749-A031-84D7-40BF4A5B3788";
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
	setAttr -k on ".FKIK_blend" 1;
createNode transform -n "leg_L_FK_hrc" -p "|leg_L_cmpnt|control";
	rename -uid "64D0E406-4A6D-188B-F41C-30B07F51364D";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "leg_L_fk01_ctrl_srtBuffer" -p "leg_L_FK_hrc";
	rename -uid "5292B358-470F-1628-499F-F7A1FA4D32A1";
createNode transform -n "leg_L_fk01_ctrl" -p "leg_L_fk01_ctrl_srtBuffer";
	rename -uid "5D55EC18-4622-ACCE-8913-D4B5302B5287";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.96589994 ;
createNode nurbsCurve -n "leg_L_fk01_ctrlShape" -p "leg_L_fk01_ctrl";
	rename -uid "2EE59C62-44D4-A5B3-6262-8E9216E18965";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0 0
		0 1 0
		1 0 0
		0 0 0
		0 0 3.7889897830403561
		;
createNode transform -n "leg_L_fk02_ctrl_srtBuffer" -p "leg_L_fk01_ctrl";
	rename -uid "74DA8440-423B-3FBF-8884-13ABB5AFE275";
createNode transform -n "leg_L_fk02_ctrl" -p "leg_L_fk02_ctrl_srtBuffer";
	rename -uid "38E1AD64-45F2-391B-5159-50B4B02C1E19";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.96589994 ;
createNode nurbsCurve -n "leg_L_fk02_ctrlShape" -p "leg_L_fk02_ctrl";
	rename -uid "8E106F5B-4EC0-D119-C5B1-1A8C940B061B";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 0 0
		0 1 0
		1 0 0
		0 0 0
		0 0 3.7991526061261869
		;
createNode transform -n "leg_L_fk03_ctrl_srtBuffer" -p "leg_L_fk02_ctrl";
	rename -uid "71CDC795-4D22-9AD9-47DD-C9B54A94931E";
	setAttr ".s" -type "double3" 0.99999999999999967 0.99999999999999956 0.99999999999999978 ;
createNode transform -n "leg_L_fk03_ctrl" -p "leg_L_fk03_ctrl_srtBuffer";
	rename -uid "5EB9D51D-4A4B-3594-E70B-2B9A759F454F";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.96589994 ;
createNode nurbsCurve -n "leg_L_fk03_ctrlShape" -p "leg_L_fk03_ctrl";
	rename -uid "DFC17D9B-471B-5F3F-A0E9-BE9232B2EE66";
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
createNode transform -n "leg_L_limitedAnkle_srt" -p "|leg_L_cmpnt|control";
	rename -uid "64FD68AC-4684-0D67-93B8-22AA58DDC9B1";
createNode transform -n "leg_L_configParameters" -p "|leg_L_cmpnt|control";
	rename -uid "E62BED8E-43F2-71EA-1E95-9CA900A8FB4F";
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
	setAttr -k on ".invertedHandedness";
createNode transform -n "deform" -p "leg_L_cmpnt";
	rename -uid "BE886250-4E99-706C-8107-F692667EA87F";
createNode joint -n "leg_L_j01_srt" -p "|leg_L_cmpnt|deform";
	rename -uid "98970791-455C-BE5A-1357-2E9FD271ADA3";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.7068965517241379;
createNode joint -n "leg_L_j02_srt" -p "leg_L_j01_srt";
	rename -uid "67F90693-4BB6-3D28-9E20-59BA4BEB32BA";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.7068965517241379;
createNode joint -n "leg_L_j03_srt" -p "leg_L_j02_srt";
	rename -uid "E75362BD-446D-D3B9-E287-58A4ACE9C8BC";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.7068965517241379;
createNode transform -n "guide" -p "leg_L_cmpnt";
	rename -uid "C30102FB-43C1-7A2F-DA1B-089C14F4A396";
createNode transform -n "leg_L_toolParameters" -p "|leg_L_cmpnt|guide";
	rename -uid "50C7B28C-4F4C-D89E-5C0E-62B4BB922252";
	addAttr -ci true -m -sn "toSwap" -ln "toSwap" -at "compound" -nc 2;
	addAttr -s false -ci true -sn "origin" -ln "origin" -at "message" -p "toSwap";
	addAttr -s false -ci true -sn "guided" -ln "guided" -at "message" -p "toSwap";
	addAttr -s false -ci true -m -sn "toDelete" -ln "toDelete" -at "message";
	setAttr -s 8 ".toSwap";
	setAttr -s 12 ".toDelete";
createNode transform -n "leg_L_guide_hipPos_ctrl_srtBuffer" -p "|leg_L_cmpnt|guide";
	rename -uid "5B975D03-455F-EC02-E557-5594D0D54960";
createNode transform -n "leg_L_guide_hipPos_ctrl" -p "leg_L_guide_hipPos_ctrl_srtBuffer";
	rename -uid "48571531-46D1-5A06-9F0A-87811ED3BC73";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 2.1101686522353278 -3.5436528339302011 0.11647361510475107 ;
createNode nurbsCurve -n "leg_L_guide_hipPos_ctrlShape" -p "leg_L_guide_hipPos_ctrl";
	rename -uid "75441603-4624-4633-AC95-B198A506FD45";
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
createNode transform -n "leg_L_guide_kneePos_ctrl_srtBuffer" -p "leg_L_guide_hipPos_ctrl";
	rename -uid "5E8BAAA8-42FC-7775-B941-FDB6E2B06DA2";
createNode transform -n "leg_L_guide_kneePos_ctrl" -p "leg_L_guide_kneePos_ctrl_srtBuffer";
	rename -uid "D9FC3244-47EA-FA80-3F75-F2A118013441";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 0 -2.3856530387133721 2.9436547275218712 ;
	setAttr -l on ".tx";
createNode nurbsCurve -n "leg_L_guide_kneePos_ctrlShape" -p "leg_L_guide_kneePos_ctrl";
	rename -uid "E16C0C0D-431F-5F1B-1D36-C6852CBD892D";
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
createNode aimConstraint -n "leg_L_guide_kneeUpV_aim_cns" -p "leg_L_guide_kneePos_ctrl_srtBuffer";
	rename -uid "0FCD3C8C-414B-706E-2E56-B198A64BBE4F";
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
createNode transform -n "legGlobal_L_cmpnt";
	rename -uid "0E378926-444A-68FF-58B9-3F987790DD6A";
	setAttr ".ove" yes;
	setAttr ".ovc" 19;
	setAttr ".ovrgb" -type "float3" 0.059300009 0.5043 0.17050005 ;
createNode transform -n "legGlobal_L_input" -p "legGlobal_L_cmpnt";
	rename -uid "6195041D-49BC-6253-98B1-4BA978F47BFB";
	addAttr -ci true -sn "endWorld" -ln "endWorld" -at "matrix";
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
createNode transform -n "legGlobal_L_ankle_rest_srt" -p "|legGlobal_L_cmpnt|control|roll_mechanics";
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
createNode transform -n "legGlobal_L_roll_world_srt" -p "|legGlobal_L_cmpnt|control|roll_mechanics";
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
	setAttr ".t" -type "double3" 0 0 0 ;
	setAttr -av ".tx";
	setAttr -av ".ty";
	setAttr -av ".tz";
	setAttr ".r" -type "double3" 0 0 0 ;
	setAttr -av ".rx";
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
createNode transform -n "foot_L_cpmnt";
	rename -uid "E3F865EB-498D-5A0D-2C5F-18A87C4D0E0F";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.1814 0.29659995 0.5783 ;
	setAttr ".it" no;
createNode transform -n "foot_L_input" -p "foot_L_cpmnt";
	rename -uid "6C1132A6-46EC-E323-85FC-6EB64FCDBD07";
	addAttr -ci true -sn "tarsiLength" -ln "tarsiLength" -dv 4 -min 0 -max 50 -at "double";
	addAttr -ci true -sn "startMtx" -ln "startMtx" -at "matrix";
	addAttr -ci true -sn "toeAngle" -ln "toeAngle" -at "doubleAngle";
	addAttr -ci true -sn "tarsiAngle" -ln "tarsiAngle" -at "doubleAngle";
	addAttr -ci true -sn "toeLength" -ln "toeLength" -dv 3 -min 0.01 -max 10 -at "double";
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
	setAttr -k on ".toeLength";
createNode transform -n "foot_L_output" -p "foot_L_cpmnt";
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
createNode transform -n "control" -p "foot_L_cpmnt";
	rename -uid "66B07850-4C23-F05C-B849-C6B5847E9E2E";
	setAttr ".it" no;
createNode transform -n "foot_L_ankleSpace_srt" -p "|foot_L_cpmnt|control";
	rename -uid "F8CC1B11-42DE-835E-F514-6C98ABF1E0CA";
createNode transform -n "foot_L_tarsii_ctrl_srtBuffer" -p "foot_L_ankleSpace_srt";
	rename -uid "50F94EB5-42AA-6C61-1668-F393638190F8";
createNode transform -n "foot_L_tarsii_ctrl" -p "foot_L_tarsii_ctrl_srtBuffer";
	rename -uid "D888E2B2-4784-9C27-6ACA-C1986E0E6970";
createNode nurbsCurve -n "foot_L_tarsii_ctrlShape" -p "foot_L_tarsii_ctrl";
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
createNode joint -n "diagnostic_ankle" -p "foot_L_tarsii_ctrl";
	rename -uid "CBF7DBB2-4849-8D79-31E5-DAAC89E6E917";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode joint -n "diagnostic_tarsi" -p "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|diagnostic_ankle";
	rename -uid "4C3DFC2F-4EAE-86B6-D413-069D72C93699";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode transform -n "foot_L_toes_ctrl_srtBuffer" -p "foot_L_tarsii_ctrl";
	rename -uid "E306CA04-4965-9C72-B977-67A77A3C61B8";
createNode transform -n "foot_L_toes_ctrl" -p "foot_L_toes_ctrl_srtBuffer";
	rename -uid "DA5338BF-4B9F-0380-A369-23A3456591AA";
createNode nurbsCurve -n "foot_L_toes_ctrlShape" -p "foot_L_toes_ctrl";
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
createNode joint -n "diagnostic_toes" -p "foot_L_toes_ctrl";
	rename -uid "E52B0F22-447C-E71B-8E15-6DB88DBCC0CB";
	setAttr ".t" -type "double3" 0 0 4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode joint -n "diagnostic_tip" -p "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|foot_L_toes_ctrl_srtBuffer|foot_L_toes_ctrl|diagnostic_toes";
	rename -uid "2FDE15DE-4DEE-E2F3-B505-71B862062BD6";
	setAttr ".t" -type "double3" 2.384185791015625e-07 -8.5989402265340686e-09 2.4857768956930508 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode transform -n "guide" -p "foot_L_cpmnt";
	rename -uid "4B3DDE1D-47FF-4987-F21A-2B81C3D4F3F3";
createNode transform -n "godNode_M_cmpnt";
	rename -uid "AFE7A71D-42D4-A877-7569-BA93BBC83A51";
createNode transform -n "godNode_M_output" -p "godNode_M_cmpnt";
	rename -uid "12D12E26-45BB-8AE7-2D7E-6EA22DE507BA";
createNode transform -n "output_master_srt" -p "godNode_M_output";
	rename -uid "F4EB587D-46F7-40DC-6496-1F83C22926A8";
createNode transform -n "output_com_srt" -p "output_master_srt";
	rename -uid "B245381C-497E-66A7-B535-99A4C3D0F82D";
createNode transform -n "output_end_srt" -p "output_com_srt";
	rename -uid "0E5A177D-4973-CB3A-38A8-939117B648C1";
createNode transform -n "control" -p "godNode_M_cmpnt";
	rename -uid "6D9E4A95-44F5-3FD7-A452-0E90387D09EC";
createNode transform -n "godNode_M_master_ctrl_srtBuffer" -p "|godNode_M_cmpnt|control";
	rename -uid "8D4AC092-4CB9-6F75-9A7D-CB9202E11643";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0 0 ;
createNode transform -n "godNode_M_master_ctrl" -p "godNode_M_master_ctrl_srtBuffer";
	rename -uid "60559F65-44FA-93E3-0C43-72BA713F5168";
	setAttr ".rp" -type "double3" 5.5511151231257827e-15 4.1078251911130792e-15 -8.8817841970012523e-16 ;
	setAttr ".rpt" -type "double3" -5.5511151231257827e-15 -4.1078251911130792e-15 8.8817841970012523e-16 ;
	setAttr ".sp" -type "double3" 5.5511151231257827e-15 4.1078251911130792e-15 -8.8817841970012523e-16 ;
createNode nurbsCurve -n "godNode_M_master_ctrlShape" -p "godNode_M_master_ctrl";
	rename -uid "71FAD962-44E2-55A9-6340-E2A890CD6369";
	setAttr -k off ".v";
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.10010004 ;
	setAttr ".cc" -type "nurbsCurve" 
		1 48 2 no 3
		49 0 0.125 0.25 0.375 0.5 0.625 0.75 0.875 0.94378600000000001 0.96638900000000005
		 0.97895100000000002 1 1.0210490000000001 1.0336110000000001 1.056214 1.125 1.25 1.375
		 1.5 1.625 1.75 1.875 1.8960399999999999 1.919448 1.957708 2.0422920000000002 2.080552
		 2.100813 2.125 2.25 2.375 2.5 2.625 2.75 2.9437859999999998 2.9561022079999999 2.9789509999999999
		 3 3.0210490000000001 3.0436231170000001 3.0562140000000002 3.25 3.375 3.5 3.625 3.75
		 3.875 4 4.125
		49
		-7.3700607400608211 -1.4325234110046381e-08 1.4931252748754476
		-7.0577185932091879 -1.4325234332090986e-08 2.4209409247871401
		-6.5169375920182624 -1.4325234332090986e-08 3.4588354571938744
		-5.9352489841292186 -1.4325234332090986e-08 4.4366188028662199
		-5.1826985228498375 -1.4325234554135591e-08 5.3038359226232341
		-4.3154814030928224 -1.4325234554135591e-08 6.0563863839026135
		-3.3376980574204831 -1.4325234776180196e-08 6.6380749917916733
		-2.2998035250137399 -1.4325234776180196e-08 7.1788559929825952
		-1.371987875102054 -1.4325234776180196e-08 7.4911981398342471
		-1.371987875102054 -1.4325234776180196e-08 8.2409572479540998
		-2.1217469832218994 -1.4325234776180196e-08 8.2409572479540998
		0.12753034113764192 -1.4325234998224801e-08 10.490234572313639
		2.3768076654971897 -1.4325234776180196e-08 8.2409572479540998
		1.6270485573773383 -1.4325234776180196e-08 8.2409572479540998
		1.6270485573773383 -1.4325234776180196e-08 7.4911981398342471
		2.5548642072890315 -1.4325234776180196e-08 7.1788559929825952
		3.5927587396957645 -1.4325234776180196e-08 6.6380749917916733
		4.5705420853681025 -1.4325234554135591e-08 6.0563863839026135
		5.437759205125106 -1.4325234554135591e-08 5.3038359226232341
		6.1903096664044881 -1.4325234332090986e-08 4.4366188028662199
		6.7719982742935443 -1.4325234332090986e-08 3.4588354571938744
		7.3127792754844894 -1.4325234332090986e-08 2.4209409247871401
		7.6251214223361261 -1.4325234110046381e-08 1.4931252748754476
		7.939557646376751 -1.4325234110046381e-08 -0.0063929413642423438
		6.1256032060964234 1.1042596245013216 -0.0063929413642420463
		6.1256032060964234 -1.104259653151789 -0.0063929413642424939
		7.939557646376751 -1.4325234110046381e-08 -0.0063929413642423438
		7.6251214223361261 -1.4325233888001776e-08 -1.5059111576039381
		7.3127792754844894 -1.4325233888001776e-08 -2.4337268075156309
		6.7719982742935443 -1.4325233665957171e-08 -3.4716213399223657
		6.1903096664044881 -1.4325233665957171e-08 -4.4494046855947023
		5.437759205125106 -1.4325233443912566e-08 -5.3166218053517138
		4.5705420853681025 -1.4325233443912566e-08 -6.0691722666310897
		3.5927587396957645 -1.4325233443912566e-08 -6.7542249144428483
		0.12753034113764192 -1.4325233443912566e-08 -6.7542249144428483
		0.12753034113764192 0.55212980508804299 -6.754224914442851
		0.12753034113764192 0.55212980508804421 -7.5039840225627108
		0.12753034113764192 2.2085192633278754 -6.7542249144428483
		0.12753034113764192 0.55212980508804377 -6.0044658063230205
		0.12753034113764192 0.55212980508804299 -6.754224914442851
		0.12753034113764192 -1.4325233443912566e-08 -6.7542249144428483
		-3.3376980574204831 -1.4325233443912566e-08 -6.7542249144428483
		-4.3154814030928224 -1.4325233443912566e-08 -6.0691722666310897
		-5.1826985228498375 -1.4325233443912566e-08 -5.3166218053517138
		-5.9352489841292186 -1.4325233665957171e-08 -4.4494046855947023
		-6.5169375920182624 -1.4325233665957171e-08 -3.4716213399223657
		-7.0577185932091879 -1.4325233888001776e-08 -2.4337268075156309
		-7.3700607400608211 -1.4325233888001776e-08 -1.5059111576039381
		-7.3700607400608211 -1.4325234110046381e-08 1.4931252748754476
		;
createNode transform -n "godNode_M_masterOffset_ctrl" -p "godNode_M_master_ctrl";
	rename -uid "9A8A1293-458C-8DD7-CE64-BE96CD0FF2C6";
createNode nurbsCurve -n "godNode_M_masterOffset_ctrlShape" -p "godNode_M_masterOffset_ctrl";
	rename -uid "C3A05D69-4C2D-5F0A-706B-BA968C2BDAD2";
	setAttr -k off ".v";
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.030600017 0.3123 0.058800008 ;
	setAttr ".cc" -type "nurbsCurve" 
		1 42 2 no 3
		43 0 0.125 0.25 0.375 0.5 0.625 0.75 0.875 0.94378600000000001 1 1.056214 1.125
		 1.25 1.375 1.5 1.625 1.75 1.875 1.8960399999999999 1.919448 1.957708 2.0422920000000002
		 2.080552 2.100813 2.125 2.25 2.375 2.5 2.625 2.75 2.9437859999999998 2.9789509999999999
		 3 3.0210490000000001 3.0562140000000002 3.25 3.375 3.5 3.625 3.75 3.875 4 4.125
		43
		-6.7557900038205121 -0.00052725306467737987 1.3256850154312154
		-6.4688655622006133 -0.00052725306467760191 2.1779971031865313
		-5.9720921092120731 -0.00052725306467760191 3.1314301002152041
		-5.4377400190521463 -0.00052725306467760191 4.0296436244230502
		-4.7464304309294381 -0.00052725306467760191 4.8262885548546475
		-3.9497855004978351 -0.00052725306467782396 5.5175981429773628
		-3.0515719762899951 -0.00052725306467782396 6.0519502331372887
		-2.0981389792613143 -0.00052725306467782396 6.5487236861258538
		-1.2458268915060029 -0.00052725306467782396 6.8356481277457259
		0.13166388657262301 -0.00052725306467715782 5.4581573496670961
		1.5091546646512528 -0.00052725306467782396 6.8356481277457259
		2.3614667524065633 -0.00052725306467782396 6.5487236861258538
		3.3148997494352361 -0.00052725306467782396 6.0519502331372887
		4.2131132736430734 -0.00052725306467782396 5.5175981429773628
		5.0097582040746786 -0.00052725306467760191 4.8262885548546475
		5.7010677921973878 -0.00052725306467760191 4.0296436244230502
		6.2354198823573066 -0.00052725306467760191 3.1314301002152041
		6.7321933353458681 -0.00052725306467760191 2.1779971031865313
		7.0191177769657518 -0.00052725306467737987 1.3256850154312154
		7.3079658844572206 -0.00052725306467715782 -0.051805762647408563
		6.4943499222719403 0.49476814557975712 -0.051805762647408445
		6.4943499222719403 -0.49582265170911088 -0.051805762647408563
		7.3079658844572206 -0.00052725306467715782 -0.051805762647408563
		7.0191177769657518 -0.00052725306467715782 -1.4292965407260336
		6.7321933353458681 -0.00052725306467715782 -2.2816086284813464
		6.2354198823573066 -0.00052725306467693578 -3.2350416255100174
		5.7010677921973878 -0.00052725306467693578 -4.1332551497178631
		5.0097582040746786 -0.00052725306467671373 -4.9299000801494621
		4.2131132736430734 -0.00052725306467671373 -5.6212096682721659
		3.3148997494352361 -0.00052725306467671373 -6.250514264001219
		0.13166388657262301 -0.00052725306467671373 -6.250514264001219
		0.13166388657262301 -0.000527253064678046 -5.561768874961909
		0.13166388657262301 -0.50772598283484993 -6.2505142640012172
		0.13166388657262301 -0.00052725306467893418 -6.9392596530405237
		0.13166388657262301 -0.00052725306467671373 -6.250514264001219
		-3.0515719762899951 -0.00052725306467671373 -6.250514264001219
		-3.9497855004978351 -0.00052725306467671373 -5.6212096682721659
		-4.7464304309294381 -0.00052725306467671373 -4.9299000801494621
		-5.4377400190521463 -0.00052725306467693578 -4.1332551497178631
		-5.9720921092120731 -0.00052725306467693578 -3.2350416255100174
		-6.4688655622006133 -0.00052725306467715782 -2.2816086284813464
		-6.7557900038205121 -0.00052725306467715782 -1.4292965407260336
		-6.7557900038205121 -0.00052725306467737987 1.3256850154312154
		;
createNode transform -n "godNode_M_com_ctrl_srtBuffer" -p "godNode_M_masterOffset_ctrl";
	rename -uid "327E9413-43CA-345F-D268-BF88B1D63201";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.018899918 ;
createNode transform -n "godNode_M_com_ctrl" -p "godNode_M_com_ctrl_srtBuffer";
	rename -uid "AFFF6791-4D19-5BA4-23CF-94AA6D9952EB";
	setAttr ".rp" -type "double3" 5.5511151231257827e-15 4.1078251911130792e-15 -8.8817841970012523e-16 ;
	setAttr ".rpt" -type "double3" -5.5511151231257827e-15 -4.1078251911130792e-15 8.8817841970012523e-16 ;
	setAttr ".sp" -type "double3" 5.5511151231257827e-15 4.1078251911130792e-15 -8.8817841970012523e-16 ;
createNode nurbsCurve -n "godNode_M_com_ctrlShape" -p "godNode_M_com_ctrl";
	rename -uid "E357B596-4A1C-7B1F-9ABB-EA8AAB8D5E90";
	setAttr -k off ".v";
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.10010004 ;
	setAttr ".cc" -type "nurbsCurve" 
		1 48 2 no 3
		49 0 0.125 0.25 0.375 0.5 0.625 0.75 0.875 0.94378600000000001 0.96638900000000005
		 0.97895100000000002 1 1.0210490000000001 1.0336110000000001 1.056214 1.125 1.25 1.375
		 1.5 1.625 1.75 1.875 1.8960399999999999 1.919448 1.957708 2.0422920000000002 2.080552
		 2.100813 2.125 2.25 2.375 2.5 2.625 2.75 2.9437859999999998 2.9561022079999999 2.9789509999999999
		 3 3.0210490000000001 3.0436231170000001 3.0562140000000002 3.25 3.375 3.5 3.625 3.75
		 3.875 4 4.125
		49
		-5.4273836241602691 -1.4325234110046381e-08 1.0995518153099955
		-5.1973718626908969 -1.4325234332090986e-08 1.7828041848866372
		-4.799135531453226 -1.4325234332090986e-08 2.5471197024197121
		-4.3707744451385491 -1.4325234332090986e-08 3.2671687638111546
		-3.8165890464075929 -1.4325234554135591e-08 3.9057957928635396
		-3.1779620173552114 -1.4325234554135591e-08 4.4599811915944922
		-2.4579129559637733 -1.4325234776180196e-08 4.8883422779091799
		-1.6935974384306927 -1.4325234776180196e-08 5.2865786091468472
		-1.0103450688540541 -1.4325234776180196e-08 5.5165903706162318
		-1.0103450688540541 -1.4325234776180196e-08 6.0687201900295076
		-1.5624748882673298 -1.4325234776180196e-08 6.0687201900295076
		0.093914569972500236 -1.4325234998224801e-08 7.7251096482693438
		1.7503040282123337 -1.4325234776180196e-08 6.0687201900295076
		1.1981742087990548 -1.4325234776180196e-08 6.0687201900295076
		1.1981742087990548 -1.4325234776180196e-08 5.5165903706162318
		1.8814265783756969 -1.4325234776180196e-08 5.2865786091468472
		2.645742095908771 -1.4325234776180196e-08 4.8883422779091799
		3.3657911573002082 -1.4325234554135591e-08 4.4599811915944922
		4.0044181863525878 -1.4325234554135591e-08 3.9057957928635396
		4.5586035850835422 -1.4325234332090986e-08 3.2671687638111546
		4.9869646713982227 -1.4325234332090986e-08 2.5471197024197121
		5.3852010026359007 -1.4325234332090986e-08 1.7828041848866372
		5.6152127641052747 -1.4325234110046381e-08 1.0995518153099955
		5.8467666241602743 -1.4325234110046381e-08 -0.0047078235165564086
		4.5109531252787161 1.1042596245013216 -0.0047078235165561866
		4.5109531252787161 -1.104259653151789 -0.0047078235165565196
		5.8467666241602743 -1.4325234110046381e-08 -0.0047078235165564086
		5.6152127641052747 -1.4325233888001776e-08 -1.1089674623431109
		5.3852010026359007 -1.4325233888001776e-08 -1.7922198319197535
		4.9869646713982227 -1.4325233665957171e-08 -2.55653534945283
		4.5586035850835422 -1.4325233665957171e-08 -3.276584410844265
		4.0044181863525878 -1.4325233443912566e-08 -3.9152114398966482
		3.3657911573002082 -1.4325233443912566e-08 -4.4693968386275973
		2.645742095908771 -1.4325233443912566e-08 -4.973876198236038
		0.093914569972500236 -1.4325233443912566e-08 -4.973876198236038
		0.093914569972500236 0.55212980508804299 -4.9738761982360415
		0.093914569972500236 0.55212980508804421 -5.5260060176493244
		0.093914569972500236 2.2085192633278754 -4.973876198236038
		0.093914569972500236 0.55212980508804377 -4.4217463788227747
		0.093914569972500236 0.55212980508804299 -4.9738761982360415
		0.093914569972500236 -1.4325233443912566e-08 -4.973876198236038
		-2.4579129559637733 -1.4325233443912566e-08 -4.973876198236038
		-3.1779620173552114 -1.4325233443912566e-08 -4.4693968386275973
		-3.8165890464075929 -1.4325233443912566e-08 -3.9152114398966482
		-4.3707744451385491 -1.4325233665957171e-08 -3.276584410844265
		-4.799135531453226 -1.4325233665957171e-08 -2.55653534945283
		-5.1973718626908969 -1.4325233888001776e-08 -1.7922198319197535
		-5.4273836241602691 -1.4325233888001776e-08 -1.1089674623431109
		-5.4273836241602691 -1.4325234110046381e-08 1.0995518153099955
		;
createNode transform -n "godNode_M_comOffset_ctrl" -p "godNode_M_com_ctrl";
	rename -uid "33E8B1D8-40F7-C97E-1C87-49B74D492845";
createNode nurbsCurve -n "godNode_M_comOffset_ctrlShape" -p "godNode_M_comOffset_ctrl";
	rename -uid "44569705-4D72-81BB-58F4-8A84442F5206";
	setAttr -k off ".v";
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.030600017 0.3123 0.058800008 ;
	setAttr ".cc" -type "nurbsCurve" 
		1 42 2 no 3
		43 0 0.125 0.25 0.375 0.5 0.625 0.75 0.875 0.94378600000000001 1 1.056214 1.125
		 1.25 1.375 1.5 1.625 1.75 1.875 1.8960399999999999 1.919448 1.957708 2.0422920000000002
		 2.080552 2.100813 2.125 2.25 2.375 2.5 2.625 2.75 2.9437859999999998 2.9789509999999999
		 3 3.0210490000000001 3.0562140000000002 3.25 3.375 3.5 3.625 3.75 3.875 4 4.125
		43
		-4.9686510601453175 -0.00052725306467737987 1.0096896360237846
		-4.7573571413103553 -0.00052725306467760191 1.6373404561334262
		-4.3915283918928436 -0.00052725306467760191 2.3394576865491912
		-3.9980263725803278 -0.00052725306467760191 3.0009107660043695
		-3.4889393419392247 -0.00052725306467760191 3.5875677559790669
		-2.9022823519645278 -0.00052725306467782396 4.0966547866201735
		-2.2408292725093522 -0.00052725306467782396 4.4901568059326857
		-1.5387120420935827 -0.00052725306467782396 4.8559855553502151
		-0.91106122198394446 -0.00052725306467782396 5.0672794741851606
		0.10333623755639811 -0.00052725306467715782 4.0528820146448181
		1.1177336970967433 -0.00052725306467782396 5.0672794741851606
		1.7453845172063809 -0.00052725306467782396 4.8559855553502151
		2.4475017476221437 -0.00052725306467782396 4.4901568059326857
		3.1089548270773188 -0.00052725306467782396 4.0966547866201735
		3.6956118170520176 -0.00052725306467760191 3.5875677559790669
		4.2046988476931215 -0.00052725306467760191 3.0009107660043695
		4.5982008670056302 -0.00052725306467760191 2.3394576865491912
		4.9640296164231561 -0.00052725306467760191 1.6373404561334262
		5.1753235352581086 -0.00052725306467737987 1.0096896360237846
		5.3880340601453103 -0.00052725306467715782 -0.0047078235165572968
		4.7888794391369425 0.49476814557975712 -0.0047078235165571858
		4.7888794391369425 -0.49582265170911088 -0.0047078235165572968
		5.3880340601453103 -0.00052725306467715782 -0.0047078235165572968
		5.1753235352581086 -0.00052725306467715782 -1.0191052830568998
		4.9640296164231561 -0.00052725306467715782 -1.6467561031665401
		4.5982008670056302 -0.00052725306467693578 -2.3488733335823038
		4.2046988476931215 -0.00052725306467693578 -3.0103264130374816
		3.6956118170520176 -0.00052725306467671373 -3.596983403012179
		3.1089548270773188 -0.00052725306467671373 -4.1060704336532838
		2.4475017476221437 -0.00052725306467671373 -4.5694963914480971
		0.10333623755639811 -0.00052725306467671373 -4.5694963914480971
		0.10333623755639811 -0.000527253064678046 -4.0622976616779249
		0.10333623755639811 -0.50772598283484993 -4.5694963914480953
		0.10333623755639811 -0.00052725306467893418 -5.0766951212182621
		0.10333623755639811 -0.00052725306467671373 -4.5694963914480971
		-2.2408292725093522 -0.00052725306467671373 -4.5694963914480971
		-2.9022823519645278 -0.00052725306467671373 -4.1060704336532838
		-3.4889393419392247 -0.00052725306467671373 -3.596983403012179
		-3.9980263725803278 -0.00052725306467693578 -3.0103264130374816
		-4.3915283918928436 -0.00052725306467693578 -2.3488733335823038
		-4.7573571413103553 -0.00052725306467715782 -1.6467561031665401
		-4.9686510601453175 -0.00052725306467715782 -1.0191052830568998
		-4.9686510601453175 -0.00052725306467737987 1.0096896360237846
		;
createNode transform -n "godNode_M_end_ctrl_srtBuffer" -p "godNode_M_comOffset_ctrl";
	rename -uid "428DBACC-47F7-BE73-39B1-F49E4C446B0E";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 0.44880009 1 ;
createNode transform -n "godNode_M_end_ctrl" -p "godNode_M_end_ctrl_srtBuffer";
	rename -uid "D3DD7F38-473B-CC4E-C927-CAA1585EA67E";
	setAttr ".rp" -type "double3" 5.5511151231257827e-15 4.1078251911130792e-15 -8.8817841970012523e-16 ;
	setAttr ".rpt" -type "double3" -5.5511151231257827e-15 -4.1078251911130792e-15 8.8817841970012523e-16 ;
	setAttr ".sp" -type "double3" 5.5511151231257827e-15 4.1078251911130792e-15 -8.8817841970012523e-16 ;
createNode nurbsCurve -n "godNode_M_end_ctrlShape" -p "godNode_M_end_ctrl";
	rename -uid "69061ED0-4C7F-8140-C0B0-13B6AA8ED056";
	setAttr -k off ".v";
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 1 0.10010004 ;
	setAttr ".cc" -type "nurbsCurve" 
		1 48 2 no 3
		49 0 0.125 0.25 0.375 0.5 0.625 0.75 0.875 0.94378600000000001 0.96638900000000005
		 0.97895100000000002 1 1.0210490000000001 1.0336110000000001 1.056214 1.125 1.25 1.375
		 1.5 1.625 1.75 1.875 1.8960399999999999 1.919448 1.957708 2.0422920000000002 2.080552
		 2.100813 2.125 2.25 2.375 2.5 2.625 2.75 2.9437859999999998 2.9561022079999999 2.9789509999999999
		 3 3.0210490000000001 3.0436231170000001 3.0562140000000002 3.25 3.375 3.5 3.625 3.75
		 3.875 4 4.125
		49
		-4.5307738982179702 -1.4325234110046381e-08 0.84782458335870836
		-4.3393056575135311 -1.4325234332090986e-08 1.416583016946023
		-4.0078025672386435 -1.4325234332090986e-08 2.0528206882298341
		-3.6512227860180397 -1.4325234332090986e-08 2.6522097200114172
		-3.1899033185210128 -1.4325234554135591e-08 3.1838207686718372
		-2.6582922698605937 -1.4325234554135591e-08 3.6451402361688632
		-2.0589032380790178 -1.4325234776180196e-08 4.0017200173894709
		-1.4226655667951997 -1.4325234776180196e-08 4.3332231076643586
		-0.85390713320788847 -1.4325234776180196e-08 4.5246913483688127
		-0.85390713320788847 -1.4325234776180196e-08 4.9842996939950641
		-1.3135154788341481 -1.4325234776180196e-08 4.9842996939950641
		0.065309558044632413 -1.4325234998224801e-08 6.3631247308738548
		1.4441345949234143 -1.4325234776180196e-08 4.9842996939950641
		0.98452624929715193 -1.4325234776180196e-08 4.9842996939950641
		0.98452624929715193 -1.4325234776180196e-08 4.5246913483688127
		1.5532846828844677 -1.4325234776180196e-08 4.3332231076643586
		2.1895223541682767 -1.4325234776180196e-08 4.0017200173894709
		2.7889113859498522 -1.4325234554135591e-08 3.6451402361688632
		3.3205224346102682 -1.4325234554135591e-08 3.1838207686718372
		3.7818419021072942 -1.4325234332090986e-08 2.6522097200114172
		4.1384216833279002 -1.4325234332090986e-08 2.0528206882298341
		4.4699247736027923 -1.4325234332090986e-08 1.416583016946023
		4.6613930143072331 -1.4325234110046381e-08 0.84782458335870836
		4.8541449411210147 -1.4325234110046381e-08 -0.07139210789381023
		3.7421763230547107 1.1042596245013216 -0.071392107893809981
		3.7421763230547107 -1.104259653151789 -0.071392107893810272
		4.8541449411210147 -1.4325234110046381e-08 -0.07139210789381023
		4.6613930143072331 -1.4325233888001776e-08 -0.99060879914633104
		4.4699247736027923 -1.4325233888001776e-08 -1.559367232733647
		4.1384216833279002 -1.4325233665957171e-08 -2.1956049040174621
		3.7818419021072942 -1.4325233665957171e-08 -2.7949939357990345
		3.3205224346102682 -1.4325233443912566e-08 -3.3266049844594519
		2.7889113859498522 -1.4325233443912566e-08 -3.7879244519564761
		2.1895223541682767 -1.4325233443912566e-08 -4.2078672185301436
		0.065309558044632413 -1.4325233443912566e-08 -4.2078672185301436
		0.065309558044632413 0.55212980508804299 -4.2078672185301462
		0.065309558044632413 0.55212980508804421 -4.6674755641564074
		0.065309558044632413 2.2085192633278754 -4.2078672185301436
		0.065309558044632413 0.55212980508804377 -3.7482588729038926
		0.065309558044632413 0.55212980508804299 -4.2078672185301462
		0.065309558044632413 -1.4325233443912566e-08 -4.2078672185301436
		-2.0589032380790178 -1.4325233443912566e-08 -4.2078672185301436
		-2.6582922698605937 -1.4325233443912566e-08 -3.7879244519564761
		-3.1899033185210128 -1.4325233443912566e-08 -3.3266049844594519
		-3.6512227860180397 -1.4325233665957171e-08 -2.7949939357990345
		-4.0078025672386435 -1.4325233665957171e-08 -2.1956049040174621
		-4.3393056575135311 -1.4325233888001776e-08 -1.559367232733647
		-4.5307738982179702 -1.4325233888001776e-08 -0.99060879914633104
		-4.5307738982179702 -1.4325234110046381e-08 0.84782458335870836
		;
createNode transform -n "godNode_M_endOffset_ctrl" -p "godNode_M_end_ctrl";
	rename -uid "931A9B5D-43E7-5006-8090-53AC9D8EE747";
createNode nurbsCurve -n "godNode_M_endOffset_ctrlShape" -p "godNode_M_endOffset_ctrl";
	rename -uid "15669AC3-4D63-2B2A-AC04-ABBEB0A9D7BF";
	setAttr -k off ".v";
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.030600017 0.3123 0.058800008 ;
	setAttr ".cc" -type "nurbsCurve" 
		1 42 2 no 3
		43 0 0.125 0.25 0.375 0.5 0.625 0.75 0.875 0.94378600000000001 1 1.056214 1.125
		 1.25 1.375 1.5 1.625 1.75 1.875 1.8960399999999999 1.919448 1.957708 2.0422920000000002
		 2.080552 2.100813 2.125 2.25 2.375 2.5 2.625 2.75 2.9437859999999998 2.9789509999999999
		 3 3.0210490000000001 3.0562140000000002 3.25 3.375 3.5 3.625 3.75 3.875 4 4.125
		43
		-4.1360444834772121 -0.00052725306467737987 0.84049396879525629
		-3.9601574999054385 -0.00052725306467760191 1.3629681133145732
		-3.6556313895769317 -0.00052725306467760191 1.9474301861111465
		-3.3280692733177424 -0.00052725306467760191 2.4980422792613517
		-2.9042909521588132 -0.00052725306467760191 2.9863920099440371
		-2.4159412214761296 -0.00052725306467782396 3.4101703311029707
		-1.8653291283259252 -0.00052725306467782396 3.7377324473621623
		-1.2808670555293498 -0.00052725306467782396 4.0422585576906798
		-0.75839291101003392 -0.00052725306467782396 4.2181455412624347
		0.086019982106759305 -0.00052725306467715782 3.3737326481456393
		0.93043287522355422 -0.00052725306467782396 4.2181455412624347
		1.4529070197428702 -0.00052725306467782396 4.0422585576906798
		2.0373690925394419 -0.00052725306467782396 3.7377324473621623
		2.5879811856896446 -0.00052725306467782396 3.4101703311029707
		3.0763309163723291 -0.00052725306467760191 2.9863920099440371
		3.500109237531261 -0.00052725306467760191 2.4980422792613517
		3.8276713537904481 -0.00052725306467760191 1.9474301861111465
		4.1321974641189598 -0.00052725306467760191 1.3629681133145732
		4.3080844476907245 -0.00052725306467737987 0.84049396879525629
		4.4851506538677217 -0.00052725306467715782 -0.0039189243215384121
		3.9863975446286406 0.49476814557975712 -0.0039189243215383184
		3.9863975446286406 -0.49582265170911088 -0.0039189243215384121
		4.4851506538677217 -0.00052725306467715782 -0.0039189243215384121
		4.3080844476907245 -0.00052725306467715782 -0.8483318174383323
		4.1321974641189598 -0.00052725306467715782 -1.3708059619576498
		3.8276713537904481 -0.00052725306467693578 -1.955268034754222
		3.500109237531261 -0.00052725306467693578 -2.5058801279044265
		3.0763309163723291 -0.00052725306467671373 -2.9942298585871123
		2.5879811856896446 -0.00052725306467671373 -3.4180081797460447
		2.0373690925394419 -0.00052725306467671373 -3.8037769433471067
		0.086019982106759305 -0.00052725306467671373 -3.8037769433471067
		0.086019982106759305 -0.000527253064678046 -3.3815704967887115
		0.086019982106759305 -0.50772598283484993 -3.8037769433471067
		0.086019982106759305 -0.00052725306467893418 -4.225983389905501
		0.086019982106759305 -0.00052725306467671373 -3.8037769433471067
		-1.8653291283259252 -0.00052725306467671373 -3.8037769433471067
		-2.4159412214761296 -0.00052725306467671373 -3.4180081797460447
		-2.9042909521588132 -0.00052725306467671373 -2.9942298585871123
		-3.3280692733177424 -0.00052725306467693578 -2.5058801279044265
		-3.6556313895769317 -0.00052725306467693578 -1.955268034754222
		-3.9601574999054385 -0.00052725306467715782 -1.3708059619576498
		-4.1360444834772121 -0.00052725306467715782 -0.8483318174383323
		-4.1360444834772121 -0.00052725306467737987 0.84049396879525629
		;
createNode transform -n "guide" -p "godNode_M_cmpnt";
	rename -uid "E8F18417-4AD6-8DBC-B179-8690C1BB8651";
	setAttr ".v" no;
createNode transform -n "guide_world_ctrl" -p "|godNode_M_cmpnt|guide";
	rename -uid "333F42C2-4329-B369-A643-9D879D7E05C0";
createNode locator -n "guide_world_ctrlShape" -p "guide_world_ctrl";
	rename -uid "A71D3993-4FC2-DA30-F968-8C8C7CDDCEB4";
	setAttr -k off ".v";
createNode transform -n "guide_com_ctrl" -p "guide_world_ctrl";
	rename -uid "8A39280F-45C8-4A3D-F2DB-5EBCBFB293AD";
	setAttr ".t" -type "double3" 0 8.5130153395356754 -2.2624579293362146e-11 ;
createNode locator -n "guide_com_ctrlShape" -p "guide_com_ctrl";
	rename -uid "CE961B34-4C85-7347-0BF3-BFA37430BDF4";
	setAttr -k off ".v";
createNode transform -n "guide_end_ctrl" -p "guide_com_ctrl";
	rename -uid "F466222B-4929-740A-DAC1-5F8E686FE462";
	setAttr ".t" -type "double3" 0 3.328573397401982 0 ;
createNode locator -n "guide_end_ctrlShape" -p "guide_end_ctrl";
	rename -uid "4D2CC180-4BFC-E4E7-6542-4FAA0F12A89C";
	setAttr -k off ".v";
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
createNode transform -n "legGlobal_R_cmpnt";
	rename -uid "35272BD4-4C1B-B0BA-96B9-918BDCB094A0";
	setAttr ".ove" yes;
	setAttr ".ovc" 19;
	setAttr ".ovrgb" -type "float3" 0.059300009 0.5043 0.17050005 ;
createNode transform -n "legGlobal_R_input" -p "legGlobal_R_cmpnt";
	rename -uid "AF918553-43C8-5E10-8994-57A15F037D63";
	addAttr -ci true -sn "endWorld" -ln "endWorld" -at "matrix";
createNode transform -n "legGlobal_R_output" -p "legGlobal_R_cmpnt";
	rename -uid "4F0DB2DC-42BB-1C3F-3ED4-5F9CD41A5BB1";
	addAttr -ci true -sn "rolledAnkle" -ln "rolledAnkle" -nn "rolledAnkle" -at "matrix";
	addAttr -ci true -sn "toeAngle" -ln "toeAngle" -at "doubleAngle";
	addAttr -ci true -sn "tarsiAngle" -ln "tarsiAngle" -at "doubleAngle";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	addAttr -ci true -sn "upVectorWorld" -ln "upVectorWorld" -at "matrix";
	addAttr -ci true -sn "rawAnkleControl" -ln "rawAnkleControl" -at "matrix";
	setAttr ".nts" -type "string" "tarsi angle represents the angle betwaddAttr -ln \"chainEnd\" -at \"matrix\";een the world flat ankle and the tarsi vector (from ankle/beginning of tarsi to beginning of toes).\nToe angle is the following angle down, the one between toes and tarsi";
createNode transform -n "control" -p "legGlobal_R_cmpnt";
	rename -uid "76ADF458-46A3-D744-F4EF-5AAC26B62539";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
createNode transform -n "legGlobal_R_animParameters" -p "|legGlobal_R_cmpnt|control";
	rename -uid "96054A63-4F98-9F2F-4625-478C087D55D7";
	addAttr -ci true -k true -sn "roll" -ln "roll" -smn -1.7 -smx 3.14 -at "doubleAngle";
	setAttr -k on ".roll";
createNode transform -n "roll_mechanics" -p "|legGlobal_R_cmpnt|control";
	rename -uid "5A714A43-43BE-6423-C83C-75B3EB77D7CE";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
createNode transform -n "legGlobal_R_ankle_rest_srt" -p "|legGlobal_R_cmpnt|control|roll_mechanics";
	rename -uid "0751EB75-4390-3F64-7D0E-13B2DF7DD9EE";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr ".nts" -type "string" "right now the rest is manually placed and used as a static value to figure out the roll's ankle level offset from.\nTo make the component more dynamic and responsive to configuration this will need to eventually be the non-rolled default produced by the defaults";
createNode joint -n "legGlobal_R_ankle_rolled_srt" -p "legGlobal_R_ankle_rest_srt";
	rename -uid "C70FFAD0-44BF-F2A1-DF6D-42AF442CC5BB";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 84.553748547758588 9.5416640443905503e-15 180 ;
	setAttr ".radi" 0.5;
	setAttr ".nts" -type "string" "this is currently not connected to anything. Being the ankle we will want to compensate for the roll and make sure it remains world aligned, it should only be a matter of arithmetics on a few angles";
createNode transform -n "legGlobal_R_roll_world_srt" -p "|legGlobal_R_cmpnt|control|roll_mechanics";
	rename -uid "FA0AD2D5-4B95-C873-A4BD-77846111FBE0";
createNode joint -n "legGlobal_R_roll_heel_srt" -p "legGlobal_R_roll_world_srt";
	rename -uid "B4760D56-4931-281A-4711-13A39611385C";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.1;
createNode joint -n "legGlobal_R_roll_tip_srt" -p "legGlobal_R_roll_heel_srt";
	rename -uid "C1D96B56-481F-5F13-2BD7-C583CB0DA9AB";
	setAttr ".r" -type "double3" -21.065155320812835 180 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.1;
createNode joint -n "legGlobal_R_roll_tarsi_srt" -p "legGlobal_R_roll_tip_srt";
	rename -uid "3D06DEF2-4092-FFDD-2B4F-B3AEF3939A4F";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.1;
createNode joint -n "legGlobal_R_roll_tarsiEnd_srt" -p "legGlobal_R_roll_tarsi_srt";
	rename -uid "751D9E3E-4822-F4B7-6C67-CA954ECC910C";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.1;
createNode transform -n "legGlobal_R_worldAnkle_ctrl_srtBuffer" -p "|legGlobal_R_cmpnt|control";
	rename -uid "8CEFD4CB-4CEB-6C9F-1131-7AB755D02D60";
createNode transform -n "legGlobal_R_worldAnkle_ctrl" -p "legGlobal_R_worldAnkle_ctrl_srtBuffer";
	rename -uid "526FA887-451A-B14E-A5EE-BE9BBAC80B06";
createNode nurbsCurve -n "legGlobal_R_worldAnkle_ctrlShape" -p "legGlobal_R_worldAnkle_ctrl";
	rename -uid "5DBA6B0D-498F-73C6-702B-EFA0C3FBB3B5";
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
createNode transform -n "legGlobal_R_upVector_ctrl_srtBuffer" -p "|legGlobal_R_cmpnt|control";
	rename -uid "A4BBA20C-4F91-6898-2359-80B35575F315";
createNode transform -n "legGlobal_R_upVector_ctrl" -p "legGlobal_R_upVector_ctrl_srtBuffer";
	rename -uid "6C855B05-444D-189B-F5A9-94B7B6B50901";
createNode nurbsCurve -n "legGlobal_R_upVector_ctrl" -p "|legGlobal_R_cmpnt|control|legGlobal_R_upVector_ctrl_srtBuffer|legGlobal_R_upVector_ctrl";
	rename -uid "87479D33-4AF7-A7F8-B00B-08B8919E7B67";
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
createNode transform -n "legGlobal_R_configParameters" -p "|legGlobal_R_cmpnt|control";
	rename -uid "4CFC3E18-4869-0BA9-A7AF-5FA9D2252C8B";
	addAttr -ci true -k true -sn "toeRest" -ln "toeRest" -smn -1.7 -smx 3.14 -at "doubleAngle";
	addAttr -ci true -k true -sn "tarsirest" -ln "tarsirest" -smn -1.7 -smx 3.14 -at "doubleAngle";
	addAttr -ci true -k true -sn "toeLength" -ln "toeLength" -smn 0.01 -smx 10 -at "double";
	addAttr -ci true -k true -sn "tarsiLength" -ln "tarsiLength" -smn 0.01 -smx 10 -at "double";
	addAttr -ci true -sn "plantLength" -ln "plantLength" -min 0 -max 100 -at "double";
	addAttr -ci true -sn "ankleRest" -ln "ankleRest" -at "doubleAngle";
	addAttr -ci true -sn "ankleGlobalOffset" -ln "ankleGlobalOffset" -at "matrix";
	addAttr -ci true -sn "upVecGlobalOffset" -ln "upVecGlobalOffset" -at "matrix";
	setAttr -k on ".toeRest";
	setAttr -k on ".tarsirest" -32.928389796476075;
	setAttr -k on ".toeLength" 2.4857768956930508;
	setAttr -k on ".tarsiLength" 1.8769453361236783;
	setAttr -k on ".plantLength" 5;
	setAttr ".ankleGlobalOffset" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.2528433333772928 2.5444464459297729 -0.51882775330918474 1;
	setAttr ".upVecGlobalOffset" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -4.7380000000000004 6.7561481902608396 -9.2158626204103253 1;
createNode transform -n "legGlobal_R_worldAnkle_rolled_srt" -p "|legGlobal_R_cmpnt|control";
	rename -uid "EE33BEE4-4753-303E-3F75-28B3BC18EC11";
createNode transform -n "guide" -p "legGlobal_R_cmpnt";
	rename -uid "4DD7416D-409E-374A-F4F5-3E9C9A8C8EE8";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode transform -n "legGlobal_R_guide_global_ctrl" -p "|legGlobal_R_cmpnt|guide";
	rename -uid "FE129D5C-4DD6-9986-2784-4DA26C51070D";
	setAttr ".t" -type "double3" -3.279 0.13294181866603688 0.013700291599500813 ;
createNode nurbsCurve -n "legGlobal_R_guide_global_ctrlShape" -p "legGlobal_R_guide_global_ctrl";
	rename -uid "848B0EAF-40E4-67E3-AA7A-BC8A5833736F";
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
createNode transform -n "legGlobal_R_guide_basisVector" -p "legGlobal_R_guide_global_ctrl";
	rename -uid "8D7B30A7-4166-D302-2B1C-3B90B6B5CEAF";
	setAttr ".t" -type "double3" 0 0 1 ;
createNode transform -n "legGlobal_R_guide_heel_ctrl" -p "legGlobal_R_guide_global_ctrl";
	rename -uid "FDCDC8B8-418E-13BF-5B44-D4AA2913B10F";
	setAttr ".t" -type "double3" -3.3306690738754696e-16 0 -2.1093375553363201 ;
	setAttr ".ro" 2;
createNode nurbsCurve -n "legGlobal_R_guide_heel_ctrlShape" -p "legGlobal_R_guide_heel_ctrl";
	rename -uid "EE5309BF-4217-89EB-0626-18AAD43B93FA";
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
createNode transform -n "legGlobal_R_guide_tip_ctrl" -p "legGlobal_R_guide_heel_ctrl";
	rename -uid "61312F3B-4470-420F-EFFD-47BAF4A97653";
	setAttr ".t" -type "double3" 0 0 5 ;
	setAttr -l on -k off ".ty";
	setAttr -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "legGlobal_R_guide_tip_ctrlShape" -p "legGlobal_R_guide_tip_ctrl";
	rename -uid "08141CA6-4B04-1BEC-0538-6C9926C70D8A";
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
createNode transform -n "legGlobal_R_guide_toe2Tarsi_ctrl" -p "legGlobal_R_guide_heel_ctrl";
	rename -uid "AF37C559-475A-667A-62E2-96A6A9960AC9";
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
createNode nurbsCurve -n "legGlobal_R_guide_toe2Tarsi_ctrlShape" -p "legGlobal_R_guide_toe2Tarsi_ctrl";
	rename -uid "6268E790-469F-51BD-93E1-8DBFE46CF5D5";
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
createNode transform -n "legGlobal_R_guide_ankle_ctrl" -p "legGlobal_R_guide_heel_ctrl";
	rename -uid "DA035348-4BAF-E9BF-395B-94A8E076FFF7";
	setAttr ".t" -type "double3" 0.026156666622707547 2.4115046272637359 1.5768095104276343 ;
	setAttr -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "legGlobal_R_guide_ankle_ctrlShape" -p "legGlobal_R_guide_ankle_ctrl";
	rename -uid "F7EEE24A-4E4F-CDA8-5EAA-2EA74A4C3E65";
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
createNode transform -n "legGlobal_R_guide_upVector_ctrl_srtBuffer" -p "|legGlobal_R_cmpnt|guide";
	rename -uid "A90F663E-4F24-5ED9-4D31-09A317FECA04";
createNode transform -n "legGlobal_R_guide_upVector_ctrl" -p "legGlobal_R_guide_upVector_ctrl_srtBuffer";
	rename -uid "B2EC9258-43B1-7B6A-1243-228E191BF23B";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" -4.738 6.7561481902608396 -9.2158626204103253 ;
createNode nurbsCurve -n "legGlobal_R_guide_upVector_ctrlShape" -p "legGlobal_R_guide_upVector_ctrl";
	rename -uid "04C77FF7-4FCD-B3DD-5382-08967B317AFF";
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
createNode transform -n "legGlobal_R_toolParameters" -p "|legGlobal_R_cmpnt|guide";
	rename -uid "C298B133-486C-2C90-EEE8-0782B24B4256";
	addAttr -ci true -m -sn "toSwap" -ln "toSwap" -at "compound" -nc 2;
	addAttr -s false -ci true -sn "origin" -ln "origin" -at "message" -p "toSwap";
	addAttr -s false -ci true -sn "guided" -ln "guided" -at "message" -p "toSwap";
	addAttr -s false -ci true -m -sn "toDelete" -ln "toDelete" -at "message";
	setAttr -s 6 ".toSwap";
	setAttr -s 9 ".toDelete";
createNode transform -n "foot_R_cpmnt";
	rename -uid "3592E902-4ECE-7695-8994-16BA890AF979";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.1814 0.29659995 0.5783 ;
	setAttr ".it" no;
createNode transform -n "foot_R_input" -p "foot_R_cpmnt";
	rename -uid "1A6B655C-4003-0137-37A7-55985C5D00EA";
	addAttr -ci true -sn "tarsiLength" -ln "tarsiLength" -dv 4 -min 0 -max 50 -at "double";
	addAttr -ci true -sn "startMtx" -ln "startMtx" -at "matrix";
	addAttr -ci true -sn "toeAngle" -ln "toeAngle" -at "doubleAngle";
	addAttr -ci true -sn "tarsiAngle" -ln "tarsiAngle" -at "doubleAngle";
	addAttr -ci true -sn "toeLength" -ln "toeLength" -dv 3 -min 0.01 -max 10 -at "double";
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
	setAttr -k on ".toeLength";
createNode transform -n "foot_R_output" -p "foot_R_cpmnt";
	rename -uid "DC0A98FF-496F-4899-709D-118FCD7052C5";
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
createNode transform -n "control" -p "foot_R_cpmnt";
	rename -uid "195FE7C7-4F63-EF5C-B5BC-83B898E8370D";
	setAttr ".it" no;
createNode transform -n "foot_R_ankleSpace_srt" -p "|foot_R_cpmnt|control";
	rename -uid "4D7D6116-4ABD-85DB-E299-BF9BEB7B474D";
createNode transform -n "foot_R_tarsii_ctrl_srtBuffer" -p "foot_R_ankleSpace_srt";
	rename -uid "CDE67213-4544-A2E6-3A14-7E99687F2F05";
createNode transform -n "foot_R_tarsii_ctrl" -p "foot_R_tarsii_ctrl_srtBuffer";
	rename -uid "0C8FBA9E-4242-A035-BEC4-16AED69D6F05";
createNode nurbsCurve -n "foot_R_tarsii_ctrlShape" -p "foot_R_tarsii_ctrl";
	rename -uid "E43D4D56-489F-7858-CAE0-9299DE50C0B9";
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
createNode joint -n "diagnostic_ankle" -p "foot_R_tarsii_ctrl";
	rename -uid "41C2545E-4396-A087-BE1C-498B25727C58";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode joint -n "diagnostic_tarsi" -p "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|diagnostic_ankle";
	rename -uid "668C2D91-42D7-9067-DB02-56B43FA34CAA";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode transform -n "foot_R_toes_ctrl_srtBuffer" -p "foot_R_tarsii_ctrl";
	rename -uid "B7F49A0A-4DB3-C2C6-F7F3-46A5E376FDC5";
createNode transform -n "foot_R_toes_ctrl" -p "foot_R_toes_ctrl_srtBuffer";
	rename -uid "6BD88E32-4FCC-689A-D34E-FE94CAF2C7C6";
createNode nurbsCurve -n "foot_R_toes_ctrlShape" -p "foot_R_toes_ctrl";
	rename -uid "B19CFD33-470B-6C25-7157-678822CFBD61";
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
createNode joint -n "diagnostic_toes" -p "foot_R_toes_ctrl";
	rename -uid "CD1C3D75-4E13-CF8F-9A88-A592C7AF9DF9";
	setAttr ".t" -type "double3" 0 0 4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode joint -n "diagnostic_tip" -p "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|foot_R_toes_ctrl_srtBuffer|foot_R_toes_ctrl|diagnostic_toes";
	rename -uid "F9FD3915-4FBE-7774-304D-248C6E53E4F8";
	setAttr ".t" -type "double3" 2.384185791015625e-07 -8.5989402265340686e-09 2.4857768956930508 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode transform -n "guide" -p "foot_R_cpmnt";
	rename -uid "2F5E37C4-4815-6C6F-A97C-59A20F47FCC5";
parent -s -nc -r -add "|leg_L_cmpnt|control|leg_L_IK_srtBuffer|leg_L_hip_srt|diagnosticCube_geoShape" "leg_L_tibiaStart_srt" ;
parent -s -nc -r -add "|leg_L_cmpnt|control|leg_L_IK_srtBuffer|leg_L_hip_srt|diagnosticCube_geoShape" "leg_L_tibiaEnd_srt" ;
parent -s -nc -r -add "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|diagnosticCube_geoShape" "leg_R_tibiaStart_srt" ;
parent -s -nc -r -add "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|diagnosticCube_geoShape" "leg_R_tibiaEnd_srt" ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "90A5DC83-4248-0C73-F27A-C189664A8166";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "E57A28C2-4AF4-9EB6-9578-1DB8E6BAEF35";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "997FD3DB-46AA-7625-F624-A2B9ECBABD36";
createNode displayLayerManager -n "layerManager";
	rename -uid "89F95FA1-4610-0496-AFCE-18B8EA9E0896";
createNode displayLayer -n "defaultLayer";
	rename -uid "47B7C211-461A-819B-0D92-70A10B7C297F";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "03AA2AD6-4456-F521-6E06-7FB1D053A650";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "60B4784F-4303-8975-139B-5DB969DA38AD";
	setAttr ".g" yes;
createNode plusMinusAverage -n "leg_L_hip2Ankle_displacement";
	rename -uid "39A26E34-49A1-7863-A6CC-90940ABDA672";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "leg_L_limitedWorldAnkle_translate";
	rename -uid "BE42F8A2-4875-120E-6F0B-8B9FA8CECCDC";
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode vectorProduct -n "leg_L_hip2ankle_direction_normal";
	rename -uid "050E5DA2-4B07-438D-24A7-D6A9A9779760";
	setAttr ".op" 0;
	setAttr ".no" yes;
createNode multiplyDivide -n "leg_L_hip2Ankle_clamped_displacement";
	rename -uid "12AF279A-4014-A059-C248-A18F4D71A0AB";
createNode clamp -n "leg_L_ankle2hip_clampedDistance";
	rename -uid "334F40F3-4D9A-EAFF-B1E1-7394A84D1984";
	setAttr ".mn" -type "float3" 3 3 3 ;
createNode distanceBetween -n "leg_L_hip2ankle_distance";
	rename -uid "E7500AAA-428B-262E-6F0C-4D9EBFBFDB34";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "6D8108E1-4E25-54D3-01AD-F49859AB7A44";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1617\n            -height 448\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 1\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 0\n            -showAssets 1\n            -showContainedOnly 0\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 0\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n"
		+ "            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 0\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 0\n            -ignoreDagHierarchy 0\n"
		+ "            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n"
		+ "            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n"
		+ "                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n"
		+ "                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n"
		+ "            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n"
		+ "                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n"
		+ "                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n"
		+ "            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n"
		+ "                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n"
		+ "\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit 1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n"
		+ "                -gridSnap 1\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 0\n                -showShapes 0\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 0\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n"
		+ "                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit 1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 1\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 0\n                -showShapes 0\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 0\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n"
		+ "                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n"
		+ "        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1617\\n    -height 448\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1617\\n    -height 448\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "5A55784D-4B1D-6C0F-66BC-E182D8E41028";
	setAttr ".b" -type "string" "playbackOptions -min -40 -max 120 -ast -40 -aet 200 ";
	setAttr ".st" 6;
createNode animCurveUA -n "legGlobal_L_roll_toe_fCurve";
	rename -uid "8C0A3869-4FD6-03D8-CB75-EBA484C47AFA";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  40 0 140 140;
createNode unitConversion -n "legGlobal_L_roll_UC";
	rename -uid "982BED6E-4A93-708A-9813-65966C2CD41C";
	setAttr ".cf" 57.295779513082323;
createNode animCurveUA -n "legGlobal_L_roll_tarsi_fCurve";
	rename -uid "EFF6015D-4515-1E59-B23B-BC9BDDF73B3D";
	setAttr ".tan" 2;
	setAttr -s 3 ".ktv[0:2]"  0 0 40 38 81 -20;
createNode clamp -n "legGlobal_L_heelBack_rollClamp";
	rename -uid "7DFB4809-43F9-DC24-E2E9-E4BB9A48C420";
	setAttr ".mn" -type "float3" 0 0 -40 ;
createNode unitConversion -n "legGlobal_L_heelback_roll_UC";
	rename -uid "F43D9424-4F9F-44DB-85F2-9E86113E1EB0";
	setAttr ".cf" 0.017453292519943295;
createNode animCurveTA -n "animParameters_roll";
	rename -uid "AB41605F-4D7C-54D7-0A6E-2B8D317F2E41";
	setAttr ".tan" 2;
	setAttr -s 3 ".ktv[0:2]"  -40 -40 0 0 120 119.99999999999999;
createNode decomposeMatrix -n "legGlobal_L_roll_tarsi_world_mtx";
	rename -uid "05F8FCF5-4B4F-107E-6F19-4CA4AA2CC108";
createNode decomposeMatrix -n "leg_L_rolledAnkle_ctrl_world_mtx2srt";
	rename -uid "58574282-45A4-446A-9AA7-87A264FCAEE6";
createNode plusMinusAverage -n "legGlobal_L_tarsi_worldDirection_vec3";
	rename -uid "9A0CE03C-4235-00F8-AECA-76BF436A4D10";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode decomposeMatrix -n "legGlobal_L_roll_toes_world_mtx2srt";
	rename -uid "67237A7C-4832-8CC2-2473-FDA54AACD3D9";
createNode angleBetween -n "legGlobal_L_tarsi_rolledAngle";
	rename -uid "FE18DCAE-4A64-B37F-BEB2-BFBE94A48267";
createNode decomposeMatrix -n "foot_L_start_mtx2srt";
	rename -uid "1A530E00-4818-05F8-2026-98A898BD8DA5";
createNode decomposeMatrix -n "leg_L_hipWorld_srt";
	rename -uid "A3D76CE4-4825-8345-0274-25B6FA1AA1D3";
createNode angleBetween -n "leg_L_IK_tension_rot";
	rename -uid "D232B1BB-48F9-5FBE-7E18-38A3B0036C6F";
	setAttr ".v1" -type "double3" 0 -1 0 ;
createNode plusMinusAverage -n "leg_L_IK_ankleDisplacement_vec";
	rename -uid "C2F783CD-4111-E585-7670-9CA942DBE7C2";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode expression -n "leg_L_IK_solver_xpr";
	rename -uid "A610C83E-421D-18C7-7275-9D9806DE1023";
	setAttr -k on ".nds";
	setAttr -s 3 ".in";
	setAttr -s 3 ".in";
	setAttr -s 2 ".out";
	setAttr ".ixp" -type "string" "float $a = .I[0];\nfloat $b = .I[1];\nfloat $c = .I[2];\n\nfloat $sqA = pow($a, 2);\nfloat $sqB = pow($b, 2);\nfloat $sqC = pow($c, 2);\n\n.O[0] = (deg_to_rad(180.0) - acos(($sqA + $sqB - $sqC)/(2.0 * $a * $b)));\n.O[1] = deg_to_rad(90.0) + (-acos(($sqC + $sqA - $sqB)/(2.0 * $c * $a)));";
	setAttr ".uno" 1;
createNode multMatrix -n "leg_L_IK_upVector_hipFramed_mtx";
	rename -uid "9AC66924-4731-0ECF-EC6F-258192577A90";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "leg_L_IK_upVector_hipYProjected_srt";
	rename -uid "528C26EB-40A2-AF9F-5005-01A41BAB7827";
createNode angleBetween -n "leg_L_IK_upVectoringAngle";
	rename -uid "60703B5A-4794-FAE7-2B8B-0C8EE191BE9D";
	setAttr ".v1" -type "double3" 0 0 -1 ;
createNode animBlendNodeAdditiveDA -n "legGlobal_L_toeRollOffset_angle";
	rename -uid "14366C82-4FEA-D2C9-0843-5095E74B4371";
	setAttr ".wa" -1;
	setAttr ".wb" -1;
	setAttr ".o" -21.065155320812835;
createNode animBlendNodeAdditiveDA -n "legGlobal_L_tarsiRollOffset_angle";
	rename -uid "4976BE3E-4491-7F37-1C42-01B5DC91E4B0";
	setAttr ".wa" -1;
	setAttr ".o" -32.928389796476075;
createNode multMatrix -n "legGlobal_L_ankleFramed_tarsi_mtx";
	rename -uid "12B84281-4004-9025-36F0-44BC86686BB9";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "legGlobal_L_ankleFramed_tarsi_srt";
	rename -uid "D8D0DE40-484E-8CE6-2769-80AB795948E3";
createNode pointMatrixMult -n "legGlobal_L_ankleFramed_rollOffset_srt";
	rename -uid "4C4EFD89-43A5-85FE-BDB6-97BB24962684";
createNode decomposeMatrix -n "legGlobal_L_worldAnkle_ctrl_world_srt";
	rename -uid "15339721-4C64-F922-A7AF-23AE4AD5DDBD";
createNode decomposeMatrix -n "godNode_M_debuffer_com_output_srt";
	rename -uid "9E979403-47E3-0692-1C59-60959033FC08";
createNode decomposeMatrix -n "godNode_M_debuffer_end_output_srt";
	rename -uid "B3F7BD88-40FF-B132-E261-D4A683381B2F";
createNode decomposeMatrix -n "godNode_M_master_ctrl_wMtx_output_fNode";
	rename -uid "C1883D18-4126-88C7-19D8-C0A1F0410053";
createNode multMatrix -n "godNode_M_debuffer_com_output_mtx";
	rename -uid "CE7B6B20-4688-E453-61DD-38B08D98D82A";
	setAttr -s 2 ".i";
createNode multMatrix -n "godNode_M_debuffer_end_output_mtx";
	rename -uid "0074F918-4F83-A92B-157E-E788CB66CBCF";
	setAttr -s 2 ".i";
createNode multMatrix -n "leg_L_hipWorld_mtx";
	rename -uid "BC8E42EE-48F8-5881-D72B-0590F944BC78";
	setAttr -s 2 ".i";
createNode multMatrix -n "legGlobal_L_ankleReparent_mtxMult";
	rename -uid "A7696441-4AD1-1B6A-5C1A-988C94245A25";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "legGlobal_L_ankleReparent_srt";
	rename -uid "A4E64472-487F-6017-861A-B6A06F00CAD0";
createNode multMatrix -n "legGlobal_L_upVecReparent_mtxMult";
	rename -uid "EAA42958-4DB4-C5B4-F73E-70B09258AB0E";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "legGlobal_L_upVecReparent_srt";
	rename -uid "A0081B1F-484C-46F6-9AA5-9E93D881F122";
createNode decomposeMatrix -n "leg_L_limitedAnkleWorld_srt";
	rename -uid "04E2E717-41CD-9D1C-CAD7-C6B5604C43C1";
createNode animBlendNodeAdditiveRotation -n "leg_L_fkik_j01_blended_rot";
	rename -uid "AAE795CF-4481-6FF8-79F5-5180F788EEDA";
	setAttr ".o" -type "double3" 57.396422809610783 -13.97639433920642 9.9391099864197514 ;
createNode decomposeMatrix -n "leg_L_hip_rot";
	rename -uid "26FFE79B-43D9-FDEB-CA55-469424F3CAEA";
createNode decomposeMatrix -n "leg_L_fk01_ctrl_world_mtx";
	rename -uid "771700E6-428D-0C93-6685-769C03FDB771";
createNode animBlendNodeAdditiveF -n "leg_L_fkik_blend_complement";
	rename -uid "0F0763FE-4739-302B-C123-5598AE7E4BCD";
	setAttr ".wb" -1;
	setAttr ".ia" 1;
createNode multMatrix -n "leg_L_fk02reframed01_mtx";
	rename -uid "BF0FE583-4FB1-2AC0-41CA-398A061BE5E6";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "leg_L_fk02reframed01_rot";
	rename -uid "EFCD7AA7-4CA9-80FD-3F5D-BA91D46C7E9A";
createNode animBlendNodeAdditiveRotation -n "leg_L_fkik_j02_blended_rot";
	rename -uid "3495DBCC-452A-3501-C062-1995FE1A044A";
	setAttr ".o" -type "double3" 77.811821390002237 0 0 ;
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
createNode container -n "leg_L_container";
	rename -uid "F0B3A6DF-4AD3-A068-E5A1-93B00733779A";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".isc" yes;
	setAttr -s 2 ".pni";
	setAttr ".ctor" -type "string" "Jaco";
	setAttr ".cdat" -type "string" "2018/02/16 08:27:10";
	setAttr ".aal" -type "attributeAlias" {"child","canBeChild[0]","parent","canBeParent[0]"
		,"leg_L_fk01_ctrl","publishedNodeInfo[0]","leg_L_fk02_ctrl","publishedNodeInfo[1]"
		} ;
createNode hyperLayout -n "hyperLayout2";
	rename -uid "E31C78DB-4425-B85A-2892-B1AD3094943E";
	setAttr ".ihi" 0;
	setAttr -s 81 ".hyp";
createNode animCurveTL -n "legGlobal_L_worldAnkle_ctrl_translateX";
	rename -uid "FF042EE9-4ED7-954C-2E25-669365A49712";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 0;
createNode animCurveTL -n "legGlobal_L_worldAnkle_ctrl_translateY";
	rename -uid "CD680875-4DF3-E90B-5BF5-DC8EC550E811";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 0;
createNode animCurveTL -n "legGlobal_L_worldAnkle_ctrl_translateZ";
	rename -uid "102BE357-4E19-1635-DBEF-4F920F3C8562";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 0;
createNode animCurveTU -n "legGlobal_L_worldAnkle_ctrl_visibility";
	rename -uid "A2A404AB-4060-5367-6549-7F9709E3DCC1";
	setAttr ".tan" 9;
	setAttr ".ktv[0]"  0 1;
	setAttr ".kot[0]"  5;
createNode animCurveTA -n "legGlobal_L_worldAnkle_ctrl_rotateX";
	rename -uid "41DD788E-4A3F-2AC0-C4E3-F49BCF4401BE";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 0;
createNode animCurveTA -n "legGlobal_L_worldAnkle_ctrl_rotateY";
	rename -uid "AEAC8296-42D1-F918-5391-B2A8CEFD49A2";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 0;
createNode animCurveTA -n "legGlobal_L_worldAnkle_ctrl_rotateZ";
	rename -uid "358BAEC2-4AF7-E4EA-57E5-2CB62E5734F0";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 0;
createNode animCurveTU -n "legGlobal_L_worldAnkle_ctrl_scaleX";
	rename -uid "06D00CC6-4FA1-EE68-62EE-899825638C5F";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 1;
createNode animCurveTU -n "legGlobal_L_worldAnkle_ctrl_scaleY";
	rename -uid "86986329-4F1A-6694-AAF4-74BEA5009CF1";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 1;
createNode animCurveTU -n "legGlobal_L_worldAnkle_ctrl_scaleZ";
	rename -uid "A1B3B5A3-4A7C-EE54-D773-6B9E52D9E361";
	setAttr ".tan" 18;
	setAttr ".ktv[0]"  0 1;
createNode decomposeMatrix -n "leg_L_rolledAnkle_frame_srt";
	rename -uid "95BE8D3C-4D00-9E65-36A1-86B429F6E532";
createNode container -n "godNode_M_container";
	rename -uid "D410DCEC-4A2B-1A1E-2F8A-8190019A3AC5";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".isc" yes;
	setAttr -s 6 ".pni";
	setAttr ".ctor" -type "string" "Jaco";
	setAttr ".cdat" -type "string" "2018/02/24 11:39:54";
	setAttr ".aal" -type "attributeAlias" {"child","canBeChild[0]","parent","canBeParent[0]"
		,"godnode_M_master_ctrl","publishedNodeInfo[0]","godNode_M_masterOffset_ctrl","publishedNodeInfo[1]"
		,"godNode_M_com_ctrl","publishedNodeInfo[2]","godNode_M_comOffset_ctrl","publishedNodeInfo[3]"
		,"godNode_M_end_ctrl","publishedNodeInfo[4]","godNode_M_endOffset_ctrl","publishedNodeInfo[5]"
		} ;
createNode hyperLayout -n "hyperLayout3";
	rename -uid "9190EDA4-40C0-1F3C-8045-59835D87A96E";
	setAttr ".ihi" 0;
	setAttr -s 33 ".hyp";
createNode decomposeMatrix -n "leg_L_guide_upVector_srt";
	rename -uid "585B7875-4624-2252-78C7-34A8953A93EF";
createNode addDoubleLinear -n "leg_L_totalLength_fNode_add";
	rename -uid "24CF2356-4CB9-55BF-1F12-1EAD9E5AB312";
createNode multDoubleLinear -n "leg_L_lengthLimit_fNode";
	rename -uid "31BB6C0A-47FE-0C25-E3D2-FF99C4F6B0B8";
	setAttr ".i2" 0.992;
createNode container -n "foot_L_container";
	rename -uid "9D06642C-4CA6-10CE-F6DB-8798A8F67EB9";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".isc" yes;
	setAttr -s 2 ".pni";
	setAttr ".ctor" -type "string" "Jaco";
	setAttr ".cdat" -type "string" "2018/03/17 08:15:34";
	setAttr ".aal" -type "attributeAlias" {"child","canBeChild[0]","parent","canBeParent[0]"
		,"foot_M_tarsii_ctrl","publishedNodeInfo[0]","foot_M_toes_ctrl","publishedNodeInfo[1]"
		} ;
createNode hyperLayout -n "hyperLayout4";
	rename -uid "E1942EBA-414F-0AC8-7C07-FD8AAB130E9D";
	setAttr ".ihi" 0;
	setAttr -s 17 ".hyp";
createNode decomposeMatrix -n "leg_L_FK_start_srt";
	rename -uid "BB5F6F9C-4459-62F6-2E1C-E3AD6E98284E";
createNode multMatrix -n "leg_L_FK_start_mtx";
	rename -uid "AC7042CF-4CA9-7887-446C-349E8E271BC8";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "leg_L_fk03_worldMtx";
	rename -uid "C9B6355A-481E-BCC4-89C4-3EBBEBEB0FB5";
createNode animBlendNodeAdditiveRotation -n "leg_L_ankle_rotBlend";
	rename -uid "B6CA0FA8-445C-9045-9853-2791F3943A75";
createNode decomposeMatrix -n "leg_L_j03_worldMtx";
	rename -uid "05EE1BFD-4B5F-6A9D-D46E-3DBEABB677B9";
createNode composeMatrix -n "leg_L_ankle_blend_mtx";
	rename -uid "B3F5D677-4CC3-9B03-075E-6DB099D0044D";
	setAttr ".omat" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.2788047940669824 2.5447580023815384 -0.51870483828642122 1;
createNode decomposeMatrix -n "leg_L_globalAnkle_srt";
	rename -uid "B44FA443-430A-CB57-2BE5-26BE96D52A48";
createNode animBlendNodeAdditiveDA -n "legGlobal_L_guide_tarsi_rest_negate_angle";
	rename -uid "B666A5F1-43F0-A742-F1D7-DDAEEF9E45FF";
	setAttr ".wa" -1;
	setAttr ".o" -32.928389796476075;
createNode distanceBetween -n "legGlobal_L_guide_toe_length";
	rename -uid "79AB0E96-41E2-8F6A-55B7-878B8316A6C4";
createNode distanceBetween -n "legGlobal_L_guide_tarsi_length";
	rename -uid "9B09A564-426C-A525-43FC-01A71E0F9CAE";
createNode angleBetween -n "legGlobal_L_guide_toe_rest_angle";
	rename -uid "DBBF67C9-43E3-DEE5-7F47-EEBF2925F82F";
createNode decomposeMatrix -n "legGlobal_L_guide_ankle_world_srt";
	rename -uid "8D9675C6-4033-D98A-39BA-968890A595C2";
createNode plusMinusAverage -n "legGlobal_L_guide_toe_direction_vec";
	rename -uid "D31DF879-4A3A-0197-5FF9-05A86D73C6F4";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "legGlobal_L_guide_tarsi_direction_vec";
	rename -uid "0E469812-4503-35E2-5EEE-BBB80B88CBA0";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode angleBetween -n "legGlobal_L_guide_tarsi2Toe_rest_angle";
	rename -uid "2C140304-48AB-94EE-248F-11A698C1C301";
createNode angleBetween -n "legGlobal_L_guide_tarsi2World_rest_angle";
	rename -uid "B66299D2-4A72-1048-9B85-368EA388101A";
createNode inverseMatrix -n "leg_L_guide_endWorldInverse_mtx";
	rename -uid "264CEB67-4CD4-398C-D9F7-51A0E2F835AE";
	setAttr ".omat" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 1.6653345369377348e-14 -11.841588736937647 2.2621914758103049e-11 1;
createNode multMatrix -n "leg_L_guide_ikHip_local_mtx";
	rename -uid "19E3DDFF-44FF-6238-E556-15ACEC593EA3";
	setAttr -s 2 ".i";
createNode multMatrix -n "leg_L_guide_globalAnkleInfk02Space";
	rename -uid "6AC3AFD2-472E-455C-12AE-30A5D4D944DE";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "leg_L_guide_globalAnkleInfk02Space_srt";
	rename -uid "081B7033-49F6-F601-3E9B-77B4576C0DE3";
createNode plusMinusAverage -n "leg_L_guide_hip2UpV_vec";
	rename -uid "856A7020-4CB5-6820-645D-66A38B41B575";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode decomposeMatrix -n "leg_L_guide_ankle_world_srt";
	rename -uid "B805C7EC-49F0-5B09-D404-3B961CF55703";
createNode distanceBetween -n "leg_L_guide_tibiaLength";
	rename -uid "0BEC7A44-4E36-FF2E-4D90-4A97FAE1A84B";
createNode decomposeMatrix -n "leg_L_guide_knee_world_srt";
	rename -uid "904C5C67-4518-2410-1AF4-989A6693A6B6";
createNode distanceBetween -n "leg_L_guide_femurLength";
	rename -uid "CEBB4E0C-4FDD-60B0-78E5-A581536D20D6";
createNode decomposeMatrix -n "leg_L_guide_hip_world_srt";
	rename -uid "69F577B3-41AC-15BB-B899-FA97726AA75B";
createNode decomposeMatrix -n "leg_L_guide_hipInput_srt";
	rename -uid "7AC8ADAD-4751-DE36-95C0-8A8E6795554D";
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
	setAttr ".o" -type "double3" 77.944508003938381 -4.7708320221952752e-15 -1.5902773407317584e-15 ;
createNode animBlendNodeAdditiveRotation -n "leg_R_fkik_j01_blended_rot";
	rename -uid "FF117057-4B49-E9C5-D856-41A7F04932D0";
	setAttr ".o" -type "double3" 57.285987229634486 13.97399045812613 -9.9428850465099092 ;
createNode decomposeMatrix -n "leg_R_fk01_ctrl_world_mtx";
	rename -uid "75A2E388-4823-3B4E-65E1-70A5CA2AEE7F";
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
	setAttr -s 3 ".i";
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
createNode decomposeMatrix -n "leg_R_FK_start_srt";
	rename -uid "6500E1E8-42B6-1B61-B7F4-45B0ED46E7C3";
	setAttr ".ro" 5;
createNode decomposeMatrix -n "leg_R_guide_upVector_srt";
	rename -uid "E60A7044-4C6D-3FC5-98EE-008F1B58F759";
createNode decomposeMatrix -n "leg_R_globalAnkle_srt";
	rename -uid "C5EF69D0-4754-BAFC-F174-0D839108152E";
createNode composeMatrix -n "leg_R_ankle_blend_mtx";
	rename -uid "D24019D5-4C9C-52A4-0FF3-5DBBC22B23F7";
	setAttr ".omat" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.2789999662764027 2.5447580120232667 -0.51870483510114651 1;
createNode decomposeMatrix -n "leg_R_j03_worldMtx";
	rename -uid "66EEECA4-48FD-C6FC-0005-62ACB8B5F09A";
createNode animBlendNodeAdditiveRotation -n "leg_R_ankle_rotBlend";
	rename -uid "A3972A5A-4EBE-8F62-29BA-AA93850B3A87";
	setAttr ".o" -type "double3" -3.1805546814635183e-15 -3.1805546814635168e-15 6.3611093629270335e-15 ;
createNode decomposeMatrix -n "leg_R_fk03_worldMtx";
	rename -uid "FDBD2D5C-4F98-7E28-DA2F-959C7314EB2C";
createNode multMatrix -n "leg_R_FK_start_mtx";
	rename -uid "F82AA626-4100-D2A1-D482-04883AF33621";
	setAttr -s 2 ".i";
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
createNode inverseMatrix -n "leg_R_guide_endWorldInverse_mtx";
	rename -uid "6D511D45-4B5F-0F51-4110-3DBFEFAAC315";
	setAttr ".omat" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 1.6653345369377348e-14 -11.841588736937647 2.2621914758103049e-11 1;
createNode multMatrix -n "leg_R_guide_ikHip_local_mtx";
	rename -uid "3D88E326-4D8B-A566-BFBC-70A4E14E8DE7";
	setAttr -s 2 ".i";
createNode multMatrix -n "leg_R_guide_globalAnkleInfk02Space";
	rename -uid "6D652101-48AC-F95B-6342-12A1A381B586";
	setAttr -s 2 ".i";
createNode decomposeMatrix -n "leg_R_guide_globalAnkleInfk02Space_srt";
	rename -uid "E0C862E6-46F0-F17F-FC8F-FE8FC828EE55";
	setAttr ".ro" 4;
createNode plusMinusAverage -n "leg_R_guide_hip2UpV_vec";
	rename -uid "B48437A9-4F8D-C7D0-C1E3-ACA565098E1F";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode decomposeMatrix -n "leg_R_guide_ankle_world_srt";
	rename -uid "B8D3491A-4377-CAA9-A8E9-3987642EC07F";
createNode distanceBetween -n "leg_R_guide_tibiaLength";
	rename -uid "A3FF7D37-4362-7E7E-85D6-2ABE533E0A86";
createNode decomposeMatrix -n "leg_R_guide_knee_world_srt";
	rename -uid "BFE26CE5-4B75-4B9A-F6FF-67A4DC3319F1";
createNode distanceBetween -n "leg_R_guide_femurLength";
	rename -uid "FD044778-44F4-5742-A7EF-D5974893EE22";
createNode decomposeMatrix -n "leg_R_guide_hip_world_srt";
	rename -uid "385012F3-4A24-2BCA-149A-FCB487F73F5A";
createNode decomposeMatrix -n "leg_R_guide_hipInput_srt";
	rename -uid "F770B47B-41BD-DB6A-7908-EBAE36AD8433";
createNode floatCondition -n "leg_R_handedNessSign";
	rename -uid "55E8FF85-44F6-A090-A9E0-3DBD0FA86892";
	setAttr "._fa" -1;
createNode multDoubleLinear -n "multDoubleLinear1";
	rename -uid "9CA75758-43B5-4DE9-E9AA-90AE358F27D5";
createNode animBlendNodeAdditiveDA -n "animBlendNodeAdditiveDA1";
	rename -uid "F22BF4EC-4E36-4170-2CA7-58A3727FDDDD";
	setAttr ".o" 17.066629620449635;
createNode angleBetween -n "legGlobal_R_guide_tarsi2Toe_rest_angle";
	rename -uid "B3A9470A-4649-A952-F0E5-0DB4CED496AA";
createNode angleBetween -n "legGlobal_R_guide_tarsi2World_rest_angle";
	rename -uid "FD06CACB-471E-CDC4-0325-7283C1819F2B";
createNode angleBetween -n "legGlobal_R_guide_toe_rest_angle";
	rename -uid "3157543D-4BAD-16DB-CE10-EF9FC836A8CD";
createNode angleBetween -n "legGlobal_R_tarsi_rolledAngle";
	rename -uid "F1E8376D-4BCB-613A-1D8F-AD9AB5886AA3";
createNode animBlendNodeAdditiveDA -n "legGlobal_R_guide_tarsi_rest_negate_angle";
	rename -uid "B6684D59-4169-A02A-6372-5FB8FE4438FA";
	setAttr ".wa" -1;
	setAttr ".o" -32.928389796476075;
createNode animBlendNodeAdditiveDA -n "legGlobal_R_tarsiRollOffset_angle";
	rename -uid "C6937C08-4750-DDAD-F1FE-079C6CD8C26C";
	setAttr ".wa" -1;
	setAttr ".o" -32.928389796476075;
createNode animBlendNodeAdditiveDA -n "legGlobal_R_toeRollOffset_angle";
	rename -uid "E67FB230-4956-4725-089D-5886EAB48A11";
	setAttr ".wa" -1;
	setAttr ".wb" -1;
	setAttr ".o" -21.065155320812835;
createNode animCurveUA -n "legGlobal_R_roll_tarsi_fCurve";
	rename -uid "DB159076-4C1C-91A2-9252-0D94EFAA717B";
	setAttr ".tan" 2;
	setAttr -s 3 ".ktv[0:2]"  0 0 40 38 81 -20;
createNode animCurveUA -n "legGlobal_R_roll_toe_fCurve";
	rename -uid "F304151A-4BD7-E9C9-1AC9-D9899365C1DF";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  40 0 140 140;
createNode clamp -n "legGlobal_R_heelBack_rollClamp";
	rename -uid "7F944938-4A50-9988-906F-8B85DAAB545C";
	setAttr ".mn" -type "float3" 0 0 -40 ;
createNode decomposeMatrix -n "legGlobal_R_ankleFramed_tarsi_srt";
	rename -uid "0E31B8C3-475F-A3D1-D1F0-7EBFCEDA5D8B";
createNode decomposeMatrix -n "legGlobal_R_ankleReparent_srt";
	rename -uid "BE80C836-4AF7-31EB-AADF-7A9225DAA46E";
createNode decomposeMatrix -n "legGlobal_R_guide_ankle_world_srt";
	rename -uid "A6765559-4F8E-FD0E-1377-ECB3A6E9333C";
createNode decomposeMatrix -n "legGlobal_R_roll_tarsi_world_mtx";
	rename -uid "C5911113-4243-898D-8F42-53882F4515D7";
createNode decomposeMatrix -n "legGlobal_R_roll_toes_world_mtx2srt";
	rename -uid "5EA64280-40E2-21FD-0ADF-428621B8500B";
createNode decomposeMatrix -n "legGlobal_R_upVecReparent_srt";
	rename -uid "2E500F4F-44E9-7AD9-75D5-F198360715E5";
createNode decomposeMatrix -n "legGlobal_R_worldAnkle_ctrl_world_srt";
	rename -uid "69E5C259-455A-13CE-D6ED-6F9142812243";
createNode distanceBetween -n "legGlobal_R_guide_tarsi_length";
	rename -uid "BEF93D78-448A-43DB-8A2D-3CA5FD18199F";
createNode distanceBetween -n "legGlobal_R_guide_toe_length";
	rename -uid "C8BEAC08-4532-5F72-DEAB-A2858AF497D7";
createNode multMatrix -n "legGlobal_R_ankleFramed_tarsi_mtx";
	rename -uid "27340748-4319-CC01-DEAD-09ABE4106BAC";
	setAttr -s 2 ".i";
createNode multMatrix -n "legGlobal_R_ankleReparent_mtxMult";
	rename -uid "F9140C02-4515-6F20-7059-3CB059A67BE2";
	setAttr -s 2 ".i";
createNode multMatrix -n "legGlobal_R_upVecReparent_mtxMult";
	rename -uid "3A32A1A1-4245-E168-5981-999DF4170E74";
	setAttr -s 2 ".i";
createNode plusMinusAverage -n "legGlobal_R_guide_tarsi_direction_vec";
	rename -uid "0E544700-44CF-72E1-0699-AFB531456117";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "legGlobal_R_guide_toe_direction_vec";
	rename -uid "03F94C08-4D6E-1D2F-0FEA-3C93A74A6C80";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode plusMinusAverage -n "legGlobal_R_tarsi_worldDirection_vec3";
	rename -uid "9E89B3D6-46F6-C6F1-B96C-5A8132EC159C";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode pointMatrixMult -n "legGlobal_R_ankleFramed_rollOffset_srt";
	rename -uid "8F339961-4967-D12A-02FA-98949E6519E4";
createNode unitConversion -n "legGlobal_R_roll_UC";
	rename -uid "92D1988B-4BF2-88DD-36A4-6187AF8EF7EB";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "legGlobal_R_heelback_roll_UC";
	rename -uid "67F238A3-4615-FE75-9B39-41A29DB3DA37";
	setAttr ".cf" 0.017453292519943295;
createNode container -n "legGlobal_R_container";
	rename -uid "3D1544BB-464A-A074-71A8-1292BBA0E4A3";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".isc" yes;
	setAttr -s 2 ".pni";
	setAttr ".ctor" -type "string" "Jaco";
	setAttr ".cdat" -type "string" "2018/02/16 08:10:51";
	setAttr ".aal" -type "attributeAlias" {"child","canBeChild[0]","parent","canBeParent[0]"
		,"legGlobal_L_worldAnkle_ctrl","publishedNodeInfo[0]","legGlobal_L_upVector_ctrl"
		,"publishedNodeInfo[1]"} ;
createNode hyperLayout -n "hyperLayout6";
	rename -uid "D71481EE-4E8B-49E8-4DAE-64B2212A78BC";
	setAttr ".ihi" 0;
	setAttr -s 65 ".hyp";
createNode animBlendNodeAdditiveDA -n "animBlendNodeAdditiveDA2";
	rename -uid "B484D72F-43F9-F915-0A4E-05B208642555";
	setAttr ".o" 0.95862059441954717;
createNode multMatrix -n "leg_R_unhandedFK01_mtx";
	rename -uid "DFA6218A-4E02-B483-4BC9-AC87A7091090";
	setAttr -s 2 ".i";
createNode composeMatrix -n "leg_R_handednessMatrix";
	rename -uid "3DDF1613-4ECA-80A9-22EE-CA86EC63DE0E";
	setAttr ".omat" -type "matrix" -1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode inverseMatrix -n "leg_R_unhandedFK01_inverse_mtx";
	rename -uid "E0F707D8-4B4A-D103-368A-42ACCBB4BAC8";
	setAttr ".omat" -type "matrix" 0.955830310499581 0.29344252320070202 -0.016730305074326008 0
		 -0.16755640722170151 0.49724691784750108 -0.85127572095656268 0 -0.2414814028641335 0.81647840649264292 0.52445185079471712 0
		 3.4353004943847139 -3.6020575199537812 6.9674456215786069 1;
createNode nodeGraphEditorBookmarkInfo -n "nodeView1";
	rename -uid "85106454-4573-6A88-3054-788AA89033C5";
	setAttr ".nm" -type "string" "leg_guide_addition";
	setAttr ".vl" -type "double2" -3269.4018873419773 -1161.9392382045116 ;
	setAttr ".vh" -type "double2" 2443.0932099175448 2218.4188812378761 ;
	setAttr -s 30 ".ni";
	setAttr ".ni[0].x" -345.71429443359375;
	setAttr ".ni[0].y" 270;
	setAttr ".ni[0].nvs" 18312;
	setAttr ".ni[1].x" -1117.142822265625;
	setAttr ".ni[1].y" 741.4285888671875;
	setAttr ".ni[1].nvs" 18312;
	setAttr ".ni[2].x" -2145.71435546875;
	setAttr ".ni[2].y" 441.42855834960938;
	setAttr ".ni[2].nvs" 18312;
	setAttr ".ni[3].x" -988.5714111328125;
	setAttr ".ni[3].y" 141.42857360839844;
	setAttr ".ni[3].nvs" 18312;
	setAttr ".ni[4].x" -45.714286804199219;
	setAttr ".ni[4].y" 527.14288330078125;
	setAttr ".ni[4].nvs" 18313;
	setAttr ".ni[5].x" -345.71429443359375;
	setAttr ".ni[5].y" 441.42855834960938;
	setAttr ".ni[5].nvs" 18312;
	setAttr ".ni[6].x" 254.28572082519531;
	setAttr ".ni[6].y" 612.85711669921875;
	setAttr ".ni[6].nvs" 18313;
	setAttr ".ni[7].x" -345.71429443359375;
	setAttr ".ni[7].y" 184.28572082519531;
	setAttr ".ni[7].nvs" 18313;
	setAttr ".ni[8].x" -45.714286804199219;
	setAttr ".ni[8].y" 612.85711669921875;
	setAttr ".ni[8].nvs" 18312;
	setAttr ".ni[9].x" -345.71429443359375;
	setAttr ".ni[9].y" 527.14288330078125;
	setAttr ".ni[9].nvs" 18312;
	setAttr ".ni[10].x" -731.4285888671875;
	setAttr ".ni[10].y" 312.85714721679688;
	setAttr ".ni[10].nvs" 18313;
	setAttr ".ni[11].x" -1331.4285888671875;
	setAttr ".ni[11].y" 1200;
	setAttr ".ni[11].nvs" 18305;
	setAttr ".ni[12].x" -1845.7142333984375;
	setAttr ".ni[12].y" 1500;
	setAttr ".ni[12].nvs" 18305;
	setAttr ".ni[13].x" -2145.71435546875;
	setAttr ".ni[13].y" 1212.857177734375;
	setAttr ".ni[13].nvs" 18312;
	setAttr ".ni[14].x" -388.57144165039063;
	setAttr ".ni[14].y" -244.28572082519531;
	setAttr ".ni[14].nvs" 18312;
	setAttr ".ni[15].x" 511.42855834960938;
	setAttr ".ni[15].y" 484.28570556640625;
	setAttr ".ni[15].nvs" 18313;
	setAttr ".ni[16].x" -1845.7142333984375;
	setAttr ".ni[16].y" 1298.5714111328125;
	setAttr ".ni[16].nvs" 18313;
	setAttr ".ni[17].x" 125.71428680419922;
	setAttr ".ni[17].y" -244.28572082519531;
	setAttr ".ni[17].nvs" 18313;
	setAttr ".ni[18].x" -1845.7142333984375;
	setAttr ".ni[18].y" 612.85711669921875;
	setAttr ".ni[18].nvs" 18313;
	setAttr ".ni[19].x" -1845.7142333984375;
	setAttr ".ni[19].y" 827.14288330078125;
	setAttr ".ni[19].nvs" 18313;
	setAttr ".ni[20].x" -1331.4285888671875;
	setAttr ".ni[20].y" 827.14288330078125;
	setAttr ".ni[20].nvs" 18313;
	setAttr ".ni[21].x" -1845.7142333984375;
	setAttr ".ni[21].y" 1084.2857666015625;
	setAttr ".ni[21].nvs" 18313;
	setAttr ".ni[22].x" 768.5714111328125;
	setAttr ".ni[22].y" 741.4285888671875;
	setAttr ".ni[22].nvs" 18313;
	setAttr ".ni[23].x" -1545.7142333984375;
	setAttr ".ni[23].y" 784.28570556640625;
	setAttr ".ni[23].nvs" 18313;
	setAttr ".ni[24].x" -2145.71435546875;
	setAttr ".ni[24].y" 955.71429443359375;
	setAttr ".ni[24].nvs" 18312;
	setAttr ".ni[25].x" 125.71428680419922;
	setAttr ".ni[25].y" -158.57142639160156;
	setAttr ".ni[25].nvs" 18312;
	setAttr ".ni[26].x" -388.57144165039063;
	setAttr ".ni[26].y" -372.85714721679688;
	setAttr ".ni[26].nvs" 18312;
	setAttr ".ni[27].x" -2145.71435546875;
	setAttr ".ni[27].y" 1084.2857666015625;
	setAttr ".ni[27].nvs" 18312;
	setAttr ".ni[28].x" -2145.71435546875;
	setAttr ".ni[28].y" 698.5714111328125;
	setAttr ".ni[28].nvs" 18313;
	setAttr ".ni[29].x" -131.42857360839844;
	setAttr ".ni[29].y" -72.857139587402344;
	setAttr ".ni[29].nvs" 18313;
createNode decomposeMatrix -n "foot_R_start_mtx2srt";
	rename -uid "F68D7833-4CDD-AAA2-CCC2-36A0FDAA1214";
createNode container -n "foot_R_container";
	rename -uid "AAF33ABC-453C-D1BF-5AE8-EB96E5E53796";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".isc" yes;
	setAttr -s 2 ".pni";
	setAttr ".ctor" -type "string" "Jaco";
	setAttr ".cdat" -type "string" "2018/03/17 08:15:34";
	setAttr ".aal" -type "attributeAlias" {"child","canBeChild[0]","parent","canBeParent[0]"
		,"foot_M_tarsii_ctrl","publishedNodeInfo[0]","foot_M_toes_ctrl","publishedNodeInfo[1]"
		} ;
createNode hyperLayout -n "hyperLayout7";
	rename -uid "57A4E988-4709-1614-9E74-EE866EFA4187";
	setAttr ".ihi" 0;
	setAttr -s 17 ".hyp";
createNode multMatrix -n "leg_R_unhandedFK03_mtx";
	rename -uid "ABA40A1D-4BDE-D673-C8C4-C4BE72525A1E";
	setAttr -s 2 ".i";
createNode nodeGraphEditorBookmarks -n "MayaNodeEditorBookmarks";
	rename -uid "26A481D3-40BD-6E59-6E33-A99B807CA0A1";
createNode nodeGraphEditorBookmarkInfo -n "nodeView2";
	rename -uid "1C3D67CF-48A1-6063-9A55-5D9530836507";
	setAttr ".nm" -type "string" "leg2foot_001";
	setAttr ".vl" -type "double2" -3799.1393817789362 -1303.104116977544 ;
	setAttr ".vh" -type "double2" 3521.8114750901068 1499.69621107176 ;
	setAttr -s 38 ".ni";
	setAttr ".ni[0].x" -411.42855834960938;
	setAttr ".ni[0].y" 392.85714721679688;
	setAttr ".ni[0].nvs" 18313;
	setAttr ".ni[1].x" -454.28570556640625;
	setAttr ".ni[1].y" 7.1428570747375488;
	setAttr ".ni[1].nvs" 18312;
	setAttr ".ni[2].x" 145.71427917480469;
	setAttr ".ni[2].y" 92.857139587402344;
	setAttr ".ni[2].nvs" 18313;
	setAttr ".ni[3].x" -154.28572082519531;
	setAttr ".ni[3].y" 478.57144165039063;
	setAttr ".ni[3].nvs" 18312;
	setAttr ".ni[4].x" -1268.5714111328125;
	setAttr ".ni[4].y" 564.28570556640625;
	setAttr ".ni[4].nvs" 18312;
	setAttr ".ni[5].x" -1825.7142333984375;
	setAttr ".ni[5].y" 864.28570556640625;
	setAttr ".ni[5].nvs" 18313;
	setAttr ".ni[6].x" 445.71429443359375;
	setAttr ".ni[6].y" 650;
	setAttr ".ni[6].nvs" 18313;
	setAttr ".ni[7].x" -2125.71435546875;
	setAttr ".ni[7].y" 735.71429443359375;
	setAttr ".ni[7].nvs" 18313;
	setAttr ".ni[8].x" 568.5714111328125;
	setAttr ".ni[8].y" 398.57144165039063;
	setAttr ".ni[8].nvs" 18313;
	setAttr ".ni[9].x" -154.28572082519531;
	setAttr ".ni[9].y" 564.28570556640625;
	setAttr ".ni[9].nvs" 18312;
	setAttr ".ni[10].x" -2125.71435546875;
	setAttr ".ni[10].y" 478.57144165039063;
	setAttr ".ni[10].nvs" 18312;
	setAttr ".ni[11].x" -1054.2857666015625;
	setAttr ".ni[11].y" 178.57142639160156;
	setAttr ".ni[11].nvs" 18312;
	setAttr ".ni[12].x" -154.28572082519531;
	setAttr ".ni[12].y" 264.28570556640625;
	setAttr ".ni[12].nvs" 18312;
	setAttr ".ni[13].x" 825.71429443359375;
	setAttr ".ni[13].y" 784.28570556640625;
	setAttr ".ni[13].nvs" 18313;
	setAttr ".ni[14].x" -1525.7142333984375;
	setAttr ".ni[14].y" 821.4285888671875;
	setAttr ".ni[14].nvs" 18313;
	setAttr ".ni[15].x" -1825.7142333984375;
	setAttr ".ni[15].y" 650;
	setAttr ".ni[15].nvs" 18313;
	setAttr ".ni[16].x" -797.14288330078125;
	setAttr ".ni[16].y" 392.85714721679688;
	setAttr ".ni[16].nvs" 18313;
	setAttr ".ni[17].x" -454.28570556640625;
	setAttr ".ni[17].y" -121.42857360839844;
	setAttr ".ni[17].nvs" 18312;
	setAttr ".ni[18].x" -1011.4285888671875;
	setAttr ".ni[18].y" 564.28570556640625;
	setAttr ".ni[18].nvs" 18312;
	setAttr ".ni[19].x" 145.71427917480469;
	setAttr ".ni[19].y" 650;
	setAttr ".ni[19].nvs" 18312;
	setAttr ".ni[20].x" 145.71427917480469;
	setAttr ".ni[20].y" 564.28570556640625;
	setAttr ".ni[20].nvs" 18313;
	setAttr ".ni[21].x" -154.28572082519531;
	setAttr ".ni[21].y" 178.57142639160156;
	setAttr ".ni[21].nvs" 18313;
	setAttr ".ni[22].x" 145.71427917480469;
	setAttr ".ni[22].y" 178.57142639160156;
	setAttr ".ni[22].nvs" 18312;
	setAttr ".ni[23].x" 440;
	setAttr ".ni[23].y" -201.42857360839844;
	setAttr ".ni[23].nvs" 18313;
	setAttr ".ni[24].x" 440;
	setAttr ".ni[24].y" -415.71429443359375;
	setAttr ".ni[24].nvs" 18313;
	setAttr ".ni[25].x" -117.14286041259766;
	setAttr ".ni[25].y" -330;
	setAttr ".ni[25].nvs" 18312;
	setAttr ".ni[26].x" 140;
	setAttr ".ni[26].y" -158.57142639160156;
	setAttr ".ni[26].nvs" 18314;
	setAttr ".ni[27].x" 1425.7142333984375;
	setAttr ".ni[27].y" -158.57142639160156;
	setAttr ".ni[27].nvs" 18313;
	setAttr ".ni[28].x" 1125.7142333984375;
	setAttr ".ni[28].y" -115.71428680419922;
	setAttr ".ni[28].nvs" 18313;
	setAttr ".ni[29].x" 2154.28564453125;
	setAttr ".ni[29].y" 184.28572082519531;
	setAttr ".ni[29].nvs" 18313;
	setAttr ".ni[30].x" 2111.428466796875;
	setAttr ".ni[30].y" -30;
	setAttr ".ni[30].nvs" 18313;
	setAttr ".ni[31].x" 1682.857177734375;
	setAttr ".ni[31].y" -158.57142639160156;
	setAttr ".ni[31].nvs" 18313;
	setAttr ".ni[32].x" 2111.428466796875;
	setAttr ".ni[32].y" -201.42857360839844;
	setAttr ".ni[32].nvs" 18312;
	setAttr ".ni[33].x" 2111.428466796875;
	setAttr ".ni[33].y" -287.14285278320313;
	setAttr ".ni[33].nvs" 18313;
	setAttr ".ni[34].x" 1940;
	setAttr ".ni[34].y" 184.28572082519531;
	setAttr ".ni[34].nvs" 18313;
	setAttr ".ni[35].x" 2111.428466796875;
	setAttr ".ni[35].y" -458.57144165039063;
	setAttr ".ni[35].nvs" 18312;
	setAttr ".ni[36].x" 782.85711669921875;
	setAttr ".ni[36].y" 12.857142448425293;
	setAttr ".ni[36].nvs" 18313;
	setAttr ".ni[37].x" 782.85711669921875;
	setAttr ".ni[37].y" -244.28572082519531;
	setAttr ".ni[37].nvs" 18313;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "24703782-42D9-1F6C-8994-34ACBD55969A";
	setAttr -s 8 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "wholeLeg";
	setAttr ".tgi[0].vl" -type "double2" -17662.828804944966 -8186.9044365864147 ;
	setAttr ".tgi[0].vh" -type "double2" 16234.257433139861 4790.4760001197728 ;
	setAttr -s 137 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -8078.4169921875;
	setAttr ".tgi[0].ni[0].y" -1602.5159912109375;
	setAttr ".tgi[0].ni[0].nvs" 18312;
	setAttr ".tgi[0].ni[1].x" -4543.71240234375;
	setAttr ".tgi[0].ni[1].y" -769.58367919921875;
	setAttr ".tgi[0].ni[1].nvs" 18312;
	setAttr ".tgi[0].ni[2].x" -9848.9736328125;
	setAttr ".tgi[0].ni[2].y" -1439.05029296875;
	setAttr ".tgi[0].ni[2].nvs" 18312;
	setAttr ".tgi[0].ni[3].x" -9898.9169921875;
	setAttr ".tgi[0].ni[3].y" -691.2335205078125;
	setAttr ".tgi[0].ni[3].nvs" 18312;
	setAttr ".tgi[0].ni[4].x" -5883.68115234375;
	setAttr ".tgi[0].ni[4].y" -2066.437744140625;
	setAttr ".tgi[0].ni[4].nvs" 18312;
	setAttr ".tgi[0].ni[5].x" -5632.8173828125;
	setAttr ".tgi[0].ni[5].y" -753.28009033203125;
	setAttr ".tgi[0].ni[5].nvs" 18312;
	setAttr ".tgi[0].ni[6].x" -3015.8037109375;
	setAttr ".tgi[0].ni[6].y" -524.63604736328125;
	setAttr ".tgi[0].ni[6].nvs" 18312;
	setAttr ".tgi[0].ni[7].x" -5608.55712890625;
	setAttr ".tgi[0].ni[7].y" -2309.990478515625;
	setAttr ".tgi[0].ni[7].nvs" 18312;
	setAttr ".tgi[0].ni[8].x" -8117.9375;
	setAttr ".tgi[0].ni[8].y" -211.45658874511719;
	setAttr ".tgi[0].ni[8].nvs" 18312;
	setAttr ".tgi[0].ni[9].x" -7514.720703125;
	setAttr ".tgi[0].ni[9].y" -880.32269287109375;
	setAttr ".tgi[0].ni[9].nvs" 18312;
	setAttr ".tgi[0].ni[10].x" -5608.55712890625;
	setAttr ".tgi[0].ni[10].y" -2532.847412109375;
	setAttr ".tgi[0].ni[10].nvs" 18312;
	setAttr ".tgi[0].ni[11].x" -9519.26953125;
	setAttr ".tgi[0].ni[11].y" -1193.0020751953125;
	setAttr ".tgi[0].ni[11].nvs" 18312;
	setAttr ".tgi[0].ni[12].x" -5291.642578125;
	setAttr ".tgi[0].ni[12].y" -2601.214599609375;
	setAttr ".tgi[0].ni[12].nvs" 18312;
	setAttr ".tgi[0].ni[13].x" -76.354240417480469;
	setAttr ".tgi[0].ni[13].y" -671.159912109375;
	setAttr ".tgi[0].ni[13].nvs" 18312;
	setAttr ".tgi[0].ni[14].x" 562.0626220703125;
	setAttr ".tgi[0].ni[14].y" -1028.8543701171875;
	setAttr ".tgi[0].ni[14].nvs" 18312;
	setAttr ".tgi[0].ni[15].x" -7056.5537109375;
	setAttr ".tgi[0].ni[15].y" -1337.6885986328125;
	setAttr ".tgi[0].ni[15].nvs" 18312;
	setAttr ".tgi[0].ni[16].x" -7336.0625;
	setAttr ".tgi[0].ni[16].y" -523.00628662109375;
	setAttr ".tgi[0].ni[16].nvs" 18312;
	setAttr ".tgi[0].ni[17].x" -8570.9765625;
	setAttr ".tgi[0].ni[17].y" -402.114501953125;
	setAttr ".tgi[0].ni[17].nvs" 18312;
	setAttr ".tgi[0].ni[18].x" -1496.220703125;
	setAttr ".tgi[0].ni[18].y" -804.78253173828125;
	setAttr ".tgi[0].ni[18].nvs" 18312;
	setAttr ".tgi[0].ni[19].x" -2292.238037109375;
	setAttr ".tgi[0].ni[19].y" -640.76385498046875;
	setAttr ".tgi[0].ni[19].nvs" 18312;
	setAttr ".tgi[0].ni[20].x" -4989.51416015625;
	setAttr ".tgi[0].ni[20].y" -2186.2333984375;
	setAttr ".tgi[0].ni[20].nvs" 18312;
	setAttr ".tgi[0].ni[21].x" -7979.232421875;
	setAttr ".tgi[0].ni[21].y" -362.21389770507813;
	setAttr ".tgi[0].ni[21].nvs" 18312;
	setAttr ".tgi[0].ni[22].x" -4271.71142578125;
	setAttr ".tgi[0].ni[22].y" -796.7247314453125;
	setAttr ".tgi[0].ni[22].nvs" 18312;
	setAttr ".tgi[0].ni[23].x" -312.75311279296875;
	setAttr ".tgi[0].ni[23].y" -1021.129638671875;
	setAttr ".tgi[0].ni[23].nvs" 18312;
	setAttr ".tgi[0].ni[24].x" -9953.2392578125;
	setAttr ".tgi[0].ni[24].y" -297.43670654296875;
	setAttr ".tgi[0].ni[24].nvs" 18312;
	setAttr ".tgi[0].ni[25].x" -1199.75927734375;
	setAttr ".tgi[0].ni[25].y" -915.1937255859375;
	setAttr ".tgi[0].ni[25].nvs" 18312;
	setAttr ".tgi[0].ni[26].x" -601.9510498046875;
	setAttr ".tgi[0].ni[26].y" -998.0311279296875;
	setAttr ".tgi[0].ni[26].nvs" 18312;
	setAttr ".tgi[0].ni[27].x" -670.4638671875;
	setAttr ".tgi[0].ni[27].y" -912.91827392578125;
	setAttr ".tgi[0].ni[27].nvs" 18312;
	setAttr ".tgi[0].ni[28].x" 799.12030029296875;
	setAttr ".tgi[0].ni[28].y" -959.5562744140625;
	setAttr ".tgi[0].ni[28].nvs" 18312;
	setAttr ".tgi[0].ni[29].x" 1589.138427734375;
	setAttr ".tgi[0].ni[29].y" -1045.8658447265625;
	setAttr ".tgi[0].ni[29].nvs" 18312;
	setAttr ".tgi[0].ni[30].x" -8238.287109375;
	setAttr ".tgi[0].ni[30].y" -362.21389770507813;
	setAttr ".tgi[0].ni[30].nvs" 18312;
	setAttr ".tgi[0].ni[31].x" -4991.05322265625;
	setAttr ".tgi[0].ni[31].y" -2461.436767578125;
	setAttr ".tgi[0].ni[31].nvs" 18312;
	setAttr ".tgi[0].ni[32].x" 2185.6171875;
	setAttr ".tgi[0].ni[32].y" -1038.1419677734375;
	setAttr ".tgi[0].ni[32].nvs" 18312;
	setAttr ".tgi[0].ni[33].x" -7256.54150390625;
	setAttr ".tgi[0].ni[33].y" -1097.672119140625;
	setAttr ".tgi[0].ni[33].nvs" 18312;
	setAttr ".tgi[0].ni[34].x" -7854.927734375;
	setAttr ".tgi[0].ni[34].y" -1640.9664306640625;
	setAttr ".tgi[0].ni[34].nvs" 18312;
	setAttr ".tgi[0].ni[35].x" -4031.529296875;
	setAttr ".tgi[0].ni[35].y" -729.0382080078125;
	setAttr ".tgi[0].ni[35].nvs" 18312;
	setAttr ".tgi[0].ni[36].x" -4405.59423828125;
	setAttr ".tgi[0].ni[36].y" -2325.015625;
	setAttr ".tgi[0].ni[36].nvs" 18312;
	setAttr ".tgi[0].ni[37].x" -5293.45166015625;
	setAttr ".tgi[0].ni[37].y" -2166.519775390625;
	setAttr ".tgi[0].ni[37].nvs" 18312;
	setAttr ".tgi[0].ni[38].x" -6987.67919921875;
	setAttr ".tgi[0].ni[38].y" -692.7315673828125;
	setAttr ".tgi[0].ni[38].nvs" 18312;
	setAttr ".tgi[0].ni[39].x" -9898.9169921875;
	setAttr ".tgi[0].ni[39].y" -889.584716796875;
	setAttr ".tgi[0].ni[39].nvs" 18312;
	setAttr ".tgi[0].ni[40].x" 2261.232421875;
	setAttr ".tgi[0].ni[40].y" -1135.0823974609375;
	setAttr ".tgi[0].ni[40].nvs" 18312;
	setAttr ".tgi[0].ni[41].x" -8802.02734375;
	setAttr ".tgi[0].ni[41].y" -1585.4764404296875;
	setAttr ".tgi[0].ni[41].nvs" 18312;
	setAttr ".tgi[0].ni[42].x" -8150.0498046875;
	setAttr ".tgi[0].ni[42].y" 98.738182067871094;
	setAttr ".tgi[0].ni[42].nvs" 18312;
	setAttr ".tgi[0].ni[43].x" -4714.990234375;
	setAttr ".tgi[0].ni[43].y" -2187.7744140625;
	setAttr ".tgi[0].ni[43].nvs" 18312;
	setAttr ".tgi[0].ni[44].x" -718.76678466796875;
	setAttr ".tgi[0].ni[44].y" -839.19439697265625;
	setAttr ".tgi[0].ni[44].nvs" 18312;
	setAttr ".tgi[0].ni[45].x" -353.15109252929688;
	setAttr ".tgi[0].ni[45].y" -804.27532958984375;
	setAttr ".tgi[0].ni[45].nvs" 18312;
	setAttr ".tgi[0].ni[46].x" -5855.84375;
	setAttr ".tgi[0].ni[46].y" -2465.9814453125;
	setAttr ".tgi[0].ni[46].nvs" 18305;
	setAttr ".tgi[0].ni[47].x" -543.28131103515625;
	setAttr ".tgi[0].ni[47].y" -1078.2364501953125;
	setAttr ".tgi[0].ni[47].nvs" 18312;
	setAttr ".tgi[0].ni[48].x" -7773.775390625;
	setAttr ".tgi[0].ni[48].y" -880.32269287109375;
	setAttr ".tgi[0].ni[48].nvs" 18312;
	setAttr ".tgi[0].ni[49].x" -9501.8837890625;
	setAttr ".tgi[0].ni[49].y" -947.91119384765625;
	setAttr ".tgi[0].ni[49].nvs" 18312;
	setAttr ".tgi[0].ni[50].x" -8577.5732421875;
	setAttr ".tgi[0].ni[50].y" -779.9840087890625;
	setAttr ".tgi[0].ni[50].nvs" 18312;
	setAttr ".tgi[0].ni[51].x" -81.336387634277344;
	setAttr ".tgi[0].ni[51].y" -806.85894775390625;
	setAttr ".tgi[0].ni[51].nvs" 18312;
	setAttr ".tgi[0].ni[52].x" 538.54888916015625;
	setAttr ".tgi[0].ni[52].y" -835.18426513671875;
	setAttr ".tgi[0].ni[52].nvs" 18312;
	setAttr ".tgi[0].ni[53].x" -7181.00830078125;
	setAttr ".tgi[0].ni[53].y" -1172.8489990234375;
	setAttr ".tgi[0].ni[53].nvs" 18312;
	setAttr ".tgi[0].ni[54].x" -8596.169921875;
	setAttr ".tgi[0].ni[54].y" -1169.5584716796875;
	setAttr ".tgi[0].ni[54].nvs" 18312;
	setAttr ".tgi[0].ni[55].x" -9036.3974609375;
	setAttr ".tgi[0].ni[55].y" -1558.3602294921875;
	setAttr ".tgi[0].ni[55].nvs" 18312;
	setAttr ".tgi[0].ni[56].x" -8577.7373046875;
	setAttr ".tgi[0].ni[56].y" -308.61642456054688;
	setAttr ".tgi[0].ni[56].nvs" 18312;
	setAttr ".tgi[0].ni[57].x" -746.84210205078125;
	setAttr ".tgi[0].ni[57].y" -751.2593994140625;
	setAttr ".tgi[0].ni[57].nvs" 18312;
	setAttr ".tgi[0].ni[58].x" -9846.578125;
	setAttr ".tgi[0].ni[58].y" -1306.1279296875;
	setAttr ".tgi[0].ni[58].nvs" 18312;
	setAttr ".tgi[0].ni[59].x" -7626.11181640625;
	setAttr ".tgi[0].ni[59].y" -1674.1461181640625;
	setAttr ".tgi[0].ni[59].nvs" 18312;
	setAttr ".tgi[0].ni[60].x" -8575.94140625;
	setAttr ".tgi[0].ni[60].y" -1633.5867919921875;
	setAttr ".tgi[0].ni[60].nvs" 18312;
	setAttr ".tgi[0].ni[61].x" -4709.4775390625;
	setAttr ".tgi[0].ni[61].y" -2324.571533203125;
	setAttr ".tgi[0].ni[61].nvs" 18936;
	setAttr ".tgi[0].ni[62].x" -1791.9951171875;
	setAttr ".tgi[0].ni[62].y" -783.6904296875;
	setAttr ".tgi[0].ni[62].nvs" 18312;
	setAttr ".tgi[0].ni[63].x" -6478.50341796875;
	setAttr ".tgi[0].ni[63].y" -969.65179443359375;
	setAttr ".tgi[0].ni[63].nvs" 18312;
	setAttr ".tgi[0].ni[64].x" -9236.8291015625;
	setAttr ".tgi[0].ni[64].y" -1019.781982421875;
	setAttr ".tgi[0].ni[64].nvs" 18312;
	setAttr ".tgi[0].ni[65].x" -8238.287109375;
	setAttr ".tgi[0].ni[65].y" -442.61007690429688;
	setAttr ".tgi[0].ni[65].nvs" 18312;
	setAttr ".tgi[0].ni[66].x" -2533.426513671875;
	setAttr ".tgi[0].ni[66].y" -676.4954833984375;
	setAttr ".tgi[0].ni[66].nvs" 18312;
	setAttr ".tgi[0].ni[67].x" -70.607040405273438;
	setAttr ".tgi[0].ni[67].y" -1080.9964599609375;
	setAttr ".tgi[0].ni[67].nvs" 18312;
	setAttr ".tgi[0].ni[68].x" -3259.354736328125;
	setAttr ".tgi[0].ni[68].y" -554.84112548828125;
	setAttr ".tgi[0].ni[68].nvs" 18312;
	setAttr ".tgi[0].ni[69].x" -1249.1724853515625;
	setAttr ".tgi[0].ni[69].y" -837.17803955078125;
	setAttr ".tgi[0].ni[69].nvs" 18312;
	setAttr ".tgi[0].ni[70].x" -7134.65478515625;
	setAttr ".tgi[0].ni[70].y" -1265.6070556640625;
	setAttr ".tgi[0].ni[70].nvs" 18312;
	setAttr ".tgi[0].ni[71].x" -8086.39794921875;
	setAttr ".tgi[0].ni[71].y" -1080.6304931640625;
	setAttr ".tgi[0].ni[71].nvs" 18312;
	setAttr ".tgi[0].ni[72].x" -8979.1826171875;
	setAttr ".tgi[0].ni[72].y" -1165.702880859375;
	setAttr ".tgi[0].ni[72].nvs" 18312;
	setAttr ".tgi[0].ni[73].x" -1082.829833984375;
	setAttr ".tgi[0].ni[73].y" -963.5560302734375;
	setAttr ".tgi[0].ni[73].nvs" 18312;
	setAttr ".tgi[0].ni[74].x" -8845.724609375;
	setAttr ".tgi[0].ni[74].y" -308.61642456054688;
	setAttr ".tgi[0].ni[74].nvs" 18312;
	setAttr ".tgi[0].ni[75].x" -5945.1689453125;
	setAttr ".tgi[0].ni[75].y" -744.9273681640625;
	setAttr ".tgi[0].ni[75].nvs" 18312;
	setAttr ".tgi[0].ni[76].x" -5263.533203125;
	setAttr ".tgi[0].ni[76].y" -985.8724365234375;
	setAttr ".tgi[0].ni[76].nvs" 18312;
	setAttr ".tgi[0].ni[77].x" 2609.6669921875;
	setAttr ".tgi[0].ni[77].y" -1203.943115234375;
	setAttr ".tgi[0].ni[77].nvs" 18312;
	setAttr ".tgi[0].ni[78].x" -4987.0625;
	setAttr ".tgi[0].ni[78].y" -2269.23974609375;
	setAttr ".tgi[0].ni[78].nvs" 18312;
	setAttr ".tgi[0].ni[79].x" -3161.90234375;
	setAttr ".tgi[0].ni[79].y" -890.49859619140625;
	setAttr ".tgi[0].ni[79].nvs" 18312;
	setAttr ".tgi[0].ni[80].x" -4986.38916015625;
	setAttr ".tgi[0].ni[80].y" -1133.0675048828125;
	setAttr ".tgi[0].ni[80].nvs" 18312;
	setAttr ".tgi[0].ni[81].x" 2484.9296875;
	setAttr ".tgi[0].ni[81].y" -1135.979736328125;
	setAttr ".tgi[0].ni[81].nvs" 18312;
	setAttr ".tgi[0].ni[82].x" -8228.322265625;
	setAttr ".tgi[0].ni[82].y" -542.935302734375;
	setAttr ".tgi[0].ni[82].nvs" 18312;
	setAttr ".tgi[0].ni[83].x" 1307.2757568359375;
	setAttr ".tgi[0].ni[83].y" -964.7872314453125;
	setAttr ".tgi[0].ni[83].nvs" 18312;
	setAttr ".tgi[0].ni[84].x" -8589.5517578125;
	setAttr ".tgi[0].ni[84].y" -976.1368408203125;
	setAttr ".tgi[0].ni[84].nvs" 18312;
	setAttr ".tgi[0].ni[85].x" -9519.896484375;
	setAttr ".tgi[0].ni[85].y" -1369.886962890625;
	setAttr ".tgi[0].ni[85].nvs" 18312;
	setAttr ".tgi[0].ni[86].x" -5270.1044921875;
	setAttr ".tgi[0].ni[86].y" -666.1173095703125;
	setAttr ".tgi[0].ni[86].nvs" 18312;
	setAttr ".tgi[0].ni[87].x" -7965.2822265625;
	setAttr ".tgi[0].ni[87].y" -603.5430908203125;
	setAttr ".tgi[0].ni[87].nvs" 18312;
	setAttr ".tgi[0].ni[88].x" -7633.80322265625;
	setAttr ".tgi[0].ni[88].y" -601.5501708984375;
	setAttr ".tgi[0].ni[88].nvs" 18312;
	setAttr ".tgi[0].ni[89].x" -7392.8779296875;
	setAttr ".tgi[0].ni[89].y" -1699.0902099609375;
	setAttr ".tgi[0].ni[89].nvs" 18312;
	setAttr ".tgi[0].ni[90].x" -9913.4013671875;
	setAttr ".tgi[0].ni[90].y" -410.9234619140625;
	setAttr ".tgi[0].ni[90].nvs" 18312;
	setAttr ".tgi[0].ni[91].x" -4835.81591796875;
	setAttr ".tgi[0].ni[91].y" -1001.673828125;
	setAttr ".tgi[0].ni[91].nvs" 18312;
	setAttr ".tgi[0].ni[92].x" -7564.7470703125;
	setAttr ".tgi[0].ni[92].y" -701.5654296875;
	setAttr ".tgi[0].ni[92].nvs" 18312;
	setAttr ".tgi[0].ni[93].x" -4838.33984375;
	setAttr ".tgi[0].ni[93].y" -753.64862060546875;
	setAttr ".tgi[0].ni[93].nvs" 18312;
	setAttr ".tgi[0].ni[94].x" -3496.999755859375;
	setAttr ".tgi[0].ni[94].y" -694.21343994140625;
	setAttr ".tgi[0].ni[94].nvs" 18312;
	setAttr ".tgi[0].ni[95].x" -7515.96533203125;
	setAttr ".tgi[0].ni[95].y" -1058.0289306640625;
	setAttr ".tgi[0].ni[95].nvs" 18312;
	setAttr ".tgi[0].ni[96].x" -2051.04931640625;
	setAttr ".tgi[0].ni[96].y" -837.287841796875;
	setAttr ".tgi[0].ni[96].nvs" 18312;
	setAttr ".tgi[0].ni[97].x" 438.29196166992188;
	setAttr ".tgi[0].ni[97].y" -685.9176025390625;
	setAttr ".tgi[0].ni[97].nvs" 18312;
	setAttr ".tgi[0].ni[98].x" -7768.646484375;
	setAttr ".tgi[0].ni[98].y" -1011.1056518554688;
	setAttr ".tgi[0].ni[98].nvs" 18312;
	setAttr ".tgi[0].ni[99].x" -7268.7001953125;
	setAttr ".tgi[0].ni[99].y" -694.37969970703125;
	setAttr ".tgi[0].ni[99].nvs" 18312;
	setAttr ".tgi[0].ni[100].x" -6478.50341796875;
	setAttr ".tgi[0].ni[100].y" -1085.7796630859375;
	setAttr ".tgi[0].ni[100].nvs" 18312;
	setAttr ".tgi[0].ni[101].x" -7487.6845703125;
	setAttr ".tgi[0].ni[101].y" -1266.96142578125;
	setAttr ".tgi[0].ni[101].nvs" 18312;
	setAttr ".tgi[0].ni[102].x" -4285.9853515625;
	setAttr ".tgi[0].ni[102].y" -698.2950439453125;
	setAttr ".tgi[0].ni[102].nvs" 18312;
	setAttr ".tgi[0].ni[103].x" -775.98065185546875;
	setAttr ".tgi[0].ni[103].y" -660.9757080078125;
	setAttr ".tgi[0].ni[103].nvs" 18312;
	setAttr ".tgi[0].ni[104].x" 2280.759033203125;
	setAttr ".tgi[0].ni[104].y" -955.23809814453125;
	setAttr ".tgi[0].ni[104].nvs" 18312;
	setAttr ".tgi[0].ni[105].x" -1052.759033203125;
	setAttr ".tgi[0].ni[105].y" -1125.654541015625;
	setAttr ".tgi[0].ni[105].nvs" 18312;
	setAttr ".tgi[0].ni[106].x" -8307.9541015625;
	setAttr ".tgi[0].ni[106].y" -1571.0565185546875;
	setAttr ".tgi[0].ni[106].nvs" 18312;
	setAttr ".tgi[0].ni[107].x" -5629.0048828125;
	setAttr ".tgi[0].ni[107].y" -2131.474609375;
	setAttr ".tgi[0].ni[107].nvs" 18312;
	setAttr ".tgi[0].ni[108].x" 237.77378845214844;
	setAttr ".tgi[0].ni[108].y" -775.43768310546875;
	setAttr ".tgi[0].ni[108].nvs" 18312;
	setAttr ".tgi[0].ni[109].x" -7738.78369140625;
	setAttr ".tgi[0].ni[109].y" -1228.60009765625;
	setAttr ".tgi[0].ni[109].nvs" 18312;
	setAttr ".tgi[0].ni[110].x" -2783.548095703125;
	setAttr ".tgi[0].ni[110].y" -640.76385498046875;
	setAttr ".tgi[0].ni[110].nvs" 18312;
	setAttr ".tgi[0].ni[111].x" 795.654541015625;
	setAttr ".tgi[0].ni[111].y" -885.43182373046875;
	setAttr ".tgi[0].ni[111].nvs" 18312;
	setAttr ".tgi[0].ni[112].x" -4293.2099609375;
	setAttr ".tgi[0].ni[112].y" -524.63604736328125;
	setAttr ".tgi[0].ni[112].nvs" 18312;
	setAttr ".tgi[0].ni[113].x" 2426.903076171875;
	setAttr ".tgi[0].ni[113].y" -1039.646728515625;
	setAttr ".tgi[0].ni[113].nvs" 18312;
	setAttr ".tgi[0].ni[114].x" -8582.3642578125;
	setAttr ".tgi[0].ni[114].y" -593.41363525390625;
	setAttr ".tgi[0].ni[114].nvs" 18312;
	setAttr ".tgi[0].ni[115].x" 189.11207580566406;
	setAttr ".tgi[0].ni[115].y" -637.365966796875;
	setAttr ".tgi[0].ni[115].nvs" 18312;
	setAttr ".tgi[0].ni[116].x" -7979.232421875;
	setAttr ".tgi[0].ni[116].y" -496.20751953125;
	setAttr ".tgi[0].ni[116].nvs" 18312;
	setAttr ".tgi[0].ni[117].x" -76.354240417480469;
	setAttr ".tgi[0].ni[117].y" -581.830810546875;
	setAttr ".tgi[0].ni[117].nvs" 18312;
	setAttr ".tgi[0].ni[118].x" 1046.4547119140625;
	setAttr ".tgi[0].ni[118].y" -942.46063232421875;
	setAttr ".tgi[0].ni[118].nvs" 18312;
	setAttr ".tgi[0].ni[119].x" -5628.73876953125;
	setAttr ".tgi[0].ni[119].y" -1984.2183837890625;
	setAttr ".tgi[0].ni[119].nvs" 18312;
	setAttr ".tgi[0].ni[120].x" -3761.83349609375;
	setAttr ".tgi[0].ni[120].y" -623.95269775390625;
	setAttr ".tgi[0].ni[120].nvs" 18312;
	setAttr ".tgi[0].ni[121].x" -4561.23583984375;
	setAttr ".tgi[0].ni[121].y" -964.45086669921875;
	setAttr ".tgi[0].ni[121].nvs" 18312;
	setAttr ".tgi[0].ni[122].x" -7639.78173828125;
	setAttr ".tgi[0].ni[122].y" -496.20751953125;
	setAttr ".tgi[0].ni[122].nvs" 18312;
	setAttr ".tgi[0].ni[123].x" 2127.74169921875;
	setAttr ".tgi[0].ni[123].y" -893.91229248046875;
	setAttr ".tgi[0].ni[123].nvs" 18312;
	setAttr ".tgi[0].ni[124].x" -4440.9072265625;
	setAttr ".tgi[0].ni[124].y" -2191.058349609375;
	setAttr ".tgi[0].ni[124].nvs" 18312;
	setAttr ".tgi[0].ni[125].x" -6728.625;
	setAttr ".tgi[0].ni[125].y" -880.32269287109375;
	setAttr ".tgi[0].ni[125].nvs" 18312;
	setAttr ".tgi[0].ni[126].x" -9255.7646484375;
	setAttr ".tgi[0].ni[126].y" -1523.4044189453125;
	setAttr ".tgi[0].ni[126].nvs" 18312;
	setAttr ".tgi[0].ni[127].x" -7237.80078125;
	setAttr ".tgi[0].ni[127].y" -835.65814208984375;
	setAttr ".tgi[0].ni[127].nvs" 18312;
	setAttr ".tgi[0].ni[128].x" -4025.22265625;
	setAttr ".tgi[0].ni[128].y" -551.43475341796875;
	setAttr ".tgi[0].ni[128].nvs" 18312;
	setAttr ".tgi[0].ni[129].x" -5373.517578125;
	setAttr ".tgi[0].ni[129].y" -1873.5970458984375;
	setAttr ".tgi[0].ni[129].nvs" 18312;
	setAttr ".tgi[0].ni[130].x" -5291.642578125;
	setAttr ".tgi[0].ni[130].y" -2401.214599609375;
	setAttr ".tgi[0].ni[130].nvs" 18312;
	setAttr ".tgi[0].ni[131].x" -7684.4462890625;
	setAttr ".tgi[0].ni[131].y" -397.94552612304688;
	setAttr ".tgi[0].ni[131].nvs" 18312;
	setAttr ".tgi[0].ni[132].x" -8972.08984375;
	setAttr ".tgi[0].ni[132].y" -977.12628173828125;
	setAttr ".tgi[0].ni[132].nvs" 18312;
	setAttr ".tgi[0].ni[133].x" 1824.2755126953125;
	setAttr ".tgi[0].ni[133].y" -759.72491455078125;
	setAttr ".tgi[0].ni[133].nvs" 18312;
	setAttr ".tgi[0].ni[134].x" -6987.67919921875;
	setAttr ".tgi[0].ni[134].y" -880.32269287109375;
	setAttr ".tgi[0].ni[134].nvs" 18312;
	setAttr ".tgi[0].ni[135].x" 490.63726806640625;
	setAttr ".tgi[0].ni[135].y" -756.914794921875;
	setAttr ".tgi[0].ni[135].nvs" 18312;
	setAttr ".tgi[0].ni[136].x" -4568.8076171875;
	setAttr ".tgi[0].ni[136].y" -500.37945556640625;
	setAttr ".tgi[0].ni[136].nvs" 18312;
	setAttr ".tgi[1].tn" -type "string" "Untitled_1";
	setAttr ".tgi[1].vl" -type "double2" -8673.1405026083485 -7257.1425687699193 ;
	setAttr ".tgi[1].vh" -type "double2" 5842.1882341479059 -1699.9999324480721 ;
	setAttr -s 81 ".tgi[1].ni";
	setAttr ".tgi[1].ni[0].x" 3618.7880859375;
	setAttr ".tgi[1].ni[0].y" -181.86212158203125;
	setAttr ".tgi[1].ni[0].nvs" 18305;
	setAttr ".tgi[1].ni[1].x" 3251.428466796875;
	setAttr ".tgi[1].ni[1].y" 297.14285278320313;
	setAttr ".tgi[1].ni[1].nvs" 18929;
	setAttr ".tgi[1].ni[2].x" 3251.428466796875;
	setAttr ".tgi[1].ni[2].y" -1547.142822265625;
	setAttr ".tgi[1].ni[2].nvs" 18305;
	setAttr ".tgi[1].ni[3].x" 2860;
	setAttr ".tgi[1].ni[3].y" -565.71429443359375;
	setAttr ".tgi[1].ni[3].nvs" 18305;
	setAttr ".tgi[1].ni[4].x" 2172.857177734375;
	setAttr ".tgi[1].ni[4].y" -451.42855834960938;
	setAttr ".tgi[1].ni[4].nvs" 18305;
	setAttr ".tgi[1].ni[5].x" 2172.857177734375;
	setAttr ".tgi[1].ni[5].y" -218.57142639160156;
	setAttr ".tgi[1].ni[5].nvs" 18305;
	setAttr ".tgi[1].ni[6].x" 2860;
	setAttr ".tgi[1].ni[6].y" -1940;
	setAttr ".tgi[1].ni[6].nvs" 18305;
	setAttr ".tgi[1].ni[7].x" 2860;
	setAttr ".tgi[1].ni[7].y" -1207.142822265625;
	setAttr ".tgi[1].ni[7].nvs" 18305;
	setAttr ".tgi[1].ni[8].x" 1807.142822265625;
	setAttr ".tgi[1].ni[8].y" -1351.4285888671875;
	setAttr ".tgi[1].ni[8].nvs" 18305;
	setAttr ".tgi[1].ni[9].x" -3428.571533203125;
	setAttr ".tgi[1].ni[9].y" 234.28572082519531;
	setAttr ".tgi[1].ni[9].nvs" 18305;
	setAttr ".tgi[1].ni[10].x" 3614.28564453125;
	setAttr ".tgi[1].ni[10].y" 297.14285278320313;
	setAttr ".tgi[1].ni[10].nvs" 18305;
	setAttr ".tgi[1].ni[11].x" 2860;
	setAttr ".tgi[1].ni[11].y" -2595.71435546875;
	setAttr ".tgi[1].ni[11].nvs" 18305;
	setAttr ".tgi[1].ni[12].x" 3614.28564453125;
	setAttr ".tgi[1].ni[12].y" -917.14288330078125;
	setAttr ".tgi[1].ni[12].nvs" 18305;
	setAttr ".tgi[1].ni[13].x" 3614.28564453125;
	setAttr ".tgi[1].ni[13].y" -701.4285888671875;
	setAttr ".tgi[1].ni[13].nvs" 18305;
	setAttr ".tgi[1].ni[14].x" 3251.428466796875;
	setAttr ".tgi[1].ni[14].y" -2908.571533203125;
	setAttr ".tgi[1].ni[14].nvs" 18305;
	setAttr ".tgi[1].ni[15].x" 841.4285888671875;
	setAttr ".tgi[1].ni[15].y" -1967.142822265625;
	setAttr ".tgi[1].ni[15].nvs" 18305;
	setAttr ".tgi[1].ni[16].x" 2172.857177734375;
	setAttr ".tgi[1].ni[16].y" -42.857143402099609;
	setAttr ".tgi[1].ni[16].nvs" 18305;
	setAttr ".tgi[1].ni[17].x" 3614.28564453125;
	setAttr ".tgi[1].ni[17].y" 25.714284896850586;
	setAttr ".tgi[1].ni[17].nvs" 18305;
	setAttr ".tgi[1].ni[18].x" -2812.857177734375;
	setAttr ".tgi[1].ni[18].y" -601.4285888671875;
	setAttr ".tgi[1].ni[18].nvs" 18305;
	setAttr ".tgi[1].ni[19].x" -1524.2857666015625;
	setAttr ".tgi[1].ni[19].y" -1670;
	setAttr ".tgi[1].ni[19].nvs" 18305;
	setAttr ".tgi[1].ni[20].x" -3121.428466796875;
	setAttr ".tgi[1].ni[20].y" -604.28570556640625;
	setAttr ".tgi[1].ni[20].nvs" 18305;
	setAttr ".tgi[1].ni[21].x" 2860;
	setAttr ".tgi[1].ni[21].y" -1535.7142333984375;
	setAttr ".tgi[1].ni[21].nvs" 18305;
	setAttr ".tgi[1].ni[22].x" -1524.2857666015625;
	setAttr ".tgi[1].ni[22].y" -1208.5714111328125;
	setAttr ".tgi[1].ni[22].nvs" 18305;
	setAttr ".tgi[1].ni[23].x" -851.4285888671875;
	setAttr ".tgi[1].ni[23].y" -1670;
	setAttr ".tgi[1].ni[23].nvs" 18305;
	setAttr ".tgi[1].ni[24].x" 1455.7142333984375;
	setAttr ".tgi[1].ni[24].y" -2075.71435546875;
	setAttr ".tgi[1].ni[24].nvs" 18305;
	setAttr ".tgi[1].ni[25].x" 2172.857177734375;
	setAttr ".tgi[1].ni[25].y" -2154.28564453125;
	setAttr ".tgi[1].ni[25].nvs" 18305;
	setAttr ".tgi[1].ni[26].x" -4354.54833984375;
	setAttr ".tgi[1].ni[26].y" 285.52386474609375;
	setAttr ".tgi[1].ni[26].nvs" 18305;
	setAttr ".tgi[1].ni[27].x" 2492.857177734375;
	setAttr ".tgi[1].ni[27].y" -14.285714149475098;
	setAttr ".tgi[1].ni[27].nvs" 18305;
	setAttr ".tgi[1].ni[28].x" -3121.428466796875;
	setAttr ".tgi[1].ni[28].y" 32.857143402099609;
	setAttr ".tgi[1].ni[28].nvs" 18305;
	setAttr ".tgi[1].ni[29].x" 2172.857177734375;
	setAttr ".tgi[1].ni[29].y" -917.14288330078125;
	setAttr ".tgi[1].ni[29].nvs" 18305;
	setAttr ".tgi[1].ni[30].x" -47.142856597900391;
	setAttr ".tgi[1].ni[30].y" -8614.2861328125;
	setAttr ".tgi[1].ni[30].nvs" 18305;
	setAttr ".tgi[1].ni[31].x" 2172.857177734375;
	setAttr ".tgi[1].ni[31].y" 247.14285278320313;
	setAttr ".tgi[1].ni[31].nvs" 18305;
	setAttr ".tgi[1].ni[32].x" 2492.857177734375;
	setAttr ".tgi[1].ni[32].y" -2220;
	setAttr ".tgi[1].ni[32].nvs" 18305;
	setAttr ".tgi[1].ni[33].x" 197.14285278320313;
	setAttr ".tgi[1].ni[33].y" -1822.857177734375;
	setAttr ".tgi[1].ni[33].nvs" 18305;
	setAttr ".tgi[1].ni[34].x" 3251.428466796875;
	setAttr ".tgi[1].ni[34].y" -895.71429443359375;
	setAttr ".tgi[1].ni[34].nvs" 18305;
	setAttr ".tgi[1].ni[35].x" -2198.571533203125;
	setAttr ".tgi[1].ni[35].y" -878.5714111328125;
	setAttr ".tgi[1].ni[35].nvs" 18305;
	setAttr ".tgi[1].ni[36].x" 505.71429443359375;
	setAttr ".tgi[1].ni[36].y" -1944.2857666015625;
	setAttr ".tgi[1].ni[36].nvs" 18305;
	setAttr ".tgi[1].ni[37].x" 3614.28564453125;
	setAttr ".tgi[1].ni[37].y" -1237.142822265625;
	setAttr ".tgi[1].ni[37].nvs" 18305;
	setAttr ".tgi[1].ni[38].x" 2492.857177734375;
	setAttr ".tgi[1].ni[38].y" -1901.4285888671875;
	setAttr ".tgi[1].ni[38].nvs" 18305;
	setAttr ".tgi[1].ni[39].x" -47.142856597900391;
	setAttr ".tgi[1].ni[39].y" -8980;
	setAttr ".tgi[1].ni[39].nvs" 18305;
	setAttr ".tgi[1].ni[40].x" 2492.857177734375;
	setAttr ".tgi[1].ni[40].y" -780;
	setAttr ".tgi[1].ni[40].nvs" 18305;
	setAttr ".tgi[1].ni[41].x" -47.142856597900391;
	setAttr ".tgi[1].ni[41].y" -8248.5712890625;
	setAttr ".tgi[1].ni[41].nvs" 18305;
	setAttr ".tgi[1].ni[42].x" -1200;
	setAttr ".tgi[1].ni[42].y" -1675.7142333984375;
	setAttr ".tgi[1].ni[42].nvs" 18305;
	setAttr ".tgi[1].ni[43].x" 3614.28564453125;
	setAttr ".tgi[1].ni[43].y" -2104.28564453125;
	setAttr ".tgi[1].ni[43].nvs" 18305;
	setAttr ".tgi[1].ni[44].x" -1891.4285888671875;
	setAttr ".tgi[1].ni[44].y" -838.5714111328125;
	setAttr ".tgi[1].ni[44].nvs" 18305;
	setAttr ".tgi[1].ni[45].x" 2860;
	setAttr ".tgi[1].ni[45].y" -228.57142639160156;
	setAttr ".tgi[1].ni[45].nvs" 18305;
	setAttr ".tgi[1].ni[46].x" 2172.857177734375;
	setAttr ".tgi[1].ni[46].y" -741.4285888671875;
	setAttr ".tgi[1].ni[46].nvs" 18305;
	setAttr ".tgi[1].ni[47].x" -3121.428466796875;
	setAttr ".tgi[1].ni[47].y" -314.28570556640625;
	setAttr ".tgi[1].ni[47].nvs" 18305;
	setAttr ".tgi[1].ni[48].x" 1148.5714111328125;
	setAttr ".tgi[1].ni[48].y" -1988.5714111328125;
	setAttr ".tgi[1].ni[48].nvs" 18305;
	setAttr ".tgi[1].ni[49].x" 3251.428466796875;
	setAttr ".tgi[1].ni[49].y" -1094.2857666015625;
	setAttr ".tgi[1].ni[49].nvs" 18305;
	setAttr ".tgi[1].ni[50].x" 1807.142822265625;
	setAttr ".tgi[1].ni[50].y" -28.571428298950195;
	setAttr ".tgi[1].ni[50].nvs" 18305;
	setAttr ".tgi[1].ni[51].x" -1200;
	setAttr ".tgi[1].ni[51].y" -1191.4285888671875;
	setAttr ".tgi[1].ni[51].nvs" 18305;
	setAttr ".tgi[1].ni[52].x" 2860;
	setAttr ".tgi[1].ni[52].y" -974.28570556640625;
	setAttr ".tgi[1].ni[52].nvs" 18305;
	setAttr ".tgi[1].ni[53].x" -1891.4285888671875;
	setAttr ".tgi[1].ni[53].y" -1292.857177734375;
	setAttr ".tgi[1].ni[53].nvs" 18305;
	setAttr ".tgi[1].ni[54].x" -2505.71435546875;
	setAttr ".tgi[1].ni[54].y" -420;
	setAttr ".tgi[1].ni[54].nvs" 18305;
	setAttr ".tgi[1].ni[55].x" -2812.857177734375;
	setAttr ".tgi[1].ni[55].y" -60;
	setAttr ".tgi[1].ni[55].nvs" 18305;
	setAttr ".tgi[1].ni[56].x" -1891.4285888671875;
	setAttr ".tgi[1].ni[56].y" -1094.2857666015625;
	setAttr ".tgi[1].ni[56].nvs" 18305;
	setAttr ".tgi[1].ni[57].x" 2492.857177734375;
	setAttr ".tgi[1].ni[57].y" -547.14288330078125;
	setAttr ".tgi[1].ni[57].nvs" 18305;
	setAttr ".tgi[1].ni[58].x" -3428.571533203125;
	setAttr ".tgi[1].ni[58].y" 35.714286804199219;
	setAttr ".tgi[1].ni[58].nvs" 18305;
	setAttr ".tgi[1].ni[59].x" 3614.28564453125;
	setAttr ".tgi[1].ni[59].y" -2331.428466796875;
	setAttr ".tgi[1].ni[59].nvs" 18305;
	setAttr ".tgi[1].ni[60].x" 4107.7861328125;
	setAttr ".tgi[1].ni[60].y" -394.19049072265625;
	setAttr ".tgi[1].ni[60].nvs" 18305;
	setAttr ".tgi[1].ni[61].x" 3251.428466796875;
	setAttr ".tgi[1].ni[61].y" -167.14285278320313;
	setAttr ".tgi[1].ni[61].nvs" 18305;
	setAttr ".tgi[1].ni[62].x" 3251.428466796875;
	setAttr ".tgi[1].ni[62].y" -37.142856597900391;
	setAttr ".tgi[1].ni[62].nvs" 18305;
	setAttr ".tgi[1].ni[63].x" 1807.142822265625;
	setAttr ".tgi[1].ni[63].y" -2102.857177734375;
	setAttr ".tgi[1].ni[63].nvs" 18305;
	setAttr ".tgi[1].ni[64].x" -47.142856597900391;
	setAttr ".tgi[1].ni[64].y" -8431.4287109375;
	setAttr ".tgi[1].ni[64].nvs" 18305;
	setAttr ".tgi[1].ni[65].x" -110;
	setAttr ".tgi[1].ni[65].y" -1740;
	setAttr ".tgi[1].ni[65].nvs" 18305;
	setAttr ".tgi[1].ni[66].x" 2172.857177734375;
	setAttr ".tgi[1].ni[66].y" -1552.857177734375;
	setAttr ".tgi[1].ni[66].nvs" 18305;
	setAttr ".tgi[1].ni[67].x" 3614.28564453125;
	setAttr ".tgi[1].ni[67].y" -2874.28564453125;
	setAttr ".tgi[1].ni[67].nvs" 18305;
	setAttr ".tgi[1].ni[68].x" 3251.428466796875;
	setAttr ".tgi[1].ni[68].y" -1722.857177734375;
	setAttr ".tgi[1].ni[68].nvs" 18305;
	setAttr ".tgi[1].ni[69].x" 2860;
	setAttr ".tgi[1].ni[69].y" -1360;
	setAttr ".tgi[1].ni[69].nvs" 18305;
	setAttr ".tgi[1].ni[70].x" -3428.571533203125;
	setAttr ".tgi[1].ni[70].y" -335.71429443359375;
	setAttr ".tgi[1].ni[70].nvs" 18305;
	setAttr ".tgi[1].ni[71].x" 2492.857177734375;
	setAttr ".tgi[1].ni[71].y" -190;
	setAttr ".tgi[1].ni[71].nvs" 18305;
	setAttr ".tgi[1].ni[72].x" 3251.428466796875;
	setAttr ".tgi[1].ni[72].y" -387.14285278320313;
	setAttr ".tgi[1].ni[72].nvs" 18305;
	setAttr ".tgi[1].ni[73].x" -461.42855834960938;
	setAttr ".tgi[1].ni[73].y" -1584.2857666015625;
	setAttr ".tgi[1].ni[73].nvs" 18305;
	setAttr ".tgi[1].ni[74].x" -4342.193359375;
	setAttr ".tgi[1].ni[74].y" 35.148033142089844;
	setAttr ".tgi[1].ni[74].nvs" 18305;
	setAttr ".tgi[1].ni[75].x" 3251.428466796875;
	setAttr ".tgi[1].ni[75].y" -568.5714111328125;
	setAttr ".tgi[1].ni[75].nvs" 18305;
	setAttr ".tgi[1].ni[76].x" 2860;
	setAttr ".tgi[1].ni[76].y" -798.5714111328125;
	setAttr ".tgi[1].ni[76].nvs" 18305;
	setAttr ".tgi[1].ni[77].x" -1524.2857666015625;
	setAttr ".tgi[1].ni[77].y" -1010;
	setAttr ".tgi[1].ni[77].nvs" 18305;
	setAttr ".tgi[1].ni[78].x" 1807.142822265625;
	setAttr ".tgi[1].ni[78].y" -542.85711669921875;
	setAttr ".tgi[1].ni[78].nvs" 18305;
	setAttr ".tgi[1].ni[79].x" -461.42855834960938;
	setAttr ".tgi[1].ni[79].y" -1760;
	setAttr ".tgi[1].ni[79].nvs" 18305;
	setAttr ".tgi[1].ni[80].x" 3660;
	setAttr ".tgi[1].ni[80].y" -3112.857177734375;
	setAttr ".tgi[1].ni[80].nvs" 18305;
	setAttr ".tgi[2].tn" -type "string" "Untitled_2";
	setAttr ".tgi[2].vl" -type "double2" -11938.832047238462 -4526.1902963358325 ;
	setAttr ".tgi[2].vh" -type "double2" 7847.1655431600111 3048.8094026607237 ;
	setAttr -s 78 ".tgi[2].ni";
	setAttr ".tgi[2].ni[0].x" 590;
	setAttr ".tgi[2].ni[0].y" 514.28570556640625;
	setAttr ".tgi[2].ni[0].nvs" 18312;
	setAttr ".tgi[2].ni[1].x" 953.77899169921875;
	setAttr ".tgi[2].ni[1].y" 964.6190185546875;
	setAttr ".tgi[2].ni[1].nvs" 18312;
	setAttr ".tgi[2].ni[2].x" -808.5714111328125;
	setAttr ".tgi[2].ni[2].y" 267.14285278320313;
	setAttr ".tgi[2].ni[2].nvs" 18312;
	setAttr ".tgi[2].ni[3].x" -501.42855834960938;
	setAttr ".tgi[2].ni[3].y" -487.14285278320313;
	setAttr ".tgi[2].ni[3].nvs" 18312;
	setAttr ".tgi[2].ni[4].x" 953.77899169921875;
	setAttr ".tgi[2].ni[4].y" 1094.6190185546875;
	setAttr ".tgi[2].ni[4].nvs" 18312;
	setAttr ".tgi[2].ni[5].x" 261.42855834960938;
	setAttr ".tgi[2].ni[5].y" 891.4285888671875;
	setAttr ".tgi[2].ni[5].nvs" 18312;
	setAttr ".tgi[2].ni[6].x" -6679.7509765625;
	setAttr ".tgi[2].ni[6].y" 664.36639404296875;
	setAttr ".tgi[2].ni[6].nvs" 18314;
	setAttr ".tgi[2].ni[7].x" -131.42857360839844;
	setAttr ".tgi[2].ni[7].y" 398.57144165039063;
	setAttr ".tgi[2].ni[7].nvs" 18312;
	setAttr ".tgi[2].ni[8].x" -4194.28564453125;
	setAttr ".tgi[2].ni[8].y" -990;
	setAttr ".tgi[2].ni[8].nvs" 18312;
	setAttr ".tgi[2].ni[9].x" -2481.428466796875;
	setAttr ".tgi[2].ni[9].y" -988.5714111328125;
	setAttr ".tgi[2].ni[9].nvs" 18312;
	setAttr ".tgi[2].ni[10].x" 590;
	setAttr ".tgi[2].ni[10].y" -300;
	setAttr ".tgi[2].ni[10].nvs" 18312;
	setAttr ".tgi[2].ni[11].x" 261.42855834960938;
	setAttr ".tgi[2].ni[11].y" -860;
	setAttr ".tgi[2].ni[11].nvs" 18312;
	setAttr ".tgi[2].ni[12].x" -501.42855834960938;
	setAttr ".tgi[2].ni[12].y" -588.5714111328125;
	setAttr ".tgi[2].ni[12].nvs" 18312;
	setAttr ".tgi[2].ni[13].x" 590;
	setAttr ".tgi[2].ni[13].y" 254.28572082519531;
	setAttr ".tgi[2].ni[13].nvs" 18312;
	setAttr ".tgi[2].ni[14].x" -4194.28564453125;
	setAttr ".tgi[2].ni[14].y" -602.85711669921875;
	setAttr ".tgi[2].ni[14].nvs" 18312;
	setAttr ".tgi[2].ni[15].x" 590;
	setAttr ".tgi[2].ni[15].y" 361.42855834960938;
	setAttr ".tgi[2].ni[15].nvs" 18312;
	setAttr ".tgi[2].ni[16].x" 590;
	setAttr ".tgi[2].ni[16].y" 948.5714111328125;
	setAttr ".tgi[2].ni[16].nvs" 18312;
	setAttr ".tgi[2].ni[17].x" -6427.14306640625;
	setAttr ".tgi[2].ni[17].y" 708.5714111328125;
	setAttr ".tgi[2].ni[17].nvs" 18312;
	setAttr ".tgi[2].ni[18].x" 261.42855834960938;
	setAttr ".tgi[2].ni[18].y" 140;
	setAttr ".tgi[2].ni[18].nvs" 18312;
	setAttr ".tgi[2].ni[19].x" 261.42855834960938;
	setAttr ".tgi[2].ni[19].y" -961.4285888671875;
	setAttr ".tgi[2].ni[19].nvs" 18312;
	setAttr ".tgi[2].ni[20].x" -131.42857360839844;
	setAttr ".tgi[2].ni[20].y" -530;
	setAttr ".tgi[2].ni[20].nvs" 18312;
	setAttr ".tgi[2].ni[21].x" -131.42857360839844;
	setAttr ".tgi[2].ni[21].y" 614.28570556640625;
	setAttr ".tgi[2].ni[21].nvs" 18312;
	setAttr ".tgi[2].ni[22].x" -1175.7142333984375;
	setAttr ".tgi[2].ni[22].y" -464.28570556640625;
	setAttr ".tgi[2].ni[22].nvs" 18312;
	setAttr ".tgi[2].ni[23].x" -6120;
	setAttr ".tgi[2].ni[23].y" 550;
	setAttr ".tgi[2].ni[23].nvs" 18312;
	setAttr ".tgi[2].ni[24].x" 590;
	setAttr ".tgi[2].ni[24].y" 790;
	setAttr ".tgi[2].ni[24].nvs" 18312;
	setAttr ".tgi[2].ni[25].x" -5195.71435546875;
	setAttr ".tgi[2].ni[25].y" -341.42855834960938;
	setAttr ".tgi[2].ni[25].nvs" 18312;
	setAttr ".tgi[2].ni[26].x" -1175.7142333984375;
	setAttr ".tgi[2].ni[26].y" -1047.142822265625;
	setAttr ".tgi[2].ni[26].nvs" 18312;
	setAttr ".tgi[2].ni[27].x" -501.42855834960938;
	setAttr ".tgi[2].ni[27].y" -100;
	setAttr ".tgi[2].ni[27].nvs" 18312;
	setAttr ".tgi[2].ni[28].x" -5810;
	setAttr ".tgi[2].ni[28].y" 601.4285888671875;
	setAttr ".tgi[2].ni[28].nvs" 18312;
	setAttr ".tgi[2].ni[29].x" -5502.85693359375;
	setAttr ".tgi[2].ni[29].y" 404.28570556640625;
	setAttr ".tgi[2].ni[29].nvs" 18312;
	setAttr ".tgi[2].ni[30].x" 261.42855834960938;
	setAttr ".tgi[2].ni[30].y" 412.85714721679688;
	setAttr ".tgi[2].ni[30].nvs" 18312;
	setAttr ".tgi[2].ni[31].x" -1837.142822265625;
	setAttr ".tgi[2].ni[31].y" -1004.2857055664063;
	setAttr ".tgi[2].ni[31].nvs" 18312;
	setAttr ".tgi[2].ni[32].x" -131.42857360839844;
	setAttr ".tgi[2].ni[32].y" -1221.4285888671875;
	setAttr ".tgi[2].ni[32].nvs" 18312;
	setAttr ".tgi[2].ni[33].x" -131.42857360839844;
	setAttr ".tgi[2].ni[33].y" -904.28570556640625;
	setAttr ".tgi[2].ni[33].nvs" 18312;
	setAttr ".tgi[2].ni[34].x" -501.42855834960938;
	setAttr ".tgi[2].ni[34].y" -1524.2857666015625;
	setAttr ".tgi[2].ni[34].nvs" 18312;
	setAttr ".tgi[2].ni[35].x" -501.42855834960938;
	setAttr ".tgi[2].ni[35].y" -1105.7142333984375;
	setAttr ".tgi[2].ni[35].nvs" 18312;
	setAttr ".tgi[2].ni[36].x" -6120;
	setAttr ".tgi[2].ni[36].y" 708.5714111328125;
	setAttr ".tgi[2].ni[36].nvs" 18312;
	setAttr ".tgi[2].ni[37].x" 590;
	setAttr ".tgi[2].ni[37].y" 615.71429443359375;
	setAttr ".tgi[2].ni[37].nvs" 18312;
	setAttr ".tgi[2].ni[38].x" 590;
	setAttr ".tgi[2].ni[38].y" -860;
	setAttr ".tgi[2].ni[38].nvs" 18312;
	setAttr ".tgi[2].ni[39].x" -4520;
	setAttr ".tgi[2].ni[39].y" -1025.7142333984375;
	setAttr ".tgi[2].ni[39].nvs" 18312;
	setAttr ".tgi[2].ni[40].x" 953.77899169921875;
	setAttr ".tgi[2].ni[40].y" 1548.90478515625;
	setAttr ".tgi[2].ni[40].nvs" 18312;
	setAttr ".tgi[2].ni[41].x" -131.42857360839844;
	setAttr ".tgi[2].ni[41].y" -142.85714721679688;
	setAttr ".tgi[2].ni[41].nvs" 18312;
	setAttr ".tgi[2].ni[42].x" -131.42857360839844;
	setAttr ".tgi[2].ni[42].y" -1322.857177734375;
	setAttr ".tgi[2].ni[42].nvs" 18312;
	setAttr ".tgi[2].ni[43].x" -501.42855834960938;
	setAttr ".tgi[2].ni[43].y" -1321.4285888671875;
	setAttr ".tgi[2].ni[43].nvs" 18312;
	setAttr ".tgi[2].ni[44].x" -4520;
	setAttr ".tgi[2].ni[44].y" -480;
	setAttr ".tgi[2].ni[44].nvs" 18312;
	setAttr ".tgi[2].ni[45].x" -6427.14306640625;
	setAttr ".tgi[2].ni[45].y" 820;
	setAttr ".tgi[2].ni[45].nvs" 18312;
	setAttr ".tgi[2].ni[46].x" -3100;
	setAttr ".tgi[2].ni[46].y" -985.71429443359375;
	setAttr ".tgi[2].ni[46].nvs" 18312;
	setAttr ".tgi[2].ni[47].x" -3844.28564453125;
	setAttr ".tgi[2].ni[47].y" -1010;
	setAttr ".tgi[2].ni[47].nvs" 18312;
	setAttr ".tgi[2].ni[48].x" -5810;
	setAttr ".tgi[2].ni[48].y" 760;
	setAttr ".tgi[2].ni[48].nvs" 18312;
	setAttr ".tgi[2].ni[49].x" 261.42855834960938;
	setAttr ".tgi[2].ni[49].y" 615.71429443359375;
	setAttr ".tgi[2].ni[49].nvs" 18312;
	setAttr ".tgi[2].ni[50].x" -4520;
	setAttr ".tgi[2].ni[50].y" -581.4285888671875;
	setAttr ".tgi[2].ni[50].nvs" 18312;
	setAttr ".tgi[2].ni[51].x" -131.42857360839844;
	setAttr ".tgi[2].ni[51].y" -688.5714111328125;
	setAttr ".tgi[2].ni[51].nvs" 18312;
	setAttr ".tgi[2].ni[52].x" -808.5714111328125;
	setAttr ".tgi[2].ni[52].y" -551.4285888671875;
	setAttr ".tgi[2].ni[52].nvs" 18312;
	setAttr ".tgi[2].ni[53].x" -808.5714111328125;
	setAttr ".tgi[2].ni[53].y" -1095.7142333984375;
	setAttr ".tgi[2].ni[53].nvs" 18312;
	setAttr ".tgi[2].ni[54].x" -501.42855834960938;
	setAttr ".tgi[2].ni[54].y" 344.28570556640625;
	setAttr ".tgi[2].ni[54].nvs" 18312;
	setAttr ".tgi[2].ni[55].x" -6120;
	setAttr ".tgi[2].ni[55].y" 867.14288330078125;
	setAttr ".tgi[2].ni[55].nvs" 18312;
	setAttr ".tgi[2].ni[56].x" 590;
	setAttr ".tgi[2].ni[56].y" -961.4285888671875;
	setAttr ".tgi[2].ni[56].nvs" 18312;
	setAttr ".tgi[2].ni[57].x" -3452.857177734375;
	setAttr ".tgi[2].ni[57].y" -1025.7142333984375;
	setAttr ".tgi[2].ni[57].nvs" 18312;
	setAttr ".tgi[2].ni[58].x" -808.5714111328125;
	setAttr ".tgi[2].ni[58].y" -450;
	setAttr ".tgi[2].ni[58].nvs" 18312;
	setAttr ".tgi[2].ni[59].x" -808.5714111328125;
	setAttr ".tgi[2].ni[59].y" -1375.7142333984375;
	setAttr ".tgi[2].ni[59].nvs" 18312;
	setAttr ".tgi[2].ni[60].x" -2792.857177734375;
	setAttr ".tgi[2].ni[60].y" -995.71429443359375;
	setAttr ".tgi[2].ni[60].nvs" 18312;
	setAttr ".tgi[2].ni[61].x" -4888.5712890625;
	setAttr ".tgi[2].ni[61].y" -365.71429443359375;
	setAttr ".tgi[2].ni[61].nvs" 18312;
	setAttr ".tgi[2].ni[62].x" 261.42855834960938;
	setAttr ".tgi[2].ni[62].y" -418.57144165039063;
	setAttr ".tgi[2].ni[62].nvs" 18312;
	setAttr ".tgi[2].ni[63].x" -2144.28564453125;
	setAttr ".tgi[2].ni[63].y" -1010;
	setAttr ".tgi[2].ni[63].nvs" 18312;
	setAttr ".tgi[2].ni[64].x" -808.5714111328125;
	setAttr ".tgi[2].ni[64].y" 165.71427917480469;
	setAttr ".tgi[2].ni[64].nvs" 18312;
	setAttr ".tgi[2].ni[65].x" -501.42855834960938;
	setAttr ".tgi[2].ni[65].y" -1422.857177734375;
	setAttr ".tgi[2].ni[65].nvs" 18312;
	setAttr ".tgi[2].ni[66].x" -131.42857360839844;
	setAttr ".tgi[2].ni[66].y" -1005.7142944335938;
	setAttr ".tgi[2].ni[66].nvs" 18312;
	setAttr ".tgi[2].ni[67].x" 953.77899169921875;
	setAttr ".tgi[2].ni[67].y" 1246.0477294921875;
	setAttr ".tgi[2].ni[67].nvs" 18312;
	setAttr ".tgi[2].ni[68].x" 261.42855834960938;
	setAttr ".tgi[2].ni[68].y" 514.28570556640625;
	setAttr ".tgi[2].ni[68].nvs" 18312;
	setAttr ".tgi[2].ni[69].x" -4888.5712890625;
	setAttr ".tgi[2].ni[69].y" -625.71429443359375;
	setAttr ".tgi[2].ni[69].nvs" 18312;
	setAttr ".tgi[2].ni[70].x" 953.77899169921875;
	setAttr ".tgi[2].ni[70].y" 1397.476318359375;
	setAttr ".tgi[2].ni[70].nvs" 18312;
	setAttr ".tgi[2].ni[71].x" 590;
	setAttr ".tgi[2].ni[71].y" -401.42855834960938;
	setAttr ".tgi[2].ni[71].nvs" 18312;
	setAttr ".tgi[2].ni[72].x" -4888.5712890625;
	setAttr ".tgi[2].ni[72].y" -524.28570556640625;
	setAttr ".tgi[2].ni[72].nvs" 18312;
	setAttr ".tgi[2].ni[73].x" -131.42857360839844;
	setAttr ".tgi[2].ni[73].y" 182.85714721679688;
	setAttr ".tgi[2].ni[73].nvs" 18312;
	setAttr ".tgi[2].ni[74].x" -1530;
	setAttr ".tgi[2].ni[74].y" -1011.4285888671875;
	setAttr ".tgi[2].ni[74].nvs" 18312;
	setAttr ".tgi[2].ni[75].x" -3452.857177734375;
	setAttr ".tgi[2].ni[75].y" -924.28570556640625;
	setAttr ".tgi[2].ni[75].nvs" 18312;
	setAttr ".tgi[2].ni[76].x" 261.42855834960938;
	setAttr ".tgi[2].ni[76].y" -727.14288330078125;
	setAttr ".tgi[2].ni[76].nvs" 18312;
	setAttr ".tgi[2].ni[77].x" 261.42855834960938;
	setAttr ".tgi[2].ni[77].y" -1062.857177734375;
	setAttr ".tgi[2].ni[77].nvs" 18312;
	setAttr ".tgi[3].tn" -type "string" "Untitled_3";
	setAttr ".tgi[3].vl" -type "double2" -12222.058110504784 -4391.6664921575193 ;
	setAttr ".tgi[3].vh" -type "double2" 13263.724735779335 5365.4759772713305 ;
	setAttr -s 32 ".tgi[3].ni";
	setAttr ".tgi[3].ni[0].x" -495.111572265625;
	setAttr ".tgi[3].ni[0].y" -676.455810546875;
	setAttr ".tgi[3].ni[0].nvs" 18312;
	setAttr ".tgi[3].ni[1].x" -309.33856201171875;
	setAttr ".tgi[3].ni[1].y" 209.53846740722656;
	setAttr ".tgi[3].ni[1].nvs" 18312;
	setAttr ".tgi[3].ni[2].x" 262.2706298828125;
	setAttr ".tgi[3].ni[2].y" -362.07073974609375;
	setAttr ".tgi[3].ni[2].nvs" 18312;
	setAttr ".tgi[3].ni[3].x" -1395.39599609375;
	setAttr ".tgi[3].ni[3].y" 509.63330078125;
	setAttr ".tgi[3].ni[3].nvs" 18312;
	setAttr ".tgi[3].ni[4].x" -1366.8155517578125;
	setAttr ".tgi[3].ni[4].y" 309.570068359375;
	setAttr ".tgi[3].ni[4].nvs" 18314;
	setAttr ".tgi[3].ni[5].x" -495.111572265625;
	setAttr ".tgi[3].ni[5].y" -776.4874267578125;
	setAttr ".tgi[3].ni[5].nvs" 18312;
	setAttr ".tgi[3].ni[6].x" -380.78973388671875;
	setAttr ".tgi[3].ni[6].y" 309.570068359375;
	setAttr ".tgi[3].ni[6].nvs" 18312;
	setAttr ".tgi[3].ni[7].x" 233.69017028808594;
	setAttr ".tgi[3].ni[7].y" 438.18215942382813;
	setAttr ".tgi[3].ni[7].nvs" 18312;
	setAttr ".tgi[3].ni[8].x" -495.111572265625;
	setAttr ".tgi[3].ni[8].y" -576.4241943359375;
	setAttr ".tgi[3].ni[8].nvs" 18312;
	setAttr ".tgi[3].ni[9].x" -1495.4276123046875;
	setAttr ".tgi[3].ni[9].y" 781.14764404296875;
	setAttr ".tgi[3].ni[9].nvs" 18313;
	setAttr ".tgi[3].ni[10].x" -652.3040771484375;
	setAttr ".tgi[3].ni[10].y" 938.3402099609375;
	setAttr ".tgi[3].ni[10].nvs" 18313;
	setAttr ".tgi[3].ni[11].x" -495.111572265625;
	setAttr ".tgi[3].ni[11].y" -76.266128540039063;
	setAttr ".tgi[3].ni[11].nvs" 18312;
	setAttr ".tgi[3].ni[12].x" -537.98223876953125;
	setAttr ".tgi[3].ni[12].y" 509.63330078125;
	setAttr ".tgi[3].ni[12].nvs" 18312;
	setAttr ".tgi[3].ni[13].x" -923.8184814453125;
	setAttr ".tgi[3].ni[13].y" 381.021240234375;
	setAttr ".tgi[3].ni[13].nvs" 18312;
	setAttr ".tgi[3].ni[14].x" 233.69017028808594;
	setAttr ".tgi[3].ni[14].y" 238.11892700195313;
	setAttr ".tgi[3].ni[14].nvs" 18312;
	setAttr ".tgi[3].ni[15].x" 233.69017028808594;
	setAttr ".tgi[3].ni[15].y" 338.15054321289063;
	setAttr ".tgi[3].ni[15].nvs" 18312;
	setAttr ".tgi[3].ni[16].x" -909.52825927734375;
	setAttr ".tgi[3].ni[16].y" 766.857421875;
	setAttr ".tgi[3].ni[16].nvs" 18312;
	setAttr ".tgi[3].ni[17].x" 305.14132690429688;
	setAttr ".tgi[3].ni[17].y" 52.345939636230469;
	setAttr ".tgi[3].ni[17].nvs" 18312;
	setAttr ".tgi[3].ni[18].x" -495.111572265625;
	setAttr ".tgi[3].ni[18].y" -176.29774475097656;
	setAttr ".tgi[3].ni[18].nvs" 18312;
	setAttr ".tgi[3].ni[19].x" -1266.783935546875;
	setAttr ".tgi[3].ni[19].y" 952.63043212890625;
	setAttr ".tgi[3].ni[19].nvs" 18314;
	setAttr ".tgi[3].ni[20].x" -495.111572265625;
	setAttr ".tgi[3].ni[20].y" -276.329345703125;
	setAttr ".tgi[3].ni[20].nvs" 18312;
	setAttr ".tgi[3].ni[21].x" -1881.263916015625;
	setAttr ".tgi[3].ni[21].y" 509.63330078125;
	setAttr ".tgi[3].ni[21].nvs" 18314;
	setAttr ".tgi[3].ni[22].x" -495.111572265625;
	setAttr ".tgi[3].ni[22].y" -376.3609619140625;
	setAttr ".tgi[3].ni[22].nvs" 18312;
	setAttr ".tgi[3].ni[23].x" -2309.970703125;
	setAttr ".tgi[3].ni[23].y" -204.87820434570313;
	setAttr ".tgi[3].ni[23].nvs" 18312;
	setAttr ".tgi[3].ni[24].x" -495.111572265625;
	setAttr ".tgi[3].ni[24].y" -476.392578125;
	setAttr ".tgi[3].ni[24].nvs" 18312;
	setAttr ".tgi[3].ni[25].x" -923.8184814453125;
	setAttr ".tgi[3].ni[25].y" 623.95513916015625;
	setAttr ".tgi[3].ni[25].nvs" 1931;
	setAttr ".tgi[3].ni[26].x" 305.14132690429688;
	setAttr ".tgi[3].ni[26].y" -119.13681793212891;
	setAttr ".tgi[3].ni[26].nvs" 18312;
	setAttr ".tgi[3].ni[27].x" -695.1748046875;
	setAttr ".tgi[3].ni[27].y" 1009.7913208007813;
	setAttr ".tgi[3].ni[27].nvs" 18312;
	setAttr ".tgi[3].ni[28].x" -1852.683349609375;
	setAttr ".tgi[3].ni[28].y" 766.857421875;
	setAttr ".tgi[3].ni[28].nvs" 18312;
	setAttr ".tgi[3].ni[29].x" -595.1431884765625;
	setAttr ".tgi[3].ni[29].y" 623.95513916015625;
	setAttr ".tgi[3].ni[29].nvs" 18312;
	setAttr ".tgi[3].ni[30].x" -495.111572265625;
	setAttr ".tgi[3].ni[30].y" 23.765480041503906;
	setAttr ".tgi[3].ni[30].nvs" 18312;
	setAttr ".tgi[3].ni[31].x" -437.95065307617188;
	setAttr ".tgi[3].ni[31].y" 409.6016845703125;
	setAttr ".tgi[3].ni[31].nvs" 18312;
	setAttr ".tgi[4].tn" -type "string" "Untitled_4";
	setAttr ".tgi[4].vl" -type "double2" -4078.7162108391817 -2276.1903857427969 ;
	setAttr ".tgi[4].vh" -type "double2" 4422.7638162155772 978.57138968649485 ;
	setAttr -s 42 ".tgi[4].ni";
	setAttr ".tgi[4].ni[0].x" -1095.31396484375;
	setAttr ".tgi[4].ni[0].y" 249.16046142578125;
	setAttr ".tgi[4].ni[0].nvs" 18313;
	setAttr ".tgi[4].ni[1].x" 464.41000366210938;
	setAttr ".tgi[4].ni[1].y" 136.61129760742188;
	setAttr ".tgi[4].ni[1].nvs" 18313;
	setAttr ".tgi[4].ni[2].x" -255.96687316894531;
	setAttr ".tgi[4].ni[2].y" -1657.2646484375;
	setAttr ".tgi[4].ni[2].nvs" 18313;
	setAttr ".tgi[4].ni[3].x" 41.865879058837891;
	setAttr ".tgi[4].ni[3].y" -518.15325927734375;
	setAttr ".tgi[4].ni[3].nvs" 18313;
	setAttr ".tgi[4].ni[4].x" -1648.0574951171875;
	setAttr ".tgi[4].ni[4].y" -713.47607421875;
	setAttr ".tgi[4].ni[4].nvs" 18313;
	setAttr ".tgi[4].ni[5].x" 465.67672729492188;
	setAttr ".tgi[4].ni[5].y" -70.190788269042969;
	setAttr ".tgi[4].ni[5].nvs" 18314;
	setAttr ".tgi[4].ni[6].x" 450.50030517578125;
	setAttr ".tgi[4].ni[6].y" 341.39724731445313;
	setAttr ".tgi[4].ni[6].nvs" 18313;
	setAttr ".tgi[4].ni[7].x" 155.06015014648438;
	setAttr ".tgi[4].ni[7].y" 59.168106079101563;
	setAttr ".tgi[4].ni[7].nvs" 18313;
	setAttr ".tgi[4].ni[8].x" -1156.243896484375;
	setAttr ".tgi[4].ni[8].y" -889.52825927734375;
	setAttr ".tgi[4].ni[8].nvs" 18313;
	setAttr ".tgi[4].ni[9].x" -1392.09814453125;
	setAttr ".tgi[4].ni[9].y" 316.61895751953125;
	setAttr ".tgi[4].ni[9].nvs" 18313;
	setAttr ".tgi[4].ni[10].x" -1156.243896484375;
	setAttr ".tgi[4].ni[10].y" -443.81396484375;
	setAttr ".tgi[4].ni[10].nvs" 18313;
	setAttr ".tgi[4].ni[11].x" 1307.949462890625;
	setAttr ".tgi[4].ni[11].y" -1102.361572265625;
	setAttr ".tgi[4].ni[11].nvs" 18313;
	setAttr ".tgi[4].ni[12].x" -1392.09814453125;
	setAttr ".tgi[4].ni[12].y" 102.57495880126953;
	setAttr ".tgi[4].ni[12].nvs" 18313;
	setAttr ".tgi[4].ni[13].x" 580.47393798828125;
	setAttr ".tgi[4].ni[13].y" -732.3731689453125;
	setAttr ".tgi[4].ni[13].nvs" 18312;
	setAttr ".tgi[4].ni[14].x" -254.07272338867188;
	setAttr ".tgi[4].ni[14].y" -1358.9840087890625;
	setAttr ".tgi[4].ni[14].nvs" 18313;
	setAttr ".tgi[4].ni[15].x" -1163.593017578125;
	setAttr ".tgi[4].ni[15].y" -1110.548095703125;
	setAttr ".tgi[4].ni[15].nvs" 18313;
	setAttr ".tgi[4].ni[16].x" -793.72650146484375;
	setAttr ".tgi[4].ni[16].y" 104.58580780029297;
	setAttr ".tgi[4].ni[16].nvs" 18313;
	setAttr ".tgi[4].ni[17].x" -1988.7552490234375;
	setAttr ".tgi[4].ni[17].y" -985.50360107421875;
	setAttr ".tgi[4].ni[17].nvs" 18313;
	setAttr ".tgi[4].ni[18].x" -115.71428680419922;
	setAttr ".tgi[4].ni[18].y" -184.28572082519531;
	setAttr ".tgi[4].ni[18].nvs" 18313;
	setAttr ".tgi[4].ni[19].x" -1988.7552490234375;
	setAttr ".tgi[4].ni[19].y" -1185.5035400390625;
	setAttr ".tgi[4].ni[19].nvs" 18313;
	setAttr ".tgi[4].ni[20].x" 605.20062255859375;
	setAttr ".tgi[4].ni[20].y" -1445.7021484375;
	setAttr ".tgi[4].ni[20].nvs" 18305;
	setAttr ".tgi[4].ni[21].x" -845.44207763671875;
	setAttr ".tgi[4].ni[21].y" -1038.04248046875;
	setAttr ".tgi[4].ni[21].nvs" 18313;
	setAttr ".tgi[4].ni[22].x" -422.85714721679688;
	setAttr ".tgi[4].ni[22].y" -317.14285278320313;
	setAttr ".tgi[4].ni[22].nvs" 18313;
	setAttr ".tgi[4].ni[23].x" -1084.3885498046875;
	setAttr ".tgi[4].ni[23].y" -27.977771759033203;
	setAttr ".tgi[4].ni[23].nvs" 18313;
	setAttr ".tgi[4].ni[24].x" 1103.57177734375;
	setAttr ".tgi[4].ni[24].y" -431.02005004882813;
	setAttr ".tgi[4].ni[24].nvs" 18312;
	setAttr ".tgi[4].ni[25].x" -1638.8651123046875;
	setAttr ".tgi[4].ni[25].y" -1124.0875244140625;
	setAttr ".tgi[4].ni[25].nvs" 18313;
	setAttr ".tgi[4].ni[26].x" -794.5484619140625;
	setAttr ".tgi[4].ni[26].y" 327.843505859375;
	setAttr ".tgi[4].ni[26].nvs" 18313;
	setAttr ".tgi[4].ni[27].x" -422.85714721679688;
	setAttr ".tgi[4].ni[27].y" -50;
	setAttr ".tgi[4].ni[27].nvs" 18313;
	setAttr ".tgi[4].ni[28].x" 875.1959228515625;
	setAttr ".tgi[4].ni[28].y" -881.17059326171875;
	setAttr ".tgi[4].ni[28].nvs" 18313;
	setAttr ".tgi[4].ni[29].x" -845.44207763671875;
	setAttr ".tgi[4].ni[29].y" -793.7568359375;
	setAttr ".tgi[4].ni[29].nvs" 18313;
	setAttr ".tgi[4].ni[30].x" -231.15638732910156;
	setAttr ".tgi[4].ni[30].y" -838.04254150390625;
	setAttr ".tgi[4].ni[30].nvs" 18313;
	setAttr ".tgi[4].ni[31].x" -538.29925537109375;
	setAttr ".tgi[4].ni[31].y" -905.18536376953125;
	setAttr ".tgi[4].ni[31].nvs" 18313;
	setAttr ".tgi[4].ni[32].x" 824.03948974609375;
	setAttr ".tgi[4].ni[32].y" 131.30455017089844;
	setAttr ".tgi[4].ni[32].nvs" 18314;
	setAttr ".tgi[4].ni[33].x" -252.37808227539063;
	setAttr ".tgi[4].ni[33].y" -1857.716796875;
	setAttr ".tgi[4].ni[33].nvs" 18313;
	setAttr ".tgi[4].ni[34].x" 606.15838623046875;
	setAttr ".tgi[4].ni[34].y" -1251.337890625;
	setAttr ".tgi[4].ni[34].nvs" 18305;
	setAttr ".tgi[4].ni[35].x" -794.5484619140625;
	setAttr ".tgi[4].ni[35].y" 550.70062255859375;
	setAttr ".tgi[4].ni[35].nvs" 18313;
	setAttr ".tgi[4].ni[36].x" -776.57208251953125;
	setAttr ".tgi[4].ni[36].y" -184.27005004882813;
	setAttr ".tgi[4].ni[36].nvs" 18313;
	setAttr ".tgi[4].ni[37].x" 569.50750732421875;
	setAttr ".tgi[4].ni[37].y" -994.04205322265625;
	setAttr ".tgi[4].ni[37].nvs" 18313;
	setAttr ".tgi[4].ni[38].x" 893.02789306640625;
	setAttr ".tgi[4].ni[38].y" -1243.4075927734375;
	setAttr ".tgi[4].ni[38].nvs" 18313;
	setAttr ".tgi[4].ni[39].x" 75.986473083496094;
	setAttr ".tgi[4].ni[39].y" -859.4710693359375;
	setAttr ".tgi[4].ni[39].nvs" 18313;
	setAttr ".tgi[4].ni[40].x" -1156.243896484375;
	setAttr ".tgi[4].ni[40].y" -666.67108154296875;
	setAttr ".tgi[4].ni[40].nvs" 18313;
	setAttr ".tgi[4].ni[41].x" -388.92889404296875;
	setAttr ".tgi[4].ni[41].y" -1084.80029296875;
	setAttr ".tgi[4].ni[41].nvs" 18313;
	setAttr ".tgi[5].tn" -type "string" "Untitled_5";
	setAttr ".tgi[5].vl" -type "double2" -2832.5408583787671 141.66666103733925 ;
	setAttr ".tgi[5].vh" -type "double2" 2155.1599329145147 2051.1903946834932 ;
	setAttr -s 30 ".tgi[5].ni";
	setAttr ".tgi[5].ni[0].x" 511.42855834960938;
	setAttr ".tgi[5].ni[0].y" 484.28570556640625;
	setAttr ".tgi[5].ni[0].nvs" 18313;
	setAttr ".tgi[5].ni[1].x" -1845.7142333984375;
	setAttr ".tgi[5].ni[1].y" 612.85711669921875;
	setAttr ".tgi[5].ni[1].nvs" 18313;
	setAttr ".tgi[5].ni[2].x" -2145.71435546875;
	setAttr ".tgi[5].ni[2].y" 441.42855834960938;
	setAttr ".tgi[5].ni[2].nvs" 18312;
	setAttr ".tgi[5].ni[3].x" -345.71429443359375;
	setAttr ".tgi[5].ni[3].y" 270;
	setAttr ".tgi[5].ni[3].nvs" 18312;
	setAttr ".tgi[5].ni[4].x" 254.28572082519531;
	setAttr ".tgi[5].ni[4].y" 612.85711669921875;
	setAttr ".tgi[5].ni[4].nvs" 18313;
	setAttr ".tgi[5].ni[5].x" -1331.4285888671875;
	setAttr ".tgi[5].ni[5].y" 827.14288330078125;
	setAttr ".tgi[5].ni[5].nvs" 18313;
	setAttr ".tgi[5].ni[6].x" -2145.71435546875;
	setAttr ".tgi[5].ni[6].y" 1084.2857666015625;
	setAttr ".tgi[5].ni[6].nvs" 18312;
	setAttr ".tgi[5].ni[7].x" 768.5714111328125;
	setAttr ".tgi[5].ni[7].y" 741.4285888671875;
	setAttr ".tgi[5].ni[7].nvs" 18313;
	setAttr ".tgi[5].ni[8].x" -345.71429443359375;
	setAttr ".tgi[5].ni[8].y" 184.28572082519531;
	setAttr ".tgi[5].ni[8].nvs" 18313;
	setAttr ".tgi[5].ni[9].x" -1117.142822265625;
	setAttr ".tgi[5].ni[9].y" 741.4285888671875;
	setAttr ".tgi[5].ni[9].nvs" 18312;
	setAttr ".tgi[5].ni[10].x" -2145.71435546875;
	setAttr ".tgi[5].ni[10].y" 698.5714111328125;
	setAttr ".tgi[5].ni[10].nvs" 18313;
	setAttr ".tgi[5].ni[11].x" -131.42857360839844;
	setAttr ".tgi[5].ni[11].y" -72.857139587402344;
	setAttr ".tgi[5].ni[11].nvs" 18313;
	setAttr ".tgi[5].ni[12].x" 125.71428680419922;
	setAttr ".tgi[5].ni[12].y" -158.57142639160156;
	setAttr ".tgi[5].ni[12].nvs" 18312;
	setAttr ".tgi[5].ni[13].x" -345.71429443359375;
	setAttr ".tgi[5].ni[13].y" 527.14288330078125;
	setAttr ".tgi[5].ni[13].nvs" 18312;
	setAttr ".tgi[5].ni[14].x" 125.71428680419922;
	setAttr ".tgi[5].ni[14].y" -244.28572082519531;
	setAttr ".tgi[5].ni[14].nvs" 18313;
	setAttr ".tgi[5].ni[15].x" -388.57144165039063;
	setAttr ".tgi[5].ni[15].y" -372.85714721679688;
	setAttr ".tgi[5].ni[15].nvs" 18312;
	setAttr ".tgi[5].ni[16].x" -1331.4285888671875;
	setAttr ".tgi[5].ni[16].y" 1200;
	setAttr ".tgi[5].ni[16].nvs" 18305;
	setAttr ".tgi[5].ni[17].x" -2145.71435546875;
	setAttr ".tgi[5].ni[17].y" 1212.857177734375;
	setAttr ".tgi[5].ni[17].nvs" 18312;
	setAttr ".tgi[5].ni[18].x" -1845.7142333984375;
	setAttr ".tgi[5].ni[18].y" 827.14288330078125;
	setAttr ".tgi[5].ni[18].nvs" 18313;
	setAttr ".tgi[5].ni[19].x" -1845.7142333984375;
	setAttr ".tgi[5].ni[19].y" 1500;
	setAttr ".tgi[5].ni[19].nvs" 18305;
	setAttr ".tgi[5].ni[20].x" -345.71429443359375;
	setAttr ".tgi[5].ni[20].y" 441.42855834960938;
	setAttr ".tgi[5].ni[20].nvs" 18312;
	setAttr ".tgi[5].ni[21].x" -1845.7142333984375;
	setAttr ".tgi[5].ni[21].y" 1298.5714111328125;
	setAttr ".tgi[5].ni[21].nvs" 18313;
	setAttr ".tgi[5].ni[22].x" -1545.7142333984375;
	setAttr ".tgi[5].ni[22].y" 784.28570556640625;
	setAttr ".tgi[5].ni[22].nvs" 18313;
	setAttr ".tgi[5].ni[23].x" -731.4285888671875;
	setAttr ".tgi[5].ni[23].y" 312.85714721679688;
	setAttr ".tgi[5].ni[23].nvs" 18313;
	setAttr ".tgi[5].ni[24].x" -2145.71435546875;
	setAttr ".tgi[5].ni[24].y" 955.71429443359375;
	setAttr ".tgi[5].ni[24].nvs" 18312;
	setAttr ".tgi[5].ni[25].x" -45.714286804199219;
	setAttr ".tgi[5].ni[25].y" 612.85711669921875;
	setAttr ".tgi[5].ni[25].nvs" 18312;
	setAttr ".tgi[5].ni[26].x" -988.5714111328125;
	setAttr ".tgi[5].ni[26].y" 141.42857360839844;
	setAttr ".tgi[5].ni[26].nvs" 18312;
	setAttr ".tgi[5].ni[27].x" -1845.7142333984375;
	setAttr ".tgi[5].ni[27].y" 1084.2857666015625;
	setAttr ".tgi[5].ni[27].nvs" 18313;
	setAttr ".tgi[5].ni[28].x" -45.714286804199219;
	setAttr ".tgi[5].ni[28].y" 527.14288330078125;
	setAttr ".tgi[5].ni[28].nvs" 18313;
	setAttr ".tgi[5].ni[29].x" -388.57144165039063;
	setAttr ".tgi[5].ni[29].y" -244.28572082519531;
	setAttr ".tgi[5].ni[29].nvs" 18312;
	setAttr ".tgi[6].tn" -type "string" "leg2foot";
	setAttr ".tgi[6].vl" -type "double2" -4488.151104897468 -1283.3332823382509 ;
	setAttr ".tgi[6].vh" -type "double2" 2732.1987937203626 1480.9523221046227 ;
	setAttr -s 38 ".tgi[6].ni";
	setAttr ".tgi[6].ni[0].x" 445.71429443359375;
	setAttr ".tgi[6].ni[0].y" 650;
	setAttr ".tgi[6].ni[0].nvs" 18313;
	setAttr ".tgi[6].ni[1].x" 2154.28564453125;
	setAttr ".tgi[6].ni[1].y" 184.28572082519531;
	setAttr ".tgi[6].ni[1].nvs" 18313;
	setAttr ".tgi[6].ni[2].x" -1825.7142333984375;
	setAttr ".tgi[6].ni[2].y" 650;
	setAttr ".tgi[6].ni[2].nvs" 18313;
	setAttr ".tgi[6].ni[3].x" -2125.71435546875;
	setAttr ".tgi[6].ni[3].y" 735.71429443359375;
	setAttr ".tgi[6].ni[3].nvs" 18313;
	setAttr ".tgi[6].ni[4].x" 145.71427917480469;
	setAttr ".tgi[6].ni[4].y" 178.57142639160156;
	setAttr ".tgi[6].ni[4].nvs" 18312;
	setAttr ".tgi[6].ni[5].x" 782.85711669921875;
	setAttr ".tgi[6].ni[5].y" -244.28572082519531;
	setAttr ".tgi[6].ni[5].nvs" 18313;
	setAttr ".tgi[6].ni[6].x" -154.28572082519531;
	setAttr ".tgi[6].ni[6].y" 264.28570556640625;
	setAttr ".tgi[6].ni[6].nvs" 18312;
	setAttr ".tgi[6].ni[7].x" 2111.428466796875;
	setAttr ".tgi[6].ni[7].y" -30;
	setAttr ".tgi[6].ni[7].nvs" 18313;
	setAttr ".tgi[6].ni[8].x" -1825.7142333984375;
	setAttr ".tgi[6].ni[8].y" 864.28570556640625;
	setAttr ".tgi[6].ni[8].nvs" 18313;
	setAttr ".tgi[6].ni[9].x" 782.85711669921875;
	setAttr ".tgi[6].ni[9].y" 12.857142448425293;
	setAttr ".tgi[6].ni[9].nvs" 18313;
	setAttr ".tgi[6].ni[10].x" -797.14288330078125;
	setAttr ".tgi[6].ni[10].y" 392.85714721679688;
	setAttr ".tgi[6].ni[10].nvs" 18313;
	setAttr ".tgi[6].ni[11].x" -411.42855834960938;
	setAttr ".tgi[6].ni[11].y" 392.85714721679688;
	setAttr ".tgi[6].ni[11].nvs" 18313;
	setAttr ".tgi[6].ni[12].x" 568.5714111328125;
	setAttr ".tgi[6].ni[12].y" 398.57144165039063;
	setAttr ".tgi[6].ni[12].nvs" 18313;
	setAttr ".tgi[6].ni[13].x" 825.71429443359375;
	setAttr ".tgi[6].ni[13].y" 784.28570556640625;
	setAttr ".tgi[6].ni[13].nvs" 18313;
	setAttr ".tgi[6].ni[14].x" -154.28572082519531;
	setAttr ".tgi[6].ni[14].y" 178.57142639160156;
	setAttr ".tgi[6].ni[14].nvs" 18313;
	setAttr ".tgi[6].ni[15].x" 2111.428466796875;
	setAttr ".tgi[6].ni[15].y" -287.14285278320313;
	setAttr ".tgi[6].ni[15].nvs" 18313;
	setAttr ".tgi[6].ni[16].x" -1054.2857666015625;
	setAttr ".tgi[6].ni[16].y" 178.57142639160156;
	setAttr ".tgi[6].ni[16].nvs" 18312;
	setAttr ".tgi[6].ni[17].x" -117.14286041259766;
	setAttr ".tgi[6].ni[17].y" -330;
	setAttr ".tgi[6].ni[17].nvs" 18312;
	setAttr ".tgi[6].ni[18].x" 145.71427917480469;
	setAttr ".tgi[6].ni[18].y" 92.857139587402344;
	setAttr ".tgi[6].ni[18].nvs" 18313;
	setAttr ".tgi[6].ni[19].x" 1125.7142333984375;
	setAttr ".tgi[6].ni[19].y" -115.71428680419922;
	setAttr ".tgi[6].ni[19].nvs" 18313;
	setAttr ".tgi[6].ni[20].x" -454.28570556640625;
	setAttr ".tgi[6].ni[20].y" -121.42857360839844;
	setAttr ".tgi[6].ni[20].nvs" 18312;
	setAttr ".tgi[6].ni[21].x" -1525.7142333984375;
	setAttr ".tgi[6].ni[21].y" 821.4285888671875;
	setAttr ".tgi[6].ni[21].nvs" 18313;
	setAttr ".tgi[6].ni[22].x" -1011.4285888671875;
	setAttr ".tgi[6].ni[22].y" 564.28570556640625;
	setAttr ".tgi[6].ni[22].nvs" 18312;
	setAttr ".tgi[6].ni[23].x" 2111.428466796875;
	setAttr ".tgi[6].ni[23].y" -458.57144165039063;
	setAttr ".tgi[6].ni[23].nvs" 18312;
	setAttr ".tgi[6].ni[24].x" -154.28572082519531;
	setAttr ".tgi[6].ni[24].y" 478.57144165039063;
	setAttr ".tgi[6].ni[24].nvs" 18312;
	setAttr ".tgi[6].ni[25].x" 140;
	setAttr ".tgi[6].ni[25].y" -158.57142639160156;
	setAttr ".tgi[6].ni[25].nvs" 18314;
	setAttr ".tgi[6].ni[26].x" 145.71427917480469;
	setAttr ".tgi[6].ni[26].y" 650;
	setAttr ".tgi[6].ni[26].nvs" 18312;
	setAttr ".tgi[6].ni[27].x" -154.28572082519531;
	setAttr ".tgi[6].ni[27].y" 564.28570556640625;
	setAttr ".tgi[6].ni[27].nvs" 18312;
	setAttr ".tgi[6].ni[28].x" -454.28570556640625;
	setAttr ".tgi[6].ni[28].y" 7.1428570747375488;
	setAttr ".tgi[6].ni[28].nvs" 18312;
	setAttr ".tgi[6].ni[29].x" -1268.5714111328125;
	setAttr ".tgi[6].ni[29].y" 564.28570556640625;
	setAttr ".tgi[6].ni[29].nvs" 18312;
	setAttr ".tgi[6].ni[30].x" 440;
	setAttr ".tgi[6].ni[30].y" -415.71429443359375;
	setAttr ".tgi[6].ni[30].nvs" 18313;
	setAttr ".tgi[6].ni[31].x" 2111.428466796875;
	setAttr ".tgi[6].ni[31].y" -201.42857360839844;
	setAttr ".tgi[6].ni[31].nvs" 18312;
	setAttr ".tgi[6].ni[32].x" -2125.71435546875;
	setAttr ".tgi[6].ni[32].y" 478.57144165039063;
	setAttr ".tgi[6].ni[32].nvs" 18312;
	setAttr ".tgi[6].ni[33].x" 1682.857177734375;
	setAttr ".tgi[6].ni[33].y" -158.57142639160156;
	setAttr ".tgi[6].ni[33].nvs" 18313;
	setAttr ".tgi[6].ni[34].x" 1940;
	setAttr ".tgi[6].ni[34].y" 184.28572082519531;
	setAttr ".tgi[6].ni[34].nvs" 18313;
	setAttr ".tgi[6].ni[35].x" 145.71427917480469;
	setAttr ".tgi[6].ni[35].y" 564.28570556640625;
	setAttr ".tgi[6].ni[35].nvs" 18313;
	setAttr ".tgi[6].ni[36].x" 1425.7142333984375;
	setAttr ".tgi[6].ni[36].y" -158.57142639160156;
	setAttr ".tgi[6].ni[36].nvs" 18313;
	setAttr ".tgi[6].ni[37].x" 440;
	setAttr ".tgi[6].ni[37].y" -201.42857360839844;
	setAttr ".tgi[6].ni[37].nvs" 18313;
	setAttr ".tgi[7].tn" -type "string" "Untitled_6";
	setAttr ".tgi[7].vl" -type "double2" -1334.0348109357979 -842.85710936501061 ;
	setAttr ".tgi[7].vh" -type "double2" 1197.1300544711421 126.19047117611737 ;
	setAttr -s 11 ".tgi[7].ni";
	setAttr ".tgi[7].ni[0].x" -480;
	setAttr ".tgi[7].ni[0].y" -112.85713958740234;
	setAttr ".tgi[7].ni[0].nvs" 18305;
	setAttr ".tgi[7].ni[1].x" 77.142860412597656;
	setAttr ".tgi[7].ni[1].y" 144.28572082519531;
	setAttr ".tgi[7].ni[1].nvs" 18305;
	setAttr ".tgi[7].ni[2].x" 77.142860412597656;
	setAttr ".tgi[7].ni[2].y" -670;
	setAttr ".tgi[7].ni[2].nvs" 18305;
	setAttr ".tgi[7].ni[3].x" -222.85714721679688;
	setAttr ".tgi[7].ni[3].y" -112.85713958740234;
	setAttr ".tgi[7].ni[3].nvs" 18305;
	setAttr ".tgi[7].ni[4].x" -222.85714721679688;
	setAttr ".tgi[7].ni[4].y" -412.85714721679688;
	setAttr ".tgi[7].ni[4].nvs" 18305;
	setAttr ".tgi[7].ni[5].x" -222.85714721679688;
	setAttr ".tgi[7].ni[5].y" -584.28570556640625;
	setAttr ".tgi[7].ni[5].nvs" 18305;
	setAttr ".tgi[7].ni[6].x" -214.28572082519531;
	setAttr ".tgi[7].ni[6].y" 385.71429443359375;
	setAttr ".tgi[7].ni[6].nvs" 18305;
	setAttr ".tgi[7].ni[7].x" -214.28572082519531;
	setAttr ".tgi[7].ni[7].y" 214.28572082519531;
	setAttr ".tgi[7].ni[7].nvs" 18305;
	setAttr ".tgi[7].ni[8].x" -222.85714721679688;
	setAttr ".tgi[7].ni[8].y" -927.14288330078125;
	setAttr ".tgi[7].ni[8].nvs" 18305;
	setAttr ".tgi[7].ni[9].x" -480;
	setAttr ".tgi[7].ni[9].y" -927.14288330078125;
	setAttr ".tgi[7].ni[9].nvs" 18305;
	setAttr ".tgi[7].ni[10].x" -822.85711669921875;
	setAttr ".tgi[7].ni[10].y" -412.85714721679688;
	setAttr ".tgi[7].ni[10].nvs" 18305;
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
connectAttr "legGlobal_L_output.rolledAnkle" "leg_L_input.rolledAnkle";
connectAttr "legGlobal_L_output.upVectorWorld" "leg_L_input.upVectorFrame";
connectAttr "output_end_srt.wm" "leg_L_input.endWorld";
connectAttr "legGlobal_L_output.rawAnkleControl" "leg_L_input.rawAnkleControl";
connectAttr "leg_L_ankle_blend_mtx.omat" "leg_L_output.chainEnd";
connectAttr "leg_L_hipWorld_srt.ot" "leg_L_IK_srtBuffer.t";
connectAttr "leg_L_IK_tension_rot.eux" "leg_L_IK_srtBuffer.rx";
connectAttr "leg_L_IK_tension_rot.euy" "leg_L_IK_srtBuffer.ry";
connectAttr "leg_L_IK_tension_rot.euz" "leg_L_IK_srtBuffer.rz";
connectAttr "leg_L_hipWorld_srt.os" "leg_L_IK_srtBuffer.s";
connectAttr "leg_L_IK_solver_xpr.out[1]" "leg_L_hip_srt.rx";
connectAttr "leg_L_IK_upVectoringAngle.euy" "leg_L_hip_srt.ry";
connectAttr "leg_L_configParameters.femurLength" "leg_L_femurEnd_srt.tz";
connectAttr "leg_L_IK_solver_xpr.out[0]" "leg_L_tibiaStart_srt.rx";
connectAttr "leg_L_configParameters.tibiaLength" "leg_L_tibiaEnd_srt.tz";
connectAttr "leg_L_FK_start_srt.ot" "leg_L_fk01_ctrl_srtBuffer.t";
connectAttr "leg_L_FK_start_srt.or" "leg_L_fk01_ctrl_srtBuffer.r";
connectAttr "leg_L_configParameters.femurLength" "leg_L_fk01_ctrlShape.cp[4].zv"
		;
connectAttr "leg_L_configParameters.femurLength" "leg_L_fk02_ctrl_srtBuffer.tz";
connectAttr "leg_L_tibiaStart_srt.rx" "leg_L_fk02_ctrl_srtBuffer.rx";
connectAttr "leg_L_configParameters.tibiaLength" "leg_L_fk02_ctrlShape.cp[4].zv"
		;
connectAttr "leg_L_guide_globalAnkleInfk02Space_srt.ot" "leg_L_fk03_ctrl_srtBuffer.t"
		;
connectAttr "leg_L_guide_globalAnkleInfk02Space_srt.or" "leg_L_fk03_ctrl_srtBuffer.r"
		;
connectAttr "leg_L_limitedWorldAnkle_translate.o3" "leg_L_limitedAnkle_srt.t";
connectAttr "leg_L_rolledAnkle_frame_srt.or" "leg_L_limitedAnkle_srt.r";
connectAttr "leg_L_guide_femurLength.d" "leg_L_configParameters.femurLength";
connectAttr "leg_L_guide_tibiaLength.d" "leg_L_configParameters.tibiaLength";
connectAttr "leg_L_guide_hipPos_ctrl.m" "leg_L_configParameters.hipOffsetIK";
connectAttr "leg_L_guide_ikHip_local_mtx.o" "leg_L_configParameters.hipOffsetFK"
		;
connectAttr "leg_L_fkik_j01_blended_rot.o" "leg_L_j01_srt.r";
connectAttr "leg_L_hipWorld_srt.ot" "leg_L_j01_srt.t";
connectAttr "leg_L_configParameters.femurLength" "leg_L_j02_srt.tz";
connectAttr "leg_L_fkik_j02_blended_rot.o" "leg_L_j02_srt.r";
connectAttr "leg_L_configParameters.tibiaLength" "leg_L_j03_srt.tz";
connectAttr "leg_L_configParameters.femurLength" "leg_L_toolParameters.toSwap[0].guided"
		;
connectAttr "leg_L_configParameters.tibiaLength" "leg_L_toolParameters.toSwap[1].guided"
		;
connectAttr "leg_L_fk01_ctrlShape.cp[4].zv" "leg_L_toolParameters.toSwap[2].guided"
		;
connectAttr "leg_L_fk02_ctrlShape.cp[4].zv" "leg_L_toolParameters.toSwap[3].guided"
		;
connectAttr "leg_L_fk02_ctrl_srtBuffer.rx" "leg_L_toolParameters.toSwap[4].guided"
		;
connectAttr "leg_L_fk03_ctrl_srtBuffer.t" "leg_L_toolParameters.toSwap[7].guided"
		;
connectAttr "leg_L_fk03_ctrl_srtBuffer.r" "leg_L_toolParameters.toSwap[8].guided"
		;
connectAttr "leg_L_configParameters.hipOffsetFK" "leg_L_toolParameters.toSwap[9].guided"
		;
connectAttr "leg_L_guide_hipInput_srt.msg" "leg_L_toolParameters.toDelete[0]";
connectAttr "leg_L_guide_hip_world_srt.msg" "leg_L_toolParameters.toDelete[1]";
connectAttr "leg_L_guide_hipPos_ctrl.msg" "leg_L_toolParameters.toDelete[2]";
connectAttr "leg_L_guide_ankle_world_srt.msg" "leg_L_toolParameters.toDelete[3]"
		;
connectAttr "leg_L_guide_femurLength.msg" "leg_L_toolParameters.toDelete[4]";
connectAttr "leg_L_guide_tibiaLength.msg" "leg_L_toolParameters.toDelete[5]";
connectAttr "leg_L_guide_knee_world_srt.msg" "leg_L_toolParameters.toDelete[6]";
connectAttr "leg_L_guide_hip2UpV_vec.msg" "leg_L_toolParameters.toDelete[7]";
connectAttr "leg_L_guide_globalAnkleInfk02Space_srt.msg" "leg_L_toolParameters.toDelete[8]"
		;
connectAttr "leg_L_guide_globalAnkleInfk02Space.msg" "leg_L_toolParameters.toDelete[9]"
		;
connectAttr "leg_L_guide_ikHip_local_mtx.msg" "leg_L_toolParameters.toDelete[11]"
		;
connectAttr "leg_L_guide_endWorldInverse_mtx.msg" "leg_L_toolParameters.toDelete[12]"
		;
connectAttr "leg_L_guide_hipInput_srt.or" "leg_L_guide_hipPos_ctrl_srtBuffer.r";
connectAttr "leg_L_guide_hipInput_srt.os" "leg_L_guide_hipPos_ctrl_srtBuffer.s";
connectAttr "leg_L_guide_hipInput_srt.ot" "leg_L_guide_hipPos_ctrl_srtBuffer.t";
connectAttr "leg_L_guide_kneeUpV_aim_cns.cr" "leg_L_guide_kneePos_ctrl_srtBuffer.r"
		;
connectAttr "leg_L_guide_hipPos_ctrl.wim" "leg_L_guide_kneeUpV_aim_cns.cpim";
connectAttr "leg_L_input.rawAnkleControl" "leg_L_guide_kneeUpV_aim_cns.tg[0].tpm"
		;
connectAttr "leg_L_guide_hip2UpV_vec.o3" "leg_L_guide_kneeUpV_aim_cns.wu";
connectAttr "output_master_srt.wm" "legGlobal_L_input.endWorld";
connectAttr "legGlobal_L_worldAnkle_rolled_srt.wm" "legGlobal_L_output.rolledAnkle"
		;
connectAttr "|legGlobal_L_cmpnt|control|legGlobal_L_upVector_ctrl_srtBuffer|legGlobal_L_upVector_ctrl.wm" "legGlobal_L_output.upVectorWorld"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.wm" "legGlobal_L_output.rawAnkleControl"
		;
connectAttr "legGlobal_L_roll_tarsi_srt.rx" "legGlobal_L_output.toeAngle";
connectAttr "legGlobal_L_tarsi_rolledAngle.a" "legGlobal_L_output.tarsiAngle";
connectAttr "animParameters_roll.o" "legGlobal_L_animParameters.roll";
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
connectAttr "legGlobal_L_worldAnkle_ctrl_translateX.o" "legGlobal_L_worldAnkle_ctrl.tx"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_translateY.o" "legGlobal_L_worldAnkle_ctrl.ty"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_translateZ.o" "legGlobal_L_worldAnkle_ctrl.tz"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_rotateX.o" "legGlobal_L_worldAnkle_ctrl.rx"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_rotateZ.o" "legGlobal_L_worldAnkle_ctrl.rz"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_rotateY.o" "legGlobal_L_worldAnkle_ctrl.ry"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_visibility.o" "legGlobal_L_worldAnkle_ctrl.v"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_scaleX.o" "legGlobal_L_worldAnkle_ctrl.sx"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_scaleY.o" "legGlobal_L_worldAnkle_ctrl.sy"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_scaleZ.o" "legGlobal_L_worldAnkle_ctrl.sz"
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
connectAttr "legGlobal_L_configParameters.tarsiLength" "foot_L_input.tarsiLength"
		;
connectAttr "legGlobal_L_configParameters.toeLength" "foot_L_input.toeLength";
connectAttr "leg_L_output.chainEnd" "foot_L_input.startMtx";
connectAttr "legGlobal_L_output.toeAngle" "foot_L_input.toeAngle";
connectAttr "legGlobal_L_output.tarsiAngle" "foot_L_input.tarsiAngle";
connectAttr "foot_L_start_mtx2srt.ot" "foot_L_ankleSpace_srt.t";
connectAttr "foot_L_start_mtx2srt.or" "foot_L_ankleSpace_srt.r";
connectAttr "foot_L_input.tarsiAngle" "foot_L_tarsii_ctrl_srtBuffer.rx";
connectAttr "foot_L_input.tarsiLength" "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|diagnostic_ankle|diagnostic_tarsi.tz"
		;
connectAttr "foot_L_input.toeAngle" "foot_L_toes_ctrl_srtBuffer.rx";
connectAttr "foot_L_input.tarsiLength" "foot_L_toes_ctrl_srtBuffer.tz";
connectAttr "foot_L_input.toeLength" "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|foot_L_toes_ctrl_srtBuffer|foot_L_toes_ctrl|diagnostic_toes|diagnostic_tip.tz"
		;
connectAttr "godNode_M_master_ctrl_wMtx_output_fNode.ot" "output_master_srt.t";
connectAttr "godNode_M_master_ctrl_wMtx_output_fNode.or" "output_master_srt.r";
connectAttr "godNode_M_master_ctrl_wMtx_output_fNode.os" "output_master_srt.s";
connectAttr "godNode_M_debuffer_com_output_srt.ot" "output_com_srt.t";
connectAttr "godNode_M_debuffer_com_output_srt.or" "output_com_srt.r";
connectAttr "godNode_M_debuffer_com_output_srt.os" "output_com_srt.s";
connectAttr "godNode_M_debuffer_end_output_srt.or" "output_end_srt.r";
connectAttr "godNode_M_debuffer_end_output_srt.os" "output_end_srt.s";
connectAttr "godNode_M_debuffer_end_output_srt.ot" "output_end_srt.t";
connectAttr "guide_world_ctrl.t" "godNode_M_master_ctrl_srtBuffer.t";
connectAttr "guide_world_ctrl.r" "godNode_M_master_ctrl_srtBuffer.r";
connectAttr "guide_world_ctrl.s" "godNode_M_master_ctrl_srtBuffer.s";
connectAttr "guide_com_ctrl.t" "godNode_M_com_ctrl_srtBuffer.t";
connectAttr "guide_com_ctrl.r" "godNode_M_com_ctrl_srtBuffer.r";
connectAttr "guide_com_ctrl.s" "godNode_M_com_ctrl_srtBuffer.s";
connectAttr "guide_end_ctrl.t" "godNode_M_end_ctrl_srtBuffer.t";
connectAttr "guide_end_ctrl.r" "godNode_M_end_ctrl_srtBuffer.r";
connectAttr "guide_end_ctrl.s" "godNode_M_end_ctrl_srtBuffer.s";
connectAttr "legGlobal_R_output.rawAnkleControl" "leg_R_input.rawAnkleControl";
connectAttr "legGlobal_R_output.upVectorWorld" "leg_R_input.upVectorFrame";
connectAttr "legGlobal_R_output.rolledAnkle" "leg_R_input.rolledAnkle";
connectAttr "output_end_srt.wm" "leg_R_input.endWorld";
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
connectAttr "multDoubleLinear1.o" "leg_R_fk01_ctrl_srtBuffer.tx";
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
connectAttr "output_master_srt.wm" "legGlobal_R_input.endWorld";
connectAttr "legGlobal_R_worldAnkle_ctrl.wm" "legGlobal_R_output.rawAnkleControl"
		;
connectAttr "|legGlobal_R_cmpnt|control|legGlobal_R_upVector_ctrl_srtBuffer|legGlobal_R_upVector_ctrl.wm" "legGlobal_R_output.upVectorWorld"
		;
connectAttr "legGlobal_R_worldAnkle_rolled_srt.wm" "legGlobal_R_output.rolledAnkle"
		;
connectAttr "legGlobal_R_roll_tarsi_srt.rx" "legGlobal_R_output.toeAngle";
connectAttr "legGlobal_R_tarsi_rolledAngle.a" "legGlobal_R_output.tarsiAngle";
connectAttr "legGlobal_R_guide_ankle_world_srt.ot" "legGlobal_R_ankle_rest_srt.t"
		;
connectAttr "legGlobal_R_roll_world_srt.r" "legGlobal_R_ankle_rest_srt.r";
connectAttr "legGlobal_R_ankleFramed_tarsi_srt.or" "legGlobal_R_ankle_rolled_srt.r"
		;
connectAttr "legGlobal_R_ankleFramed_tarsi_srt.ot" "legGlobal_R_ankle_rolled_srt.t"
		;
connectAttr "legGlobal_R_guide_global_ctrl.r" "legGlobal_R_roll_world_srt.r";
connectAttr "legGlobal_R_guide_global_ctrl.s" "legGlobal_R_roll_world_srt.s";
connectAttr "legGlobal_R_guide_global_ctrl.t" "legGlobal_R_roll_world_srt.t";
connectAttr "legGlobal_R_heelback_roll_UC.o" "legGlobal_R_roll_heel_srt.rx";
connectAttr "legGlobal_R_guide_heel_ctrl.t" "legGlobal_R_roll_heel_srt.t";
connectAttr "legGlobal_R_toeRollOffset_angle.o" "legGlobal_R_roll_tip_srt.rx";
connectAttr "legGlobal_R_configParameters.plantLength" "legGlobal_R_roll_tip_srt.tz"
		;
connectAttr "legGlobal_R_tarsiRollOffset_angle.o" "legGlobal_R_roll_tarsi_srt.rx"
		;
connectAttr "legGlobal_R_configParameters.toeLength" "legGlobal_R_roll_tarsi_srt.tz"
		;
connectAttr "legGlobal_R_configParameters.tarsiLength" "legGlobal_R_roll_tarsiEnd_srt.tz"
		;
connectAttr "legGlobal_R_ankleReparent_srt.ot" "legGlobal_R_worldAnkle_ctrl_srtBuffer.t"
		;
connectAttr "legGlobal_R_ankleReparent_srt.or" "legGlobal_R_worldAnkle_ctrl_srtBuffer.r"
		;
connectAttr "legGlobal_R_upVecReparent_srt.or" "legGlobal_R_upVector_ctrl_srtBuffer.r"
		;
connectAttr "legGlobal_R_upVecReparent_srt.ot" "legGlobal_R_upVector_ctrl_srtBuffer.t"
		;
connectAttr "legGlobal_R_guide_toe_rest_angle.a" "legGlobal_R_configParameters.toeRest"
		;
connectAttr "legGlobal_R_guide_tarsi2World_rest_angle.a" "legGlobal_R_configParameters.ankleRest"
		;
connectAttr "legGlobal_R_ankleFramed_rollOffset_srt.o" "legGlobal_R_worldAnkle_rolled_srt.t"
		;
connectAttr "legGlobal_R_worldAnkle_ctrl_world_srt.or" "legGlobal_R_worldAnkle_rolled_srt.r"
		;
connectAttr "legGlobal_R_configParameters.ankleGlobalOffset" "legGlobal_R_toolParameters.toSwap[0].guided"
		;
connectAttr "legGlobal_R_guide_ankle_ctrl.wm" "legGlobal_R_toolParameters.toSwap[0].origin"
		;
connectAttr "legGlobal_R_configParameters.plantLength" "legGlobal_R_toolParameters.toSwap[1].guided"
		;
connectAttr "legGlobal_R_guide_tip_ctrl.tz" "legGlobal_R_toolParameters.toSwap[1].origin"
		;
connectAttr "legGlobal_R_configParameters.tarsiLength" "legGlobal_R_toolParameters.toSwap[2].guided"
		;
connectAttr "legGlobal_R_guide_tarsi_length.d" "legGlobal_R_toolParameters.toSwap[2].origin"
		;
connectAttr "legGlobal_R_configParameters.tarsirest" "legGlobal_R_toolParameters.toSwap[3].guided"
		;
connectAttr "legGlobal_R_guide_tarsi_rest_negate_angle.o" "legGlobal_R_toolParameters.toSwap[3].origin"
		;
connectAttr "legGlobal_R_configParameters.toeLength" "legGlobal_R_toolParameters.toSwap[4].guided"
		;
connectAttr "legGlobal_R_guide_toe_length.d" "legGlobal_R_toolParameters.toSwap[4].origin"
		;
connectAttr "legGlobal_R_configParameters.upVecGlobalOffset" "legGlobal_R_toolParameters.toSwap[5].guided"
		;
connectAttr "legGlobal_R_guide_upVector_ctrl.m" "legGlobal_R_toolParameters.toSwap[5].origin"
		;
connectAttr "legGlobal_R_guide_tarsi2World_rest_angle.msg" "legGlobal_R_toolParameters.toDelete[0]"
		;
connectAttr "legGlobal_R_guide_tarsi2Toe_rest_angle.msg" "legGlobal_R_toolParameters.toDelete[1]"
		;
connectAttr "legGlobal_R_guide_tarsi_direction_vec.msg" "legGlobal_R_toolParameters.toDelete[2]"
		;
connectAttr "legGlobal_R_guide_toe_direction_vec.msg" "legGlobal_R_toolParameters.toDelete[3]"
		;
connectAttr "legGlobal_R_guide_ankle_world_srt.msg" "legGlobal_R_toolParameters.toDelete[4]"
		;
connectAttr "legGlobal_R_guide_toe_rest_angle.msg" "legGlobal_R_toolParameters.toDelete[5]"
		;
connectAttr "legGlobal_R_guide_tarsi_length.msg" "legGlobal_R_toolParameters.toDelete[6]"
		;
connectAttr "legGlobal_R_guide_toe_length.msg" "legGlobal_R_toolParameters.toDelete[7]"
		;
connectAttr "legGlobal_R_guide_tarsi_rest_negate_angle.msg" "legGlobal_R_toolParameters.toDelete[8]"
		;
connectAttr "legGlobal_R_configParameters.tarsiLength" "foot_R_input.tarsiLength"
		;
connectAttr "legGlobal_R_configParameters.toeLength" "foot_R_input.toeLength";
connectAttr "legGlobal_R_output.tarsiAngle" "foot_R_input.tarsiAngle";
connectAttr "legGlobal_R_output.toeAngle" "foot_R_input.toeAngle";
connectAttr "leg_R_output.chainEnd" "foot_R_input.startMtx";
connectAttr "foot_R_start_mtx2srt.ot" "foot_R_ankleSpace_srt.t";
connectAttr "foot_R_start_mtx2srt.or" "foot_R_ankleSpace_srt.r";
connectAttr "foot_R_input.tarsiAngle" "foot_R_tarsii_ctrl_srtBuffer.rx";
connectAttr "foot_R_input.tarsiLength" "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|diagnostic_ankle|diagnostic_tarsi.tz"
		;
connectAttr "foot_R_input.toeAngle" "foot_R_toes_ctrl_srtBuffer.rx";
connectAttr "foot_R_input.tarsiLength" "foot_R_toes_ctrl_srtBuffer.tz";
connectAttr "foot_R_input.toeLength" "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|foot_R_toes_ctrl_srtBuffer|foot_R_toes_ctrl|diagnostic_toes|diagnostic_tip.tz"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "leg_L_rolledAnkle_ctrl_world_mtx2srt.ot" "leg_L_hip2Ankle_displacement.i3[0]"
		;
connectAttr "leg_L_hipWorld_srt.ot" "leg_L_hip2Ankle_displacement.i3[1]";
connectAttr "leg_L_hip2Ankle_clamped_displacement.o" "leg_L_limitedWorldAnkle_translate.i3[0]"
		;
connectAttr "leg_L_hipWorld_srt.ot" "leg_L_limitedWorldAnkle_translate.i3[1]";
connectAttr "leg_L_hip2Ankle_displacement.o3" "leg_L_hip2ankle_direction_normal.i1"
		;
connectAttr "leg_L_hip2ankle_direction_normal.o" "leg_L_hip2Ankle_clamped_displacement.i1"
		;
connectAttr "leg_L_ankle2hip_clampedDistance.opr" "leg_L_hip2Ankle_clamped_displacement.i2x"
		;
connectAttr "leg_L_ankle2hip_clampedDistance.opr" "leg_L_hip2Ankle_clamped_displacement.i2y"
		;
connectAttr "leg_L_ankle2hip_clampedDistance.opr" "leg_L_hip2Ankle_clamped_displacement.i2z"
		;
connectAttr "leg_L_lengthLimit_fNode.o" "leg_L_ankle2hip_clampedDistance.mxr";
connectAttr "leg_L_hip2ankle_distance.d" "leg_L_ankle2hip_clampedDistance.ipr";
connectAttr "leg_L_rolledAnkle_ctrl_world_mtx2srt.ot" "leg_L_hip2ankle_distance.p1"
		;
connectAttr "leg_L_hipWorld_srt.ot" "leg_L_hip2ankle_distance.p2";
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_roll_toe_fCurve.i";
connectAttr "legGlobal_L_animParameters.roll" "legGlobal_L_roll_UC.i";
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_roll_tarsi_fCurve.i";
connectAttr "legGlobal_L_roll_UC.o" "legGlobal_L_heelBack_rollClamp.ipb";
connectAttr "legGlobal_L_heelBack_rollClamp.opb" "legGlobal_L_heelback_roll_UC.i"
		;
connectAttr "legGlobal_L_roll_tarsiEnd_srt.wm" "legGlobal_L_roll_tarsi_world_mtx.imat"
		;
connectAttr "leg_L_input.rolledAnkle" "leg_L_rolledAnkle_ctrl_world_mtx2srt.imat"
		;
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.ot" "legGlobal_L_tarsi_worldDirection_vec3.i3[0]"
		;
connectAttr "legGlobal_L_roll_tarsi_world_mtx.ot" "legGlobal_L_tarsi_worldDirection_vec3.i3[1]"
		;
connectAttr "legGlobal_L_roll_tarsi_srt.wm" "legGlobal_L_roll_toes_world_mtx2srt.imat"
		;
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.o3" "legGlobal_L_tarsi_rolledAngle.v1"
		;
connectAttr "foot_L_input.startMtx" "foot_L_start_mtx2srt.imat";
connectAttr "leg_L_hipWorld_mtx.o" "leg_L_hipWorld_srt.imat";
connectAttr "leg_L_IK_ankleDisplacement_vec.o3" "leg_L_IK_tension_rot.v2";
connectAttr "leg_L_limitedAnkleWorld_srt.ot" "leg_L_IK_ankleDisplacement_vec.i3[0]"
		;
connectAttr "leg_L_hipWorld_srt.ot" "leg_L_IK_ankleDisplacement_vec.i3[1]";
connectAttr "leg_L_configParameters.femurLength" "leg_L_IK_solver_xpr.in[0]";
connectAttr "leg_L_configParameters.tibiaLength" "leg_L_IK_solver_xpr.in[1]";
connectAttr "leg_L_ankle2hip_clampedDistance.opr" "leg_L_IK_solver_xpr.in[2]";
connectAttr ":time1.o" "leg_L_IK_solver_xpr.tim";
connectAttr "leg_L_input.upVectorFrame" "leg_L_IK_upVector_hipFramed_mtx.i[0]";
connectAttr "leg_L_IK_srtBuffer.wim" "leg_L_IK_upVector_hipFramed_mtx.i[1]";
connectAttr "leg_L_IK_upVector_hipFramed_mtx.o" "leg_L_IK_upVector_hipYProjected_srt.imat"
		;
connectAttr "leg_L_IK_upVector_hipYProjected_srt.otz" "leg_L_IK_upVectoringAngle.v2z"
		;
connectAttr "leg_L_IK_upVector_hipYProjected_srt.otx" "leg_L_IK_upVectoringAngle.v2x"
		;
connectAttr "legGlobal_L_configParameters.toeRest" "legGlobal_L_toeRollOffset_angle.ib"
		;
connectAttr "legGlobal_L_roll_toe_fCurve.o" "legGlobal_L_toeRollOffset_angle.ia"
		;
connectAttr "legGlobal_L_configParameters.tarsirest" "legGlobal_L_tarsiRollOffset_angle.ib"
		;
connectAttr "legGlobal_L_roll_tarsi_fCurve.o" "legGlobal_L_tarsiRollOffset_angle.ia"
		;
connectAttr "legGlobal_L_roll_tarsiEnd_srt.wm" "legGlobal_L_ankleFramed_tarsi_mtx.i[0]"
		;
connectAttr "legGlobal_L_ankle_rest_srt.wim" "legGlobal_L_ankleFramed_tarsi_mtx.i[1]"
		;
connectAttr "legGlobal_L_ankleFramed_tarsi_mtx.o" "legGlobal_L_ankleFramed_tarsi_srt.imat"
		;
connectAttr "legGlobal_L_ankle_rolled_srt.t" "legGlobal_L_ankleFramed_rollOffset_srt.ip"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.wm" "legGlobal_L_ankleFramed_rollOffset_srt.im"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.wm" "legGlobal_L_worldAnkle_ctrl_world_srt.imat"
		;
connectAttr "godNode_M_debuffer_com_output_mtx.o" "godNode_M_debuffer_com_output_srt.imat"
		;
connectAttr "godNode_M_debuffer_end_output_mtx.o" "godNode_M_debuffer_end_output_srt.imat"
		;
connectAttr "godNode_M_masterOffset_ctrl.wm" "godNode_M_master_ctrl_wMtx_output_fNode.imat"
		;
connectAttr "godNode_M_comOffset_ctrl.wm" "godNode_M_debuffer_com_output_mtx.i[0]"
		;
connectAttr "output_master_srt.wim" "godNode_M_debuffer_com_output_mtx.i[1]";
connectAttr "godNode_M_endOffset_ctrl.wm" "godNode_M_debuffer_end_output_mtx.i[0]"
		;
connectAttr "output_com_srt.wim" "godNode_M_debuffer_end_output_mtx.i[1]";
connectAttr "leg_L_configParameters.hipOffsetIK" "leg_L_hipWorld_mtx.i[1]";
connectAttr "leg_L_input.endWorld" "leg_L_hipWorld_mtx.i[2]";
connectAttr "legGlobal_L_configParameters.ankleGlobalOffset" "legGlobal_L_ankleReparent_mtxMult.i[0]"
		;
connectAttr "legGlobal_L_input.endWorld" "legGlobal_L_ankleReparent_mtxMult.i[1]"
		;
connectAttr "legGlobal_L_ankleReparent_mtxMult.o" "legGlobal_L_ankleReparent_srt.imat"
		;
connectAttr "legGlobal_L_configParameters.upVecGlobalOffset" "legGlobal_L_upVecReparent_mtxMult.i[0]"
		;
connectAttr "legGlobal_L_input.endWorld" "legGlobal_L_upVecReparent_mtxMult.i[1]"
		;
connectAttr "legGlobal_L_upVecReparent_mtxMult.o" "legGlobal_L_upVecReparent_srt.imat"
		;
connectAttr "leg_L_limitedAnkle_srt.wm" "leg_L_limitedAnkleWorld_srt.imat";
connectAttr "leg_L_fk01_ctrl_world_mtx.or" "leg_L_fkik_j01_blended_rot.ia";
connectAttr "leg_L_hip_rot.or" "leg_L_fkik_j01_blended_rot.ib";
connectAttr "leg_L_animParameters.FKIK_blend" "leg_L_fkik_j01_blended_rot.wb";
connectAttr "leg_L_fkik_blend_complement.o" "leg_L_fkik_j01_blended_rot.wa";
connectAttr "leg_L_hip_srt.wm" "leg_L_hip_rot.imat";
connectAttr "leg_L_fk01_ctrl.wm" "leg_L_fk01_ctrl_world_mtx.imat";
connectAttr "leg_L_animParameters.FKIK_blend" "leg_L_fkik_blend_complement.ib";
connectAttr "leg_L_fk02_ctrl.wm" "leg_L_fk02reframed01_mtx.i[0]";
connectAttr "leg_L_fk01_ctrl.wim" "leg_L_fk02reframed01_mtx.i[1]";
connectAttr "leg_L_fk02reframed01_mtx.o" "leg_L_fk02reframed01_rot.imat";
connectAttr "leg_L_fk02reframed01_rot.or" "leg_L_fkik_j02_blended_rot.ia";
connectAttr "leg_L_tibiaStart_srt.rx" "leg_L_fkik_j02_blended_rot.ibx";
connectAttr "leg_L_animParameters.FKIK_blend" "leg_L_fkik_j02_blended_rot.wb";
connectAttr "leg_L_fkik_blend_complement.o" "leg_L_fkik_j02_blended_rot.wa";
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
connectAttr "|legGlobal_L_cmpnt|control|roll_mechanics.msg" "hyperLayout1.hyp[5].dn"
		;
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
connectAttr "hyperLayout2.msg" "leg_L_container.hl";
connectAttr "leg_L_cmpnt.msg" "leg_L_container.cbp[0]";
connectAttr "leg_L_cmpnt.msg" "leg_L_container.cbc[0]";
connectAttr "leg_L_fk01_ctrl.msg" "leg_L_container.pni[0].pnod";
connectAttr "leg_L_fk02_ctrl.msg" "leg_L_container.pni[1].pnod";
connectAttr "leg_L_cmpnt.msg" "hyperLayout2.hyp[0].dn";
connectAttr "leg_L_input.msg" "hyperLayout2.hyp[1].dn";
connectAttr "leg_L_output.msg" "hyperLayout2.hyp[2].dn";
connectAttr "|leg_L_cmpnt|control.msg" "hyperLayout2.hyp[3].dn";
connectAttr "leg_L_animParameters.msg" "hyperLayout2.hyp[4].dn";
connectAttr "leg_L_IK_srtBuffer.msg" "hyperLayout2.hyp[5].dn";
connectAttr "leg_L_hip_srt.msg" "hyperLayout2.hyp[6].dn";
connectAttr "leg_L_femurEnd_srt.msg" "hyperLayout2.hyp[7].dn";
connectAttr "leg_L_tibiaStart_srt.msg" "hyperLayout2.hyp[8].dn";
connectAttr "leg_L_tibiaEnd_srt.msg" "hyperLayout2.hyp[9].dn";
connectAttr "leg_L_FK_hrc.msg" "hyperLayout2.hyp[10].dn";
connectAttr "leg_L_fk01_ctrl_srtBuffer.msg" "hyperLayout2.hyp[11].dn";
connectAttr "leg_L_fk01_ctrl.msg" "hyperLayout2.hyp[12].dn";
connectAttr "leg_L_fk02_ctrl_srtBuffer.msg" "hyperLayout2.hyp[13].dn";
connectAttr "leg_L_fk02_ctrl.msg" "hyperLayout2.hyp[14].dn";
connectAttr "|leg_L_cmpnt|deform.msg" "hyperLayout2.hyp[15].dn";
connectAttr "leg_L_j01_srt.msg" "hyperLayout2.hyp[16].dn";
connectAttr "leg_L_j02_srt.msg" "hyperLayout2.hyp[17].dn";
connectAttr "leg_L_j03_srt.msg" "hyperLayout2.hyp[18].dn";
connectAttr "|leg_L_cmpnt|guide.msg" "hyperLayout2.hyp[19].dn";
connectAttr "leg_L_configParameters.msg" "hyperLayout2.hyp[20].dn";
connectAttr "leg_L_IK_tension_rot.msg" "hyperLayout2.hyp[21].dn";
connectAttr "leg_L_IK_upVectoringAngle.msg" "hyperLayout2.hyp[22].dn";
connectAttr "leg_L_fkik_blend_complement.msg" "hyperLayout2.hyp[23].dn";
connectAttr "leg_L_fkik_j02_blended_rot.msg" "hyperLayout2.hyp[24].dn";
connectAttr "leg_L_fkik_j01_blended_rot.msg" "hyperLayout2.hyp[25].dn";
connectAttr "leg_L_fk01_ctrl_world_mtx.msg" "hyperLayout2.hyp[26].dn";
connectAttr "leg_L_fk02reframed01_rot.msg" "hyperLayout2.hyp[27].dn";
connectAttr "leg_L_hip_rot.msg" "hyperLayout2.hyp[29].dn";
connectAttr "leg_L_hipWorld_srt.msg" "hyperLayout2.hyp[30].dn";
connectAttr "leg_L_IK_upVector_hipYProjected_srt.msg" "hyperLayout2.hyp[31].dn";
connectAttr "leg_L_limitedAnkleWorld_srt.msg" "hyperLayout2.hyp[32].dn";
connectAttr "leg_L_IK_solver_xpr.msg" "hyperLayout2.hyp[34].dn";
connectAttr "leg_L_fk02reframed01_mtx.msg" "hyperLayout2.hyp[35].dn";
connectAttr "leg_L_IK_upVector_hipFramed_mtx.msg" "hyperLayout2.hyp[36].dn";
connectAttr "leg_L_IK_ankleDisplacement_vec.msg" "hyperLayout2.hyp[37].dn";
connectAttr "|leg_L_cmpnt|control|leg_L_IK_srtBuffer|leg_L_hip_srt|diagnosticCube_geoShape.msg" "hyperLayout2.hyp[38].dn"
		;
connectAttr "leg_L_fk01_ctrlShape.msg" "hyperLayout2.hyp[39].dn";
connectAttr "leg_L_fk02_ctrlShape.msg" "hyperLayout2.hyp[40].dn";
connectAttr "leg_L_toolParameters.msg" "hyperLayout2.hyp[41].dn";
connectAttr "leg_L_rolledAnkle_ctrl_world_mtx2srt.msg" "hyperLayout2.hyp[42].dn"
		;
connectAttr "leg_L_totalLength_fNode_add.msg" "hyperLayout2.hyp[43].dn";
connectAttr "leg_L_limitedWorldAnkle_translate.msg" "hyperLayout2.hyp[44].dn";
connectAttr "leg_L_lengthLimit_fNode.msg" "hyperLayout2.hyp[45].dn";
connectAttr "leg_L_ankle2hip_clampedDistance.msg" "hyperLayout2.hyp[46].dn";
connectAttr "leg_L_hip2Ankle_clamped_displacement.msg" "hyperLayout2.hyp[47].dn"
		;
connectAttr "leg_L_hip2ankle_distance.msg" "hyperLayout2.hyp[48].dn";
connectAttr "leg_L_hip2Ankle_displacement.msg" "hyperLayout2.hyp[50].dn";
connectAttr "leg_L_hip2ankle_direction_normal.msg" "hyperLayout2.hyp[51].dn";
connectAttr "leg_L_limitedAnkle_srt.msg" "hyperLayout2.hyp[52].dn";
connectAttr "leg_L_rolledAnkle_frame_srt.msg" "hyperLayout2.hyp[53].dn";
connectAttr "leg_L_hipWorld_mtx.msg" "hyperLayout2.hyp[55].dn";
connectAttr "leg_L_guide_femurLength.msg" "hyperLayout2.hyp[56].dn";
connectAttr "leg_L_guide_tibiaLength.msg" "hyperLayout2.hyp[57].dn";
connectAttr "leg_L_FK_start_srt.msg" "hyperLayout2.hyp[58].dn";
connectAttr "leg_L_guide_upVector_srt.msg" "hyperLayout2.hyp[59].dn";
connectAttr "leg_L_guide_knee_world_srt.msg" "hyperLayout2.hyp[60].dn";
connectAttr "leg_L_guide_hipInput_srt.msg" "hyperLayout2.hyp[61].dn";
connectAttr "leg_L_guide_hip_world_srt.msg" "hyperLayout2.hyp[62].dn";
connectAttr "leg_L_guide_ankle_world_srt.msg" "hyperLayout2.hyp[63].dn";
connectAttr "leg_L_guide_hipPos_ctrl_srtBuffer.msg" "hyperLayout2.hyp[64].dn";
connectAttr "leg_L_guide_hipPos_ctrl.msg" "hyperLayout2.hyp[65].dn";
connectAttr "leg_L_guide_hipPos_ctrlShape.msg" "hyperLayout2.hyp[66].dn";
connectAttr "leg_L_guide_kneePos_ctrl_srtBuffer.msg" "hyperLayout2.hyp[67].dn";
connectAttr "leg_L_guide_kneePos_ctrl.msg" "hyperLayout2.hyp[68].dn";
connectAttr "leg_L_guide_kneePos_ctrlShape.msg" "hyperLayout2.hyp[69].dn";
connectAttr "leg_L_guide_kneeUpV_aim_cns.msg" "hyperLayout2.hyp[70].dn";
connectAttr "leg_L_guide_hip2UpV_vec.msg" "hyperLayout2.hyp[71].dn";
connectAttr "leg_L_guide_globalAnkleInfk02Space_srt.msg" "hyperLayout2.hyp[72].dn"
		;
connectAttr "leg_L_guide_globalAnkleInfk02Space.msg" "hyperLayout2.hyp[73].dn";
connectAttr "leg_L_fk03_ctrl_srtBuffer.msg" "hyperLayout2.hyp[74].dn";
connectAttr "leg_L_fk03_ctrl.msg" "hyperLayout2.hyp[75].dn";
connectAttr "leg_L_fk03_ctrlShape.msg" "hyperLayout2.hyp[76].dn";
connectAttr "leg_L_globalAnkle_srt.msg" "hyperLayout2.hyp[77].dn";
connectAttr "leg_L_guide_ikHip_local_mtx.msg" "hyperLayout2.hyp[78].dn";
connectAttr "leg_L_guide_endWorldInverse_mtx.msg" "hyperLayout2.hyp[79].dn";
connectAttr "leg_L_ankle_blend_mtx.msg" "hyperLayout2.hyp[80].dn";
connectAttr "leg_L_j03_worldMtx.msg" "hyperLayout2.hyp[81].dn";
connectAttr "leg_L_ankle_rotBlend.msg" "hyperLayout2.hyp[82].dn";
connectAttr "leg_L_fk03_worldMtx.msg" "hyperLayout2.hyp[83].dn";
connectAttr "leg_L_FK_start_mtx.msg" "hyperLayout2.hyp[84].dn";
connectAttr "leg_L_input.rolledAnkle" "leg_L_rolledAnkle_frame_srt.imat";
connectAttr "hyperLayout3.msg" "godNode_M_container.hl";
connectAttr "godNode_M_cmpnt.msg" "godNode_M_container.cbp[0]";
connectAttr "godNode_M_cmpnt.msg" "godNode_M_container.cbc[0]";
connectAttr "godNode_M_master_ctrl.msg" "godNode_M_container.pni[0].pnod";
connectAttr "godNode_M_masterOffset_ctrl.msg" "godNode_M_container.pni[1].pnod";
connectAttr "godNode_M_com_ctrl.msg" "godNode_M_container.pni[2].pnod";
connectAttr "godNode_M_comOffset_ctrl.msg" "godNode_M_container.pni[3].pnod";
connectAttr "godNode_M_end_ctrl.msg" "godNode_M_container.pni[4].pnod";
connectAttr "godNode_M_endOffset_ctrl.msg" "godNode_M_container.pni[5].pnod";
connectAttr "godNode_M_cmpnt.msg" "hyperLayout3.hyp[0].dn";
connectAttr "godNode_M_output.msg" "hyperLayout3.hyp[1].dn";
connectAttr "output_master_srt.msg" "hyperLayout3.hyp[2].dn";
connectAttr "output_com_srt.msg" "hyperLayout3.hyp[3].dn";
connectAttr "output_end_srt.msg" "hyperLayout3.hyp[4].dn";
connectAttr "|godNode_M_cmpnt|control.msg" "hyperLayout3.hyp[5].dn";
connectAttr "godNode_M_master_ctrl_srtBuffer.msg" "hyperLayout3.hyp[6].dn";
connectAttr "godNode_M_master_ctrl.msg" "hyperLayout3.hyp[7].dn";
connectAttr "godNode_M_masterOffset_ctrl.msg" "hyperLayout3.hyp[8].dn";
connectAttr "godNode_M_com_ctrl_srtBuffer.msg" "hyperLayout3.hyp[9].dn";
connectAttr "godNode_M_com_ctrl.msg" "hyperLayout3.hyp[10].dn";
connectAttr "godNode_M_comOffset_ctrl.msg" "hyperLayout3.hyp[11].dn";
connectAttr "godNode_M_end_ctrl_srtBuffer.msg" "hyperLayout3.hyp[12].dn";
connectAttr "godNode_M_end_ctrl.msg" "hyperLayout3.hyp[13].dn";
connectAttr "godNode_M_endOffset_ctrl.msg" "hyperLayout3.hyp[14].dn";
connectAttr "|godNode_M_cmpnt|guide.msg" "hyperLayout3.hyp[15].dn";
connectAttr "guide_world_ctrl.msg" "hyperLayout3.hyp[16].dn";
connectAttr "guide_com_ctrl.msg" "hyperLayout3.hyp[17].dn";
connectAttr "guide_end_ctrl.msg" "hyperLayout3.hyp[18].dn";
connectAttr "godNode_M_debuffer_end_output_srt.msg" "hyperLayout3.hyp[19].dn";
connectAttr "godNode_M_master_ctrl_wMtx_output_fNode.msg" "hyperLayout3.hyp[20].dn"
		;
connectAttr "godNode_M_debuffer_com_output_srt.msg" "hyperLayout3.hyp[21].dn";
connectAttr "godNode_M_debuffer_com_output_mtx.msg" "hyperLayout3.hyp[22].dn";
connectAttr "godNode_M_debuffer_end_output_mtx.msg" "hyperLayout3.hyp[23].dn";
connectAttr "godNode_M_masterOffset_ctrlShape.msg" "hyperLayout3.hyp[24].dn";
connectAttr "godNode_M_comOffset_ctrlShape.msg" "hyperLayout3.hyp[25].dn";
connectAttr "godNode_M_endOffset_ctrlShape.msg" "hyperLayout3.hyp[26].dn";
connectAttr "godNode_M_master_ctrlShape.msg" "hyperLayout3.hyp[27].dn";
connectAttr "godNode_M_com_ctrlShape.msg" "hyperLayout3.hyp[28].dn";
connectAttr "godNode_M_end_ctrlShape.msg" "hyperLayout3.hyp[29].dn";
connectAttr "guide_com_ctrlShape.msg" "hyperLayout3.hyp[30].dn";
connectAttr "guide_end_ctrlShape.msg" "hyperLayout3.hyp[31].dn";
connectAttr "guide_world_ctrlShape.msg" "hyperLayout3.hyp[32].dn";
connectAttr "leg_L_input.upVectorFrame" "leg_L_guide_upVector_srt.imat";
connectAttr "leg_L_configParameters.tibiaLength" "leg_L_totalLength_fNode_add.i2"
		;
connectAttr "leg_L_configParameters.femurLength" "leg_L_totalLength_fNode_add.i1"
		;
connectAttr "leg_L_totalLength_fNode_add.o" "leg_L_lengthLimit_fNode.i1";
connectAttr "hyperLayout4.msg" "foot_L_container.hl";
connectAttr "foot_L_tarsii_ctrl.msg" "foot_L_container.pni[0].pnod";
connectAttr "foot_L_toes_ctrl.msg" "foot_L_container.pni[1].pnod";
connectAttr "foot_L_cpmnt.msg" "foot_L_container.cbp[0]";
connectAttr "foot_L_cpmnt.msg" "foot_L_container.cbc[0]";
connectAttr "foot_L_cpmnt.msg" "hyperLayout4.hyp[0].dn";
connectAttr "foot_L_input.msg" "hyperLayout4.hyp[1].dn";
connectAttr "foot_L_output.msg" "hyperLayout4.hyp[2].dn";
connectAttr "|foot_L_cpmnt|control.msg" "hyperLayout4.hyp[3].dn";
connectAttr "foot_L_ankleSpace_srt.msg" "hyperLayout4.hyp[4].dn";
connectAttr "foot_L_tarsii_ctrl_srtBuffer.msg" "hyperLayout4.hyp[5].dn";
connectAttr "foot_L_tarsii_ctrl.msg" "hyperLayout4.hyp[6].dn";
connectAttr "foot_L_tarsii_ctrlShape.msg" "hyperLayout4.hyp[7].dn";
connectAttr "foot_L_toes_ctrl_srtBuffer.msg" "hyperLayout4.hyp[8].dn";
connectAttr "foot_L_toes_ctrl.msg" "hyperLayout4.hyp[9].dn";
connectAttr "foot_L_toes_ctrlShape.msg" "hyperLayout4.hyp[10].dn";
connectAttr "foot_L_start_mtx2srt.msg" "hyperLayout4.hyp[11].dn";
connectAttr "|foot_L_cpmnt|guide.msg" "hyperLayout4.hyp[12].dn";
connectAttr "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|diagnostic_ankle.msg" "hyperLayout4.hyp[13].dn"
		;
connectAttr "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|diagnostic_ankle|diagnostic_tarsi.msg" "hyperLayout4.hyp[14].dn"
		;
connectAttr "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|foot_L_toes_ctrl_srtBuffer|foot_L_toes_ctrl|diagnostic_toes.msg" "hyperLayout4.hyp[15].dn"
		;
connectAttr "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|foot_L_toes_ctrl_srtBuffer|foot_L_toes_ctrl|diagnostic_toes|diagnostic_tip.msg" "hyperLayout4.hyp[16].dn"
		;
connectAttr "leg_L_FK_start_mtx.o" "leg_L_FK_start_srt.imat";
connectAttr "leg_L_configParameters.hipOffsetFK" "leg_L_FK_start_mtx.i[0]";
connectAttr "leg_L_input.endWorld" "leg_L_FK_start_mtx.i[1]";
connectAttr "leg_L_fk03_ctrl.wm" "leg_L_fk03_worldMtx.imat";
connectAttr "leg_L_fk03_worldMtx.or" "leg_L_ankle_rotBlend.ia";
connectAttr "leg_L_fkik_blend_complement.o" "leg_L_ankle_rotBlend.wa";
connectAttr "leg_L_animParameters.FKIK_blend" "leg_L_ankle_rotBlend.wb";
connectAttr "leg_L_globalAnkle_srt.or" "leg_L_ankle_rotBlend.ib";
connectAttr "leg_L_j03_srt.wm" "leg_L_j03_worldMtx.imat";
connectAttr "leg_L_ankle_rotBlend.o" "leg_L_ankle_blend_mtx.ir";
connectAttr "leg_L_j03_worldMtx.ot" "leg_L_ankle_blend_mtx.it";
connectAttr "leg_L_input.rawAnkleControl" "leg_L_globalAnkle_srt.imat";
connectAttr "legGlobal_L_guide_tarsi2Toe_rest_angle.a" "legGlobal_L_guide_tarsi_rest_negate_angle.ia"
		;
connectAttr "legGlobal_L_guide_tip_ctrl.t" "legGlobal_L_guide_toe_length.p1";
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.t" "legGlobal_L_guide_toe_length.p2"
		;
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.t" "legGlobal_L_guide_tarsi_length.p1"
		;
connectAttr "legGlobal_L_guide_ankle_ctrl.t" "legGlobal_L_guide_tarsi_length.p2"
		;
connectAttr "legGlobal_L_guide_toe_direction_vec.o3" "legGlobal_L_guide_toe_rest_angle.v1"
		;
connectAttr "legGlobal_L_guide_basisVector.t" "legGlobal_L_guide_toe_rest_angle.v2"
		;
connectAttr "legGlobal_L_guide_ankle_ctrl.wm" "legGlobal_L_guide_ankle_world_srt.imat"
		;
connectAttr "legGlobal_L_guide_tip_ctrl.t" "legGlobal_L_guide_toe_direction_vec.i3[0]"
		;
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.t" "legGlobal_L_guide_toe_direction_vec.i3[1]"
		;
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.t" "legGlobal_L_guide_tarsi_direction_vec.i3[0]"
		;
connectAttr "legGlobal_L_guide_ankle_ctrl.t" "legGlobal_L_guide_tarsi_direction_vec.i3[1]"
		;
connectAttr "legGlobal_L_guide_toe_direction_vec.o3" "legGlobal_L_guide_tarsi2Toe_rest_angle.v1"
		;
connectAttr "legGlobal_L_guide_tarsi_direction_vec.o3" "legGlobal_L_guide_tarsi2Toe_rest_angle.v2"
		;
connectAttr "legGlobal_L_guide_tarsi_direction_vec.o3" "legGlobal_L_guide_tarsi2World_rest_angle.v1"
		;
connectAttr "legGlobal_L_guide_basisVector.t" "legGlobal_L_guide_tarsi2World_rest_angle.v2"
		;
connectAttr "leg_L_input.endWorld" "leg_L_guide_endWorldInverse_mtx.imat";
connectAttr "leg_L_hip_srt.wm" "leg_L_guide_ikHip_local_mtx.i[0]";
connectAttr "leg_L_guide_endWorldInverse_mtx.omat" "leg_L_guide_ikHip_local_mtx.i[1]"
		;
connectAttr "leg_L_input.rolledAnkle" "leg_L_guide_globalAnkleInfk02Space.i[0]";
connectAttr "leg_L_fk02_ctrl.wim" "leg_L_guide_globalAnkleInfk02Space.i[1]";
connectAttr "leg_L_guide_globalAnkleInfk02Space.o" "leg_L_guide_globalAnkleInfk02Space_srt.imat"
		;
connectAttr "leg_L_guide_upVector_srt.ot" "leg_L_guide_hip2UpV_vec.i3[0]";
connectAttr "leg_L_guide_hip_world_srt.ot" "leg_L_guide_hip2UpV_vec.i3[1]";
connectAttr "leg_L_input.rolledAnkle" "leg_L_guide_ankle_world_srt.imat";
connectAttr "leg_L_guide_knee_world_srt.ot" "leg_L_guide_tibiaLength.p2";
connectAttr "leg_L_guide_ankle_world_srt.ot" "leg_L_guide_tibiaLength.p1";
connectAttr "leg_L_guide_kneePos_ctrl.wm" "leg_L_guide_knee_world_srt.imat";
connectAttr "leg_L_guide_knee_world_srt.ot" "leg_L_guide_femurLength.p2";
connectAttr "leg_L_guide_hip_world_srt.ot" "leg_L_guide_femurLength.p1";
connectAttr "leg_L_guide_hipPos_ctrl.wm" "leg_L_guide_hip_world_srt.imat";
connectAttr "leg_L_input.endWorld" "leg_L_guide_hipInput_srt.imat";
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
connectAttr "leg_R_unhandedFK01_mtx.o" "leg_R_fk01_ctrl_world_mtx.imat";
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
connectAttr "leg_R_handednessMatrix.omat" "leg_R_fk02reframed01_mtx.i[0]";
connectAttr "leg_R_fk02_ctrl.wm" "leg_R_fk02reframed01_mtx.i[1]";
connectAttr "leg_R_unhandedFK01_inverse_mtx.omat" "leg_R_fk02reframed01_mtx.i[2]"
		;
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
connectAttr "leg_R_FK_start_mtx.o" "leg_R_FK_start_srt.imat";
connectAttr "leg_R_input.upVectorFrame" "leg_R_guide_upVector_srt.imat";
connectAttr "leg_R_input.rawAnkleControl" "leg_R_globalAnkle_srt.imat";
connectAttr "leg_R_ankle_rotBlend.o" "leg_R_ankle_blend_mtx.ir";
connectAttr "leg_R_j03_worldMtx.ot" "leg_R_ankle_blend_mtx.it";
connectAttr "leg_R_j03_srt.wm" "leg_R_j03_worldMtx.imat";
connectAttr "leg_R_fk03_worldMtx.or" "leg_R_ankle_rotBlend.ia";
connectAttr "leg_R_fkik_blend_complement.o" "leg_R_ankle_rotBlend.wa";
connectAttr "leg_R_animParameters.FKIK_blend" "leg_R_ankle_rotBlend.wb";
connectAttr "leg_R_globalAnkle_srt.or" "leg_R_ankle_rotBlend.ib";
connectAttr "leg_R_unhandedFK03_mtx.o" "leg_R_fk03_worldMtx.imat";
connectAttr "leg_R_configParameters.hipOffsetFK" "leg_R_FK_start_mtx.i[0]";
connectAttr "leg_R_input.endWorld" "leg_R_FK_start_mtx.i[1]";
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
connectAttr "leg_R_input.endWorld" "leg_R_guide_endWorldInverse_mtx.imat";
connectAttr "leg_R_hip_srt.wm" "leg_R_guide_ikHip_local_mtx.i[0]";
connectAttr "leg_R_guide_endWorldInverse_mtx.omat" "leg_R_guide_ikHip_local_mtx.i[1]"
		;
connectAttr "leg_R_input.rolledAnkle" "leg_R_guide_globalAnkleInfk02Space.i[0]";
connectAttr "leg_R_fk02_ctrl.wim" "leg_R_guide_globalAnkleInfk02Space.i[1]";
connectAttr "leg_R_guide_globalAnkleInfk02Space.o" "leg_R_guide_globalAnkleInfk02Space_srt.imat"
		;
connectAttr "leg_R_guide_upVector_srt.ot" "leg_R_guide_hip2UpV_vec.i3[0]";
connectAttr "leg_R_guide_hip_world_srt.ot" "leg_R_guide_hip2UpV_vec.i3[1]";
connectAttr "leg_R_input.rolledAnkle" "leg_R_guide_ankle_world_srt.imat";
connectAttr "leg_R_guide_knee_world_srt.ot" "leg_R_guide_tibiaLength.p2";
connectAttr "leg_R_guide_ankle_world_srt.ot" "leg_R_guide_tibiaLength.p1";
connectAttr "leg_R_guide_kneePos_ctrl.wm" "leg_R_guide_knee_world_srt.imat";
connectAttr "leg_R_guide_knee_world_srt.ot" "leg_R_guide_femurLength.p2";
connectAttr "leg_R_guide_hip_world_srt.ot" "leg_R_guide_femurLength.p1";
connectAttr "leg_R_guide_hipPos_ctrl.wm" "leg_R_guide_hip_world_srt.imat";
connectAttr "leg_R_input.endWorld" "leg_R_guide_hipInput_srt.imat";
connectAttr "leg_R_configParameters.invertedHandedness" "leg_R_handedNessSign._cnd"
		;
connectAttr "leg_R_handedNessSign.of" "multDoubleLinear1.i2";
connectAttr "leg_R_FK_start_srt.otx" "multDoubleLinear1.i1";
connectAttr "leg_R_FK_start_srt.orz" "animBlendNodeAdditiveDA1.ib";
connectAttr "leg_R_handedNessSign.of" "animBlendNodeAdditiveDA1.wb";
connectAttr "legGlobal_R_guide_toe_direction_vec.o3" "legGlobal_R_guide_tarsi2Toe_rest_angle.v1"
		;
connectAttr "legGlobal_R_guide_tarsi_direction_vec.o3" "legGlobal_R_guide_tarsi2Toe_rest_angle.v2"
		;
connectAttr "legGlobal_R_guide_tarsi_direction_vec.o3" "legGlobal_R_guide_tarsi2World_rest_angle.v1"
		;
connectAttr "legGlobal_R_guide_basisVector.t" "legGlobal_R_guide_tarsi2World_rest_angle.v2"
		;
connectAttr "legGlobal_R_guide_toe_direction_vec.o3" "legGlobal_R_guide_toe_rest_angle.v1"
		;
connectAttr "legGlobal_R_guide_basisVector.t" "legGlobal_R_guide_toe_rest_angle.v2"
		;
connectAttr "legGlobal_R_tarsi_worldDirection_vec3.o3" "legGlobal_R_tarsi_rolledAngle.v1"
		;
connectAttr "legGlobal_R_guide_tarsi2Toe_rest_angle.a" "legGlobal_R_guide_tarsi_rest_negate_angle.ia"
		;
connectAttr "legGlobal_R_configParameters.tarsirest" "legGlobal_R_tarsiRollOffset_angle.ib"
		;
connectAttr "legGlobal_R_roll_tarsi_fCurve.o" "legGlobal_R_tarsiRollOffset_angle.ia"
		;
connectAttr "legGlobal_R_configParameters.toeRest" "legGlobal_R_toeRollOffset_angle.ib"
		;
connectAttr "legGlobal_R_roll_toe_fCurve.o" "legGlobal_R_toeRollOffset_angle.ia"
		;
connectAttr "legGlobal_R_roll_UC.o" "legGlobal_R_roll_tarsi_fCurve.i";
connectAttr "legGlobal_R_roll_UC.o" "legGlobal_R_roll_toe_fCurve.i";
connectAttr "legGlobal_R_roll_UC.o" "legGlobal_R_heelBack_rollClamp.ipb";
connectAttr "legGlobal_R_ankleFramed_tarsi_mtx.o" "legGlobal_R_ankleFramed_tarsi_srt.imat"
		;
connectAttr "legGlobal_R_ankleReparent_mtxMult.o" "legGlobal_R_ankleReparent_srt.imat"
		;
connectAttr "legGlobal_R_guide_ankle_ctrl.wm" "legGlobal_R_guide_ankle_world_srt.imat"
		;
connectAttr "legGlobal_R_roll_tarsiEnd_srt.wm" "legGlobal_R_roll_tarsi_world_mtx.imat"
		;
connectAttr "legGlobal_R_roll_tarsi_srt.wm" "legGlobal_R_roll_toes_world_mtx2srt.imat"
		;
connectAttr "legGlobal_R_upVecReparent_mtxMult.o" "legGlobal_R_upVecReparent_srt.imat"
		;
connectAttr "legGlobal_R_worldAnkle_ctrl.wm" "legGlobal_R_worldAnkle_ctrl_world_srt.imat"
		;
connectAttr "legGlobal_R_guide_toe2Tarsi_ctrl.t" "legGlobal_R_guide_tarsi_length.p1"
		;
connectAttr "legGlobal_R_guide_ankle_ctrl.t" "legGlobal_R_guide_tarsi_length.p2"
		;
connectAttr "legGlobal_R_guide_tip_ctrl.t" "legGlobal_R_guide_toe_length.p1";
connectAttr "legGlobal_R_guide_toe2Tarsi_ctrl.t" "legGlobal_R_guide_toe_length.p2"
		;
connectAttr "legGlobal_R_roll_tarsiEnd_srt.wm" "legGlobal_R_ankleFramed_tarsi_mtx.i[0]"
		;
connectAttr "legGlobal_R_ankle_rest_srt.wim" "legGlobal_R_ankleFramed_tarsi_mtx.i[1]"
		;
connectAttr "legGlobal_R_configParameters.ankleGlobalOffset" "legGlobal_R_ankleReparent_mtxMult.i[0]"
		;
connectAttr "legGlobal_R_input.endWorld" "legGlobal_R_ankleReparent_mtxMult.i[1]"
		;
connectAttr "legGlobal_R_configParameters.upVecGlobalOffset" "legGlobal_R_upVecReparent_mtxMult.i[0]"
		;
connectAttr "legGlobal_R_input.endWorld" "legGlobal_R_upVecReparent_mtxMult.i[1]"
		;
connectAttr "legGlobal_R_guide_toe2Tarsi_ctrl.t" "legGlobal_R_guide_tarsi_direction_vec.i3[0]"
		;
connectAttr "legGlobal_R_guide_ankle_ctrl.t" "legGlobal_R_guide_tarsi_direction_vec.i3[1]"
		;
connectAttr "legGlobal_R_guide_tip_ctrl.t" "legGlobal_R_guide_toe_direction_vec.i3[0]"
		;
connectAttr "legGlobal_R_guide_toe2Tarsi_ctrl.t" "legGlobal_R_guide_toe_direction_vec.i3[1]"
		;
connectAttr "legGlobal_R_roll_toes_world_mtx2srt.ot" "legGlobal_R_tarsi_worldDirection_vec3.i3[0]"
		;
connectAttr "legGlobal_R_roll_tarsi_world_mtx.ot" "legGlobal_R_tarsi_worldDirection_vec3.i3[1]"
		;
connectAttr "legGlobal_R_ankle_rolled_srt.t" "legGlobal_R_ankleFramed_rollOffset_srt.ip"
		;
connectAttr "legGlobal_R_worldAnkle_ctrl.wm" "legGlobal_R_ankleFramed_rollOffset_srt.im"
		;
connectAttr "legGlobal_R_animParameters.roll" "legGlobal_R_roll_UC.i";
connectAttr "legGlobal_R_heelBack_rollClamp.opb" "legGlobal_R_heelback_roll_UC.i"
		;
connectAttr "hyperLayout6.msg" "legGlobal_R_container.hl";
connectAttr "legGlobal_R_cmpnt.msg" "legGlobal_R_container.cbp[0]";
connectAttr "legGlobal_R_cmpnt.msg" "legGlobal_R_container.cbc[0]";
connectAttr "legGlobal_R_worldAnkle_ctrl.msg" "legGlobal_R_container.pni[0].pnod"
		;
connectAttr "|legGlobal_R_cmpnt|control|legGlobal_R_upVector_ctrl_srtBuffer|legGlobal_R_upVector_ctrl.msg" "legGlobal_R_container.pni[1].pnod"
		;
connectAttr "legGlobal_R_cmpnt.msg" "hyperLayout6.hyp[0].dn";
connectAttr "legGlobal_R_input.msg" "hyperLayout6.hyp[1].dn";
connectAttr "legGlobal_R_output.msg" "hyperLayout6.hyp[2].dn";
connectAttr "|legGlobal_R_cmpnt|control.msg" "hyperLayout6.hyp[3].dn";
connectAttr "legGlobal_R_animParameters.msg" "hyperLayout6.hyp[4].dn";
connectAttr "|legGlobal_R_cmpnt|control|roll_mechanics.msg" "hyperLayout6.hyp[5].dn"
		;
connectAttr "legGlobal_R_ankle_rest_srt.msg" "hyperLayout6.hyp[6].dn";
connectAttr "legGlobal_R_ankle_rolled_srt.msg" "hyperLayout6.hyp[7].dn";
connectAttr "legGlobal_R_roll_world_srt.msg" "hyperLayout6.hyp[8].dn";
connectAttr "legGlobal_R_roll_heel_srt.msg" "hyperLayout6.hyp[9].dn";
connectAttr "legGlobal_R_roll_tip_srt.msg" "hyperLayout6.hyp[10].dn";
connectAttr "legGlobal_R_roll_tarsi_srt.msg" "hyperLayout6.hyp[11].dn";
connectAttr "legGlobal_R_roll_tarsiEnd_srt.msg" "hyperLayout6.hyp[12].dn";
connectAttr "legGlobal_R_worldAnkle_ctrl_srtBuffer.msg" "hyperLayout6.hyp[13].dn"
		;
connectAttr "legGlobal_R_worldAnkle_ctrl.msg" "hyperLayout6.hyp[14].dn";
connectAttr "legGlobal_R_upVector_ctrl_srtBuffer.msg" "hyperLayout6.hyp[17].dn";
connectAttr "|legGlobal_R_cmpnt|control|legGlobal_R_upVector_ctrl_srtBuffer|legGlobal_R_upVector_ctrl.msg" "hyperLayout6.hyp[18].dn"
		;
connectAttr "|legGlobal_R_cmpnt|guide.msg" "hyperLayout6.hyp[19].dn";
connectAttr "legGlobal_R_guide_global_ctrl.msg" "hyperLayout6.hyp[20].dn";
connectAttr "legGlobal_R_guide_basisVector.msg" "hyperLayout6.hyp[21].dn";
connectAttr "legGlobal_R_guide_heel_ctrl.msg" "hyperLayout6.hyp[22].dn";
connectAttr "legGlobal_R_guide_tip_ctrl.msg" "hyperLayout6.hyp[23].dn";
connectAttr "legGlobal_R_guide_toe2Tarsi_ctrl.msg" "hyperLayout6.hyp[24].dn";
connectAttr "legGlobal_R_guide_ankle_ctrl.msg" "hyperLayout6.hyp[25].dn";
connectAttr "legGlobal_R_configParameters.msg" "hyperLayout6.hyp[26].dn";
connectAttr "legGlobal_R_guide_tarsi2Toe_rest_angle.msg" "hyperLayout6.hyp[28].dn"
		;
connectAttr "legGlobal_R_guide_tarsi2World_rest_angle.msg" "hyperLayout6.hyp[29].dn"
		;
connectAttr "legGlobal_R_guide_toe_rest_angle.msg" "hyperLayout6.hyp[30].dn";
connectAttr "legGlobal_R_tarsi_rolledAngle.msg" "hyperLayout6.hyp[31].dn";
connectAttr "legGlobal_R_guide_tarsi_rest_negate_angle.msg" "hyperLayout6.hyp[32].dn"
		;
connectAttr "legGlobal_R_tarsiRollOffset_angle.msg" "hyperLayout6.hyp[33].dn";
connectAttr "legGlobal_R_toeRollOffset_angle.msg" "hyperLayout6.hyp[34].dn";
connectAttr "legGlobal_R_roll_tarsi_fCurve.msg" "hyperLayout6.hyp[35].dn";
connectAttr "legGlobal_R_roll_toe_fCurve.msg" "hyperLayout6.hyp[36].dn";
connectAttr "legGlobal_R_heelBack_rollClamp.msg" "hyperLayout6.hyp[38].dn";
connectAttr "legGlobal_R_ankleFramed_tarsi_srt.msg" "hyperLayout6.hyp[41].dn";
connectAttr "legGlobal_R_ankleReparent_srt.msg" "hyperLayout6.hyp[42].dn";
connectAttr "legGlobal_R_guide_ankle_world_srt.msg" "hyperLayout6.hyp[43].dn";
connectAttr "legGlobal_R_roll_tarsi_world_mtx.msg" "hyperLayout6.hyp[44].dn";
connectAttr "legGlobal_R_roll_toes_world_mtx2srt.msg" "hyperLayout6.hyp[45].dn";
connectAttr "legGlobal_R_upVecReparent_srt.msg" "hyperLayout6.hyp[48].dn";
connectAttr "legGlobal_R_worldAnkle_ctrl_world_srt.msg" "hyperLayout6.hyp[49].dn"
		;
connectAttr "legGlobal_R_guide_tarsi_length.msg" "hyperLayout6.hyp[50].dn";
connectAttr "legGlobal_R_guide_toe_length.msg" "hyperLayout6.hyp[51].dn";
connectAttr "legGlobal_R_ankleFramed_tarsi_mtx.msg" "hyperLayout6.hyp[54].dn";
connectAttr "legGlobal_R_ankleReparent_mtxMult.msg" "hyperLayout6.hyp[55].dn";
connectAttr "legGlobal_R_upVecReparent_mtxMult.msg" "hyperLayout6.hyp[56].dn";
connectAttr "legGlobal_R_guide_tarsi_direction_vec.msg" "hyperLayout6.hyp[58].dn"
		;
connectAttr "legGlobal_R_guide_toe_direction_vec.msg" "hyperLayout6.hyp[59].dn";
connectAttr "legGlobal_R_tarsi_worldDirection_vec3.msg" "hyperLayout6.hyp[62].dn"
		;
connectAttr "legGlobal_R_ankleFramed_rollOffset_srt.msg" "hyperLayout6.hyp[63].dn"
		;
connectAttr "legGlobal_R_worldAnkle_ctrlShape.msg" "hyperLayout6.hyp[65].dn";
connectAttr "|legGlobal_R_cmpnt|control|legGlobal_R_upVector_ctrl_srtBuffer|legGlobal_R_upVector_ctrl|legGlobal_R_upVector_ctrl.msg" "hyperLayout6.hyp[67].dn"
		;
connectAttr "legGlobal_R_guide_global_ctrlShape.msg" "hyperLayout6.hyp[68].dn";
connectAttr "legGlobal_R_guide_heel_ctrlShape.msg" "hyperLayout6.hyp[69].dn";
connectAttr "legGlobal_R_guide_tip_ctrlShape.msg" "hyperLayout6.hyp[70].dn";
connectAttr "legGlobal_R_guide_toe2Tarsi_ctrlShape.msg" "hyperLayout6.hyp[71].dn"
		;
connectAttr "legGlobal_R_guide_ankle_ctrlShape.msg" "hyperLayout6.hyp[72].dn";
connectAttr "legGlobal_R_roll_UC.msg" "hyperLayout6.hyp[73].dn";
connectAttr "legGlobal_R_heelback_roll_UC.msg" "hyperLayout6.hyp[74].dn";
connectAttr "legGlobal_R_toolParameters.msg" "hyperLayout6.hyp[75].dn";
connectAttr "legGlobal_R_guide_upVector_ctrl_srtBuffer.msg" "hyperLayout6.hyp[76].dn"
		;
connectAttr "legGlobal_R_guide_upVector_ctrl.msg" "hyperLayout6.hyp[77].dn";
connectAttr "legGlobal_R_guide_upVector_ctrlShape.msg" "hyperLayout6.hyp[78].dn"
		;
connectAttr "legGlobal_R_worldAnkle_rolled_srt.msg" "hyperLayout6.hyp[79].dn";
connectAttr "leg_R_FK_start_srt.ory" "animBlendNodeAdditiveDA2.ib";
connectAttr "leg_R_handedNessSign.of" "animBlendNodeAdditiveDA2.wb";
connectAttr "leg_R_handednessMatrix.omat" "leg_R_unhandedFK01_mtx.i[0]";
connectAttr "leg_R_fk01_ctrl.wm" "leg_R_unhandedFK01_mtx.i[1]";
connectAttr "leg_R_handedNessSign.of" "leg_R_handednessMatrix.isx";
connectAttr "leg_R_unhandedFK01_mtx.o" "leg_R_unhandedFK01_inverse_mtx.imat";
connectAttr "leg_R_fkik_blend_complement.msg" "nodeView1.ni[0].dn";
connectAttr "leg_R_handednessMatrix.msg" "nodeView1.ni[1].dn";
connectAttr "leg_R_hip_srt.msg" "nodeView1.ni[2].dn";
connectAttr "leg_R_fk01_ctrl.msg" "nodeView1.ni[3].dn";
connectAttr "leg_R_fkik_j01_blended_rot.msg" "nodeView1.ni[4].dn";
connectAttr "leg_R_hip_rot.msg" "nodeView1.ni[5].dn";
connectAttr "leg_R_j01_srt.msg" "nodeView1.ni[6].dn";
connectAttr "leg_R_animParameters.msg" "nodeView1.ni[7].dn";
connectAttr "leg_R_hipWorld_srt.msg" "nodeView1.ni[8].dn";
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" "nodeView1.ni[9].dn";
connectAttr "leg_R_unhandedFK01_mtx.msg" "nodeView1.ni[10].dn";
connectAttr "leg_R_toolParameters.msg" "nodeView1.ni[11].dn";
connectAttr "leg_R_guide_hip2UpV_vec.msg" "nodeView1.ni[12].dn";
connectAttr "leg_R_guide_hip_world_srt.msg" "nodeView1.ni[13].dn";
connectAttr "leg_R_fk02_ctrl.msg" "nodeView1.ni[14].dn";
connectAttr "leg_R_fkik_j02_blended_rot.msg" "nodeView1.ni[15].dn";
connectAttr "leg_R_guide_femurLength.msg" "nodeView1.ni[16].dn";
connectAttr "leg_R_tibiaStart_srt.msg" "nodeView1.ni[17].dn";
connectAttr "leg_R_guide_ikHip_local_mtx.msg" "nodeView1.ni[18].dn";
connectAttr "leg_R_guide_hipPos_ctrl.msg" "nodeView1.ni[19].dn";
connectAttr "leg_R_handedNessSign.msg" "nodeView1.ni[20].dn";
connectAttr "leg_R_guide_tibiaLength.msg" "nodeView1.ni[21].dn";
connectAttr "leg_R_j02_srt.msg" "nodeView1.ni[22].dn";
connectAttr "leg_R_configParameters.msg" "nodeView1.ni[23].dn";
connectAttr "leg_R_guide_ankle_world_srt.msg" "nodeView1.ni[24].dn";
connectAttr "leg_R_fk02reframed01_rot.msg" "nodeView1.ni[25].dn";
connectAttr "leg_R_unhandedFK01_inverse_mtx.msg" "nodeView1.ni[26].dn";
connectAttr "leg_R_guide_knee_world_srt.msg" "nodeView1.ni[27].dn";
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" "nodeView1.ni[28].dn";
connectAttr "leg_R_fk02reframed01_mtx.msg" "nodeView1.ni[29].dn";
connectAttr "foot_R_input.startMtx" "foot_R_start_mtx2srt.imat";
connectAttr "hyperLayout7.msg" "foot_R_container.hl";
connectAttr "foot_R_tarsii_ctrl.msg" "foot_R_container.pni[0].pnod";
connectAttr "foot_R_toes_ctrl.msg" "foot_R_container.pni[1].pnod";
connectAttr "foot_R_cpmnt.msg" "foot_R_container.cbp[0]";
connectAttr "foot_R_cpmnt.msg" "foot_R_container.cbc[0]";
connectAttr "foot_R_cpmnt.msg" "hyperLayout7.hyp[0].dn";
connectAttr "foot_R_input.msg" "hyperLayout7.hyp[1].dn";
connectAttr "foot_R_output.msg" "hyperLayout7.hyp[2].dn";
connectAttr "|foot_R_cpmnt|control.msg" "hyperLayout7.hyp[3].dn";
connectAttr "foot_R_ankleSpace_srt.msg" "hyperLayout7.hyp[4].dn";
connectAttr "foot_R_tarsii_ctrl_srtBuffer.msg" "hyperLayout7.hyp[5].dn";
connectAttr "foot_R_tarsii_ctrl.msg" "hyperLayout7.hyp[6].dn";
connectAttr "foot_R_tarsii_ctrlShape.msg" "hyperLayout7.hyp[7].dn";
connectAttr "foot_R_toes_ctrl_srtBuffer.msg" "hyperLayout7.hyp[8].dn";
connectAttr "foot_R_toes_ctrl.msg" "hyperLayout7.hyp[9].dn";
connectAttr "foot_R_toes_ctrlShape.msg" "hyperLayout7.hyp[10].dn";
connectAttr "foot_R_start_mtx2srt.msg" "hyperLayout7.hyp[11].dn";
connectAttr "|foot_R_cpmnt|guide.msg" "hyperLayout7.hyp[12].dn";
connectAttr "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|diagnostic_ankle.msg" "hyperLayout7.hyp[13].dn"
		;
connectAttr "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|diagnostic_ankle|diagnostic_tarsi.msg" "hyperLayout7.hyp[14].dn"
		;
connectAttr "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|foot_R_toes_ctrl_srtBuffer|foot_R_toes_ctrl|diagnostic_toes.msg" "hyperLayout7.hyp[15].dn"
		;
connectAttr "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|foot_R_toes_ctrl_srtBuffer|foot_R_toes_ctrl|diagnostic_toes|diagnostic_tip.msg" "hyperLayout7.hyp[16].dn"
		;
connectAttr "leg_R_handednessMatrix.omat" "leg_R_unhandedFK03_mtx.i[0]";
connectAttr "leg_R_fk03_ctrl.wm" "leg_R_unhandedFK03_mtx.i[1]";
connectAttr "nodeView2.msg" "MayaNodeEditorBookmarks.b[0]";
connectAttr "leg_R_animParameters.msg" "nodeView2.ni[0].dn";
connectAttr "leg_R_fk02_ctrl.msg" "nodeView2.ni[1].dn";
connectAttr "leg_R_tibiaStart_srt.msg" "nodeView2.ni[2].dn";
connectAttr "leg_R_hip_rot.msg" "nodeView2.ni[3].dn";
connectAttr "leg_R_handedNessSign.msg" "nodeView2.ni[4].dn";
connectAttr "leg_R_guide_hipPos_ctrl.msg" "nodeView2.ni[5].dn";
connectAttr "leg_R_j01_srt.msg" "nodeView2.ni[6].dn";
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" "nodeView2.ni[7].dn";
connectAttr "leg_R_fkik_j02_blended_rot.msg" "nodeView2.ni[8].dn";
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" "nodeView2.ni[9].dn";
connectAttr "leg_R_hip_srt.msg" "nodeView2.ni[10].dn";
connectAttr "leg_R_fk01_ctrl.msg" "nodeView2.ni[11].dn";
connectAttr "leg_R_fkik_blend_complement.msg" "nodeView2.ni[12].dn";
connectAttr "leg_R_j02_srt.msg" "nodeView2.ni[13].dn";
connectAttr "leg_R_configParameters.msg" "nodeView2.ni[14].dn";
connectAttr "leg_R_guide_ikHip_local_mtx.msg" "nodeView2.ni[15].dn";
connectAttr "leg_R_unhandedFK01_mtx.msg" "nodeView2.ni[16].dn";
connectAttr "leg_R_unhandedFK01_inverse_mtx.msg" "nodeView2.ni[17].dn";
connectAttr "leg_R_handednessMatrix.msg" "nodeView2.ni[18].dn";
connectAttr "leg_R_hipWorld_srt.msg" "nodeView2.ni[19].dn";
connectAttr "leg_R_fkik_j01_blended_rot.msg" "nodeView2.ni[20].dn";
connectAttr "leg_R_fk02reframed01_mtx.msg" "nodeView2.ni[21].dn";
connectAttr "leg_R_fk02reframed01_rot.msg" "nodeView2.ni[22].dn";
connectAttr "leg_R_fk03_worldMtx.msg" "nodeView2.ni[23].dn";
connectAttr "leg_R_globalAnkle_srt.msg" "nodeView2.ni[24].dn";
connectAttr "leg_R_fk03_ctrl.msg" "nodeView2.ni[25].dn";
connectAttr "leg_R_unhandedFK03_mtx.msg" "nodeView2.ni[26].dn";
connectAttr "leg_R_output.msg" "nodeView2.ni[27].dn";
connectAttr "leg_R_ankle_blend_mtx.msg" "nodeView2.ni[28].dn";
connectAttr "foot_R_ankleSpace_srt.msg" "nodeView2.ni[29].dn";
connectAttr "foot_R_tarsii_ctrl_srtBuffer.msg" "nodeView2.ni[30].dn";
connectAttr "foot_R_input.msg" "nodeView2.ni[31].dn";
connectAttr "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|diagnostic_ankle|diagnostic_tarsi.msg" "nodeView2.ni[32].dn"
		;
connectAttr "foot_R_toes_ctrl_srtBuffer.msg" "nodeView2.ni[33].dn";
connectAttr "foot_R_start_mtx2srt.msg" "nodeView2.ni[34].dn";
connectAttr "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|foot_R_toes_ctrl_srtBuffer|foot_R_toes_ctrl|diagnostic_toes|diagnostic_tip.msg" "nodeView2.ni[35].dn"
		;
connectAttr "leg_R_ankle_rotBlend.msg" "nodeView2.ni[36].dn";
connectAttr "leg_R_j03_worldMtx.msg" "nodeView2.ni[37].dn";
connectAttr "output_com_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "leg_L_totalLength_fNode_add.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "legGlobal_L_guide_global_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn"
		;
connectAttr "legGlobal_L_guide_tip_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "leg_L_guide_globalAnkleInfk02Space.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "legGlobal_L_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "leg_L_limitedAnkleWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "leg_L_guide_hipPos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn"
		;
connectAttr "legGlobal_L_guide_heel_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "legGlobal_L_ankle_rest_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "leg_L_guide_kneePos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "legGlobal_L_guide_tarsi_direction_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "leg_L_guide_knee_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "leg_L_hip_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn";
connectAttr "leg_L_fk03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn"
		;
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn"
		;
connectAttr "legGlobal_L_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn"
		;
connectAttr "leg_L_IK_upVectoringAngle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[18].dn"
		;
connectAttr "leg_L_IK_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[19].dn"
		;
connectAttr "leg_L_guide_hip2UpV_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[20].dn"
		;
connectAttr "legGlobal_L_heelback_roll_UC.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[21].dn"
		;
connectAttr "leg_L_lengthLimit_fNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[22].dn"
		;
connectAttr "leg_L_animParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[23].dn"
		;
connectAttr "legGlobal_L_guide_upVector_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[24].dn"
		;
connectAttr "leg_L_femurEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[25].dn"
		;
connectAttr "leg_L_fk03_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[26].dn"
		;
connectAttr "leg_L_fk02_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[27].dn"
		;
connectAttr "leg_L_ankle_rotBlend.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[28].dn"
		;
connectAttr "foot_L_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[29].dn";
connectAttr "legGlobal_L_heelBack_rollClamp.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[30].dn"
		;
connectAttr "leg_L_guide_femurLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[31].dn"
		;
connectAttr "foot_L_tarsii_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[32].dn"
		;
connectAttr "legGlobal_L_upVector_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[33].dn"
		;
connectAttr "godNode_M_debuffer_end_output_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[34].dn"
		;
connectAttr "leg_L_ankle2hip_clampedDistance.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[35].dn"
		;
connectAttr "leg_L_guide_kneePos_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[36].dn"
		;
connectAttr "leg_L_guide_ankle_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[37].dn"
		;
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[38].dn"
		;
connectAttr "legGlobal_L_guide_toe2Tarsi_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[39].dn"
		;
connectAttr "foot_L_toes_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[40].dn"
		;
connectAttr "output_master_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[41].dn"
		;
connectAttr "legGlobal_L_toolParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[42].dn"
		;
connectAttr "leg_L_guide_hipInput_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[43].dn"
		;
connectAttr "leg_L_fk02_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[44].dn"
		;
connectAttr "leg_L_fk02reframed01_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[45].dn"
		;
connectAttr "animParameters_roll.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[46].dn"
		;
connectAttr "leg_L_fk03_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[47].dn"
		;
connectAttr "legGlobal_L_roll_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[48].dn"
		;
connectAttr "legGlobal_L_guide_toe_direction_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[49].dn"
		;
connectAttr "legGlobal_L_guide_tarsi_length.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[50].dn"
		;
connectAttr "leg_L_fk02reframed01_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[51].dn"
		;
connectAttr "leg_L_j03_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[52].dn";
connectAttr "|legGlobal_L_cmpnt|control|legGlobal_L_upVector_ctrl_srtBuffer|legGlobal_L_upVector_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[53].dn"
		;
connectAttr "legGlobal_L_guide_tarsi2World_rest_angle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[54].dn"
		;
connectAttr "godNode_M_master_ctrl_wMtx_output_fNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[55].dn"
		;
connectAttr "legGlobal_L_roll_UC.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[56].dn"
		;
connectAttr "leg_L_fk01_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[57].dn"
		;
connectAttr "legGlobal_L_guide_ankle_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[58].dn"
		;
connectAttr "godNode_M_debuffer_end_output_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[59].dn"
		;
connectAttr "godNode_M_debuffer_com_output_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[60].dn"
		;
connectAttr "leg_L_guide_kneeUpV_aim_cns.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[61].dn"
		;
connectAttr "leg_L_IK_upVector_hipYProjected_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[62].dn"
		;
connectAttr "legGlobal_L_ankleFramed_rollOffset_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[63].dn"
		;
connectAttr "legGlobal_L_guide_tarsi2Toe_rest_angle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[64].dn"
		;
connectAttr "legGlobal_L_roll_toe_fCurve.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[65].dn"
		;
connectAttr "leg_L_IK_tension_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[66].dn"
		;
connectAttr "leg_L_fkik_blend_complement.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[67].dn"
		;
connectAttr "leg_L_limitedAnkle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[68].dn"
		;
connectAttr "leg_L_hip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[69].dn";
connectAttr "legGlobal_L_worldAnkle_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[70].dn"
		;
connectAttr "legGlobal_L_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[71].dn"
		;
connectAttr "legGlobal_L_guide_basisVector.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[72].dn"
		;
connectAttr "leg_L_tibiaStart_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[73].dn"
		;
connectAttr "legGlobal_L_animParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[74].dn"
		;
connectAttr "legGlobal_L_tarsi_rolledAngle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[75].dn"
		;
connectAttr "leg_L_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[76].dn";
connectAttr "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|foot_L_toes_ctrl_srtBuffer|foot_L_toes_ctrl|diagnostic_toes|diagnostic_tip.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[77].dn"
		;
connectAttr "leg_L_guide_tibiaLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[78].dn"
		;
connectAttr "leg_L_IK_solver_xpr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[79].dn"
		;
connectAttr "leg_L_globalAnkle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[80].dn"
		;
connectAttr "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|foot_L_toes_ctrl_srtBuffer|foot_L_toes_ctrl|diagnostic_toes.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[81].dn"
		;
connectAttr "legGlobal_L_roll_tarsi_fCurve.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[82].dn"
		;
connectAttr "leg_L_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[83].dn";
connectAttr "legGlobal_L_guide_toe_rest_angle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[84].dn"
		;
connectAttr "legGlobal_L_guide_ankle_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[85].dn"
		;
connectAttr "leg_L_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[86].dn"
		;
connectAttr "legGlobal_L_tarsiRollOffset_angle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[87].dn"
		;
connectAttr "legGlobal_L_roll_tarsi_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[88].dn"
		;
connectAttr "output_end_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[89].dn";
connectAttr "legGlobal_L_guide_upVector_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[90].dn"
		;
connectAttr "leg_L_guide_upVector_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[91].dn"
		;
connectAttr "legGlobal_L_roll_tarsiEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[92].dn"
		;
connectAttr "leg_L_hipWorld_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[93].dn"
		;
connectAttr "leg_L_limitedWorldAnkle_translate.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[94].dn"
		;
connectAttr "legGlobal_L_upVecReparent_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[95].dn"
		;
connectAttr "leg_L_IK_upVector_hipFramed_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[96].dn"
		;
connectAttr "leg_L_j01_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[97].dn";
connectAttr "legGlobal_L_upVecReparent_mtxMult.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[98].dn"
		;
connectAttr "legGlobal_L_roll_tarsi_world_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[99].dn"
		;
connectAttr "legGlobal_L_worldAnkle_ctrl_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[100].dn"
		;
connectAttr "legGlobal_L_ankleReparent_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[101].dn"
		;
connectAttr "leg_L_hip2ankle_distance.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[102].dn"
		;
connectAttr "leg_L_fk01_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[103].dn"
		;
connectAttr "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|diagnostic_ankle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[104].dn"
		;
connectAttr "leg_L_tibiaEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[105].dn"
		;
connectAttr "godNode_M_debuffer_com_output_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[106].dn"
		;
connectAttr "leg_L_guide_globalAnkleInfk02Space_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[107].dn"
		;
connectAttr "leg_L_fkik_j02_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[108].dn"
		;
connectAttr "legGlobal_L_ankleReparent_mtxMult.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[109].dn"
		;
connectAttr "leg_L_IK_ankleDisplacement_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[110].dn"
		;
connectAttr "leg_L_j03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[111].dn"
		;
connectAttr "leg_L_hip2Ankle_displacement.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[112].dn"
		;
connectAttr "|foot_L_cpmnt|control|foot_L_ankleSpace_srt|foot_L_tarsii_ctrl_srtBuffer|foot_L_tarsii_ctrl|diagnostic_ankle|diagnostic_tarsi.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[113].dn"
		;
connectAttr "legGlobal_L_guide_toe_length.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[114].dn"
		;
connectAttr "leg_L_fkik_j01_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[115].dn"
		;
connectAttr "legGlobal_L_toeRollOffset_angle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[116].dn"
		;
connectAttr "leg_L_fk01_ctrl_world_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[117].dn"
		;
connectAttr "leg_L_ankle_blend_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[118].dn"
		;
connectAttr "leg_L_guide_endWorldInverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[119].dn"
		;
connectAttr "leg_L_hip2Ankle_clamped_displacement.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[120].dn"
		;
connectAttr "leg_L_hipWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[121].dn"
		;
connectAttr "legGlobal_L_roll_tip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[122].dn"
		;
connectAttr "foot_L_ankleSpace_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[123].dn"
		;
connectAttr "leg_L_guide_hipPos_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[124].dn"
		;
connectAttr "legGlobal_L_ankle_rolled_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[125].dn"
		;
connectAttr "godNode_M_masterOffset_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[126].dn"
		;
connectAttr "legGlobal_L_ankleFramed_tarsi_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[127].dn"
		;
connectAttr "leg_L_hip2ankle_direction_normal.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[128].dn"
		;
connectAttr "leg_L_guide_ikHip_local_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[129].dn"
		;
connectAttr "leg_L_guide_hip_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[130].dn"
		;
connectAttr "legGlobal_L_roll_heel_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[131].dn"
		;
connectAttr "legGlobal_L_guide_tarsi_rest_negate_angle.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[132].dn"
		;
connectAttr "foot_L_start_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[133].dn"
		;
connectAttr "legGlobal_L_ankleFramed_tarsi_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[134].dn"
		;
connectAttr "leg_L_j02_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[135].dn";
connectAttr "leg_L_rolledAnkle_ctrl_world_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[136].dn"
		;
connectAttr "leg_L_container.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[0].dn";
connectAttr "leg_L_guide_kneeUpV_aim_cns.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[1].dn"
		;
connectAttr "leg_L_fk02_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[2].dn"
		;
connectAttr "leg_L_fk02reframed01_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[3].dn"
		;
connectAttr "leg_L_fk01_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[4].dn";
connectAttr "leg_L_globalAnkle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[5].dn"
		;
connectAttr "leg_L_guide_globalAnkleInfk02Space_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[6].dn"
		;
connectAttr "leg_L_tibiaStart_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[7].dn"
		;
connectAttr ":time1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[8].dn";
connectAttr "leg_L_guide_hipPos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[9].dn"
		;
connectAttr "leg_L_guide_kneePos_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[10].dn"
		;
connectAttr "leg_L_guide_endWorldInverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[11].dn"
		;
connectAttr "leg_L_fk01_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[12].dn"
		;
connectAttr "leg_L_j02_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[13].dn";
connectAttr "leg_L_guide_ikHip_local_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[14].dn"
		;
connectAttr "leg_L_IK_tension_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[15].dn"
		;
connectAttr "leg_L_fk03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[16].dn"
		;
connectAttr "leg_L_guide_hipPos_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[17].dn"
		;
connectAttr "leg_L_guide_tibiaLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[18].dn"
		;
connectAttr "leg_L_hip2Ankle_displacement.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[19].dn"
		;
connectAttr "leg_L_guide_ankle_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[20].dn"
		;
connectAttr "leg_L_hip_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[21].dn";
connectAttr "leg_L_lengthLimit_fNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[22].dn"
		;
connectAttr "leg_L_hip2Ankle_clamped_displacement.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[23].dn"
		;
connectAttr "leg_L_IK_upVector_hipFramed_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[24].dn"
		;
connectAttr "leg_L_IK_upVectoringAngle.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[25].dn"
		;
connectAttr "legGlobal_L_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[26].dn"
		;
connectAttr "leg_L_j03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[27].dn"
		;
connectAttr "leg_L_guide_hip_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[28].dn"
		;
connectAttr "leg_L_fk02_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[29].dn"
		;
connectAttr "|leg_L_cmpnt|guide.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[30].dn"
		;
connectAttr "leg_L_j03_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[31].dn";
connectAttr "leg_L_hip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[32].dn";
connectAttr "leg_L_limitedAnkleWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[33].dn"
		;
connectAttr "leg_L_FK_start_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[34].dn"
		;
connectAttr "leg_L_hipWorld_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[35].dn"
		;
connectAttr "leg_L_IK_ankleDisplacement_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[36].dn"
		;
connectAttr "leg_L_j01_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[37].dn";
connectAttr "leg_L_guide_globalAnkleInfk02Space.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[38].dn"
		;
connectAttr "|leg_L_cmpnt|control.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[39].dn"
		;
connectAttr "leg_L_guide_upVector_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[40].dn"
		;
connectAttr "|leg_L_cmpnt|deform.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[41].dn"
		;
connectAttr "leg_L_hip2ankle_direction_normal.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[42].dn"
		;
connectAttr "leg_L_toolParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[43].dn"
		;
connectAttr "leg_L_totalLength_fNode_add.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[44].dn"
		;
connectAttr "leg_L_ankle_blend_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[45].dn"
		;
connectAttr "leg_L_fkik_blend_complement.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[46].dn"
		;
connectAttr "leg_L_guide_knee_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[47].dn"
		;
connectAttr "leg_L_IK_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[48].dn"
		;
connectAttr "leg_L_fkik_j01_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[49].dn"
		;
connectAttr "leg_L_fk03_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[50].dn"
		;
connectAttr "leg_L_ankle2hip_clampedDistance.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[51].dn"
		;
connectAttr "leg_L_FK_start_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[52].dn"
		;
connectAttr "leg_L_rolledAnkle_ctrl_world_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[53].dn"
		;
connectAttr "leg_L_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[54].dn"
		;
connectAttr "leg_L_guide_femurLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[55].dn"
		;
connectAttr "leg_L_hipWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[56].dn"
		;
connectAttr "leg_L_fk02reframed01_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[57].dn"
		;
connectAttr "leg_L_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[58].dn";
connectAttr "leg_L_tibiaEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[59].dn"
		;
connectAttr "foot_L_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[60].dn";
connectAttr "leg_L_guide_hipInput_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[61].dn"
		;
connectAttr "leg_L_cmpnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[62].dn";
connectAttr "leg_L_IK_upVector_hipYProjected_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[63].dn"
		;
connectAttr "leg_L_FK_hrc.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[64].dn";
connectAttr "leg_L_limitedAnkle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[65].dn"
		;
connectAttr "leg_L_IK_solver_xpr.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[66].dn"
		;
connectAttr "leg_L_femurEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[67].dn"
		;
connectAttr "leg_L_fk03_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[68].dn"
		;
connectAttr "leg_L_fk01_ctrl_world_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[69].dn"
		;
connectAttr "leg_L_guide_kneePos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[70].dn"
		;
connectAttr "leg_L_ankle_rotBlend.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[71].dn"
		;
connectAttr "leg_L_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[72].dn";
connectAttr "leg_L_rolledAnkle_frame_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[73].dn"
		;
connectAttr "output_end_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[74].dn";
connectAttr "leg_L_fkik_j02_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[75].dn"
		;
connectAttr "leg_L_guide_hip2UpV_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[76].dn"
		;
connectAttr "leg_L_hip2ankle_distance.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[77].dn"
		;
connectAttr "leg_L_animParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[78].dn"
		;
connectAttr "leg_L_limitedWorldAnkle_translate.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[79].dn"
		;
connectAttr ":initialShadingGroup.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[80].dn"
		;
connectAttr "leg_R_fk01_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[0].dn"
		;
connectAttr ":initialShadingGroup.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[1].dn"
		;
connectAttr "leg_R_fk02_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[2].dn";
connectAttr "leg_R_fkik_blend_complement.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[3].dn"
		;
connectAttr "leg_R_FK_hrc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[4].dn";
connectAttr "leg_R_cmpnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[5].dn";
connectAttr "leg_R_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[6].dn";
connectAttr "leg_R_fk02reframed01_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[7].dn"
		;
connectAttr "leg_R_hip2ankle_direction_normal.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[8].dn"
		;
connectAttr "leg_R_IK_ankleDisplacement_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[9].dn"
		;
connectAttr "leg_R_toolParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[10].dn"
		;
connectAttr "leg_R_guide_hipInput_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[11].dn"
		;
connectAttr "leg_R_guide_globalAnkleInfk02Space.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[12].dn"
		;
connectAttr "leg_R_femurEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[13].dn"
		;
connectAttr "leg_R_ankle2hip_clampedDistance.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[14].dn"
		;
connectAttr "leg_R_j02_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[15].dn";
connectAttr "leg_R_container.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[16].dn"
		;
connectAttr "leg_R_guide_kneePos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[17].dn"
		;
connectAttr "leg_R_fk02_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[18].dn"
		;
connectAttr "leg_R_ankle_blend_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[19].dn"
		;
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[20].dn"
		;
connectAttr "leg_R_FK_start_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[21].dn"
		;
connectAttr ":time1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[22].dn";
connectAttr "leg_R_guide_ankle_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[23].dn"
		;
connectAttr "leg_R_tibiaEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[24].dn"
		;
connectAttr "leg_R_hipWorld_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[25].dn"
		;
connectAttr "leg_R_IK_upVector_hipYProjected_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[26].dn"
		;
connectAttr "leg_R_guide_upVector_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[27].dn"
		;
connectAttr "leg_R_guide_tibiaLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[28].dn"
		;
connectAttr "leg_R_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[29].dn"
		;
connectAttr "leg_R_fkik_j02_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[30].dn"
		;
connectAttr "leg_R_IK_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[31].dn"
		;
connectAttr "leg_R_ankle_rotBlend.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[32].dn"
		;
connectAttr "leg_R_hip_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[33].dn";
connectAttr "leg_R_j03_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[34].dn";
connectAttr "leg_R_hip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[35].dn";
connectAttr "leg_R_guide_knee_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[36].dn"
		;
connectAttr "leg_R_guide_kneePos_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[37].dn"
		;
connectAttr "leg_R_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[38].dn";
connectAttr "leg_R_hip2Ankle_displacement.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[39].dn"
		;
connectAttr "|leg_R_cmpnt|deform.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[40].dn"
		;
connectAttr "leg_R_guide_hip2UpV_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[41].dn"
		;
connectAttr "leg_R_j03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[42].dn"
		;
connectAttr "leg_R_globalAnkle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[43].dn"
		;
connectAttr "leg_R_hip2ankle_distance.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[44].dn"
		;
connectAttr "leg_R_guide_hipPos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[45].dn"
		;
connectAttr "leg_R_limitedAnkle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[46].dn"
		;
connectAttr "leg_R_hip2Ankle_clamped_displacement.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[47].dn"
		;
connectAttr "leg_R_guide_femurLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[48].dn"
		;
connectAttr "leg_R_guide_kneeUpV_aim_cns.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[49].dn"
		;
connectAttr "leg_R_lengthLimit_fNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[50].dn"
		;
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[51].dn"
		;
connectAttr "leg_R_animParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[52].dn"
		;
connectAttr "leg_R_IK_upVectoringAngle.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[53].dn"
		;
connectAttr "leg_R_fk02reframed01_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[54].dn"
		;
connectAttr "leg_R_guide_hip_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[55].dn"
		;
connectAttr "leg_R_guide_hipPos_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[56].dn"
		;
connectAttr "leg_R_limitedWorldAnkle_translate.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[57].dn"
		;
connectAttr "leg_R_IK_solver_xpr.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[58].dn"
		;
connectAttr "leg_R_fk03_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[59].dn"
		;
connectAttr "leg_R_limitedAnkleWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[60].dn"
		;
connectAttr "leg_R_totalLength_fNode_add.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[61].dn"
		;
connectAttr "leg_R_fkik_j01_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[62].dn"
		;
connectAttr "leg_R_IK_tension_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[63].dn"
		;
connectAttr "leg_R_fk01_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[64].dn"
		;
connectAttr "leg_R_fk03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[65].dn"
		;
connectAttr "leg_R_guide_globalAnkleInfk02Space_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[66].dn"
		;
connectAttr "|leg_R_cmpnt|control.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[67].dn"
		;
connectAttr "leg_R_FK_start_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[68].dn"
		;
connectAttr "leg_R_rolledAnkle_ctrl_world_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[69].dn"
		;
connectAttr "|leg_R_cmpnt|guide.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[70].dn"
		;
connectAttr "leg_R_j01_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[71].dn";
connectAttr "leg_R_hipWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[72].dn"
		;
connectAttr "leg_R_tibiaStart_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[73].dn"
		;
connectAttr "leg_R_IK_upVector_hipFramed_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[74].dn"
		;
connectAttr "leg_R_rolledAnkle_frame_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[75].dn"
		;
connectAttr "leg_R_fk03_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[76].dn"
		;
connectAttr "leg_R_guide_ikHip_local_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[77].dn"
		;
connectAttr "leg_R_guide_hip_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[0].dn"
		;
connectAttr "leg_R_fk03_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[1].dn";
connectAttr "leg_R_FK_hrc.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[2].dn";
connectAttr "leg_R_tibiaStart_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[3].dn"
		;
connectAttr "leg_R_handedNessSign.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[4].dn"
		;
connectAttr "leg_R_guide_kneeUpV_aim_cns.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[5].dn"
		;
connectAttr "leg_R_fk03_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[6].dn"
		;
connectAttr "leg_R_guide_globalAnkleInfk02Space.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[7].dn"
		;
connectAttr "leg_R_tibiaEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[8].dn"
		;
connectAttr "leg_R_FK_start_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[9].dn"
		;
connectAttr "leg_R_fk01_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[10].dn"
		;
connectAttr "leg_R_j02_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[11].dn";
connectAttr "leg_R_fk02_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[12].dn"
		;
connectAttr "leg_R_guide_globalAnkleInfk02Space_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[13].dn"
		;
connectAttr "leg_R_fk02reframed01_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[14].dn"
		;
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[15].dn"
		;
connectAttr "animBlendNodeAdditiveDA1.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[16].dn"
		;
connectAttr "leg_R_toolParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[17].dn"
		;
connectAttr "leg_R_femurEnd_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[18].dn"
		;
connectAttr "leg_R_FK_start_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[19].dn"
		;
connectAttr "leg_R_IK_solver_xpr.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[20].dn"
		;
connectAttr "leg_R_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[21].dn"
		;
connectAttr "leg_R_hipWorld_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[22].dn"
		;
connectAttr "leg_R_guide_hipPos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[23].dn"
		;
connectAttr "leg_R_totalLength_fNode_add.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[24].dn"
		;
connectAttr "multDoubleLinear1.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[25].dn"
		;
connectAttr "leg_R_fk03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[26].dn"
		;
connectAttr "leg_R_fk_handedness.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[27].dn"
		;
connectAttr "leg_R_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[28].dn";
connectAttr "leg_R_fk01_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[29].dn"
		;
connectAttr "leg_R_j03_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[30].dn";
connectAttr "leg_R_fk02_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[31].dn"
		;
connectAttr "leg_R_hip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[0].dn";
connectAttr "animBlendNodeAdditiveDA1.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[1].dn"
		;
connectAttr "leg_R_fkik_blend_complement.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[2].dn"
		;
connectAttr "leg_R_handedNessSign.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[3].dn"
		;
connectAttr "leg_L_guide_endWorldInverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[4].dn"
		;
connectAttr "animBlendNodeAdditiveDA2.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[5].dn"
		;
connectAttr "multDoubleLinear1.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[6].dn"
		;
connectAttr "leg_R_FK_start_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[7].dn"
		;
connectAttr "leg_L_guide_femurLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[8].dn"
		;
connectAttr "leg_R_IK_upVectoringAngle.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[9].dn"
		;
connectAttr "leg_L_guide_hipPos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[10].dn"
		;
connectAttr "leg_R_j01_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[11].dn";
connectAttr "leg_R_IK_solver_xpr.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[12].dn"
		;
connectAttr "leg_R_fkik_j02_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[13].dn"
		;
connectAttr "leg_R_tibiaStart_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[14].dn"
		;
connectAttr "leg_L_guide_ikHip_local_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[15].dn"
		;
connectAttr "leg_R_guide_ikHip_local_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[16].dn"
		;
connectAttr "leg_L_IK_upVectoringAngle.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[17].dn"
		;
connectAttr "leg_R_FK_start_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[18].dn"
		;
connectAttr "leg_L_IK_solver_xpr.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[19].dn"
		;
connectAttr "leg_R_hip_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[20].dn";
connectAttr "leg_L_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[21].dn";
connectAttr "leg_R_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[22].dn";
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[23].dn"
		;
connectAttr "leg_R_j02_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[24].dn";
connectAttr "leg_L_hip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[25].dn";
connectAttr "leg_R_guide_tibiaLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[26].dn"
		;
connectAttr "leg_R_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[27].dn"
		;
connectAttr "leg_R_j03_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[28].dn";
connectAttr "leg_L_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[29].dn"
		;
connectAttr "leg_L_FK_start_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[30].dn"
		;
connectAttr "leg_L_FK_start_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[31].dn"
		;
connectAttr "leg_R_fk01_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[32].dn"
		;
connectAttr "leg_R_animParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[33].dn"
		;
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[34].dn"
		;
connectAttr "leg_R_guide_femurLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[35].dn"
		;
connectAttr "leg_R_guide_hipPos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[36].dn"
		;
connectAttr "leg_R_hipWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[37].dn"
		;
connectAttr "leg_R_fkik_j01_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[38].dn"
		;
connectAttr "leg_L_fk01_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[39].dn"
		;
connectAttr "leg_L_guide_tibiaLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[40].dn"
		;
connectAttr "leg_R_fk02reframed01_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[41].dn"
		;
connectAttr "leg_R_fkik_j02_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[0].dn"
		;
connectAttr "leg_R_guide_ikHip_local_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[1].dn"
		;
connectAttr "leg_R_hip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[2].dn";
connectAttr "leg_R_fkik_blend_complement.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[3].dn"
		;
connectAttr "leg_R_j01_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[4].dn";
connectAttr "leg_R_handedNessSign.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[5].dn"
		;
connectAttr "leg_R_guide_knee_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[6].dn"
		;
connectAttr "leg_R_j02_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[7].dn";
connectAttr "leg_R_animParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[8].dn"
		;
connectAttr "leg_R_handednessMatrix.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[9].dn"
		;
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[10].dn"
		;
connectAttr "leg_R_fk02reframed01_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[11].dn"
		;
connectAttr "leg_R_fk02reframed01_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[12].dn"
		;
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[13].dn"
		;
connectAttr "leg_R_tibiaStart_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[14].dn"
		;
connectAttr "leg_R_unhandedFK01_inverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[15].dn"
		;
connectAttr "leg_R_toolParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[16].dn"
		;
connectAttr "leg_R_guide_hip_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[17].dn"
		;
connectAttr "leg_R_guide_hipPos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[18].dn"
		;
connectAttr "leg_R_guide_hip2UpV_vec.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[19].dn"
		;
connectAttr "leg_R_hip_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[20].dn";
connectAttr "leg_R_guide_femurLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[21].dn"
		;
connectAttr "leg_R_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[22].dn"
		;
connectAttr "leg_R_unhandedFK01_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[23].dn"
		;
connectAttr "leg_R_guide_ankle_world_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[24].dn"
		;
connectAttr "leg_R_hipWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[25].dn"
		;
connectAttr "leg_R_fk01_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[26].dn"
		;
connectAttr "leg_R_guide_tibiaLength.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[27].dn"
		;
connectAttr "leg_R_fkik_j01_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[28].dn"
		;
connectAttr "leg_R_fk02_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[29].dn"
		;
connectAttr "leg_R_j01_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[0].dn";
connectAttr "foot_R_ankleSpace_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[1].dn"
		;
connectAttr "leg_R_guide_ikHip_local_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[2].dn"
		;
connectAttr "leg_R_guide_endWorldInverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[3].dn"
		;
connectAttr "leg_R_fk02reframed01_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[4].dn"
		;
connectAttr "leg_R_j03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[5].dn"
		;
connectAttr "leg_R_fkik_blend_complement.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[6].dn"
		;
connectAttr "foot_R_tarsii_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[7].dn"
		;
connectAttr "leg_R_guide_hipPos_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[8].dn"
		;
connectAttr "leg_R_ankle_rotBlend.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[9].dn"
		;
connectAttr "leg_R_unhandedFK01_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[10].dn"
		;
connectAttr "leg_R_animParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[11].dn"
		;
connectAttr "leg_R_fkik_j02_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[12].dn"
		;
connectAttr "leg_R_j02_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[13].dn";
connectAttr "leg_R_fk02reframed01_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[14].dn"
		;
connectAttr "foot_R_toes_ctrl_srtBuffer.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[15].dn"
		;
connectAttr "leg_R_fk01_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[16].dn"
		;
connectAttr "leg_R_fk03_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[17].dn"
		;
connectAttr "leg_R_tibiaStart_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[18].dn"
		;
connectAttr "leg_R_ankle_blend_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[19].dn"
		;
connectAttr "leg_R_unhandedFK01_inverse_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[20].dn"
		;
connectAttr "leg_R_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[21].dn"
		;
connectAttr "leg_R_handednessMatrix.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[22].dn"
		;
connectAttr "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|foot_R_toes_ctrl_srtBuffer|foot_R_toes_ctrl|diagnostic_toes|diagnostic_tip.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[23].dn"
		;
connectAttr "leg_R_hip_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[24].dn";
connectAttr "leg_R_unhandedFK03_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[25].dn"
		;
connectAttr "leg_R_hipWorld_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[26].dn"
		;
connectAttr "leg_R_fk01_ctrl_world_mtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[27].dn"
		;
connectAttr "leg_R_fk02_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[28].dn"
		;
connectAttr "leg_R_handedNessSign.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[29].dn"
		;
connectAttr "leg_R_globalAnkle_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[30].dn"
		;
connectAttr "|foot_R_cpmnt|control|foot_R_ankleSpace_srt|foot_R_tarsii_ctrl_srtBuffer|foot_R_tarsii_ctrl|diagnostic_ankle|diagnostic_tarsi.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[31].dn"
		;
connectAttr "leg_R_hip_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[32].dn";
connectAttr "foot_R_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[33].dn";
connectAttr "foot_R_start_mtx2srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[34].dn"
		;
connectAttr "leg_R_fkik_j01_blended_rot.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[35].dn"
		;
connectAttr "leg_R_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[36].dn";
connectAttr "leg_R_fk03_worldMtx.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[37].dn"
		;
connectAttr "legGlobal_L_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[0].dn"
		;
connectAttr "foot_L_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[1].dn";
connectAttr "foot_R_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[2].dn";
connectAttr "legGlobal_L_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[3].dn"
		;
connectAttr "leg_R_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[4].dn";
connectAttr "legGlobal_R_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[5].dn"
		;
connectAttr "leg_L_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[6].dn";
connectAttr "legGlobal_L_configParameters.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[7].dn"
		;
connectAttr "legGlobal_R_output.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[8].dn"
		;
connectAttr "legGlobal_R_input.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[9].dn"
		;
connectAttr "output_master_srt.msg" "MayaNodeEditorSavedTabsInfo.tgi[7].ni[10].dn"
		;
connectAttr "leg_L_hip2Ankle_displacement.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_L_limitedWorldAnkle_translate.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_totalLength_fNode_add.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_L_hip2ankle_direction_normal.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_hip2Ankle_clamped_displacement.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_ankle2hip_clampedDistance.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_hip2ankle_distance.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "legGlobal_L_heelBack_rollClamp.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "legGlobal_L_roll_tarsi_world_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_rolledAnkle_ctrl_world_mtx2srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_tarsi_worldDirection_vec3.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_roll_toes_world_mtx2srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_tarsi_rolledAngle.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "foot_L_start_mtx2srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_hipWorld_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_IK_tension_rot.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_IK_ankleDisplacement_vec.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "leg_L_IK_upVector_hipFramed_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_IK_upVector_hipYProjected_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_IK_upVectoringAngle.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_lengthLimit_fNode.msg" ":defaultRenderUtilityList1.u" -na;
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
connectAttr "godNode_M_master_ctrl_wMtx_output_fNode.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "godNode_M_debuffer_com_output_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "godNode_M_debuffer_com_output_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "godNode_M_debuffer_end_output_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "godNode_M_debuffer_end_output_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_hipWorld_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "legGlobal_L_ankleReparent_mtxMult.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_ankleReparent_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_L_upVecReparent_mtxMult.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_L_upVecReparent_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_L_limitedAnkleWorld_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_L_hip_rot.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_fk01_ctrl_world_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_fk02reframed01_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_fk02reframed01_rot.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_FK_start_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_rolledAnkle_frame_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_L_guide_hipInput_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_guide_femurLength.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_guide_ankle_world_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_L_guide_knee_world_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_guide_tibiaLength.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_guide_hip_world_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_guide_upVector_srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_guide_hip2UpV_vec.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_guide_globalAnkleInfk02Space.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_guide_globalAnkleInfk02Space_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_guide_ikHip_local_mtx.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_L_guide_endWorldInverse_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "leg_L_FK_start_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_fk03_worldMtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_j03_worldMtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_ankle_blend_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_L_globalAnkle_srt.msg" ":defaultRenderUtilityList1.u" -na;
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
connectAttr "multDoubleLinear1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "legGlobal_R_heelBack_rollClamp.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "legGlobal_R_roll_tarsi_world_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_tarsi_worldDirection_vec3.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_roll_toes_world_mtx2srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_tarsi_rolledAngle.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_R_guide_toe_length.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_R_guide_tarsi_length.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "legGlobal_R_guide_tarsi2Toe_rest_angle.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_guide_toe_direction_vec.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_guide_tarsi_direction_vec.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_guide_toe_rest_angle.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_guide_ankle_world_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_guide_tarsi2World_rest_angle.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_ankleFramed_tarsi_mtx.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_ankleFramed_tarsi_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_worldAnkle_ctrl_world_srt.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_ankleReparent_mtxMult.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_ankleReparent_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "legGlobal_R_upVecReparent_mtxMult.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "legGlobal_R_upVecReparent_srt.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "leg_R_unhandedFK01_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_handednessMatrix.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_unhandedFK01_inverse_mtx.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "foot_R_start_mtx2srt.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "leg_R_unhandedFK03_mtx.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "|leg_L_cmpnt|control|leg_L_IK_srtBuffer|leg_L_hip_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "|leg_L_cmpnt|control|leg_L_IK_srtBuffer|leg_L_hip_srt|leg_L_femurEnd_srt|leg_L_tibiaStart_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "|leg_L_cmpnt|control|leg_L_IK_srtBuffer|leg_L_hip_srt|leg_L_femurEnd_srt|leg_L_tibiaStart_srt|leg_L_tibiaEnd_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|leg_R_femurEnd_srt|leg_R_tibiaStart_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
connectAttr "|leg_R_cmpnt|control|leg_R_IK_srtBuffer|leg_R_hip_srt|leg_R_femurEnd_srt|leg_R_tibiaStart_srt|leg_R_tibiaEnd_srt|diagnosticCube_geoShape.iog" ":initialShadingGroup.dsm"
		 -na;
// End of id10_legSymmetry_v001_008.ma
