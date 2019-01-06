//Maya ASCII 2018 scene
//Name: rig_flexiPlane_04.ma
//Last modified: Tue, May 29, 2018 11:05:17 PM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
requires "Mayatomr" "2013.0 - 3.10.1.4 ";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "flexiPlane01";
	rename -uid "F065B938-42BC-C779-34B0-E2BF8A8D44FA";
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
	rename -uid "EA23AD00-4522-4AF9-2574-5E8D38ACB4C6";
	addAttr -ci true -sn "_" -ln "_" -min 0 -max 0 -en "volume" -at "enum";
	addAttr -ci true -sn "enable" -ln "enable" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr -cb on "._";
	setAttr -k on ".enable" yes;
createNode nurbsCurve -n "flexiPlane_cnt_global0Shape1" -p "flexiPlane_cnt_global01";
	rename -uid "773E7A36-462F-04CE-6606-ACB70A2378D3";
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
	rename -uid "88211586-41A4-C02D-DB6A-8E993799C599";
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
	rename -uid "75940351-4662-E81F-6214-D4AA05A92FBB";
createNode transform -n "flexiPlane_cnts01" -p "flexiPlane_globalMove01";
	rename -uid "6D33A2F2-41FD-75CB-3E6B-3FA0D3D84FE5";
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
	rename -uid "B3761918-4A93-01C9-0720-668E3E47A20B";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".ro" 3;
	setAttr ".rp" -type "double3" -5 0 0 ;
	setAttr ".sp" -type "double3" -5 0 0 ;
createNode nurbsCurve -n "flexiPlane_cnt_a0Shape1" -p "flexiPlane_cnt_a01";
	rename -uid "F06E67B0-4D16-359B-3228-DFA539476E2D";
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
	rename -uid "886A55DD-4B9B-2A7D-E46A-C8BAF3B914A9";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".ro" 3;
	setAttr ".rp" -type "double3" 4.9999999999999991 0 0 ;
	setAttr ".sp" -type "double3" 4.9999999999999991 0 0 ;
createNode nurbsCurve -n "flexiPlane_cnt_b0Shape1" -p "flexiPlane_cnt_b01";
	rename -uid "0EF19666-409B-B5E1-530A-DBB2407B73F5";
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
	rename -uid "E450359E-43AB-6B79-3DDE-47AA2C70F5A0";
createNode transform -n "flexiPlane_midBend01" -p "flexiPlane_grp_midBend01";
	rename -uid "30C5932A-46FA-804A-2333-6BAFF773E3EC";
createNode mesh -n "flexiPlane_midBend0Shape1" -p "flexiPlane_midBend01";
	rename -uid "8565DC7F-4FD4-58A1-E191-F6973A2EF699";
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
	rename -uid "C047DB1C-4C30-F083-6843-F791BC80E6F7";
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
	rename -uid "88FFE9EA-4C6B-51FB-0682-4C9BF6CEEBE5";
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
	rename -uid "39B5026B-4620-886C-D2A9-B987F9FBC156";
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
	rename -uid "3E9E8385-4121-4B1A-075F-108B66A90AB2";
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
	rename -uid "3B987B93-4514-4FD7-8045-9D99C59C8E50";
createNode transform -n "flexiPlane_flcs01" -p "flexiPlane_extraNodes01";
	rename -uid "CD5A4578-4320-E9D9-5A1D-1FB27948D37F";
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
	rename -uid "E038EDD0-4B1A-01D2-E9ED-3DB4F6B66552";
createNode follicle -n "flexiPlane_flc_a0Shape1" -p "flexiPlane_flc_a01";
	rename -uid "7BC4A1C8-4A92-7F6B-D0D7-DC8209D8DD90";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.1;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve1" -p "flexiPlane_flc_a01";
	rename -uid "5C8D9722-42AB-B19F-AFAF-E4A4B0311D35";
createNode nurbsCurve -n "curveShape1" -p "curve1";
	rename -uid "F75CDFF8-4F04-95E8-89DB-728FBF3B5858";
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
	rename -uid "214A6343-4B32-5F03-0C75-30A6F0794EDF";
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
	rename -uid "4C6B54E8-4F0B-33CE-87BF-599FDC8895FC";
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
	rename -uid "E370DFA4-46E1-59A9-FD17-0A87B7C45A9D";
createNode follicle -n "flexiPlane_flc_b0Shape1" -p "flexiPlane_flc_b01";
	rename -uid "A4C21A9A-4013-DB1E-C58C-439506C47830";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.3;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve2" -p "flexiPlane_flc_b01";
	rename -uid "05E52CA2-4128-EC64-DF1D-B8A706525DEC";
createNode nurbsCurve -n "curveShape2" -p "curve2";
	rename -uid "EEDD35E2-4B22-2C90-0749-C19EC65885D6";
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
	rename -uid "D979559D-45EF-3F41-46E2-D895715C1D16";
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
	rename -uid "E12BD01F-4D51-8A69-2260-1BADCE8486D8";
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
	rename -uid "681C3467-4E40-6445-062D-ACB645A0B08F";
createNode follicle -n "flexiPlane_flc_c0Shape1" -p "flexiPlane_flc_c01";
	rename -uid "DE3706F5-487C-736E-8D48-67920901E935";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.5;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve3" -p "flexiPlane_flc_c01";
	rename -uid "A051C81A-412F-1D10-EC03-A586C96C295E";
createNode nurbsCurve -n "curveShape3" -p "curve3";
	rename -uid "FC25209C-4816-F363-7C6C-A99A74B966C6";
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
	rename -uid "802E6D16-4FBF-906C-F5B9-F3AF5D858E10";
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
	rename -uid "B6186AAD-4488-38A2-4BDA-609099F84707";
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
	rename -uid "C2B66F17-4F53-6B74-4999-0FA599921FD0";
createNode follicle -n "flexiPlane_flc_d0Shape1" -p "flexiPlane_flc_d01";
	rename -uid "349F11AB-4F22-40B7-AD4D-23AF0357DF5E";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.7;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve4" -p "flexiPlane_flc_d01";
	rename -uid "A7D3D55B-43E3-60A8-661F-9491D9AD716B";
createNode nurbsCurve -n "curveShape4" -p "curve4";
	rename -uid "0675ABB0-4AC4-A52A-B170-D4B289405CF4";
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
	rename -uid "91282FEE-4D6B-181F-E6BA-48B4182D6CBA";
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
	rename -uid "DF7F0252-44C9-62CF-6582-548F41A6D346";
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
	rename -uid "75A62B12-418D-CB2D-2895-419690231768";
createNode follicle -n "flexiPlane_flc_e0Shape1" -p "flexiPlane_flc_e01";
	rename -uid "6F290B6A-4A33-4CB3-A479-C6B57A90B336";
	setAttr -k off ".v" no;
	setAttr ".pu" 0.9;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve5" -p "flexiPlane_flc_e01";
	rename -uid "7D2DD15B-463E-2A4A-1AB6-E282520C1964";
createNode nurbsCurve -n "curveShape5" -p "curve5";
	rename -uid "CEB633F2-4B90-CF9B-EA2F-6FB6A0D4AD5C";
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
	rename -uid "F7553444-4181-30B4-40D4-35A194AA3A22";
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
	rename -uid "754F5AD0-4E75-D4EC-D13B-F1A3B278AFE3";
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
	rename -uid "5F6EB8CD-4E6E-AF09-3A50-72836879F315";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 -5 ;
createNode nurbsSurface -n "flexiPlane_bShp_surface0Shape1" -p "flexiPlane_bShp_surface01";
	rename -uid "B54768CE-4196-C179-A3DE-2E91D3A0D914";
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
	rename -uid "31117ABB-4750-4364-7C03-48853EBCCB9E";
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
	rename -uid "E5CD3098-4EB6-9067-E6B1-6C8F7E513411";
	setAttr ".v" no;
createNode nurbsCurve -n "flexiPlane_wire_surface0Shape1" -p "flexiPlane_wire_surface01";
	rename -uid "6B560702-451D-A8CA-5B84-3793CA27136A";
	setAttr -k off ".v";
	setAttr -s 8 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "flexiPlane_wire_surface0Shape1Orig1" -p "flexiPlane_wire_surface01";
	rename -uid "3051932A-4D53-50F6-97A6-0D8C48080E7D";
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
	rename -uid "1A17DBCA-43EB-5E35-F2EF-BAA5EE2DF76E";
	setAttr ".v" no;
createNode nurbsCurve -n "flexiPlane_wire_surface01BaseWireShape" -p "flexiPlane_wire_surface01BaseWire";
	rename -uid "66A0E309-4B66-9A66-DB24-F29C694EB05B";
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
	rename -uid "90E2B272-4B6C-2A10-94E5-4A97328AF5D7";
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
	rename -uid "40E8DCDB-47B2-5E99-794F-C7A98FEA673C";
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
	rename -uid "F9C8A7B7-4CCD-4B33-4547-CB82825A84D6";
	setAttr ".rp" -type "double3" -5 0 -5 ;
	setAttr ".sp" -type "double3" -5 0 -5 ;
createNode clusterHandle -n "flexiPlane_cl_a01Shape" -p "flexiPlane_cl_a01";
	rename -uid "69AD33ED-4BD8-2C63-F2AA-ACA5AFA3B8DB";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -6 0 -5 ;
createNode transform -n "flexiPlane_cl_b01" -p "flexiPlane_cls01";
	rename -uid "B149BD74-4137-A0BD-6CE9-2C8273812145";
	setAttr ".rp" -type "double3" 5 0 -5 ;
	setAttr ".sp" -type "double3" 5 0 -5 ;
createNode clusterHandle -n "flexiPlane_cl_b01Shape" -p "flexiPlane_cl_b01";
	rename -uid "FD295C55-4025-E610-6FEF-1E827211DC0F";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 6 0 -5 ;
createNode transform -n "flexiPlane_cl_mid01" -p "flexiPlane_cls01";
	rename -uid "A419F0C0-468B-94C0-4F4F-C49C4B42C9AA";
	setAttr ".rp" -type "double3" 0 0 -5 ;
	setAttr ".sp" -type "double3" 0 0 -5 ;
createNode clusterHandle -n "flexiPlane_cl_mid01Shape" -p "flexiPlane_cl_mid01";
	rename -uid "DE65DCAD-4094-1202-EB44-B891C41E9712";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 0 -5 ;
createNode transform -n "flexiPlane_twist_surface01" -p "flexiPlane_extraNodes01";
	rename -uid "71BFC28C-45D6-F775-51DF-F1A7C0FDE105";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 -5 ;
	setAttr ".r" -type "double3" 0 0 90 ;
	setAttr ".s" -type "double3" 5 5 5 ;
	setAttr ".smd" 7;
createNode deformTwist -n "flexiPlane_twist_surface01Shape" -p "flexiPlane_twist_surface01";
	rename -uid "8512A0E2-4DFA-86B3-7B34-3298F9081D4C";
	setAttr -k off ".v";
	setAttr ".dd" -type "doubleArray" 4 -1 1 0 0 ;
	setAttr ".hw" 1.1;
createNode materialInfo -n "materialInfo2";
	rename -uid "C9DE85D5-423B-4798-5952-3D905AECE2E7";
createNode shadingEngine -n "surfaceShader1SG";
	rename -uid "5D1293E7-43D8-8C57-3DC5-B58E731EE6D1";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode surfaceShader -n "flexiPlane_ss_midBend01";
	rename -uid "F9A0549B-481A-AFB0-7977-F6AAA546D663";
	setAttr ".oc" -type "float3" 1 1 0 ;
createNode groupId -n "flexiPlane_bShpNode_surface01GroupId";
	rename -uid "3B8B8F12-4C78-5A49-B63A-C8BB8F66766B";
	setAttr ".ihi" 0;
createNode objectSet -n "flexiPlane_bShpNode_surface01Set";
	rename -uid "36366C9A-47E6-EEC8-819D-7FB6A3096902";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode blendShape -n "flexiPlane_bShpNode_surface01";
	rename -uid "B525B2DA-48E6-B8D1-5DB8-F5AB1DC4B5D2";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".w[0]"  1;
	setAttr ".mlid" 0;
	setAttr ".mlpr" 0;
	setAttr ".pndr[0]"  0;
	setAttr ".tgdt[0].cid" -type "Int32Array" 1 0 ;
	setAttr ".aal" -type "attributeAlias" {"flexiPlane_bShp_surface01","weight[0]"} ;
createNode groupParts -n "flexiPlane_bShpNode_surface01GroupParts";
	rename -uid "87BB8B51-4019-0083-5AAC-389E549618CA";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode tweak -n "flexiPlane_bShp_surface_tweak01";
	rename -uid "667E6BED-44C6-B7E8-05B5-0680D9FE4C29";
createNode objectSet -n "tweakSet1";
	rename -uid "73E8771C-47C5-3E17-9D08-66BC6E3B8A14";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "B4260A0F-467B-BFBF-96CA-48B67D526067";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "B171F066-4403-AD6C-8FFD-B5811A86A0C9";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode materialInfo -n "materialInfo1";
	rename -uid "C7A31EBB-410F-CDA1-2E5A-11A9EECFA1BB";
createNode shadingEngine -n "lambert2SG";
	rename -uid "467CD508-481A-E230-BF8B-E1831FD04FFA";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "flexiPlane_surface_material01";
	rename -uid "52A314C4-4379-08F6-BE24-16AB9550DF2E";
	setAttr ".c" -type "float3" 0 0.75775909 1 ;
	setAttr ".it" -type "float3" 0.74358737 0.74358737 0.74358737 ;
createNode condition -n "flexiPlane_cond_volume01";
	rename -uid "D84FE229-42FA-AA5C-D1F3-918AC6CADBE5";
	setAttr ".st" 1;
createNode multiplyDivide -n "flexiPlane_div_volume01";
	rename -uid "C12FFF58-46D0-D615-B530-F2890FC3DCFF";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
createNode multiplyDivide -n "flexiPlane_div_squashStretch_length01";
	rename -uid "0615A337-47AF-1BDC-E014-858B2573EAC8";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 10 1 1 ;
createNode curveInfo -n "flexiPlane_curveInfo01";
	rename -uid "D8CF1596-4EF2-285F-D82F-8A9673C1C0B9";
createNode groupId -n "wire1GroupId";
	rename -uid "7648EF5C-4C97-2122-DB14-0285E916FE78";
	setAttr ".ihi" 0;
createNode objectSet -n "wire1Set";
	rename -uid "BBE8EAA5-4803-7108-9FF8-1FACC721A8D4";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode wire -n "flexiPlane_wireAttrs_surface01";
	rename -uid "67CD2BEB-4012-4C3A-5926-9C9D87271E8F";
	setAttr ".dds[0]"  20;
	setAttr ".sc[0]"  1;
createNode groupParts -n "wire1GroupParts";
	rename -uid "DA105678-4DBC-570B-ACE9-5A929A671876";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode nonLinear -n "flexiPlane_twistAttrs_surface01";
	rename -uid "481E91BC-4DCC-976A-5870-CAB0E59F5C6E";
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
	rename -uid "8E65C83F-4EDB-A035-BCC5-C5B757DFA629";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "twist1GroupId";
	rename -uid "8A1204D5-4BFD-BB29-A997-D4A93285F53C";
	setAttr ".ihi" 0;
createNode groupParts -n "twist1GroupParts";
	rename -uid "9D6668CC-40C5-96E8-9255-54B75683BCE4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode tweak -n "flexiPlane_wire_surface_tweak0101";
	rename -uid "5907584F-453C-48F5-A18F-069EDB553762";
createNode objectSet -n "tweakSet3";
	rename -uid "34167DFC-4697-0E84-C290-A2B4FA85AF99";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId6";
	rename -uid "A177F992-4F7D-3276-D953-399DD906BC1A";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts6";
	rename -uid "403AFE8B-4105-063D-9500-8C9860095F61";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode cluster -n "flexiPlane_cl_mid01Cluster";
	rename -uid "3E3C7E29-4743-E879-5C26-F3A1973E52F9";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ait" 0;
createNode objectSet -n "cluster3Set";
	rename -uid "C414D280-4CFB-C1E5-8AFA-15AC487465EC";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster3GroupId";
	rename -uid "EA4CE920-40E0-47B6-B23A-E1993E755490";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster3GroupParts";
	rename -uid "3595E5D7-4895-E02D-2C79-E398901A13E2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1]";
createNode cluster -n "flexiPlane_cl_b01Cluster";
	rename -uid "0BFD2009-44C6-DB41-4D82-06AC8C121221";
	setAttr ".wl[0].w[1]"  0.5;
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ait" 0;
createNode objectSet -n "cluster2Set";
	rename -uid "C2FE431F-4D13-AF79-537B-E5A15CD57171";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster2GroupId";
	rename -uid "47603AC3-4415-C93F-CE28-7CBB780BF586";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts";
	rename -uid "6445FE0A-4B18-2345-2228-A5B4AA711A04";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1:2]";
createNode cluster -n "flexiPlane_cl_a01Cluster";
	rename -uid "EEB65069-49F3-13DA-843A-DF84401C5604";
	setAttr ".wl[0].w[1]"  0.5;
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ait" 0;
createNode objectSet -n "cluster1Set";
	rename -uid "DC1E6CB8-46AA-A91B-77D8-7A90BBCB9217";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster1GroupId";
	rename -uid "9A912CB8-4F8D-2FE8-EF77-18A5FF815E6F";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster1GroupParts";
	rename -uid "8CCB0DBF-4DFA-EDDD-7C1C-C6AD207AA7A5";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0:1]";
createNode tweak -n "flexiPlane_cl_Cluster_tweak01";
	rename -uid "331FEC3C-4636-B889-EE5B-4FB35D464774";
createNode objectSet -n "tweakSet2";
	rename -uid "73E19E14-4D21-840C-6253-A7AD8E54F52E";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId4";
	rename -uid "1687A9DD-4EEE-7621-CC54-B280E1A4A961";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	rename -uid "AE44B5EC-433D-AEA3-D6C9-3F840C83E4E7";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "2F25FA5B-45EF-8667-FD5D-0DA4B4037120";
	setAttr -s 4 ".lnk";
	setAttr -s 4 ".slnk";
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
connectAttr "surfaceShader1SG.msg" "materialInfo2.sg";
connectAttr "flexiPlane_ss_midBend01.msg" "materialInfo2.m";
connectAttr "flexiPlane_ss_midBend01.msg" "materialInfo2.t" -na;
connectAttr "flexiPlane_ss_midBend01.oc" "surfaceShader1SG.ss";
connectAttr "flexiPlane_midBend0Shape1.iog" "surfaceShader1SG.dsm" -na;
connectAttr "flexiPlane_bShpNode_surface01GroupId.msg" "flexiPlane_bShpNode_surface01Set.gn"
		 -na;
connectAttr "flexiPlane_surface0Shape1.iog.og[0]" "flexiPlane_bShpNode_surface01Set.dsm"
		 -na;
connectAttr "flexiPlane_bShpNode_surface01.msg" "flexiPlane_bShpNode_surface01Set.ub[0]"
		;
connectAttr "flexiPlane_bShpNode_surface01GroupParts.og" "flexiPlane_bShpNode_surface01.ip[0].ig"
		;
connectAttr "flexiPlane_bShpNode_surface01GroupId.id" "flexiPlane_bShpNode_surface01.ip[0].gi"
		;
connectAttr "flexiPlane_bShp_surface0Shape1.ws" "flexiPlane_bShpNode_surface01.it[0].itg[0].iti[6000].igt"
		;
connectAttr "flexiPlane_bShp_surface_tweak01.og[0]" "flexiPlane_bShpNode_surface01GroupParts.ig"
		;
connectAttr "flexiPlane_bShpNode_surface01GroupId.id" "flexiPlane_bShpNode_surface01GroupParts.gi"
		;
connectAttr "groupParts2.og" "flexiPlane_bShp_surface_tweak01.ip[0].ig";
connectAttr "groupId2.id" "flexiPlane_bShp_surface_tweak01.ip[0].gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "flexiPlane_surface0Shape1.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "flexiPlane_bShp_surface_tweak01.msg" "tweakSet1.ub[0]";
connectAttr "flexiPlane_surface0Shape1Orig1.ws" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "lambert2SG.msg" "materialInfo1.sg";
connectAttr "flexiPlane_surface_material01.msg" "materialInfo1.m";
connectAttr "flexiPlane_surface_material01.oc" "lambert2SG.ss";
connectAttr "flexiPlane_surface0Shape1.iog" "lambert2SG.dsm" -na;
connectAttr "flexiPlane_bShp_surface0Shape1.iog" "lambert2SG.dsm" -na;
connectAttr "flexiPlane_cnt_global01.enable" "flexiPlane_cond_volume01.ft";
connectAttr "flexiPlane_div_volume01.ox" "flexiPlane_cond_volume01.ctr";
connectAttr "flexiPlane_div_squashStretch_length01.ox" "flexiPlane_div_volume01.i2x"
		;
connectAttr "flexiPlane_curveInfo01.al" "flexiPlane_div_squashStretch_length01.i1x"
		;
connectAttr "flexiPlane_wire_surface0Shape1.ws" "flexiPlane_curveInfo01.ic";
connectAttr "wire1GroupId.msg" "wire1Set.gn" -na;
connectAttr "flexiPlane_bShp_surface0Shape1.iog.og[0]" "wire1Set.dsm" -na;
connectAttr "flexiPlane_wireAttrs_surface01.msg" "wire1Set.ub[0]";
connectAttr "wire1GroupParts.og" "flexiPlane_wireAttrs_surface01.ip[0].ig";
connectAttr "wire1GroupId.id" "flexiPlane_wireAttrs_surface01.ip[0].gi";
connectAttr "flexiPlane_wire_surface01BaseWireShape.ws" "flexiPlane_wireAttrs_surface01.bw[0]"
		;
connectAttr "flexiPlane_wire_surface0Shape1.ws" "flexiPlane_wireAttrs_surface01.dw[0]"
		;
connectAttr "flexiPlane_twistAttrs_surface01.og[0]" "wire1GroupParts.ig";
connectAttr "wire1GroupId.id" "wire1GroupParts.gi";
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
connectAttr "groupParts6.og" "flexiPlane_wire_surface_tweak0101.ip[0].ig";
connectAttr "groupId6.id" "flexiPlane_wire_surface_tweak0101.ip[0].gi";
connectAttr "groupId6.msg" "tweakSet3.gn" -na;
connectAttr "flexiPlane_bShp_surface0Shape1.iog.og[1]" "tweakSet3.dsm" -na;
connectAttr "flexiPlane_wire_surface_tweak0101.msg" "tweakSet3.ub[0]";
connectAttr "flexiPlane_bShp_surface0Shape1Orig1.ws" "groupParts6.ig";
connectAttr "groupId6.id" "groupParts6.gi";
connectAttr "cluster3GroupParts.og" "flexiPlane_cl_mid01Cluster.ip[0].ig";
connectAttr "cluster3GroupId.id" "flexiPlane_cl_mid01Cluster.ip[0].gi";
connectAttr "flexiPlane_cl_mid01.wm" "flexiPlane_cl_mid01Cluster.ma";
connectAttr "flexiPlane_cl_mid01Shape.x" "flexiPlane_cl_mid01Cluster.x";
connectAttr "cluster3GroupId.msg" "cluster3Set.gn" -na;
connectAttr "flexiPlane_wire_surface0Shape1.iog.og[3]" "cluster3Set.dsm" -na;
connectAttr "flexiPlane_cl_mid01Cluster.msg" "cluster3Set.ub[0]";
connectAttr "flexiPlane_cl_b01Cluster.og[0]" "cluster3GroupParts.ig";
connectAttr "cluster3GroupId.id" "cluster3GroupParts.gi";
connectAttr "cluster2GroupParts.og" "flexiPlane_cl_b01Cluster.ip[0].ig";
connectAttr "cluster2GroupId.id" "flexiPlane_cl_b01Cluster.ip[0].gi";
connectAttr "flexiPlane_cl_b01.wm" "flexiPlane_cl_b01Cluster.ma";
connectAttr "flexiPlane_cl_b01Shape.x" "flexiPlane_cl_b01Cluster.x";
connectAttr "cluster2GroupId.msg" "cluster2Set.gn" -na;
connectAttr "flexiPlane_wire_surface0Shape1.iog.og[2]" "cluster2Set.dsm" -na;
connectAttr "flexiPlane_cl_b01Cluster.msg" "cluster2Set.ub[0]";
connectAttr "flexiPlane_cl_a01Cluster.og[0]" "cluster2GroupParts.ig";
connectAttr "cluster2GroupId.id" "cluster2GroupParts.gi";
connectAttr "cluster1GroupParts.og" "flexiPlane_cl_a01Cluster.ip[0].ig";
connectAttr "cluster1GroupId.id" "flexiPlane_cl_a01Cluster.ip[0].gi";
connectAttr "flexiPlane_cl_a01.wm" "flexiPlane_cl_a01Cluster.ma";
connectAttr "flexiPlane_cl_a01Shape.x" "flexiPlane_cl_a01Cluster.x";
connectAttr "cluster1GroupId.msg" "cluster1Set.gn" -na;
connectAttr "flexiPlane_wire_surface0Shape1.iog.og[0]" "cluster1Set.dsm" -na;
connectAttr "flexiPlane_cl_a01Cluster.msg" "cluster1Set.ub[0]";
connectAttr "flexiPlane_cl_Cluster_tweak01.og[0]" "cluster1GroupParts.ig";
connectAttr "cluster1GroupId.id" "cluster1GroupParts.gi";
connectAttr "groupParts4.og" "flexiPlane_cl_Cluster_tweak01.ip[0].ig";
connectAttr "groupId4.id" "flexiPlane_cl_Cluster_tweak01.ip[0].gi";
connectAttr "groupId4.msg" "tweakSet2.gn" -na;
connectAttr "flexiPlane_wire_surface0Shape1.iog.og[1]" "tweakSet2.dsm" -na;
connectAttr "flexiPlane_cl_Cluster_tweak01.msg" "tweakSet2.ub[0]";
connectAttr "flexiPlane_wire_surface0Shape1Orig1.ws" "groupParts4.ig";
connectAttr "groupId4.id" "groupParts4.gi";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "surfaceShader1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "surfaceShader1SG.message" ":defaultLightSet.message";
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "surfaceShader1SG.pa" ":renderPartition.st" -na;
connectAttr "flexiPlane_surface_material01.msg" ":defaultShaderList1.s" -na;
connectAttr "flexiPlane_ss_midBend01.msg" ":defaultShaderList1.s" -na;
connectAttr "flexiPlane_div_squashStretch_length01.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "flexiPlane_div_volume01.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "flexiPlane_cond_volume01.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "twist1Set.pa" ":characterPartition.st" -na;
// End of rig_flexiPlane_04.ma
