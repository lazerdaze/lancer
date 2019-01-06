//Maya ASCII 2018 scene
//Name: skeleton_biped_male_A.ma
//Last modified: Tue, Apr 24, 2018 08:39:27 AM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode joint -n "CenterRoot";
	rename -uid "D70DC5A3-4925-A9C2-7591-55A3E62B2A8C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".typ" 1;
	setAttr ".radi" 0.01;
createNode joint -n "CenterCOG" -p "CenterRoot";
	rename -uid "EC6E262A-41F4-E125-E294-C1BB6B44D193";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0.60851478686443794 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 1.1146115064620972 -0.0028521490748971701 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "COG";
	setAttr ".radi" 0.01;
createNode joint -n "CenterHip" -p "CenterCOG";
	rename -uid "76ADA098-4AC1-5018-DA4C-4796850FE990";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 1.1146115064620972 -0.0028521490748971701 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.01;
createNode joint -n "LeftHip" -p "CenterHip";
	rename -uid "1478B70F-4843-75B7-4534-EE969FBEA455";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.041760080477724393 -0.049712672550012424 -0.0063925493016862012 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -170.38312757983519 ;
	setAttr ".bps" -type "matrix" 0.99968948655488055 -0.024918476511202204 0 0 0.024918476511202204 0.99968948655488055 0 0
		 0 0 1 0 0.091058291494846344 1.038119912147522 -0.011709179729223251 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.01;
createNode joint -n "LeftKnee" -p "LeftHip";
	rename -uid "383A43FA-4208-A4DE-22F2-9A9BF4C765EE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.2412809510124726 0 1.7347234759768071e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 4.7759997585470986 -4.908449026696604e-07 ;
	setAttr ".bps" -type "matrix" 0.99968842858537332 -0.024918450140025285 -0.0014548522695240857 0
		 0.024918476511202204 0.99968948655488055 0 0 0.001454400518333736 -3.6252702105405151e-05 0.99999894170187698 0
		 0.15400950610637665 0.60067391395568848 -0.01170917972922325 1;
	setAttr ".sd" 1;
	setAttr ".typ" 3;
	setAttr ".radi" 0.01;
createNode joint -n "LeftFoot" -p "LeftKnee";
	rename -uid "2855A827-415C-BFAD-8E5C-6AACF9A01E86";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.25511609741065921 -2.1779552050738005e-09 6.9388939039072284e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -62.776262225551974 0 ;
	setAttr ".bps" -type "matrix" 0.99962596981310992 -0.027345943998272299 2.4753932381426161e-05 0
		 0.027345887559513116 0.99962105009117042 -0.0031557325945230936 0 6.1551938591125578e-05 0.0031552293615888724 0.99999502035711896 0
		 0.22033925354480743 0.13975057005882252 -0.05061627924442292 1;
	setAttr ".sd" 1;
	setAttr ".typ" 4;
	setAttr ".radi" 0.01;
createNode joint -n "LeftToe" -p "LeftFoot";
	rename -uid "461B2FA1-492B-1365-DF6F-3882E5F51CFE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.10011238755946297 2.7755575615628914e-17 6.9388939039072284e-17 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1.0000000000000002 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.5902773407317588e-15 6.3611093629270335e-15 1.20820904578353e-16 ;
	setAttr ".bps" -type "matrix" 0.99962602939546408 -0.027345945628217669 2.4753933856875589e-05 0
		 0.027345887559513123 0.99962105009117064 -0.0031557325945230945 0 6.1551938591125591e-05 0.0031552293615888733 0.99999502035711918 0
		 0.24945370852947235 0.048994265496730791 0.10689163953065875 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
	setAttr ".radi" 0.01;
createNode joint -n "LeftHip1" -p "CenterHip";
	rename -uid "CDE49224-4035-581E-94EC-6297D73AADB2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.041760032515244516 0.049712677193344844 -0.0063925603683828236 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 2.1186750230640765e-30 -9.6168724201648192 ;
	setAttr ".bps" -type "matrix" 0.99968948655488055 -0.024918476511202204 0 0 0.024918476511202204 0.99968948655488055 0 0
		 0 0 1 0 0.091058291494846344 1.038119912147522 -0.011709179729223251 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 0.01;
createNode joint -n "LeftKnee1" -p "LeftHip1";
	rename -uid "168256C2-44B3-C49D-940E-618C07F59D0C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.24128116949574024 2.8909975158253332e-07 -8.6736173798840355e-19 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9090959096599259e-06 4.7759997585470941 -1.8140251365471382e-14 ;
	setAttr ".bps" -type "matrix" 0.99968842858537332 -0.024918450140025285 -0.0014548522695240857 0
		 0.024918476511202204 0.99968948655488055 0 0 0.001454400518333736 -3.6252702105405151e-05 0.99999894170187698 0
		 0.15400950610637665 0.60067391395568848 -0.01170917972922325 1;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 0.01;
createNode joint -n "LeftFoot1" -p "LeftKnee1";
	rename -uid "D877056D-4844-9E4A-2C45-1FBC25ECBE2A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.25511592207516415 -2.1663648427927562e-07 1.4914975449142887e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.3577128849686037e-07 -62.776262225551925 3.7109164015986316e-06 ;
	setAttr ".bps" -type "matrix" 0.99962596981310992 -0.027345943998272299 2.4753932381426161e-05 0
		 0.027345887559513116 0.99962105009117042 -0.0031557325945230936 0 6.1551938591125578e-05 0.0031552293615888724 0.99999502035711896 0
		 0.22033925354480743 0.13975057005882252 -0.05061627924442292 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 0.01;
createNode joint -n "LeftToe1" -p "LeftFoot1";
	rename -uid "868835A2-4733-3B7F-C8BD-04A7D4D20768";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.10011241709413463 -1.7146751302155039e-07 3.9796036410688629e-08 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1.0000000000000002 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.5977117930529869e-06 -1.3222702682412092e-22 -1.2761213786148033e-21 ;
	setAttr ".bps" -type "matrix" 0.99962602939546408 -0.027345945628217669 2.4753933856875589e-05 0
		 0.027345887559513123 0.99962105009117064 -0.0031557325945230945 0 6.1551938591125591e-05 0.0031552293615888733 0.99999502035711918 0
		 0.24945370852947235 0.048994265496730791 0.10689163953065875 1;
	setAttr ".sd" 2;
	setAttr ".typ" 5;
	setAttr ".radi" 0.01;
createNode joint -n "CenterSpine0" -p "CenterCOG";
	rename -uid "587D0295-47CE-101C-104B-8BAD10717B20";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 1.1488123535326147 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 1.1146115064620972 -0.0028521490748971701 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.01;
createNode joint -n "CenterSpine1" -p "CenterSpine0";
	rename -uid "A62B50E4-4842-E5F1-074F-EA8EB92519DC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.077090307825351201 8.2598653521093073e-18 1.5612511283791264e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.2718243159333133e-16 2.8185495037494346 -6.3508876699740731e-15 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 5.4745258291445231e-19 1.2557888031005859 -0.0028521490748971701 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.01;
createNode joint -n "CenterSpine2" -p "CenterSpine1";
	rename -uid "13C9F42F-4D5F-9D88-AA0B-B496C56198F0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.077259956084360315 2.0991148771614998e-18 6.9388939039072284e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.8036251720749374e-16 -1.0034646394935618 -1.2700185539714016e-14 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.2974787909408305e-18 1.3969660997390747 -0.0028521490748971701 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.01;
createNode joint -n "CenterSpine4" -p "CenterSpine2";
	rename -uid "E19BCCB2-4A6D-38B4-415C-DE933B52711B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.10988456038897987 1.8947852633229076e-17 2.7755575615628914e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.6844219338242294e-16 -23.931316302583639 -6.5088650572649582e-15 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99998551980503858 0.0053703790332481835 0
		 0 -0.0053703790332481835 0.99998551980503858 0 -1.8874113454994911e-32 1.5978478193283081 -0.034963306039571762 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.01;
createNode joint -n "CenterHead" -p "CenterSpine4";
	rename -uid "3415B16B-41AC-6905-04C3-2B9DB59983AC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.042454919527616819 7.3955709864469857e-32 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 -1.8735446263900163e-32 1.6705865859985352 0.0047973766922950745 1;
	setAttr ".typ" 8;
	setAttr ".radi" 0.01;
createNode joint -n "LeftCollar" -p "CenterSpine2";
	rename -uid "23FCDFAA-48F4-2AC7-1564-EAA9B33E7948";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.03613455776251695 -0.016010388427998436 -0.016072171656444874 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.0247386284653421 11.506084121514279 -89.396110600970772 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0.029326096177101135 1.4615427255630493 -0.045444544404745102 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
	setAttr ".radi" 0.01;
createNode joint -n "LeftShoulder" -p "LeftCollar";
	rename -uid "A23BB8A7-45B4-63A8-3FDC-169E7B2F875C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.085392512387548691 -1.1102230246251565e-16 6.9388939039072284e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 6.8297733615916094 -6.9034845911162535 -44.897958930924062 ;
	setAttr ".bps" -type "matrix" 0.99990798796415992 -0.013555057290700263 -0.00039600255737589572 0
		 0.013555059161483659 0.99990812596514522 0 0 0.00039596619862456139 -5.3678384132771941e-06 0.99999992159097484 0
		 0.18258699774742126 1.4615427255630493 -0.076686300337314606 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.01;
createNode joint -n "LeftElbow" -p "LeftShoulder";
	rename -uid "97231B92-438A-6139-0271-F69982BB16EF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.13485751468535107 1.1102230246251565e-15 -2.0816681711721685e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.0195238308932497e-16 -10.161446593423932 -1.267251203885514e-14 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 11;
	setAttr ".radi" 0.01;
createNode joint -n "LeftElbow1" -p "LeftElbow";
	rename -uid "A37A3FDD-4EC3-3B15-E5BF-9E965AE00769";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.13113593789529235 -0.00051579361753784081 1.8181031915739942e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9878466759146975e-16 3.180554681463516e-15 -1.2523434058262594e-14 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 12;
	setAttr ".radi" 0.01;
createNode joint -n "LeftThumb0" -p "LeftElbow1";
	rename -uid "E8B8874E-4B2A-8A52-DC22-268A41EF0AB2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.010640293593300293 -0.009417636941399854 0.015372297006846804 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 88.149105723519867 -31.120651911231388 -44.812937424680463 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.01;
createNode joint -n "LeftThumb1" -p "LeftThumb0";
	rename -uid "7796319A-4362-72AD-1FEA-A491E75B0767";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.034037890615851052 5.5511151231257827e-17 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -21.23969128291483 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.01;
createNode joint -n "LeftThumb2" -p "LeftThumb1";
	rename -uid "4251AB02-4080-4882-FAE5-408A26EBFA0D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.020553366211070734 5.5511151231257827e-17 -5.5511151231257827e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7811106216195694e-13 0 0 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.01;
createNode joint -n "LeftIndexFinger0" -p "LeftElbow1";
	rename -uid "82F89551-4AF1-8A5B-C082-D68EB4C3B14D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.056397447045649585 -0.011461799994387789 0.021842935032933091 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 29.939739339641378 -8.1521885266926475 -20.135829425563998 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
	setAttr ".radi" 0.01;
createNode joint -n "LeftIndexFinger1" -p "LeftIndexFinger0";
	rename -uid "8D8CA63F-4558-A438-C9FF-DAA05068C955";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.026210339083093614 2.2204460492503131e-16 2.7755575615628914e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -23.499270534609796 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
	setAttr ".radi" 0.01;
createNode joint -n "LeftIndexFinger2" -p "LeftIndexFinger1";
	rename -uid "F0E3D649-48F3-B42D-E8EE-169B726E1B2D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.020432508166689733 -1.6653345369377348e-16 8.3266726846886741e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
	setAttr ".radi" 0.01;
createNode joint -n "LeftMiddleFinger0" -p "LeftElbow1";
	rename -uid "D1B2973D-42E9-3419-0640-34910F87CFC3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.060715230415583049 -0.0038424632434232997 0.0045731328660746917 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 21.083074354576311 -2.7929006377023495 -20.088363613320965 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.01;
createNode joint -n "LeftMiddleFinger1" -p "LeftMiddleFinger0";
	rename -uid "EEF583FC-405A-837F-01D0-33ACB6C09C5D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.026985162542683516 2.2204460492503131e-16 -5.5511151231257827e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -22.736028920480365 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.01;
createNode joint -n "LeftMiddleFinger2" -p "LeftMiddleFinger1";
	rename -uid "5DC90F3C-4704-B9F1-89F9-5790A55FBC86";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.021322510952600793 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.01;
createNode joint -n "LeftRingFinger0" -p "LeftElbow1";
	rename -uid "44E38D49-4839-470E-8817-8A8C652CCDD2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.059057238725681832 0.00055032511913810644 -0.013265751730478562 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.2565327765607548 6.8308123791553177 -18.471630725374112 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 0.01;
createNode joint -n "LeftRingFinger1" -p "LeftRingFinger0";
	rename -uid "47B99922-4834-CCA9-9066-A98AF89DCDC9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.02480648796549656 1.1102230246251565e-16 2.7755575615628914e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -18.029891275820823 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 0.01;
createNode joint -n "LeftRingFinger2" -p "LeftRingFinger1";
	rename -uid "5F195297-4DD2-F4CB-DE7E-57BE32486FA8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.021270842752411423 1.1102230246251565e-16 -6.9388939039072284e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 0.01;
createNode joint -n "LeftPinkyFinger0" -p "LeftElbow1";
	rename -uid "E972DE5B-4A47-3752-E7C3-AD881945E0A5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.052412158251709667 -0.0015822161873983998 -0.030911639625561715 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -17.163185660313001 18.006876080203391 -16.672537237873282 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
	setAttr ".radi" 0.01;
createNode joint -n "LeftPinkyFinger1" -p "LeftPinkyFinger0";
	rename -uid "FF591B6D-4D80-0071-698F-1CB00742B1E5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.01903988761638481 1.1102230246251565e-16 -2.0816681711721685e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -27.78962530653703 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
	setAttr ".radi" 0.01;
createNode joint -n "LeftPinkyFinger2" -p "LeftPinkyFinger1";
	rename -uid "91343DA0-4999-98EC-BF3F-6098035E10F9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.016175449115120588 -1.6653345369377348e-16 -6.9388939039072284e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
	setAttr ".radi" 0.01;
createNode joint -n "RightCollar" -p "CenterSpine2";
	rename -uid "45EDFC33-4A5B-EA2E-8435-098C7C36E067";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.036133070496362496 0.01601039051508488 -0.016072224386123893 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -176.97526137153457 -11.506084121514283 -90.6038893990292 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0.029326096177101135 1.4615427255630493 -0.045444544404745102 1;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 0.01;
createNode joint -n "RightShoulder" -p "RightCollar";
	rename -uid "9B6B6F10-487E-6EB1-4907-2085A650966A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.085392516352907857 2.2204460492503131e-16 2.3744763200800323e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 6.829773361591422 -6.9034845911163334 -44.897958930924041 ;
	setAttr ".bps" -type "matrix" 0.99990798796415992 -0.013555057290700263 -0.00039600255737589572 0
		 0.013555059161483659 0.99990812596514522 0 0 0.00039596619862456139 -5.3678384132771941e-06 0.99999992159097484 0
		 0.18258699774742126 1.4615427255630493 -0.076686300337314606 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 0.01;
createNode joint -n "RightElbow" -p "RightShoulder";
	rename -uid "5E7B78F2-42BE-F735-3F56-35B3D200AA6E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.13485669827421526 -9.1689233816527604e-07 1.8402334260592124e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.0256956916386529e-15 -10.161446593423918 -1.1536529883977671e-14 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 0.01;
createNode joint -n "RightHand" -p "RightElbow";
	rename -uid "26340B21-460A-54DF-43F7-87A3964A140E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.13113602316312031 0.00051615817158601196 -1.6029800758640689e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 0.01;
createNode joint -n "RightThumb0" -p "RightHand";
	rename -uid "214C1E99-47E4-500A-F895-F18CFC61D959";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.010641039820307563 0.0094179267971399305 -0.015372184248769072 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 88.149105723519924 -31.120651911231349 -44.812937424680506 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
	setAttr ".radi" 0.01;
createNode joint -n "RightThumb1" -p "RightThumb0";
	rename -uid "FE746699-4875-EB1D-5D0F-F4A6FF0FD588";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.034037796512103313 -7.6816958960446158e-08 -2.8998369816513048e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.3609186360961444e-15 -2.3257806108201961e-14 -21.23969128291483 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
	setAttr ".radi" 0.01;
createNode joint -n "RightThumb2" -p "RightThumb1";
	rename -uid "34B70EB4-44C7-5DAF-B2CF-288A4A5436A9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.020551938844727724 -4.7599723079772005e-07 -3.1936001715360263e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
	setAttr ".radi" 0.01;
createNode joint -n "RightIndexFinger0" -p "RightHand";
	rename -uid "22F0917B-4F0E-59A3-DBA0-4B8BCED0D69A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.056396051759687149 0.011460368408949817 -0.021843177889736255 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 29.939739339641427 -8.1521885266926279 -20.135829425564012 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
	setAttr ".radi" 0.01;
createNode joint -n "RightIndexFinger1" -p "RightIndexFinger0";
	rename -uid "4DFEA656-403B-F585-867A-2A81A90CD11B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.026211533551463939 3.6471785114233768e-07 1.7160148477191051e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.7211355139932687e-15 1.7890620083232277e-14 -23.49927053460981 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
	setAttr ".radi" 0.01;
createNode joint -n "RightIndexFinger2" -p "RightIndexFinger1";
	rename -uid "85CF0815-438C-433B-2C16-E989C4579724";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.020432800675400709 1.4750857757483971e-07 -1.1538503866259653e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
	setAttr ".radi" 0.01;
createNode joint -n "RightMiddleFinger0" -p "RightHand";
	rename -uid "D5A22627-46CB-2463-4392-36A7A7A91527";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.060714522517935299 0.0038412402131223766 -0.0045732967005463407 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 21.083074354576368 -2.79290063770233 -20.088363613320983 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
	setAttr ".radi" 0.01;
createNode joint -n "RightMiddleFinger1" -p "RightMiddleFinger0";
	rename -uid "539358F4-4AA4-34EA-0A3A-1F99AA2B01AC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.026985917475815802 3.8711776906286133e-07 1.2204332683340979e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.2364541890502403e-15 2.1071174764695788e-14 -22.736028920480372 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
	setAttr ".radi" 0.01;
createNode joint -n "RightMiddleFinger2" -p "RightMiddleFinger1";
	rename -uid "D4F7980D-4B7E-9AE0-8EEE-72B4F417D602";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.021322370381261835 1.2625992246162454e-07 -6.6350147681637495e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
	setAttr ".radi" 0.01;
createNode joint -n "RightRingFinger0" -p "RightHand";
	rename -uid "87F40BDE-4DA9-298A-5ABC-0E9CAACDB605";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.05905842947636411 -0.00054913912923071351 0.013265927912682978 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.2565327765602494 6.8308123791553363 -18.471630725374101 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
	setAttr ".radi" 0.01;
createNode joint -n "RightRingFinger1" -p "RightRingFinger0";
	rename -uid "9BD3C35C-4829-46E9-FD94-159E4F9F492F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.024806312830869925 -2.2959389922583284e-07 4.0307856226384775e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.0875265742401091e-14 1.9461018957204901e-13 -18.029891275820862 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
	setAttr ".radi" 0.01;
createNode joint -n "RightRingFinger2" -p "RightRingFinger1";
	rename -uid "4B72BFC8-41DE-3046-836E-2E9E661C8995";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.021268775057841527 -4.7141758702240466e-07 -6.2182461887938523e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
	setAttr ".radi" 0.01;
createNode joint -n "RightPinkyFinger0" -p "RightHand";
	rename -uid "8DDCD9BE-4690-14B9-7BDB-B7BEB4D890BD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.052410547493042359 0.0015806690871813522 0.030911345109679494 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -17.163185660312784 18.006876080203419 -16.672537237873257 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
	setAttr ".radi" 0.01;
createNode joint -n "RightPinkyFinger1" -p "RightPinkyFinger0";
	rename -uid "9F8D74BE-4A18-B2C8-42A7-E0900A5DC4B1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.019041827334562167 6.55094191115424e-07 -1.4049340405636324e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.0966054602360744e-14 -4.4328980872897765e-14 -27.789625306537047 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
	setAttr ".radi" 0.01;
createNode joint -n "RightPinkyFinger2" -p "RightPinkyFinger1";
	rename -uid "2622F63C-46C4-1D0E-523F-F8B72B5F6F93";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.016175301628310823 3.0992483163183593e-07 1.0399592122872781e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990454055265587 -0.013555010556539715 0.0027001257659802417 0
		 0.013555059161483663 0.99990812596514544 0 0 -0.0026998775336093406 3.660036231979867e-05 0.99999635465478576 0
		 0.3587268888950349 1.2884504795074463 -0.082290463149547577 1;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
	setAttr ".radi" 0.01;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
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
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 7 ".dsm";
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
connectAttr "CenterRoot.s" "CenterCOG.is";
connectAttr "CenterCOG.s" "CenterHip.is";
connectAttr "CenterHip.s" "LeftHip.is";
connectAttr "LeftHip.s" "LeftKnee.is";
connectAttr "LeftKnee.s" "LeftFoot.is";
connectAttr "LeftFoot.s" "LeftToe.is";
connectAttr "CenterHip.s" "LeftHip1.is";
connectAttr "LeftHip1.s" "LeftKnee1.is";
connectAttr "LeftKnee1.s" "LeftFoot1.is";
connectAttr "LeftFoot1.s" "LeftToe1.is";
connectAttr "CenterCOG.s" "CenterSpine0.is";
connectAttr "CenterSpine0.s" "CenterSpine1.is";
connectAttr "CenterSpine1.s" "CenterSpine2.is";
connectAttr "CenterSpine2.s" "CenterSpine4.is";
connectAttr "CenterSpine4.s" "CenterHead.is";
connectAttr "CenterSpine2.s" "LeftCollar.is";
connectAttr "LeftCollar.s" "LeftShoulder.is";
connectAttr "LeftShoulder.s" "LeftElbow.is";
connectAttr "LeftElbow.s" "LeftElbow1.is";
connectAttr "LeftElbow1.s" "LeftThumb0.is";
connectAttr "LeftThumb0.s" "LeftThumb1.is";
connectAttr "LeftThumb1.s" "LeftThumb2.is";
connectAttr "LeftElbow1.s" "LeftIndexFinger0.is";
connectAttr "LeftIndexFinger0.s" "LeftIndexFinger1.is";
connectAttr "LeftIndexFinger1.s" "LeftIndexFinger2.is";
connectAttr "LeftElbow1.s" "LeftMiddleFinger0.is";
connectAttr "LeftMiddleFinger0.s" "LeftMiddleFinger1.is";
connectAttr "LeftMiddleFinger1.s" "LeftMiddleFinger2.is";
connectAttr "LeftElbow1.s" "LeftRingFinger0.is";
connectAttr "LeftRingFinger0.s" "LeftRingFinger1.is";
connectAttr "LeftRingFinger1.s" "LeftRingFinger2.is";
connectAttr "LeftElbow1.s" "LeftPinkyFinger0.is";
connectAttr "LeftPinkyFinger0.s" "LeftPinkyFinger1.is";
connectAttr "LeftPinkyFinger1.s" "LeftPinkyFinger2.is";
connectAttr "CenterSpine2.s" "RightCollar.is";
connectAttr "RightCollar.s" "RightShoulder.is";
connectAttr "RightShoulder.s" "RightElbow.is";
connectAttr "RightElbow.s" "RightHand.is";
connectAttr "RightHand.s" "RightThumb0.is";
connectAttr "RightThumb0.s" "RightThumb1.is";
connectAttr "RightThumb1.s" "RightThumb2.is";
connectAttr "RightHand.s" "RightIndexFinger0.is";
connectAttr "RightIndexFinger0.s" "RightIndexFinger1.is";
connectAttr "RightIndexFinger1.s" "RightIndexFinger2.is";
connectAttr "RightHand.s" "RightMiddleFinger0.is";
connectAttr "RightMiddleFinger0.s" "RightMiddleFinger1.is";
connectAttr "RightMiddleFinger1.s" "RightMiddleFinger2.is";
connectAttr "RightHand.s" "RightRingFinger0.is";
connectAttr "RightRingFinger0.s" "RightRingFinger1.is";
connectAttr "RightRingFinger1.s" "RightRingFinger2.is";
connectAttr "RightHand.s" "RightPinkyFinger0.is";
connectAttr "RightPinkyFinger0.s" "RightPinkyFinger1.is";
connectAttr "RightPinkyFinger1.s" "RightPinkyFinger2.is";
// End of skeleton_biped_male_A.ma
