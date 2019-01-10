//Maya ASCII 2018ff07 scene
//Name: foot_v001.ma
//Last modified: Sat, May 12, 2018 07:30:49 PM
//Codeset: 1252
requires maya "2018ff07";
requires -nodeType "decomposeMatrix" "matrixNodes" "1.0";
requires "stereoCamera" "10.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201711281015-8e846c9074";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -n "foot_L_cpmnt";
	rename -uid "E3F865EB-498D-5A0D-2C5F-18A87C4D0E0F";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.1814 0.29659995 0.5783 ;
	setAttr ".it" no;
createNode transform -n "foot_M_input" -p "foot_L_cpmnt";
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
	setAttr -k on ".tarsiLength" 1.8769453361236783;
	setAttr ".startMtx" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 3.2788047940669824 2.5447580023815384 -0.51870483828642122 1;
	setAttr ".toeAngle" -32.928389796476075;
	setAttr ".tarsiAngle" 53.993544810862815;
	setAttr -k on ".toeLength" 2.4857768956930508;
createNode transform -n "foot_M_output" -p "foot_L_cpmnt";
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
createNode transform -n "foot_M_ankleSpace_srt" -p "|foot_L_cpmnt|control";
	rename -uid "F8CC1B11-42DE-835E-F514-6C98ABF1E0CA";
createNode transform -n "foot_M_tarsii_ctrl_srtBuffer" -p "foot_M_ankleSpace_srt";
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
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode transform -n "foot_M_toes_ctrl_srtBuffer" -p "foot_M_tarsii_ctrl";
	rename -uid "E306CA04-4965-9C72-B977-67A77A3C61B8";
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
	setAttr ".t" -type "double3" 0 0 4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode joint -n "diagnostic_tip" -p "diagnostic_toes";
	rename -uid "2FDE15DE-4DEE-E2F3-B505-71B862062BD6";
	setAttr ".t" -type "double3" 2.384185791015625e-07 -8.5989402265340686e-09 2.4857768956930508 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.65838017133321691;
createNode transform -n "guide" -p "foot_L_cpmnt";
	rename -uid "4B3DDE1D-47FF-4987-F21A-2B81C3D4F3F3";
createNode decomposeMatrix -n "foot_M_start_mtx2srt";
	rename -uid "1A530E00-4818-05F8-2026-98A898BD8DA5";
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
	setAttr -s 131 ".u";
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
connectAttr "foot_M_start_mtx2srt.ot" "foot_M_ankleSpace_srt.t";
connectAttr "foot_M_start_mtx2srt.or" "foot_M_ankleSpace_srt.r";
connectAttr "foot_M_input.tarsiAngle" "foot_M_tarsii_ctrl_srtBuffer.rx";
connectAttr "foot_M_input.tarsiLength" "diagnostic_tarsi.tz";
connectAttr "foot_M_input.toeAngle" "foot_M_toes_ctrl_srtBuffer.rx";
connectAttr "foot_M_input.tarsiLength" "foot_M_toes_ctrl_srtBuffer.tz";
connectAttr "foot_M_input.toeLength" "diagnostic_tip.tz";
connectAttr "foot_M_input.startMtx" "foot_M_start_mtx2srt.imat";
connectAttr "hyperLayout4.msg" "foot_L_container.hl";
connectAttr "foot_M_tarsii_ctrl.msg" "foot_L_container.pni[0].pnod";
connectAttr "foot_M_toes_ctrl.msg" "foot_L_container.pni[1].pnod";
connectAttr "foot_L_cpmnt.msg" "foot_L_container.cbp[0]";
connectAttr "foot_L_cpmnt.msg" "foot_L_container.cbc[0]";
connectAttr "foot_L_cpmnt.msg" "hyperLayout4.hyp[0].dn";
connectAttr "foot_M_input.msg" "hyperLayout4.hyp[1].dn";
connectAttr "foot_M_output.msg" "hyperLayout4.hyp[2].dn";
connectAttr "|foot_L_cpmnt|control.msg" "hyperLayout4.hyp[3].dn";
connectAttr "foot_M_ankleSpace_srt.msg" "hyperLayout4.hyp[4].dn";
connectAttr "foot_M_tarsii_ctrl_srtBuffer.msg" "hyperLayout4.hyp[5].dn";
connectAttr "foot_M_tarsii_ctrl.msg" "hyperLayout4.hyp[6].dn";
connectAttr "foot_M_tarsii_ctrlShape.msg" "hyperLayout4.hyp[7].dn";
connectAttr "foot_M_toes_ctrl_srtBuffer.msg" "hyperLayout4.hyp[8].dn";
connectAttr "foot_M_toes_ctrl.msg" "hyperLayout4.hyp[9].dn";
connectAttr "foot_M_toes_ctrlShape.msg" "hyperLayout4.hyp[10].dn";
connectAttr "foot_M_start_mtx2srt.msg" "hyperLayout4.hyp[11].dn";
connectAttr "|foot_L_cpmnt|guide.msg" "hyperLayout4.hyp[12].dn";
connectAttr "diagnostic_ankle.msg" "hyperLayout4.hyp[13].dn";
connectAttr "diagnostic_tarsi.msg" "hyperLayout4.hyp[14].dn";
connectAttr "diagnostic_toes.msg" "hyperLayout4.hyp[15].dn";
connectAttr "diagnostic_tip.msg" "hyperLayout4.hyp[16].dn";
connectAttr "foot_M_start_mtx2srt.msg" ":defaultRenderUtilityList1.u" -na;
// End of foot_v001.ma
