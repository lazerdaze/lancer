//Maya ASCII 2018 scene
//Name: rig_flexiPlane_02.ma
//Last modified: Wed, May 23, 2018 10:58:34 PM
//Codeset: 1252
requires maya "2018";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2018.0.0";
requires "stereoCamera" "10.0";
requires "Mayatomr" "2013.0 - 3.10.1.4 ";
requires "Turtle" "5.4.0.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	rename -uid "33EEC504-4AC2-E884-DAA0-0696DF4EB961";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -0.11960655937056813 9.7798710600952763 11.401109618199133 ;
	setAttr ".r" -type "double3" -51.938352729603757 -1.0000000000000464 4.9703737017760717e-17 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "95789681-42AC-44BE-DD0E-71A16578E3CC";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 15.758645141593568;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "9F5AE913-429D-1AC6-8958-D4B1887173FE";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "070E53F7-406E-FF72-0C2C-96A90E45F84E";
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
	rename -uid "C00990A9-4599-0C33-1706-C89BC2B47B99";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "B835D1E0-47D0-D71F-3890-0286B6DC7FBE";
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
	rename -uid "AD622B0F-4E47-A97D-33DE-A9A4F440B638";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "7D61CCE5-4A34-60D8-B0E0-F89403600F0E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "flexiPlane01";
	rename -uid "FEE1A79E-4ABD-A526-2129-0CA5CF633E57";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "flexiPlane_cnt_global01" -p "flexiPlane01";
	rename -uid "D8A8951B-45EF-EBBA-27C9-19A68C51B3DA";
	addAttr -ci true -sn "_" -ln "_" -min 0 -max 0 -en "volume" -at "enum";
	addAttr -ci true -sn "enable" -ln "enable" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr -cb on "._";
	setAttr -k on ".enable" yes;
createNode nurbsCurve -n "flexiPlane_cnt_global0Shape1" -p "flexiPlane_cnt_global01";
	rename -uid "918DAB04-4010-D259-2AA8-94B505432165";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.23508348746736751 1.4394712022965405e-17 -2.2350834874673673
		-3.7929511823487977e-17 2.0357196969332741e-17 -2.3324582562663165
		-0.23508348746736729 1.4394712022965414e-17 -2.2350834874673673
		-0.33245825626631637 5.8990063848563562e-33 -2
		-0.23508348746736735 -1.4394712022965408e-17 -1.7649165125326327
		-1.0017616090771555e-16 -2.0357196969332744e-17 -1.6675417437336837
		0.23508348746736712 -1.4394712022965414e-17 -1.7649165125326327
		0.33245825626631637 -1.0933890203714376e-32 -2
		0.23508348746736751 1.4394712022965405e-17 -2.2350834874673673
		-3.7929511823487977e-17 2.0357196969332741e-17 -2.3324582562663165
		-0.23508348746736729 1.4394712022965414e-17 -2.2350834874673673
		;
createNode nurbsCurve -n "flexiPlane_cnt_global0Shape2" -p "flexiPlane_cnt_global01";
	rename -uid "6CA2B331-48C8-41A7-3C1E-42A1593496B3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.23508348746736751 1.4394712022965405e-17 1.7649165125326327
		-3.7929511823487977e-17 2.0357196969332741e-17 1.6675417437336837
		-0.23508348746736729 1.4394712022965414e-17 1.7649165125326327
		-0.33245825626631637 5.8990063848563562e-33 2
		-0.23508348746736735 -1.4394712022965408e-17 2.2350834874673673
		-1.0017616090771555e-16 -2.0357196969332744e-17 2.3324582562663165
		0.23508348746736712 -1.4394712022965414e-17 2.2350834874673673
		0.33245825626631637 -1.0933890203714376e-32 2
		0.23508348746736751 1.4394712022965405e-17 1.7649165125326327
		-3.7929511823487977e-17 2.0357196969332741e-17 1.6675417437336837
		-0.23508348746736729 1.4394712022965414e-17 1.7649165125326327
		;
createNode transform -n "flexiPlane_globalMove01" -p "flexiPlane_cnt_global01";
	rename -uid "FFE40FCD-45B1-B560-9C75-E8BCF7DCF99C";
createNode transform -n "flexiPlane_cnts01" -p "flexiPlane_globalMove01";
	rename -uid "48266AC4-4378-EF5E-E08F-23A4313663BE";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "flexiPlane_cnt_a01" -p "flexiPlane_cnts01";
	rename -uid "6B47F1CC-4396-93A6-27AE-3D9EE412E94B";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".ro" 3;
	setAttr ".rp" -type "double3" -5 0 0 ;
	setAttr ".sp" -type "double3" -5 0 0 ;
createNode nurbsCurve -n "flexiPlane_cnt_a0Shape1" -p "flexiPlane_cnt_a01";
	rename -uid "B363ADD8-4FCF-AC4C-0516-5BBB102FFA66";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-5.6126629382517601 0 0.61266293825175999
		-4.3873370617482408 0 0.61266293825175999
		-4.3873370617482408 0 -0.61266293825175999
		-5.6126629382517601 0 -0.61266293825175999
		-5.6126629382517601 0 0.61266293825175999
		;
createNode transform -n "flexiPlane_cnt_b01" -p "flexiPlane_cnts01";
	rename -uid "F60247B5-4F5A-1664-0191-4EAB25D2A3FC";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".ro" 3;
	setAttr ".rp" -type "double3" 4.9999999999999991 0 0 ;
	setAttr ".sp" -type "double3" 4.9999999999999991 0 0 ;
createNode nurbsCurve -n "flexiPlane_cnt_b0Shape1" -p "flexiPlane_cnt_b01";
	rename -uid "22E3B8A0-49A0-D878-AD53-9F97E09CC86F";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		4.387337061748239 0 0.61266293825175999
		5.6126629382517592 0 0.61266293825175999
		5.6126629382517592 0 -0.61266293825175999
		4.387337061748239 0 -0.61266293825175999
		4.387337061748239 0 0.61266293825175999
		;
createNode transform -n "flexiPlane_grp_midBend01" -p "flexiPlane_cnts01";
	rename -uid "5CCF3978-4C5A-12AB-6EDB-12957FAC3392";
createNode transform -n "flexiPlane_midBend01" -p "flexiPlane_grp_midBend01";
	rename -uid "ED2F17C8-447A-DF0D-E823-CAB3F02C1FFF";
createNode mesh -n "flexiPlane_midBend0Shape1" -p "flexiPlane_midBend01";
	rename -uid "7F357D6D-470F-493E-B210-FDBDF303A408";
	setAttr -k off ".v";
	setAttr ".mb" no;
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".vis" no;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 79 ".uvst[0].uvsp[0:78]" -type "float2" 0 0.125 0.125 0.125
		 0.25 0.125 0.375 0.125 0.5 0.125 0.625 0.125 0.75 0.125 0.875 0.125 1 0.125 0 0.25
		 0.125 0.25 0.25 0.25 0.375 0.25 0.5 0.25 0.625 0.25 0.75 0.25 0.875 0.25 1 0.25 0
		 0.375 0.125 0.375 0.25 0.375 0.375 0.375 0.5 0.375 0.625 0.375 0.75 0.375 0.875 0.375
		 1 0.375 0 0.5 0.125 0.5 0.25 0.5 0.375 0.5 0.5 0.5 0.625 0.5 0.75 0.5 0.875 0.5 1
		 0.5 0 0.625 0.125 0.625 0.25 0.625 0.375 0.625 0.5 0.625 0.625 0.625 0.75 0.625 0.875
		 0.625 1 0.625 0 0.75 0.125 0.75 0.25 0.75 0.375 0.75 0.5 0.75 0.625 0.75 0.75 0.75
		 0.875 0.75 1 0.75 0 0.875 0.125 0.875 0.25 0.875 0.375 0.875 0.5 0.875 0.625 0.875
		 0.75 0.875 0.875 0.875 1 0.875 0.0625 0 0.1875 0 0.3125 0 0.4375 0 0.5625 0 0.6875
		 0 0.8125 0 0.9375 0 0.0625 1 0.1875 1 0.3125 1 0.4375 1 0.5625 1 0.6875 1 0.8125
		 1 0.9375 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".smo" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ugsdt" no;
	setAttr -s 58 ".pt[0:57]" -type "float3"  0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 0 0 1.4305115e-06 
		0 0 1.4305115e-06 0;
	setAttr -s 58 ".vt[0:57]"  0.081179418 -0.27716386 -0.081179418 0 -0.27716386 -0.11480502
		 -0.081179418 -0.27716386 -0.081179418 -0.11480502 -0.27716386 0 -0.081179418 -0.27716386 0.081179418
		 0 -0.27716386 0.11480504 0.081179418 -0.27716386 0.081179418 0.11480504 -0.27716386 0
		 0.14999999 -0.21213204 -0.14999999 0 -0.21213204 -0.21213202 -0.14999999 -0.21213204 -0.14999999
		 -0.21213202 -0.21213204 0 -0.14999999 -0.21213204 0.14999999 0 -0.21213204 0.21213202
		 0.14999999 -0.21213204 0.14999999 0.21213204 -0.21213204 0 0.19598442 -0.11480504 -0.19598442
		 0 -0.11480504 -0.27716383 -0.19598442 -0.11480504 -0.19598442 -0.27716383 -0.11480504 0
		 -0.19598442 -0.11480504 0.19598442 0 -0.11480504 0.27716383 0.19598444 -0.11480504 0.19598444
		 0.27716386 -0.11480504 0 0.21213202 0 -0.21213202 0 0 -0.29999998 -0.21213202 0 -0.21213202
		 -0.29999998 0 0 -0.21213202 0 0.21213202 0 0 0.29999998 0.21213204 0 0.21213204 0.30000001 0 0
		 0.19598442 0.11480504 -0.19598442 0 0.11480504 -0.27716383 -0.19598442 0.11480504 -0.19598442
		 -0.27716383 0.11480504 0 -0.19598442 0.11480504 0.19598442 0 0.11480504 0.27716383
		 0.19598444 0.11480504 0.19598444 0.27716386 0.11480504 0 0.14999999 0.21213204 -0.14999999
		 0 0.21213204 -0.21213202 -0.14999999 0.21213204 -0.14999999 -0.21213202 0.21213204 0
		 -0.14999999 0.21213204 0.14999999 0 0.21213204 0.21213202 0.14999999 0.21213204 0.14999999
		 0.21213204 0.21213204 0 0.081179418 0.27716386 -0.081179418 0 0.27716386 -0.11480502
		 -0.081179418 0.27716386 -0.081179418 -0.11480502 0.27716386 0 -0.081179418 0.27716386 0.081179418
		 0 0.27716386 0.11480504 0.081179418 0.27716386 0.081179418 0.11480504 0.27716386 0
		 0 -0.30000001 0 0 0.30000001 0;
	setAttr -s 120 ".ed[0:119]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 0 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 8 0 16 17 0 17 18 0
		 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0 23 16 0 24 25 0 25 26 0 26 27 0 27 28 0 28 29 0
		 29 30 0 30 31 0 31 24 0 32 33 0 33 34 0 34 35 0 35 36 0 36 37 0 37 38 0 38 39 0 39 32 0
		 40 41 0 41 42 0 42 43 0 43 44 0 44 45 0 45 46 0 46 47 0 47 40 0 48 49 0 49 50 0 50 51 0
		 51 52 0 52 53 0 53 54 0 54 55 0 55 48 0 0 8 0 1 9 0 2 10 0 3 11 0 4 12 0 5 13 0 6 14 0
		 7 15 0 8 16 0 9 17 0 10 18 0 11 19 0 12 20 0 13 21 0 14 22 0 15 23 0 16 24 0 17 25 0
		 18 26 0 19 27 0 20 28 0 21 29 0 22 30 0 23 31 0 24 32 0 25 33 0 26 34 0 27 35 0 28 36 0
		 29 37 0 30 38 0 31 39 0 32 40 0 33 41 0 34 42 0 35 43 0 36 44 0 37 45 0 38 46 0 39 47 0
		 40 48 0 41 49 0 42 50 0 43 51 0 44 52 0 45 53 0 46 54 0 47 55 0 56 0 0 56 1 0 56 2 0
		 56 3 0 56 4 0 56 5 0 56 6 0 56 7 0 48 57 0 49 57 0 50 57 0 51 57 0 52 57 0 53 57 0
		 54 57 0 55 57 0;
	setAttr -s 64 -ch 240 ".fc[0:63]" -type "polyFaces" 
		f 4 0 57 -9 -57
		mu 0 4 0 1 10 9
		f 4 1 58 -10 -58
		mu 0 4 1 2 11 10
		f 4 2 59 -11 -59
		mu 0 4 2 3 12 11
		f 4 3 60 -12 -60
		mu 0 4 3 4 13 12
		f 4 4 61 -13 -61
		mu 0 4 4 5 14 13
		f 4 5 62 -14 -62
		mu 0 4 5 6 15 14
		f 4 6 63 -15 -63
		mu 0 4 6 7 16 15
		f 4 7 56 -16 -64
		mu 0 4 7 8 17 16
		f 4 8 65 -17 -65
		mu 0 4 9 10 19 18
		f 4 9 66 -18 -66
		mu 0 4 10 11 20 19
		f 4 10 67 -19 -67
		mu 0 4 11 12 21 20
		f 4 11 68 -20 -68
		mu 0 4 12 13 22 21
		f 4 12 69 -21 -69
		mu 0 4 13 14 23 22
		f 4 13 70 -22 -70
		mu 0 4 14 15 24 23
		f 4 14 71 -23 -71
		mu 0 4 15 16 25 24
		f 4 15 64 -24 -72
		mu 0 4 16 17 26 25
		f 4 16 73 -25 -73
		mu 0 4 18 19 28 27
		f 4 17 74 -26 -74
		mu 0 4 19 20 29 28
		f 4 18 75 -27 -75
		mu 0 4 20 21 30 29
		f 4 19 76 -28 -76
		mu 0 4 21 22 31 30
		f 4 20 77 -29 -77
		mu 0 4 22 23 32 31
		f 4 21 78 -30 -78
		mu 0 4 23 24 33 32
		f 4 22 79 -31 -79
		mu 0 4 24 25 34 33
		f 4 23 72 -32 -80
		mu 0 4 25 26 35 34
		f 4 24 81 -33 -81
		mu 0 4 27 28 37 36
		f 4 25 82 -34 -82
		mu 0 4 28 29 38 37
		f 4 26 83 -35 -83
		mu 0 4 29 30 39 38
		f 4 27 84 -36 -84
		mu 0 4 30 31 40 39
		f 4 28 85 -37 -85
		mu 0 4 31 32 41 40
		f 4 29 86 -38 -86
		mu 0 4 32 33 42 41
		f 4 30 87 -39 -87
		mu 0 4 33 34 43 42
		f 4 31 80 -40 -88
		mu 0 4 34 35 44 43
		f 4 32 89 -41 -89
		mu 0 4 36 37 46 45
		f 4 33 90 -42 -90
		mu 0 4 37 38 47 46
		f 4 34 91 -43 -91
		mu 0 4 38 39 48 47
		f 4 35 92 -44 -92
		mu 0 4 39 40 49 48
		f 4 36 93 -45 -93
		mu 0 4 40 41 50 49
		f 4 37 94 -46 -94
		mu 0 4 41 42 51 50
		f 4 38 95 -47 -95
		mu 0 4 42 43 52 51
		f 4 39 88 -48 -96
		mu 0 4 43 44 53 52
		f 4 40 97 -49 -97
		mu 0 4 45 46 55 54
		f 4 41 98 -50 -98
		mu 0 4 46 47 56 55
		f 4 42 99 -51 -99
		mu 0 4 47 48 57 56
		f 4 43 100 -52 -100
		mu 0 4 48 49 58 57
		f 4 44 101 -53 -101
		mu 0 4 49 50 59 58
		f 4 45 102 -54 -102
		mu 0 4 50 51 60 59
		f 4 46 103 -55 -103
		mu 0 4 51 52 61 60
		f 4 47 96 -56 -104
		mu 0 4 52 53 62 61
		f 3 -1 -105 105
		mu 0 3 1 0 63
		f 3 -2 -106 106
		mu 0 3 2 1 64
		f 3 -3 -107 107
		mu 0 3 3 2 65
		f 3 -4 -108 108
		mu 0 3 4 3 66
		f 3 -5 -109 109
		mu 0 3 5 4 67
		f 3 -6 -110 110
		mu 0 3 6 5 68
		f 3 -7 -111 111
		mu 0 3 7 6 69
		f 3 -8 -112 104
		mu 0 3 8 7 70
		f 3 48 113 -113
		mu 0 3 54 55 71
		f 3 49 114 -114
		mu 0 3 55 56 72
		f 3 50 115 -115
		mu 0 3 56 57 73
		f 3 51 116 -116
		mu 0 3 57 58 74
		f 3 52 117 -117
		mu 0 3 58 59 75
		f 3 53 118 -118
		mu 0 3 59 60 76
		f 3 54 119 -119
		mu 0 3 60 61 77
		f 3 55 112 -120
		mu 0 3 61 62 78;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode pointConstraint -n "flexiPlane_grp_midBend01_pointConstraint1" -p "flexiPlane_grp_midBend01";
	rename -uid "4E6B0D13-450A-EFF8-9EF1-228FAAC8BCC6";
	addAttr -ci true -k true -sn "w0" -ln "flexiPlane_cnt_b01W0" -dv 1 -min 0 -at "double";
	addAttr -ci true -k true -sn "w1" -ln "flexiPlane_cnt_a01W1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr ".rst" -type "double3" -4.4408920985006262e-16 0 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "flexiPlane_surface01" -p "flexiPlane_globalMove01";
	rename -uid "599821A1-4CE2-4BA2-1FA8-A48E39CD8993";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsSurface -n "flexiPlane_surface0Shape1" -p "flexiPlane_surface01";
	rename -uid "365440D5-494F-27FB-5236-BB9A86F45C17";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".mb" no;
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".vis" no;
	setAttr ".tw" yes;
	setAttr ".smo" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".nufa" 4.5;
	setAttr ".nvfa" 4.5;
createNode nurbsSurface -n "flexiPlane_surface0Shape1Orig1" -p "flexiPlane_surface01";
	rename -uid "80739825-436F-DB12-8F94-B7B71089A0EE";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".cc" -type "nurbsSurface" 
		3 3 0 0 no 
		10 0 0 0 0.20000000000000001 0.40000000000000002 0.60000000000000009 0.80000000000000004
		 1 1 1
		6 0 0 0 1 1 1
		
		32
		-5 -6.123233995736766e-17 1
		-5 -2.0410779985789222e-17 0.33333333333333337
		-5 2.0410779985789219e-17 -0.33333333333333326
		-5 6.123233995736766e-17 -1
		-4.333333333333333 -6.123233995736766e-17 1
		-4.333333333333333 -2.0410779985789222e-17 0.33333333333333337
		-4.333333333333333 2.0410779985789219e-17 -0.33333333333333326
		-4.333333333333333 6.123233995736766e-17 -1
		-2.9999999999999996 -6.123233995736766e-17 1
		-2.9999999999999996 -2.0410779985789222e-17 0.33333333333333337
		-2.9999999999999996 2.0410779985789219e-17 -0.33333333333333326
		-2.9999999999999996 6.123233995736766e-17 -1
		-0.99999999999999922 -6.123233995736766e-17 1
		-0.99999999999999922 -2.0410779985789222e-17 0.33333333333333337
		-0.99999999999999922 2.0410779985789219e-17 -0.33333333333333326
		-0.99999999999999922 6.123233995736766e-17 -1
		1.0000000000000009 -6.123233995736766e-17 1
		1.0000000000000009 -2.0410779985789222e-17 0.33333333333333337
		1.0000000000000009 2.0410779985789219e-17 -0.33333333333333326
		1.0000000000000009 6.123233995736766e-17 -1
		3.0000000000000009 -6.123233995736766e-17 1
		3.0000000000000009 -2.0410779985789222e-17 0.33333333333333337
		3.0000000000000009 2.0410779985789219e-17 -0.33333333333333326
		3.0000000000000009 6.123233995736766e-17 -1
		4.3333333333333339 -6.123233995736766e-17 1
		4.3333333333333339 -2.0410779985789222e-17 0.33333333333333337
		4.3333333333333339 2.0410779985789219e-17 -0.33333333333333326
		4.3333333333333339 6.123233995736766e-17 -1
		5 -6.123233995736766e-17 1
		5 -2.0410779985789222e-17 0.33333333333333337
		5 2.0410779985789219e-17 -0.33333333333333326
		5 6.123233995736766e-17 -1
		
		;
createNode transform -n "flexiPlane_extraNodes01" -p "flexiPlane01";
	rename -uid "C31F7655-4C8A-6B00-CC31-83BC78A0FD8F";
createNode transform -n "flexiPlane_flcs01" -p "flexiPlane_extraNodes01";
	rename -uid "0D1096A6-4CB7-784A-2DC3-19A49A5FA731";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "flexiPlane_flc_a01" -p "flexiPlane_flcs01";
	rename -uid "D6C8EE9C-4A61-A20F-0045-208C1D9CE21B";
createNode follicle -n "flexiPlane_flc_a0Shape1" -p "flexiPlane_flc_a01";
	rename -uid "52467C76-4BB4-43F6-2918-C48A0D10E4EF";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.1;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve1" -p "flexiPlane_flc_a01";
	rename -uid "BF5A3CC8-41A0-8683-3C28-8E8E6B84A719";
createNode nurbsCurve -n "curveShape1" -p "curve1";
	rename -uid "047379AF-4DC2-617E-5795-56BFF4829B2A";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode scaleConstraint -n "flexiPlane_flc_a01_scaleConstraint1" -p "flexiPlane_flc_a01";
	rename -uid "F6F4BDD7-4079-BF77-AA6F-6B9A0B8F30C0";
	addAttr -ci true -k true -sn "w0" -ln "flexiPlane_globalMove01W0" -dv 1 -min 0 
		-at "double";
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
	setAttr -k on ".w0";
createNode joint -n "flexiPlane_bind_a01" -p "flexiPlane_flc_a01";
	rename -uid "0B94CA50-4B33-888C-0AD4-8CAFDC481416";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 5.5511151231257827e-17 -9.2444637330587321e-33 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000000000002 4.9303806576313238e-32 0
		 0 -4.9303806576313238e-32 1.0000000000000002 0 -4 0 0 1;
	setAttr ".radi" 0.5;
createNode transform -n "flexiPlane_flc_b01" -p "flexiPlane_flcs01";
	rename -uid "4515B8E7-49F6-3A79-4B72-A8B656097228";
createNode follicle -n "flexiPlane_flc_b0Shape1" -p "flexiPlane_flc_b01";
	rename -uid "BEA7B4A4-4F41-6913-EA89-E9BAD8EC9938";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.3;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve2" -p "flexiPlane_flc_b01";
	rename -uid "FF18BE9B-4E83-B499-FDB6-8F8CD837A54F";
createNode nurbsCurve -n "curveShape2" -p "curve2";
	rename -uid "558BF91C-4D72-604C-B911-DD922C6B7D00";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode scaleConstraint -n "flexiPlane_flc_b01_scaleConstraint1" -p "flexiPlane_flc_b01";
	rename -uid "3429475E-41E8-F7DB-F8B1-A39E673D057F";
	addAttr -ci true -k true -sn "w0" -ln "flexiPlane_globalMove01W0" -dv 1 -min 0 
		-at "double";
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
	setAttr -k on ".w0";
createNode joint -n "flexiPlane_bind_b01" -p "flexiPlane_flc_b01";
	rename -uid "768151EE-4381-13F8-BF9B-4CBFAE3730E9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.4408920985006262e-16 5.5511151231257827e-17 -9.2444637330587321e-33 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000000000002 4.9303806576313238e-32 0
		 0 -4.9303806576313238e-32 1.0000000000000002 0 -2 0 0 1;
	setAttr ".radi" 0.5;
createNode transform -n "flexiPlane_flc_c01" -p "flexiPlane_flcs01";
	rename -uid "1E505740-460B-EB54-0735-2AB12435922F";
createNode follicle -n "flexiPlane_flc_c0Shape1" -p "flexiPlane_flc_c01";
	rename -uid "ED73A739-425B-070A-8984-B89C0F50B2FE";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.5;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve3" -p "flexiPlane_flc_c01";
	rename -uid "D4D7085C-4269-CA46-9B2F-63AEFEC226DC";
createNode nurbsCurve -n "curveShape3" -p "curve3";
	rename -uid "240F1121-4857-993A-04B7-0DB676A3D895";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode scaleConstraint -n "flexiPlane_flc_c01_scaleConstraint1" -p "flexiPlane_flc_c01";
	rename -uid "F3CCCB42-4F7D-B3C0-C264-CCAD237D6326";
	addAttr -ci true -k true -sn "w0" -ln "flexiPlane_globalMove01W0" -dv 1 -min 0 
		-at "double";
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
	setAttr -k on ".w0";
createNode joint -n "flexiPlane_bind_c01" -p "flexiPlane_flc_c01";
	rename -uid "35D79E78-443E-A800-6014-8D8BA3C77A8A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.0531133177191805e-16 5.5511151231257827e-17 -1.2325951644078307e-32 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000000000002 4.9303806576313238e-32 0
		 0 -4.9303806576313238e-32 1.0000000000000002 0 0 2.7369110631344083e-48 0 1;
	setAttr ".radi" 0.5;
createNode transform -n "flexiPlane_flc_d01" -p "flexiPlane_flcs01";
	rename -uid "159DD0D9-4E02-EA22-A757-B08BF4089146";
createNode follicle -n "flexiPlane_flc_d0Shape1" -p "flexiPlane_flc_d01";
	rename -uid "88EB64C5-4FDC-97E6-9421-018CA75C6FD4";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.7;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve4" -p "flexiPlane_flc_d01";
	rename -uid "06BB5343-4A19-0E59-339A-6B8164C66919";
createNode nurbsCurve -n "curveShape4" -p "curve4";
	rename -uid "76B19048-407B-3D17-DB8C-63B77E0054DB";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode scaleConstraint -n "flexiPlane_flc_d01_scaleConstraint1" -p "flexiPlane_flc_d01";
	rename -uid "FB9DA750-4B09-6B03-47A8-BB956C0ADCFA";
	addAttr -ci true -k true -sn "w0" -ln "flexiPlane_globalMove01W0" -dv 1 -min 0 
		-at "double";
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
	setAttr -k on ".w0";
createNode joint -n "flexiPlane_bind_d01" -p "flexiPlane_flc_d01";
	rename -uid "796153FA-48AF-E5E2-3B00-52A1965DE120";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.4408920985006262e-16 5.5511151231257827e-17 -9.2444637330587321e-33 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000000000002 4.9303806576313238e-32 0
		 0 -4.9303806576313238e-32 1.0000000000000002 0 2 0 0 1;
	setAttr ".radi" 0.5;
createNode transform -n "flexiPlane_flc_e01" -p "flexiPlane_flcs01";
	rename -uid "049A1F70-464C-6B80-BCB8-03A1F2465424";
createNode follicle -n "flexiPlane_flc_e0Shape1" -p "flexiPlane_flc_e01";
	rename -uid "37CB42AC-4EF4-20AC-4D8F-E5AEFF702440";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.9;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve5" -p "flexiPlane_flc_e01";
	rename -uid "2C3E6ADF-4570-320C-D4A0-928E074892C3";
createNode nurbsCurve -n "curveShape5" -p "curve5";
	rename -uid "AC4151AB-4F6E-19D5-99C9-ED80AED4636B";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode scaleConstraint -n "flexiPlane_flc_e01_scaleConstraint1" -p "flexiPlane_flc_e01";
	rename -uid "D90AF1BB-416E-5A18-CCC5-D48C0F5D4F1F";
	addAttr -ci true -k true -sn "w0" -ln "flexiPlane_globalMove01W0" -dv 1 -min 0 
		-at "double";
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
	setAttr -k on ".w0";
createNode joint -n "flexiPlane_bind_e01" -p "flexiPlane_flc_e01";
	rename -uid "8D59E9D9-4505-5266-F72B-21B50E0234E8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -8.8817841970012523e-16 5.5511151231257827e-17 -1.0785207688568521e-32 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000000000002 4.9303806576313238e-32 0
		 0 -4.9303806576313238e-32 1.0000000000000002 0 4 0 0 1;
	setAttr ".radi" 0.5;
createNode transform -n "flexiPlane_bShp_surface01" -p "flexiPlane_extraNodes01";
	rename -uid "80755154-4716-C54E-47D3-32B4B4C87C84";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 -5 ;
createNode nurbsSurface -n "flexiPlane_bShp_surface0Shape1" -p "flexiPlane_bShp_surface01";
	rename -uid "76718FF8-4B53-A64E-07AE-D8B775031C7F";
	setAttr -k off ".v";
	setAttr -s 6 ".iog[0].og";
	setAttr ".mb" no;
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".vis" no;
	setAttr ".tw" yes;
	setAttr ".smo" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".nufa" 4.5;
	setAttr ".nvfa" 4.5;
createNode nurbsSurface -n "flexiPlane_bShp_surface0Shape1Orig1" -p "flexiPlane_bShp_surface01";
	rename -uid "B80654DE-466C-69E9-9D65-4189F9649B30";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".cc" -type "nurbsSurface" 
		3 3 0 0 no 
		10 0 0 0 0.20000000000000001 0.40000000000000002 0.60000000000000009 0.80000000000000004
		 1 1 1
		6 0 0 0 1 1 1
		
		32
		-5 -6.123233995736766e-17 1
		-5 -2.0410779985789222e-17 0.33333333333333337
		-5 2.0410779985789219e-17 -0.33333333333333326
		-5 6.123233995736766e-17 -1
		-4.333333333333333 -6.123233995736766e-17 1
		-4.333333333333333 -2.0410779985789222e-17 0.33333333333333337
		-4.333333333333333 2.0410779985789219e-17 -0.33333333333333326
		-4.333333333333333 6.123233995736766e-17 -1
		-2.9999999999999996 -6.123233995736766e-17 1
		-2.9999999999999996 -2.0410779985789222e-17 0.33333333333333337
		-2.9999999999999996 2.0410779985789219e-17 -0.33333333333333326
		-2.9999999999999996 6.123233995736766e-17 -1
		-0.99999999999999922 -6.123233995736766e-17 1
		-0.99999999999999922 -2.0410779985789222e-17 0.33333333333333337
		-0.99999999999999922 2.0410779985789219e-17 -0.33333333333333326
		-0.99999999999999922 6.123233995736766e-17 -1
		1.0000000000000009 -6.123233995736766e-17 1
		1.0000000000000009 -2.0410779985789222e-17 0.33333333333333337
		1.0000000000000009 2.0410779985789219e-17 -0.33333333333333326
		1.0000000000000009 6.123233995736766e-17 -1
		3.0000000000000009 -6.123233995736766e-17 1
		3.0000000000000009 -2.0410779985789222e-17 0.33333333333333337
		3.0000000000000009 2.0410779985789219e-17 -0.33333333333333326
		3.0000000000000009 6.123233995736766e-17 -1
		4.3333333333333339 -6.123233995736766e-17 1
		4.3333333333333339 -2.0410779985789222e-17 0.33333333333333337
		4.3333333333333339 2.0410779985789219e-17 -0.33333333333333326
		4.3333333333333339 6.123233995736766e-17 -1
		5 -6.123233995736766e-17 1
		5 -2.0410779985789222e-17 0.33333333333333337
		5 2.0410779985789219e-17 -0.33333333333333326
		5 6.123233995736766e-17 -1
		
		;
createNode transform -n "flexiPlane_wire_surface01" -p "flexiPlane_extraNodes01";
	rename -uid "A32D2129-4ED0-080D-F0EB-339C93243BC5";
	setAttr ".v" no;
createNode nurbsCurve -n "flexiPlane_wire_surface0Shape1" -p "flexiPlane_wire_surface01";
	rename -uid "E0105D8B-4383-6B54-33E8-698F29DC870D";
	setAttr -k off ".v";
	setAttr -s 8 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "flexiPlane_wire_surface0Shape1Orig1" -p "flexiPlane_wire_surface01";
	rename -uid "6F79590B-410F-C551-A4E5-47B57EFF4A10";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 1 0 no 3
		4 0 0 1 1
		3
		-5 0 -5
		0 0 -5
		5 0 -5
		;
createNode transform -n "flexiPlane_wire_surface01BaseWire" -p "flexiPlane_extraNodes01";
	rename -uid "48DEB614-4BED-5E18-2F62-D0A9958400D3";
	setAttr ".v" no;
createNode nurbsCurve -n "flexiPlane_wire_surface01BaseWireShape" -p "flexiPlane_wire_surface01BaseWire";
	rename -uid "0809FA4B-4986-862F-7BCF-BD855D0E29BF";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "cv[0:1]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "cv[*]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "cv[1:2]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "cv[1]";
	setAttr ".cc" -type "nurbsCurve" 
		2 1 0 no 3
		4 0 0 1 1
		3
		-5 0 -5
		0 0 -5
		5 0 -5
		;
createNode nurbsCurve -n "flexiPlane_wire_surface01BaseWireShape1Orig" -p "flexiPlane_wire_surface01BaseWire";
	rename -uid "A0E8BEC6-4518-F085-3185-96AEE43642CE";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 1 0 no 3
		4 0 0 1 1
		3
		-5 0 -5
		0 0 -5
		5 0 -5
		;
createNode transform -n "flexiPlane_cls01" -p "flexiPlane_extraNodes01";
	rename -uid "D5047E29-4779-2477-FE28-B5965678506B";
	setAttr ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "flexiPlane_cl_a01" -p "flexiPlane_cls01";
	rename -uid "23885933-46B4-2E9B-C26E-6F8F5F0ECA46";
	setAttr ".rp" -type "double3" -5 0 -5 ;
	setAttr ".sp" -type "double3" -5 0 -5 ;
createNode clusterHandle -n "flexiPlane_cl_a01Shape" -p "flexiPlane_cl_a01";
	rename -uid "25D590E6-4DAB-9CC8-83BE-BAB91BBA186E";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -6 0 -5 ;
createNode transform -n "flexiPlane_cl_b01" -p "flexiPlane_cls01";
	rename -uid "4666C6E4-45E1-0AB4-AAFE-23B60401CCD5";
	setAttr ".rp" -type "double3" 5 0 -5 ;
	setAttr ".sp" -type "double3" 5 0 -5 ;
createNode clusterHandle -n "flexiPlane_cl_b01Shape" -p "flexiPlane_cl_b01";
	rename -uid "93078711-4009-6DC4-E1AB-BE877B9A631E";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 6 0 -5 ;
createNode transform -n "flexiPlane_cl_mid01" -p "flexiPlane_cls01";
	rename -uid "BE1E553B-4A46-2FD0-E4F6-3CB6EF38B8AF";
	setAttr ".rp" -type "double3" 0 0 -5 ;
	setAttr ".sp" -type "double3" 0 0 -5 ;
createNode clusterHandle -n "flexiPlane_cl_mid01Shape" -p "flexiPlane_cl_mid01";
	rename -uid "26019943-4603-F844-FA1D-99B6450300B2";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 0 -5 ;
createNode transform -n "flexiPlane_twist_surface01" -p "flexiPlane_extraNodes01";
	rename -uid "4089285F-40E9-00F2-6A1A-F1AC7785D887";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 -5 ;
	setAttr ".r" -type "double3" 0 0 90 ;
	setAttr ".s" -type "double3" 5 5 5 ;
	setAttr ".smd" 7;
createNode deformTwist -n "flexiPlane_twist_surface01Shape" -p "flexiPlane_twist_surface01";
	rename -uid "EBC14A70-44D8-21A7-9885-B3A227389B0E";
	setAttr -k off ".v";
	setAttr ".dd" -type "doubleArray" 4 -1 1 0 0 ;
	setAttr ".hw" 1.1;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "D4D67885-4709-2B05-3A10-C5870D686D01";
	setAttr -s 4 ".lnk";
	setAttr -s 4 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "B41C92DB-4077-C132-DFC1-49AF1369B817";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 1 0 ;
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "F86966CF-49CE-B4D6-24E8-E7998A157B09";
createNode displayLayerManager -n "layerManager";
	rename -uid "632AC899-4C03-EC0E-6844-AC9CD6164D0C";
createNode displayLayer -n "defaultLayer";
	rename -uid "0F68C108-4207-66C2-0A7E-86AD747C5525";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "E480B557-4F46-4A98-64B3-F99A1AD8569D";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "F848E96D-4CE3-7416-4D53-DD9A43A4C48A";
	setAttr ".g" yes;
createNode renderLayerManager -n "skeleton_renderLayerManager";
	rename -uid "9E4747C9-45EA-F8C2-1DB5-9EB3697382CD";
createNode renderLayer -n "skeleton_defaultRenderLayer";
	rename -uid "081CB3E8-46ED-52DB-74C0-0984C41C9EFE";
	setAttr ".g" yes;
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
	rename -uid "22F96CD3-42ED-740D-C5E2-31AEBAA67443";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
	rename -uid "D7EA1DD2-4C75-7DEC-8CDE-35B31100B426";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
	rename -uid "081DAB73-4EA9-77D0-67DA-3194F3265205";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
	rename -uid "1C90F4B6-4A56-7E43-38AD-A08D91282E9C";
lockNode -l 1 ;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "B635FD4F-466D-97AD-A5BA-A2A3D9C8CEF1";
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
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 852\n            -height 544\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n"
		+ "            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n"
		+ "            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n"
		+ "            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n"
		+ "                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n"
		+ "                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n"
		+ "                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n"
		+ "                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n"
		+ "                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n"
		+ "                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n"
		+ "            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n"
		+ "                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n"
		+ "\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n"
		+ "\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n"
		+ "                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n"
		+ "                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n"
		+ "                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -highlightConnections 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n"
		+ "                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 852\\n    -height 544\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 852\\n    -height 544\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 1 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "552C10A2-4260-514D-0AD8-C99D7928ADCC";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode lambert -n "flexiPlane_surface_material01";
	rename -uid "DEC7C140-4A26-6AB1-D7ED-D890412FD8FA";
	setAttr ".c" -type "float3" 0 0.75775909 1 ;
	setAttr ".it" -type "float3" 0.74358737 0.74358737 0.74358737 ;
createNode shadingEngine -n "lambert2SG";
	rename -uid "3B4F4D2B-4345-FDC6-1250-86916732C911";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "199C85C9-4A83-A818-52FD-76A46F9538DB";
createNode blendShape -n "flexiPlane_bShpNode_surface01";
	rename -uid "CD21BC92-4C23-8141-4ECF-52952D3D85A4";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".w[0]"  1;
	setAttr ".mlid" 0;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"flexiPlane_bShp_surface01","weight[0]"} ;
createNode tweak -n "flexiPlane_bShp_surface_tweak01";
	rename -uid "B191B041-424F-E1E3-C643-F8917A925F2B";
createNode objectSet -n "flexiPlane_bShpNode_surface01Set";
	rename -uid "D46A9CA2-43E9-9D48-2F43-48AEE425D5ED";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "flexiPlane_bShpNode_surface01GroupId";
	rename -uid "B9B88841-4C55-CC92-CAC7-9C803B3CFBEB";
	setAttr ".ihi" 0;
createNode groupParts -n "flexiPlane_bShpNode_surface01GroupParts";
	rename -uid "7D3B3A69-4DE6-0B78-1A8B-65B303630DB4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode objectSet -n "tweakSet1";
	rename -uid "5A6E04D0-4AF2-FA2F-373C-A8AEA8317843";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "23864C4E-462C-324F-B3EA-068FB559DAB0";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "1D83AB96-4D10-73A5-A414-B4A548B707CB";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode cluster -n "flexiPlane_cl_a01Cluster";
	rename -uid "FF9AD011-43DF-AFBD-17CC-B88AC754264A";
	setAttr ".wl[0].w[1]"  0.5;
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ait" 0;
createNode tweak -n "flexiPlane_cl_Cluster_tweak01";
	rename -uid "E94A60DD-42C1-FE20-3F35-FEBAB0371520";
createNode objectSet -n "cluster1Set";
	rename -uid "BD4A5ED2-4DB2-E063-31F5-F08D4A437914";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster1GroupId";
	rename -uid "490AC2F9-4357-F073-EB8F-7AA9BD36098C";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster1GroupParts";
	rename -uid "D5AF0D8A-4616-F44B-F0E1-CEBD2F183274";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0:1]";
createNode objectSet -n "tweakSet2";
	rename -uid "2AE21541-49EC-48F5-3175-F2B1E4E88EBE";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId4";
	rename -uid "D738E7B6-49AF-BD29-8B81-73B911606089";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	rename -uid "1BCB2765-48B0-C52B-8A74-438990789EFC";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "flexiPlane_cl_b01Cluster";
	rename -uid "1D5519BE-4B5A-2ABC-6847-249B0AF37420";
	setAttr ".wl[0].w[1]"  0.5;
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ait" 0;
createNode objectSet -n "cluster2Set";
	rename -uid "FB8A6F1F-4A40-D341-A415-75B65839A230";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster2GroupId";
	rename -uid "5DB0565A-4074-1EB8-259C-9291EE9861A4";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts";
	rename -uid "1670B921-4620-1CB2-2569-41AE48607BD5";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1:2]";
createNode cluster -n "flexiPlane_cl_mid01Cluster";
	rename -uid "9C6D30F2-4F90-C65D-C6CB-8D883CDF9AFB";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ait" 0;
createNode objectSet -n "cluster3Set";
	rename -uid "34367A1F-435D-886E-7B25-9E8EE1CC8F6D";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster3GroupId";
	rename -uid "DF7B87A0-4DE6-4867-8DCE-29A7ECC770CE";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster3GroupParts";
	rename -uid "D7307F30-415E-4296-E8A0-C5A4F50B7873";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1]";
createNode wire -n "flexiPlane_wireAttrs_surface01";
	rename -uid "B8F2B3A2-41EB-61D4-13A5-47B6E2CD474B";
	setAttr ".dds[0]"  20;
	setAttr ".sc[0]"  1;
createNode tweak -n "flexiPlane_wire_surface_tweak0101";
	rename -uid "2DD4E3CA-45F5-CBA9-492D-338C8B9EB784";
createNode objectSet -n "wire1Set";
	rename -uid "0633983A-4413-27E8-5A40-3F9D6E850B2E";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "wire1GroupId";
	rename -uid "ECF83E05-4E47-CF0C-1A59-1F89ABF5F507";
	setAttr ".ihi" 0;
createNode groupParts -n "wire1GroupParts";
	rename -uid "14E0690F-488C-E97A-7148-33B78418FB2D";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode objectSet -n "tweakSet3";
	rename -uid "C4EB9AEB-43EA-2F87-13EE-1FBB93ABDCA3";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId6";
	rename -uid "4DC9AED3-4E1E-EA40-D1C1-FF886A324807";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts6";
	rename -uid "948DB7A5-44BE-116C-E64C-69867D7C2CDE";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode surfaceShader -n "flexiPlane_ss_midBend01";
	rename -uid "C2C8CBED-4CA9-920C-9062-4B878C6D22FF";
	setAttr ".oc" -type "float3" 1 1 0 ;
createNode shadingEngine -n "surfaceShader1SG";
	rename -uid "40699115-455A-0064-C263-D684FEA8AC6B";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "C85B992C-49CE-BE20-EFB1-95B6A5FD8B2D";
createNode nonLinear -n "flexiPlane_twistAttrs_surface01";
	rename -uid "155A3013-45D1-01F0-EEE0-53BF0696EB41";
	addAttr -is true -ci true -k true -sn "sa" -ln "startAngle" -smn -15 -smx 15 -at "doubleAngle";
	addAttr -is true -ci true -k true -sn "ea" -ln "endAngle" -smn -15 -smx 15 -at "doubleAngle";
	addAttr -is true -ci true -k true -sn "lb" -ln "lowBound" -dv -1 -max 0 -smn -10 
		-smx 0 -at "double";
	addAttr -is true -ci true -k true -sn "hb" -ln "highBound" -dv 1 -min 0 -smn 0 -smx 
		10 -at "double";
	setAttr -k on ".sa";
	setAttr -k on ".ea";
	setAttr -k on ".lb";
	setAttr -k on ".hb";
createNode objectSet -n "twist1Set";
	rename -uid "D9256AF5-4399-4406-EBD3-B6A84C0925B3";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "twist1GroupId";
	rename -uid "65A814F1-4A2C-CE69-4293-8789FCBEBE15";
	setAttr ".ihi" 0;
createNode groupParts -n "twist1GroupParts";
	rename -uid "D8389556-4570-08C0-E0B3-76907498CBF0";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode curveInfo -n "flexiPlane_curveInfo01";
	rename -uid "536005FE-43B1-7F1C-A1E6-EBA5AE59195E";
createNode multiplyDivide -n "flexiPlane_div_squashStretch_length01";
	rename -uid "225ED93D-46C5-9692-C528-5E8781D20EAF";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 10 1 1 ;
createNode multiplyDivide -n "flexiPlane_div_volume01";
	rename -uid "74B17FD5-4658-D3E2-5E68-B092B28A1164";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
createNode condition -n "flexiPlane_cond_volume01";
	rename -uid "1C505427-48B3-273D-C8B4-918E0A1410CD";
	setAttr ".st" 1;
createNode dagPose -n "bindPose1";
	rename -uid "989EE98B-4F00-9D07-E821-D0BECAC6DF91";
	setAttr -s 13 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[3]" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 4.0000000000000009 -1.5407439555097887e-33 5.5511151231257827e-17 1;
	setAttr ".wm[5]" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 1.9999999999999996 -3.0814879110195774e-33 5.5511151231257827e-17 1;
	setAttr ".wm[7]" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 3.0531133177191805e-16 0 5.5511151231257827e-17 1;
	setAttr ".wm[9]" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 -1.9999999999999996 -3.0814879110195774e-33 5.5511151231257827e-17 1;
	setAttr ".wm[11]" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 -4 -3.0814879110195774e-33 5.5511151231257827e-17 1;
	setAttr -s 13 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 -1.5707963267948966 0 0 0 4.0000000000000009
		 -1.5407439555097887e-33 5.5511151231257827e-17 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 -8.8817841970012523e-16
		 5.5511151231257827e-17 -1.0785207688568521e-32 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0.70710678118654746 0 0 0.70710678118654768 1 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 -1.5707963267948966 -8.3266726846886593e-17
		 0 0 1.9999999999999996 -3.0814879110195774e-33 5.5511151231257827e-17 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 0 0 0 0 4.4408920985006262e-16
		 5.5511151231257827e-17 -9.2444637330587321e-33 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0.70710678118654746 0 0 0.70710678118654768 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 -1.5707963267948966 1.6653345369377336e-16
		 0 0 3.0531133177191805e-16 0 5.5511151231257827e-17 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 -3.0531133177191805e-16
		 5.5511151231257827e-17 -1.2325951644078307e-32 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0.70710678118654746 0 0 0.70710678118654768 1 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 -1.5707963267948966 0 0 0 -1.9999999999999996
		 -3.0814879110195774e-33 5.5511151231257827e-17 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 0 0 0 0 -4.4408920985006262e-16
		 5.5511151231257827e-17 -9.2444637330587321e-33 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0.70710678118654746 0 0 0.70710678118654768 1 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 -1.5707963267948966 0 0 0 -4
		 -3.0814879110195774e-33 5.5511151231257827e-17 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 
		0 0 0 1 1 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 5.5511151231257827e-17
		 -9.2444637330587321e-33 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0.70710678118654746 0 0 0.70710678118654768 1
		 1 1 yes;
	setAttr -s 13 ".m";
	setAttr -s 13 ".p";
	setAttr -s 13 ".g[0:12]" yes yes yes yes no yes no yes no yes no yes 
		no;
	setAttr ".bp" yes;
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
	setAttr -s 4 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 6 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 3 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 2 ".r";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :characterPartition;
connectAttr "flexiPlane_grp_midBend01_pointConstraint1.ctx" "flexiPlane_grp_midBend01.tx"
		;
connectAttr "flexiPlane_grp_midBend01_pointConstraint1.cty" "flexiPlane_grp_midBend01.ty"
		;
connectAttr "flexiPlane_grp_midBend01_pointConstraint1.ctz" "flexiPlane_grp_midBend01.tz"
		;
connectAttr "flexiPlane_grp_midBend01.pim" "flexiPlane_grp_midBend01_pointConstraint1.cpim"
		;
connectAttr "flexiPlane_grp_midBend01.rp" "flexiPlane_grp_midBend01_pointConstraint1.crp"
		;
connectAttr "flexiPlane_grp_midBend01.rpt" "flexiPlane_grp_midBend01_pointConstraint1.crt"
		;
connectAttr "flexiPlane_cnt_b01.t" "flexiPlane_grp_midBend01_pointConstraint1.tg[0].tt"
		;
connectAttr "flexiPlane_cnt_b01.rp" "flexiPlane_grp_midBend01_pointConstraint1.tg[0].trp"
		;
connectAttr "flexiPlane_cnt_b01.rpt" "flexiPlane_grp_midBend01_pointConstraint1.tg[0].trt"
		;
connectAttr "flexiPlane_cnt_b01.pm" "flexiPlane_grp_midBend01_pointConstraint1.tg[0].tpm"
		;
connectAttr "flexiPlane_grp_midBend01_pointConstraint1.w0" "flexiPlane_grp_midBend01_pointConstraint1.tg[0].tw"
		;
connectAttr "flexiPlane_cnt_a01.t" "flexiPlane_grp_midBend01_pointConstraint1.tg[1].tt"
		;
connectAttr "flexiPlane_cnt_a01.rp" "flexiPlane_grp_midBend01_pointConstraint1.tg[1].trp"
		;
connectAttr "flexiPlane_cnt_a01.rpt" "flexiPlane_grp_midBend01_pointConstraint1.tg[1].trt"
		;
connectAttr "flexiPlane_cnt_a01.pm" "flexiPlane_grp_midBend01_pointConstraint1.tg[1].tpm"
		;
connectAttr "flexiPlane_grp_midBend01_pointConstraint1.w1" "flexiPlane_grp_midBend01_pointConstraint1.tg[1].tw"
		;
connectAttr "flexiPlane_bShpNode_surface01GroupId.id" "flexiPlane_surface0Shape1.iog.og[0].gid"
		;
connectAttr "flexiPlane_bShpNode_surface01Set.mwc" "flexiPlane_surface0Shape1.iog.og[0].gco"
		;
connectAttr "groupId2.id" "flexiPlane_surface0Shape1.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "flexiPlane_surface0Shape1.iog.og[1].gco";
connectAttr "flexiPlane_bShpNode_surface01.og[0]" "flexiPlane_surface0Shape1.cr"
		;
connectAttr "flexiPlane_bShp_surface_tweak01.pl[0].cp[0]" "flexiPlane_surface0Shape1.twl"
		;
connectAttr "flexiPlane_flc_a0Shape1.ot" "flexiPlane_flc_a01.t" -l on;
connectAttr "flexiPlane_flc_a0Shape1.or" "flexiPlane_flc_a01.r" -l on;
connectAttr "flexiPlane_flc_a01_scaleConstraint1.csx" "flexiPlane_flc_a01.sx";
connectAttr "flexiPlane_flc_a01_scaleConstraint1.csy" "flexiPlane_flc_a01.sy";
connectAttr "flexiPlane_flc_a01_scaleConstraint1.csz" "flexiPlane_flc_a01.sz";
connectAttr "flexiPlane_surface0Shape1.wm" "flexiPlane_flc_a0Shape1.iwm";
connectAttr "flexiPlane_surface0Shape1.l" "flexiPlane_flc_a0Shape1.is";
connectAttr "curveShape1.l" "flexiPlane_flc_a0Shape1.sp";
connectAttr "curve1.wm" "flexiPlane_flc_a0Shape1.spm";
connectAttr "flexiPlane_flc_a01.pim" "flexiPlane_flc_a01_scaleConstraint1.cpim";
connectAttr "flexiPlane_globalMove01.s" "flexiPlane_flc_a01_scaleConstraint1.tg[0].ts"
		;
connectAttr "flexiPlane_globalMove01.pm" "flexiPlane_flc_a01_scaleConstraint1.tg[0].tpm"
		;
connectAttr "flexiPlane_flc_a01_scaleConstraint1.w0" "flexiPlane_flc_a01_scaleConstraint1.tg[0].tw"
		;
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_a01.sy";
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_a01.sz";
connectAttr "flexiPlane_flc_b0Shape1.ot" "flexiPlane_flc_b01.t" -l on;
connectAttr "flexiPlane_flc_b0Shape1.or" "flexiPlane_flc_b01.r" -l on;
connectAttr "flexiPlane_flc_b01_scaleConstraint1.csx" "flexiPlane_flc_b01.sx";
connectAttr "flexiPlane_flc_b01_scaleConstraint1.csy" "flexiPlane_flc_b01.sy";
connectAttr "flexiPlane_flc_b01_scaleConstraint1.csz" "flexiPlane_flc_b01.sz";
connectAttr "flexiPlane_surface0Shape1.wm" "flexiPlane_flc_b0Shape1.iwm";
connectAttr "flexiPlane_surface0Shape1.l" "flexiPlane_flc_b0Shape1.is";
connectAttr "curveShape2.l" "flexiPlane_flc_b0Shape1.sp";
connectAttr "curve2.wm" "flexiPlane_flc_b0Shape1.spm";
connectAttr "flexiPlane_flc_b01.pim" "flexiPlane_flc_b01_scaleConstraint1.cpim";
connectAttr "flexiPlane_globalMove01.s" "flexiPlane_flc_b01_scaleConstraint1.tg[0].ts"
		;
connectAttr "flexiPlane_globalMove01.pm" "flexiPlane_flc_b01_scaleConstraint1.tg[0].tpm"
		;
connectAttr "flexiPlane_flc_b01_scaleConstraint1.w0" "flexiPlane_flc_b01_scaleConstraint1.tg[0].tw"
		;
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_b01.sy";
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_b01.sz";
connectAttr "flexiPlane_flc_c0Shape1.ot" "flexiPlane_flc_c01.t" -l on;
connectAttr "flexiPlane_flc_c0Shape1.or" "flexiPlane_flc_c01.r" -l on;
connectAttr "flexiPlane_flc_c01_scaleConstraint1.csx" "flexiPlane_flc_c01.sx";
connectAttr "flexiPlane_flc_c01_scaleConstraint1.csy" "flexiPlane_flc_c01.sy";
connectAttr "flexiPlane_flc_c01_scaleConstraint1.csz" "flexiPlane_flc_c01.sz";
connectAttr "flexiPlane_surface0Shape1.wm" "flexiPlane_flc_c0Shape1.iwm";
connectAttr "flexiPlane_surface0Shape1.l" "flexiPlane_flc_c0Shape1.is";
connectAttr "curveShape3.l" "flexiPlane_flc_c0Shape1.sp";
connectAttr "curve3.wm" "flexiPlane_flc_c0Shape1.spm";
connectAttr "flexiPlane_flc_c01.pim" "flexiPlane_flc_c01_scaleConstraint1.cpim";
connectAttr "flexiPlane_globalMove01.s" "flexiPlane_flc_c01_scaleConstraint1.tg[0].ts"
		;
connectAttr "flexiPlane_globalMove01.pm" "flexiPlane_flc_c01_scaleConstraint1.tg[0].tpm"
		;
connectAttr "flexiPlane_flc_c01_scaleConstraint1.w0" "flexiPlane_flc_c01_scaleConstraint1.tg[0].tw"
		;
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_c01.sy";
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_c01.sz";
connectAttr "flexiPlane_flc_d0Shape1.ot" "flexiPlane_flc_d01.t" -l on;
connectAttr "flexiPlane_flc_d0Shape1.or" "flexiPlane_flc_d01.r" -l on;
connectAttr "flexiPlane_flc_d01_scaleConstraint1.csx" "flexiPlane_flc_d01.sx";
connectAttr "flexiPlane_flc_d01_scaleConstraint1.csy" "flexiPlane_flc_d01.sy";
connectAttr "flexiPlane_flc_d01_scaleConstraint1.csz" "flexiPlane_flc_d01.sz";
connectAttr "flexiPlane_surface0Shape1.wm" "flexiPlane_flc_d0Shape1.iwm";
connectAttr "flexiPlane_surface0Shape1.l" "flexiPlane_flc_d0Shape1.is";
connectAttr "curveShape4.l" "flexiPlane_flc_d0Shape1.sp";
connectAttr "curve4.wm" "flexiPlane_flc_d0Shape1.spm";
connectAttr "flexiPlane_flc_d01.pim" "flexiPlane_flc_d01_scaleConstraint1.cpim";
connectAttr "flexiPlane_globalMove01.s" "flexiPlane_flc_d01_scaleConstraint1.tg[0].ts"
		;
connectAttr "flexiPlane_globalMove01.pm" "flexiPlane_flc_d01_scaleConstraint1.tg[0].tpm"
		;
connectAttr "flexiPlane_flc_d01_scaleConstraint1.w0" "flexiPlane_flc_d01_scaleConstraint1.tg[0].tw"
		;
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_d01.sy";
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_d01.sz";
connectAttr "flexiPlane_flc_e0Shape1.ot" "flexiPlane_flc_e01.t" -l on;
connectAttr "flexiPlane_flc_e0Shape1.or" "flexiPlane_flc_e01.r" -l on;
connectAttr "flexiPlane_flc_e01_scaleConstraint1.csx" "flexiPlane_flc_e01.sx";
connectAttr "flexiPlane_flc_e01_scaleConstraint1.csy" "flexiPlane_flc_e01.sy";
connectAttr "flexiPlane_flc_e01_scaleConstraint1.csz" "flexiPlane_flc_e01.sz";
connectAttr "flexiPlane_surface0Shape1.wm" "flexiPlane_flc_e0Shape1.iwm";
connectAttr "flexiPlane_surface0Shape1.l" "flexiPlane_flc_e0Shape1.is";
connectAttr "curveShape5.l" "flexiPlane_flc_e0Shape1.sp";
connectAttr "curve5.wm" "flexiPlane_flc_e0Shape1.spm";
connectAttr "flexiPlane_flc_e01.pim" "flexiPlane_flc_e01_scaleConstraint1.cpim";
connectAttr "flexiPlane_globalMove01.s" "flexiPlane_flc_e01_scaleConstraint1.tg[0].ts"
		;
connectAttr "flexiPlane_globalMove01.pm" "flexiPlane_flc_e01_scaleConstraint1.tg[0].tpm"
		;
connectAttr "flexiPlane_flc_e01_scaleConstraint1.w0" "flexiPlane_flc_e01_scaleConstraint1.tg[0].tw"
		;
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_e01.sy";
connectAttr "flexiPlane_cond_volume01.ocr" "flexiPlane_bind_e01.sz";
connectAttr "wire1GroupId.id" "flexiPlane_bShp_surface0Shape1.iog.og[0].gid";
connectAttr "wire1Set.mwc" "flexiPlane_bShp_surface0Shape1.iog.og[0].gco";
connectAttr "groupId6.id" "flexiPlane_bShp_surface0Shape1.iog.og[1].gid";
connectAttr "tweakSet3.mwc" "flexiPlane_bShp_surface0Shape1.iog.og[1].gco";
connectAttr "twist1GroupId.id" "flexiPlane_bShp_surface0Shape1.iog.og[2].gid";
connectAttr "twist1Set.mwc" "flexiPlane_bShp_surface0Shape1.iog.og[2].gco";
connectAttr "flexiPlane_wireAttrs_surface01.og[0]" "flexiPlane_bShp_surface0Shape1.cr"
		;
connectAttr "flexiPlane_wire_surface_tweak0101.pl[0].cp[0]" "flexiPlane_bShp_surface0Shape1.twl"
		;
connectAttr "flexiPlane_cl_mid01Cluster.og[0]" "flexiPlane_wire_surface0Shape1.cr"
		;
connectAttr "flexiPlane_cl_Cluster_tweak01.pl[0].cp[0]" "flexiPlane_wire_surface0Shape1.twl"
		;
connectAttr "cluster1GroupId.id" "flexiPlane_wire_surface0Shape1.iog.og[0].gid";
connectAttr "cluster1Set.mwc" "flexiPlane_wire_surface0Shape1.iog.og[0].gco";
connectAttr "groupId4.id" "flexiPlane_wire_surface0Shape1.iog.og[1].gid";
connectAttr "tweakSet2.mwc" "flexiPlane_wire_surface0Shape1.iog.og[1].gco";
connectAttr "cluster2GroupId.id" "flexiPlane_wire_surface0Shape1.iog.og[2].gid";
connectAttr "cluster2Set.mwc" "flexiPlane_wire_surface0Shape1.iog.og[2].gco";
connectAttr "cluster3GroupId.id" "flexiPlane_wire_surface0Shape1.iog.og[3].gid";
connectAttr "cluster3Set.mwc" "flexiPlane_wire_surface0Shape1.iog.og[3].gco";
connectAttr "flexiPlane_cnt_a01.t" "flexiPlane_cl_a01.t";
connectAttr "flexiPlane_cnt_b01.t" "flexiPlane_cl_b01.t";
connectAttr "flexiPlane_midBend01.t" "flexiPlane_cl_mid01.t";
connectAttr "flexiPlane_twistAttrs_surface01.msg" "flexiPlane_twist_surface01.sml"
		;
connectAttr "flexiPlane_twistAttrs_surface01.sa" "flexiPlane_twist_surface01Shape.sa"
		;
connectAttr "flexiPlane_twistAttrs_surface01.ea" "flexiPlane_twist_surface01Shape.ea"
		;
connectAttr "flexiPlane_twistAttrs_surface01.lb" "flexiPlane_twist_surface01Shape.lb"
		;
connectAttr "flexiPlane_twistAttrs_surface01.hb" "flexiPlane_twist_surface01Shape.hb"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "surfaceShader1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "surfaceShader1SG.message" ":defaultLightSet.message";
connectAttr "flexiPlane_bShpNode_surface01.mlpr" "shapeEditorManager.bspr[0]";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "skeleton_renderLayerManager.rlmi[0]" "skeleton_defaultRenderLayer.rlid"
		;
connectAttr ":TurtleDefaultBakeLayer.idx" ":TurtleBakeLayerManager.bli[0]";
connectAttr ":TurtleRenderOptions.msg" ":TurtleDefaultBakeLayer.rset";
connectAttr "flexiPlane_surface_material01.oc" "lambert2SG.ss";
connectAttr "flexiPlane_surface0Shape1.iog" "lambert2SG.dsm" -na;
connectAttr "flexiPlane_bShp_surface0Shape1.iog" "lambert2SG.dsm" -na;
connectAttr "lambert2SG.msg" "materialInfo1.sg";
connectAttr "flexiPlane_surface_material01.msg" "materialInfo1.m";
connectAttr "flexiPlane_bShpNode_surface01GroupParts.og" "flexiPlane_bShpNode_surface01.ip[0].ig"
		;
connectAttr "flexiPlane_bShpNode_surface01GroupId.id" "flexiPlane_bShpNode_surface01.ip[0].gi"
		;
connectAttr "flexiPlane_bShp_surface0Shape1.ws" "flexiPlane_bShpNode_surface01.it[0].itg[0].iti[6000].igt"
		;
connectAttr "shapeEditorManager.obsv[0]" "flexiPlane_bShpNode_surface01.tgdt[0].dpvs"
		;
connectAttr "groupParts2.og" "flexiPlane_bShp_surface_tweak01.ip[0].ig";
connectAttr "groupId2.id" "flexiPlane_bShp_surface_tweak01.ip[0].gi";
connectAttr "flexiPlane_bShpNode_surface01GroupId.msg" "flexiPlane_bShpNode_surface01Set.gn"
		 -na;
connectAttr "flexiPlane_surface0Shape1.iog.og[0]" "flexiPlane_bShpNode_surface01Set.dsm"
		 -na;
connectAttr "flexiPlane_bShpNode_surface01.msg" "flexiPlane_bShpNode_surface01Set.ub[0]"
		;
connectAttr "flexiPlane_bShp_surface_tweak01.og[0]" "flexiPlane_bShpNode_surface01GroupParts.ig"
		;
connectAttr "flexiPlane_bShpNode_surface01GroupId.id" "flexiPlane_bShpNode_surface01GroupParts.gi"
		;
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "flexiPlane_surface0Shape1.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "flexiPlane_bShp_surface_tweak01.msg" "tweakSet1.ub[0]";
connectAttr "flexiPlane_surface0Shape1Orig1.ws" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "cluster1GroupParts.og" "flexiPlane_cl_a01Cluster.ip[0].ig";
connectAttr "cluster1GroupId.id" "flexiPlane_cl_a01Cluster.ip[0].gi";
connectAttr "flexiPlane_cl_a01.wm" "flexiPlane_cl_a01Cluster.ma";
connectAttr "flexiPlane_cl_a01Shape.x" "flexiPlane_cl_a01Cluster.x";
connectAttr "groupParts4.og" "flexiPlane_cl_Cluster_tweak01.ip[0].ig";
connectAttr "groupId4.id" "flexiPlane_cl_Cluster_tweak01.ip[0].gi";
connectAttr "cluster1GroupId.msg" "cluster1Set.gn" -na;
connectAttr "flexiPlane_wire_surface0Shape1.iog.og[0]" "cluster1Set.dsm" -na;
connectAttr "flexiPlane_cl_a01Cluster.msg" "cluster1Set.ub[0]";
connectAttr "flexiPlane_cl_Cluster_tweak01.og[0]" "cluster1GroupParts.ig";
connectAttr "cluster1GroupId.id" "cluster1GroupParts.gi";
connectAttr "groupId4.msg" "tweakSet2.gn" -na;
connectAttr "flexiPlane_wire_surface0Shape1.iog.og[1]" "tweakSet2.dsm" -na;
connectAttr "flexiPlane_cl_Cluster_tweak01.msg" "tweakSet2.ub[0]";
connectAttr "flexiPlane_wire_surface0Shape1Orig1.ws" "groupParts4.ig";
connectAttr "groupId4.id" "groupParts4.gi";
connectAttr "cluster2GroupParts.og" "flexiPlane_cl_b01Cluster.ip[0].ig";
connectAttr "cluster2GroupId.id" "flexiPlane_cl_b01Cluster.ip[0].gi";
connectAttr "flexiPlane_cl_b01.wm" "flexiPlane_cl_b01Cluster.ma";
connectAttr "flexiPlane_cl_b01Shape.x" "flexiPlane_cl_b01Cluster.x";
connectAttr "cluster2GroupId.msg" "cluster2Set.gn" -na;
connectAttr "flexiPlane_wire_surface0Shape1.iog.og[2]" "cluster2Set.dsm" -na;
connectAttr "flexiPlane_cl_b01Cluster.msg" "cluster2Set.ub[0]";
connectAttr "flexiPlane_cl_a01Cluster.og[0]" "cluster2GroupParts.ig";
connectAttr "cluster2GroupId.id" "cluster2GroupParts.gi";
connectAttr "cluster3GroupParts.og" "flexiPlane_cl_mid01Cluster.ip[0].ig";
connectAttr "cluster3GroupId.id" "flexiPlane_cl_mid01Cluster.ip[0].gi";
connectAttr "flexiPlane_cl_mid01.wm" "flexiPlane_cl_mid01Cluster.ma";
connectAttr "flexiPlane_cl_mid01Shape.x" "flexiPlane_cl_mid01Cluster.x";
connectAttr "cluster3GroupId.msg" "cluster3Set.gn" -na;
connectAttr "flexiPlane_wire_surface0Shape1.iog.og[3]" "cluster3Set.dsm" -na;
connectAttr "flexiPlane_cl_mid01Cluster.msg" "cluster3Set.ub[0]";
connectAttr "flexiPlane_cl_b01Cluster.og[0]" "cluster3GroupParts.ig";
connectAttr "cluster3GroupId.id" "cluster3GroupParts.gi";
connectAttr "wire1GroupParts.og" "flexiPlane_wireAttrs_surface01.ip[0].ig";
connectAttr "wire1GroupId.id" "flexiPlane_wireAttrs_surface01.ip[0].gi";
connectAttr "flexiPlane_wire_surface01BaseWireShape.ws" "flexiPlane_wireAttrs_surface01.bw[0]"
		;
connectAttr "flexiPlane_wire_surface0Shape1.ws" "flexiPlane_wireAttrs_surface01.dw[0]"
		;
connectAttr "groupParts6.og" "flexiPlane_wire_surface_tweak0101.ip[0].ig";
connectAttr "groupId6.id" "flexiPlane_wire_surface_tweak0101.ip[0].gi";
connectAttr "wire1GroupId.msg" "wire1Set.gn" -na;
connectAttr "flexiPlane_bShp_surface0Shape1.iog.og[0]" "wire1Set.dsm" -na;
connectAttr "flexiPlane_wireAttrs_surface01.msg" "wire1Set.ub[0]";
connectAttr "flexiPlane_twistAttrs_surface01.og[0]" "wire1GroupParts.ig";
connectAttr "wire1GroupId.id" "wire1GroupParts.gi";
connectAttr "groupId6.msg" "tweakSet3.gn" -na;
connectAttr "flexiPlane_bShp_surface0Shape1.iog.og[1]" "tweakSet3.dsm" -na;
connectAttr "flexiPlane_wire_surface_tweak0101.msg" "tweakSet3.ub[0]";
connectAttr "flexiPlane_bShp_surface0Shape1Orig1.ws" "groupParts6.ig";
connectAttr "groupId6.id" "groupParts6.gi";
connectAttr "flexiPlane_ss_midBend01.oc" "surfaceShader1SG.ss";
connectAttr "flexiPlane_midBend0Shape1.iog" "surfaceShader1SG.dsm" -na;
connectAttr "surfaceShader1SG.msg" "materialInfo2.sg";
connectAttr "flexiPlane_ss_midBend01.msg" "materialInfo2.m";
connectAttr "flexiPlane_ss_midBend01.msg" "materialInfo2.t" -na;
connectAttr "flexiPlane_cnt_b01.rx" "flexiPlane_twistAttrs_surface01.sa";
connectAttr "flexiPlane_cnt_a01.rx" "flexiPlane_twistAttrs_surface01.ea";
connectAttr "twist1GroupParts.og" "flexiPlane_twistAttrs_surface01.ip[0].ig";
connectAttr "twist1GroupId.id" "flexiPlane_twistAttrs_surface01.ip[0].gi";
connectAttr "flexiPlane_twist_surface01Shape.dd" "flexiPlane_twistAttrs_surface01.dd"
		;
connectAttr "flexiPlane_twist_surface01.wm" "flexiPlane_twistAttrs_surface01.ma"
		;
connectAttr "twist1GroupId.msg" "twist1Set.gn" -na;
connectAttr "flexiPlane_bShp_surface0Shape1.iog.og[2]" "twist1Set.dsm" -na;
connectAttr "flexiPlane_twistAttrs_surface01.msg" "twist1Set.ub[0]";
connectAttr "flexiPlane_wire_surface_tweak0101.og[0]" "twist1GroupParts.ig";
connectAttr "twist1GroupId.id" "twist1GroupParts.gi";
connectAttr "flexiPlane_wire_surface0Shape1.ws" "flexiPlane_curveInfo01.ic";
connectAttr "flexiPlane_curveInfo01.al" "flexiPlane_div_squashStretch_length01.i1x"
		;
connectAttr "flexiPlane_div_squashStretch_length01.ox" "flexiPlane_div_volume01.i2x"
		;
connectAttr "flexiPlane_cnt_global01.enable" "flexiPlane_cond_volume01.ft";
connectAttr "flexiPlane_div_volume01.ox" "flexiPlane_cond_volume01.ctr";
connectAttr "flexiPlane01.msg" "bindPose1.m[0]";
connectAttr "flexiPlane_extraNodes01.msg" "bindPose1.m[1]";
connectAttr "flexiPlane_flcs01.msg" "bindPose1.m[2]";
connectAttr "flexiPlane_flc_e01.msg" "bindPose1.m[3]";
connectAttr "flexiPlane_bind_e01.msg" "bindPose1.m[4]";
connectAttr "flexiPlane_flc_d01.msg" "bindPose1.m[5]";
connectAttr "flexiPlane_bind_d01.msg" "bindPose1.m[6]";
connectAttr "flexiPlane_flc_c01.msg" "bindPose1.m[7]";
connectAttr "flexiPlane_bind_c01.msg" "bindPose1.m[8]";
connectAttr "flexiPlane_flc_b01.msg" "bindPose1.m[9]";
connectAttr "flexiPlane_bind_b01.msg" "bindPose1.m[10]";
connectAttr "flexiPlane_flc_a01.msg" "bindPose1.m[11]";
connectAttr "flexiPlane_bind_a01.msg" "bindPose1.m[12]";
connectAttr "bindPose1.w" "bindPose1.p[0]";
connectAttr "bindPose1.m[0]" "bindPose1.p[1]";
connectAttr "bindPose1.m[1]" "bindPose1.p[2]";
connectAttr "bindPose1.m[2]" "bindPose1.p[3]";
connectAttr "bindPose1.m[3]" "bindPose1.p[4]";
connectAttr "bindPose1.m[2]" "bindPose1.p[5]";
connectAttr "bindPose1.m[5]" "bindPose1.p[6]";
connectAttr "bindPose1.m[2]" "bindPose1.p[7]";
connectAttr "bindPose1.m[7]" "bindPose1.p[8]";
connectAttr "bindPose1.m[2]" "bindPose1.p[9]";
connectAttr "bindPose1.m[9]" "bindPose1.p[10]";
connectAttr "bindPose1.m[2]" "bindPose1.p[11]";
connectAttr "bindPose1.m[11]" "bindPose1.p[12]";
connectAttr "flexiPlane_bind_e01.bps" "bindPose1.wm[4]";
connectAttr "flexiPlane_bind_d01.bps" "bindPose1.wm[6]";
connectAttr "flexiPlane_bind_c01.bps" "bindPose1.wm[8]";
connectAttr "flexiPlane_bind_b01.bps" "bindPose1.wm[10]";
connectAttr "flexiPlane_bind_a01.bps" "bindPose1.wm[12]";
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "surfaceShader1SG.pa" ":renderPartition.st" -na;
connectAttr "flexiPlane_surface_material01.msg" ":defaultShaderList1.s" -na;
connectAttr "flexiPlane_ss_midBend01.msg" ":defaultShaderList1.s" -na;
connectAttr "flexiPlane_div_squashStretch_length01.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "flexiPlane_div_volume01.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "flexiPlane_cond_volume01.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "skeleton_defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "twist1Set.pa" ":characterPartition.st" -na;
// End of rig_flexiPlane_02.ma
