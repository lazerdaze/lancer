//Maya ASCII 2018 scene
//Name: skeleton_biped_T_advanced.ma
//Last modified: Fri, May 04, 2018 12:21:48 AM
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
	rename -uid "F7527E77-4A8B-A442-D7BA-9394114B4671";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.68921241550394829 1.1733940818746784 1.6772928955838169 ;
	setAttr ".r" -type "double3" -21.338352729600118 21.400000000003239 8.5401826272819294e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "073DC20F-49AF-9488-5F2F-A6A8C3B387DD";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 1.9146785699930045;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -0.017740554231963523 -1.0408340855860843e-17 0.13200860796302746 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "380BFB04-49E5-1CA3-D695-9A89A99C1BBF";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "F3BBC445-4E37-CF1F-0757-08A4F4DA533F";
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
	rename -uid "B049D09E-4FC2-0B2C-BBF5-FBA127AD321E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "3B7150C5-47FA-D2A5-1F6D-3283A7F07AA7";
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
	rename -uid "BCF0E191-4A9D-A73E-AA9C-2B930D160460";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "B74E0196-470B-6A7A-1AFD-FD8F8ED38B52";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode joint -n "CenterRoot";
	rename -uid "86058192-4DB9-AB79-77CF-6BB6693437AB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 -0.017581218285945985 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".typ" 1;
	setAttr ".radi" 0.05;
createNode joint -n "CenterCOG" -p "CenterRoot";
	rename -uid "052E9AAA-40CA-63E0-F98A-7E9E987C607D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.3957348043445609e-17 0.64016164271386466 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -1.0313815813703893e-16 4.7304898132489202 0 1;
	setAttr ".typ" 1;
	setAttr ".otp" -type "string" "COG";
	setAttr ".radi" 0.05;
createNode joint -n "CenterSpine0" -p "CenterCOG";
	rename -uid "F0B053D2-4316-2901-4787-D18DD46EF4D5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 90 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.1102230246251565e-16 0.99979899429505004 -0.020049214613207023 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 3.4694469519536142e-18 0.020049214613207023 0.99979899429505004 0
		 -1.0313815813703893e-16 4.7304898132489202 0 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.05;
createNode joint -n "CenterSpine0Bind0" -p "CenterSpine0";
	rename -uid "F8A453BB-419E-5A1A-CD48-51A81A94357A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.1102230246251565e-16 -2.4651903288156619e-32 3.7560708472103691e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.1102230246251565e-16 0.99979899429505004 -0.020049214613207023 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 3.4694469519536142e-18 0.020049214613207023 0.99979899429505004 0
		 -1.0313815813703863e-16 4.730489813248921 2.3817715128492132e-17 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "CenterSpine1" -p "CenterSpine0";
	rename -uid "241D352F-496A-173B-43A1-2AA435EB0711";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.057613679917282168 7.8726149284826742e-18 -1.8780354236051845e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.1038231075172249e-16 0.9949371291047574 -0.10049929914573133 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 1.2398958800677588e-17 0.10049929914573133 0.9949371291047574 0
		 -1.2495515916416499e-16 5.5817940010986531 -0.017071411814487479 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.05;
createNode joint -n "CenterSpine1Bind0" -p "CenterSpine1";
	rename -uid "1C7B0D58-48E3-7C48-CD94-69A01ED53EB7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.5501049877595392e-09 5.9372193616639727e-25 4.2749583626545976e-10 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.1038231075172249e-16 0.9949371291047574 -0.10049929914573133 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 1.2398958800677588e-17 0.10049929914573133 0.9949371291047574 0
		 -1.2495516061659574e-16 5.5817940275168976 -0.017071411307947332 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "CenterSpine2" -p "CenterSpine1";
	rename -uid "80250882-4296-75CF-D524-5C954F28D86C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.057613679917282279 7.8726149284826742e-18 -1.8780354236051845e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.1038231075172249e-16 0.9949371291047574 -0.10049929914573133 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 1.2398958800677588e-17 0.10049929914573133 0.9949371291047574 0
		 -1.2495515916416499e-16 5.5817940010986531 -0.017071411814487479 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.05;
createNode joint -n "CenterSpine2Bind0" -p "CenterSpine2";
	rename -uid "14D74B1A-4FEA-5CDA-AE55-7E8B359783F5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.5501049877595392e-09 5.9372193616639727e-25 4.2749583626545976e-10 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.1038231075172249e-16 0.9949371291047574 -0.10049929914573133 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 1.2398958800677588e-17 0.10049929914573133 0.9949371291047574 0
		 -1.2495516061659574e-16 5.5817940275168976 -0.017071411307947332 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "CenterSpine3" -p "CenterSpine2";
	rename -uid "307C4661-4996-0064-E109-7F8DD3D0C9FC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.048034743598050711 -3.5739520789966003e-18 7.5121416944207382e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.1038231075172249e-16 0.9949371291047574 -0.10049929914573133 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 1.2398958800677588e-17 0.10049929914573133 0.9949371291047574 0
		 -1.2495515916416499e-16 5.5817940010986531 -0.017071411814487479 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.05;
createNode joint -n "CenterSpine3Bind0" -p "CenterSpine3";
	rename -uid "7F13ECD4-453C-843A-0CE8-A39BE013643E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 5.9372193616639727e-25 4.2749583626545976e-10 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.1038231075172249e-16 0.9949371291047574 -0.10049929914573133 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 1.2398958800677588e-17 0.10049929914573133 0.9949371291047574 0
		 -1.2495516061659574e-16 5.5817940275168976 -0.017071411307947332 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "CenterSpine4" -p "CenterSpine3";
	rename -uid "D395A19F-4F01-6A2F-A2DF-05B699B49D41";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0.048034743598050822 -3.5739520789966003e-18 7.5121416944207382e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.0656500788582773e-16 0.96248033785653608 -0.27135143124658129 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 3.133508896627239e-17 0.27135143124658129 0.96248033785653608 0
		 -7.304422013375937e-17 6.2881076095445021 -0.088416646150823425 1;
	setAttr ".typ" 6;
	setAttr ".radi" 0.05;
createNode joint -n "CenterSpine5" -p "CenterSpine4";
	rename -uid "CC4D43C8-484E-9D6F-AC24-328088A641D7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.10252708495754392 2.8066375649485767e-17 -2.1033996744378068e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.0635046211846882e-16 0.95416341629659751 0.2992861089345879 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 -3.2055700170466698e-17 -0.2992861089345879 0.95416341629659751 0
		 -1.1896845951857058e-16 7.0173080781608741 -0.29399964150363439 1;
	setAttr ".typ" 7;
	setAttr ".radi" 0.05;
createNode joint -n "CenterSpine5Bind0" -p "CenterSpine5";
	rename -uid "F288E4E2-4207-DAE1-B1DF-EB85B2B489E8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.6286079929095365e-08 -3.8267951400619483e-24 5.4175162014820146e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.0635046211846882e-16 0.95416341629659751 0.2992861089345879 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 -3.2055700170466698e-17 -0.2992861089345879 0.95416341629659751 0
		 -1.1896844382132259e-16 7.0173079513494825 -0.29399963932373796 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "CenterHead" -p "CenterSpine5";
	rename -uid "BE71F8FF-494D-B035-AAFE-CC949C192D62";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.053199462767419936 3.2684220623969304e-18 6.0097133555365906e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.0635046211846882e-16 0.95416341629659751 0.2992861089345879 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 -3.2055700170466698e-17 -0.2992861089345879 0.95416341629659751 0
		 -6.547195594559847e-17 7.392407565802829 -0.1763446735994551 1;
	setAttr ".typ" 8;
	setAttr ".radi" 0.05;
createNode joint -n "CenterHeadBind0" -p "CenterHead";
	rename -uid "0148D6B5-4F21-3C72-BE15-C891A69CDFF6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.2249531328455419e-08 -5.0986751537435581e-18 -6.2406368316116181e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.0635046211846882e-16 0.95416341629659751 0.2992861089345879 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 -3.2055700170466698e-17 -0.2992861089345879 0.95416341629659751 0
		 -6.5471975055046205e-17 7.392407736481803 -0.17634466839436042 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "CenterSpine4Bind0" -p "CenterSpine4";
	rename -uid "21BFFFBB-43BF-1A65-197A-FCA2A731AE73";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.3306690738754696e-16 4.9303806576313238e-32 -1.2019426711073181e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 1.0656500788582773e-16 0.96248033785653608 -0.27135143124658129 0
		 -1 1.1102230246251565e-16 1.7347234759768071e-18 0 3.133508896627239e-17 0.27135143124658129 0.96248033785653608 0
		 -7.3044220133759801e-17 6.2881076095445039 -0.088416646150824757 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmCollar" -p "CenterSpine4";
	rename -uid "A6721F18-43F5-7B73-BA90-67811F90E9F1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.040709496805691137 -0.017772618170804121 -0.0047057949765326951 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -89.999999999999986 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.97305201972346023 0 -0.23058570404969816 0 -1.1097505889215843e-16 1.0000000000000002 -5.5511151231257827e-17 0
		 0.23058570404969822 5.5511151231257827e-17 0.97305201972346 0 0.13133118825323004 6.5682087431419998 -0.20351450736092658 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmCollarBind0" -p "LeftArmCollar";
	rename -uid "0EEA7B91-41E0-597D-B54F-8CBE39259D83";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -1.1102230246251565e-16 1.2056328158038809e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.97305201972346023 0 -0.23058570404969816 0 -1.1097505889215843e-16 1.0000000000000002 -5.5511151231257827e-17 0
		 0.23058570404969822 5.5511151231257827e-17 0.97305201972346 0 0.13133118825323017 6.5682087431419998 -0.20351450736092569 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmShoulder" -p "LeftArmCollar";
	rename -uid "606ED914-421E-4E24-1E16-D9963C5B78A0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.094791486423624213 -2.2204460492503131e-16 1.2056328158038809e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.7119945091961758 -0.70072897459233585 -0.045196493683368158 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 0.06335120101038072 8.0622012025724807e-15 0.99799129521782015 0
		 0.81291906172835171 6.5682087431419989 -0.36503148332040558 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmElbow" -p "LeftArmShoulder";
	rename -uid "09C054B1-41F9-B080-CE96-12BBC9FE6536";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0.14384821153945868 1.4432899320127035e-15 7.8062556418956319e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782216 -0.68973772012602541 0.1315805042892606 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 1.5697477294632858 5.8233549985777255 -0.41307399159661645 1;
	setAttr ".sd" 1;
	setAttr ".typ" 11;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmElbowBind0" -p "LeftArmElbow";
	rename -uid "A0102CEE-4950-5790-DCC6-C6B10CAF2F2C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.27675647831893e-15 -3.3306690738754696e-16 -8.2399365108898337e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782216 -0.68973772012602541 0.1315805042892606 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 1.5697477294632887 5.8233549985777175 -0.41307399159661579 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmElbowBind2" -p "LeftArmElbow";
	rename -uid "CC8688CD-4697-3153-5C39-97B6D4B5C886";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.071390534091226754 -0.00028628296748334225 1.0091089894248562e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782216 -0.68973772012602541 0.1315805042892606 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 1.9438798689384276 5.4579801779158599 -0.34356509123075385 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmHand" -p "LeftArmElbow";
	rename -uid "BEA03427-4328-BAE2-C9D5-9485027D4F02";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0.14278106818245329 -0.00057256593496646246 2.0182179802808592e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.66440249694361053 -0.73522428745423385 0.1342183638423228 0
		 0.74469336950618259 0.66645500513450662 -0.035630205510113158 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 2.318012008413568 5.0926053572539951 -0.27405619086489036 1;
	setAttr ".sd" 1;
	setAttr ".typ" 12;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmMiddleFinger0" -p "LeftArmHand";
	rename -uid "57193313-49DB-F341-BC4A-8C943CC538E5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.063280099032483661 0 0.0046845435479171442 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.37445221034305071 -0.90939875232994727 0.18105096362610004 0
		 0.86402614152767931 0.41306881781095889 0.28780718981472242 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.618713781902053 4.7461154051879859 -0.17664051722583043 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmMiddleFinger1" -p "LeftArmMiddleFinger0";
	rename -uid "8C5157A0-4764-52E7-8D73-AEA06C5A40BC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.029955362563816423 0 -3.7560829013044694e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.01142141538714897 -0.99837948880152516 0.05574896959549859 0
		 0.94160776459445139 0.029501446191894265 0.33541687841852452 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.7016009767525628 4.5448146530516302 -0.13656382363067343 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmMiddleFinger2" -p "LeftArmMiddleFinger1";
	rename -uid "7F902915-4FD1-60C6-C9CC-5B972807A80D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.023669434836487924 0 -9.0144634378591659e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.01142141538714897 -0.99837948880152516 0.05574896959549859 0
		 0.94160776459445139 0.029501446191894265 0.33541687841852452 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.7035986491926174 4.370192233509953 -0.1268130023578857 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmThumb0" -p "LeftArmHand";
	rename -uid "85E41ED9-4EF1-FC85-19CE-5DBCE4387A33";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.011811448304917038 0 0.017064293370491337 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90 -45 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.11810587762855372 -0.83466938998200524 0.5379386685270513 0
		 -0.23443662107677021 0.54985384016060734 0.80168586438750478 0 -0.96493029404599817 -0.031428711200126289 -0.26061804186318932 0
		 2.3104967149926043 4.9925381467033825 -0.13471373314552587 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmThumb1" -p "LeftArmThumb0";
	rename -uid "85E12359-4644-2FE0-7926-8584CAD9EA8F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.035241891747225029 -4.9960036108132044e-16 -4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.025153871789096463 -0.97716859625079389 0.21097112891405528 0
		 -0.26129831680728782 0.21012798626920759 0.94210902714076916 0 -0.96493029404599817 -0.031428711200126289 -0.26061804186318932 0
		 2.279739487342062 4.775172872797544 0.0053766876035133138 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmThumb2" -p "LeftArmThumb1";
	rename -uid "8D74180C-4994-AA79-191D-95A825C83C51";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.022815631952767979 -5.5511151231257827e-17 2.2204460492503131e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.025153871789096463 -0.97716859625079389 0.21097112891405528 0
		 -0.26129831680728782 0.21012798626920759 0.94210902714076916 0 -0.96493029404599817 -0.031428711200126289 -0.26061804186318932 0
		 2.2754986285836001 4.6104255116497388 0.040945715200510019 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmRingFinger0" -p "LeftArmHand";
	rename -uid "2F2BCB67-424C-03CD-0CBC-898AB660D288";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.060807550654815801 0 -0.01412598522019708 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.39895292243837926 -0.91675711659422954 0.01982308885393691 0
		 0.91549560634568683 0.39944375549094641 0.048088262196011998 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.6352499107880449 4.7601588327315936 -0.31769820346088251 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmRingFinger1" -p "LeftArmRingFinger0";
	rename -uid "A306E29F-4866-A21B-3F90-28B0C314FADE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.027536885863333638 0 2.3939183968479938e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.096004506833477832 -0.9953729992529331 0.0039657314434298884 0
		 0.99402151597842237 0.096080783641149192 0.051862402440130614 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.7164306381824965 4.5736129888904449 -0.31366451256188488 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmRingFinger2" -p "LeftArmRingFinger1";
	rename -uid "A193C9E3-4735-9822-1A9B-1DBE5986A125";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.023612079626297133 0 -1.1102230246251565e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.096004506833477832 -0.9953729992529331 0.0039657314434298884 0
		 0.99402151597842237 0.096080783641149192 0.051862402440130614 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.7331816993029254 4.3999382886284364 -0.31297256369420051 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmIndexFinger0" -p "LeftArmHand";
	rename -uid "76D0757F-4FB9-82EB-1016-958995388986";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.059555715616277483 0 0.019830647721849434 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33586554333643248 -0.89175006831631209 0.30327570370403234 0
		 0.77282429731831681 0.4449626700159679 0.45249400854233496 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.5525955922138412 4.743714447219582 -0.067546450606751435 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmIndexFinger1" -p "LeftArmIndexFinger0";
	rename -uid "A31D0C4B-4D55-B839-08D2-339E9FF70317";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.029095255917497398 0 9.0205620750793969e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6248067147488707 4.551988100973607 -0.0023421465732985092 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmIndexFinger2" -p "LeftArmIndexFinger1";
	rename -uid "6C2180E7-4765-BD0B-8829-45958D4FC222";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.022681471317921753 0 -6.0715321659188248e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6247826867638016 4.3851846204334235 0.014032435983179822 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmPinkyFinger0" -p "LeftArmHand";
	rename -uid "707315BC-437E-A535-26CF-3AAA0A855F1A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.058063808018648078 0 -0.031268954740110502 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33127684384618067 -0.92729159809668693 -0.1743156471192594 0
		 0.93121877117526597 0.35107632841835718 -0.097862208411182511 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.629090201304674 4.7587767521231896 -0.44583689027085693 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmPinkyFinger1" -p "LeftArmPinkyFinger0";
	rename -uid "405B177A-49AA-D80C-61AA-8E91195025BA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.021135567955946122 0 3.8857805861880479e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.14108966550627738 -0.98402387587804507 -0.10858507258954506 0
		 0.97826706647274286 -0.12174279435913848 -0.16784587774635135 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.6808296105534977 4.613950693863611 -0.47306181942697717 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmPinkyFinger2" -p "LeftArmPinkyFinger1";
	rename -uid "2C1484BA-4F38-21A6-BC2F-418FDDE436D1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.017955846740206949 0 -1.0408340855860843e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.14108966550627738 -0.98402387587804507 -0.10858507258954506 0
		 0.97826706647274286 -0.12174279435913848 -0.16784587774635135 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.6621091056886419 4.4833853282898861 -0.48746944717468027 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
	setAttr ".radi" 0.05;
createNode joint -n "LeftArmHandBind0" -p "LeftArmHand";
	rename -uid "81560A34-4967-DC80-F9A7-94B8A9613E13";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.7208456881689926e-15 8.8817841970012523e-16 4.5102810375396984e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.66440249694361053 -0.73522428745423385 0.1342183638423228 0
		 0.74469336950618259 0.66645500513450662 -0.035630205510113158 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 2.3180120084135649 5.0926053572540093 -0.2740561908648918 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmElbowBind1" -p "LeftArmElbow";
	rename -uid "29EEA307-4742-6F96-A396-65A4672AF9AC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.035695267045613988 -0.00028628296748334225 1.0091089894248562e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782216 -0.68973772012602541 0.1315805042892606 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 1.9438798689384276 5.4579801779158599 -0.34356509123075385 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmElbowBind3" -p "LeftArmElbow";
	rename -uid "01EB64A9-40FB-EBF1-0440-18ADF6EAEDD4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.10708580113683919 -0.00028628296748334225 1.0091089894248562e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782216 -0.68973772012602541 0.1315805042892606 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 1.9438798689384276 5.4579801779158599 -0.34356509123075385 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmShoulderBind0" -p "LeftArmShoulder";
	rename -uid "29BC6979-4F67-35B9-294F-15B103E1189E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.3877787807814457e-17 1.2212453270876722e-15 7.5460471204991109e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.7119945091961758 -0.70072897459233585 -0.045196493683368158 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 0.06335120101038072 8.0622012025724807e-15 0.99799129521782015 0
		 0.81291906172835737 6.5682087431420033 -0.36503148332040553 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmShoulderBind2" -p "LeftArmShoulder";
	rename -uid "61383CD9-4FFA-50EB-CC53-3EBDE863FB11";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.071924105769729157 9.9920072216264089e-16 5.9847959921199845e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.7119945091961758 -0.70072897459233585 -0.045196493683368158 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 0.06335120101038072 8.0622012025724807e-15 0.99799129521782015 0
		 1.1913333955958183 6.1957818708598635 -0.38905273745851066 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmShoulderBind1" -p "LeftArmShoulder";
	rename -uid "532F7B0F-4165-A6DE-8E5B-309C9CF19CE8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.035962052884864593 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.7119945091961758 -0.70072897459233585 -0.045196493683368158 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 0.06335120101038072 8.0622012025724807e-15 0.99799129521782015 0
		 1.1913333955958183 6.1957818708598635 -0.38905273745851066 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftArmShoulderBind3" -p "LeftArmShoulder";
	rename -uid "06A07001-4795-3AC6-93E6-E6978A95283B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.10788615865459456 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.7119945091961758 -0.70072897459233585 -0.045196493683368158 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 0.06335120101038072 8.0622012025724807e-15 0.99799129521782015 0
		 1.1913333955958183 6.1957818708598635 -0.38905273745851066 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightArmCollar" -p "CenterSpine4";
	rename -uid "BF724C16-4C81-E8D1-801D-C987981A8605";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.040709795710326957 0.01777263101651156 -0.0047056545031013072 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 -89.999999999999986 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.97305201972346023 -6.2450045135165055e-17 0.2305857040496983 0
		 -1.110695460328729e-16 -1 4.9960036108132044e-16 0 0.23058570404969828 -4.9960036108132044e-16 -0.97305201972346034 0
		 -0.13133128317689327 6.5682111507043466 -0.20351410762673294 1;
	setAttr ".sd" 2;
	setAttr ".typ" 9;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmShoulder" -p "RightArmCollar";
	rename -uid "64F4574E-4FC7-11DB-FA60-7F9A60722B88";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.094791427131955153 5.5511151231257827e-16 2.2504468665321409e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71199450919617557 0.70072897459233585 0.045196493683368102 0
		 0.69932141695006 -0.71342757457696682 0.044392022123202271 0 0.063351201010380331 -7.7053258005012518e-15 -0.99799129521782048 0
		 -0.81291869197593458 6.5682111507043421 -0.36503114437397 1;
	setAttr ".sd" 2;
	setAttr ".typ" 10;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmElbow" -p "RightArmShoulder";
	rename -uid "293FB292-4946-A481-6D37-668F9BB1BF54";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -0.14384856506839297 -3.5380437990450986e-07 -2.0866556251983304e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782183 0.68973772012602552 -0.13158050428926046 0
		 0.69932141695006 -0.71342757457696682 0.044392022123202271 0 -0.06325430790565964 -0.12362432312687886 -0.99031102147900874 0
		 -1.5697510578392362 5.823357440766137 -0.41307373289833127 1;
	setAttr ".sd" 2;
	setAttr ".typ" 11;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmHand" -p "RightArmElbow";
	rename -uid "DCC6D08D-4EBD-7D02-15AA-15AE3B7BAD61";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -0.14278075696968096 0.00057348827552061721 -1.4371694821713188e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.66440249694361209 0.73522428745423229 -0.13421836384232258 0
		 0.74469336950618115 -0.66645500513450828 0.035630205510113075 0 -0.06325430790565964 -0.12362432312687886 -0.99031102147900874 0
		 -2.3180089602097551 5.092604470083737 -0.27405635741039258 1;
	setAttr ".sd" 2;
	setAttr ".typ" 12;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmPinkyFinger0" -p "RightArmHand";
	rename -uid "6D1E085B-49DB-6E5A-D39B-A9A1B2197DFC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.058063310777046406 0 0.031268844057266119 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.3312768438461805 0.92729159809668671 0.17431564711925923 0
		 0.93121877117526586 -0.35107632841835695 0.097862208411181567 0 0.15194490100737507 0.12990651917274454 -0.97981480052828396 0
		 -2.6290865255371276 4.7587803370098092 -0.44583682926924112 1;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmPinkyFinger1" -p "RightArmPinkyFinger0";
	rename -uid "7A769AE4-42D7-5AE6-EDDE-988F6DBDA2EE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.021136257089846344 0 -1.0280906578147286e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.14108966550627799 0.98402387587804474 0.10858507258954529 0
		 0.97826706647274264 0.12174279435913904 0.16784587774635046 0 0.15194490100737507 0.12990651917274454 -0.97981480052828396 0
		 -2.6808302505083841 4.6139504054796019 -0.47306216585446775 1;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmPinkyFinger2" -p "RightArmPinkyFinger1";
	rename -uid "838D2501-4389-61B8-419F-C3BE50A0CFB2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.017955784970935917 0 -4.1167895585558778e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.14108966550627799 0.98402387587804474 0.10858507258954529 0
		 0.97826706647274264 0.12174279435913904 0.16784587774635046 0 0.15194490100737507 0.12990651917274454 -0.97981480052828396 0
		 -2.6621112935672939 4.4833852706718105 -0.48746969257284534 1;
	setAttr ".sd" 2;
	setAttr ".typ" 22;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmIndexFinger0" -p "RightArmHand";
	rename -uid "CB21B0F1-465C-B4FC-89D6-7FACBCE4BA4D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.059556104012470357 0 -0.019830615779080352 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33586554333643237 0.89175006831631209 -0.30327570370403245 0
		 0.77282429731831681 -0.4449626700159679 -0.45249400854233501 0 -0.5384579299014669 -0.082401686573235239 -0.83861374885945783 0
		 -2.5525947317265727 4.7437116587009633 -0.067546478414484967 1;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmIndexFinger1" -p "RightArmIndexFinger0";
	rename -uid "87D41E98-4B37-13F9-155D-8CA98EB49607";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.029095130131174651 0 -9.8846175642167133e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280883553 0.99521616621410469 -0.097697297577012593 0
		 0.84265238216834049 -0.052485660479655971 -0.53589384981546062 0 -0.5384579299014669 -0.082401686573235239 -0.83861374885945783 0
		 -2.6248046256584052 4.5519859003380523 -0.002342150016423919 1;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmIndexFinger2" -p "RightArmIndexFinger1";
	rename -uid "A2C8AC6D-42E0-14A4-AA48-CF89345C76AE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.022680628706698014 0 -1.0941634582574411e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280883553 0.99521616621410469 -0.097697297577012593 0
		 0.84265238216834049 -0.052485660479655971 -0.53589384981546062 0 -0.5384579299014669 -0.082401686573235239 -0.83861374885945783 0
		 -2.6247800170384115 4.3851886740277122 0.014032409320955754 1;
	setAttr ".sd" 2;
	setAttr ".typ" 19;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmHandBind0" -p "RightArmHand";
	rename -uid "F852457A-4517-F568-B7CF-508A939ED894";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -8.8817841970012523e-16 -6.7654215563095477e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.66440249694361209 0.73522428745423229 -0.13421836384232258 0
		 0.74469336950618115 -0.66645500513450828 0.035630205510113075 0 -0.06325430790565964 -0.12362432312687886 -0.99031102147900874 0
		 -2.3180089602097587 5.0926044700837387 -0.27405635741039203 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightArmRingFinger0" -p "RightArmHand";
	rename -uid "50312D8A-4D5C-FDC2-42D1-FB90451ED635";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.060807510174012369 0 0.014125941869420599 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.39895292243837904 0.91675711659422954 -0.019823088853937035 0
		 0.91549560634568672 -0.39944375549094646 -0.048088262196011047 0 -0.052003465650089689 0.0010370019881021791 -0.9986463659310324 0
		 -2.635246883408628 4.7601584197294002 -0.31769810439273061 1;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmRingFinger1" -p "RightArmRingFinger0";
	rename -uid "E2259E3B-4B3B-CCCD-81E6-9395D60B6C5C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.027536519218047228 0 6.8179481203106684e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.096004506833477332 0.9953729992529331 -0.0039657314434302839 0
		 0.99402151597842214 -0.096080783641148859 -0.051862402440129747 0 -0.052003465650089689 0.0010370019881021791 -0.9986463659310324 0
		 -2.7164307207644507 4.5736168773116175 -0.31366475157593215 1;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmRingFinger2" -p "RightArmRingFinger1";
	rename -uid "EFBB7F13-4BC8-C31B-4AA9-82979722A811";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.023612707560021706 0 -5.6746139249358452e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.096004506833477332 0.9953729992529331 -0.0039657314434302839 0
		 0.99402151597842214 -0.096080783641148859 -0.051862402440129747 0 -0.052003465650089689 0.0010370019881021791 -0.9986463659310324 0
		 -2.7331809881061302 4.3999374402766618 -0.31297242906680495 1;
	setAttr ".sd" 2;
	setAttr ".typ" 21;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmThumb0" -p "RightArmHand";
	rename -uid "05FE1A89-4210-BD13-2535-0ABF9238C5CA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.011811554394750901 0 -0.017064363498293482 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90 -45 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.11810587762855382 0.83466938998200513 -0.53793866852705141 0
		 -0.23443662107676935 -0.54985384016060712 -0.80168586438750522 0 -0.96493029404599817 0.031428711200125851 0.26061804186318871 0
		 -2.3104951282386632 4.9925376183202044 -0.1347133278512182 1;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmThumb1" -p "RightArmThumb0";
	rename -uid "1C871FFC-4DE9-2CFF-596D-53A2F6FC4B43";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.035242089063025395 3.9002180818314969e-07 5.8230812405302146e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.025153871789096963 0.97716859625079366 -0.21097112891405556 0
		 -0.26129831680728705 -0.21012798626920781 -0.94210902714076949 0 -0.96493029404599817 0.031428711200125851 0.26061804186318871 0
		 -2.2797425561211533 4.7751696779249295 0.0053766881649595921 1;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmThumb2" -p "RightArmThumb1";
	rename -uid "A04575F7-4C67-14F4-EA06-1E9923E5B558";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.022815519018816288 -2.4294212530584502e-08 -1.1728040760772274e-10 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.025153871789096963 0.97716859625079366 -0.21097112891405556 0
		 -0.26129834556445064 -0.21012798533255914 -0.94210901937374614 0 -0.96493028625870103 0.031428717462427827 0.26061806994022557 0
		 -2.2755016706090836 4.6104231699473193 0.040945708604674301 1;
	setAttr ".sd" 2;
	setAttr ".typ" 14;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmMiddleFinger0" -p "RightArmHand";
	rename -uid "3AE57E3C-4EB9-FAEA-FD46-53AC7C39534E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.063279965452830877 0 -0.0046845617778567394 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.37445221034305021 0.90939875232994727 -0.18105096362610013 0
		 0.86402614152767954 -0.41306881781095856 -0.28780718981472225 0 -0.33651800683766475 -0.048662727142982878 -0.94041882693883461 0
		 -2.6187098907735527 4.7461151005869127 -0.17664067430739996 1;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmMiddleFinger1" -p "RightArmMiddleFinger0";
	rename -uid "52D1EB5B-45F9-7E9A-24A0-D0B28AE48F3E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.02995523281685708 0 1.038140026622302e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.011421415387148359 0.99837948880152494 -0.055748969595498743 0
		 0.94160776459445139 -0.029501446191893987 -0.33541687841852436 0 -0.33651800683766475 -0.048662727142982878 -0.94041882693883461 0
		 -2.7015999257822072 4.5448165890468566 -0.13656389607466587 1;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmMiddleFinger2" -p "RightArmMiddleFinger1";
	rename -uid "B2C33189-4FFA-1BA5-5912-F6A68D46C5DB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.023669487265570388 0 1.8501446764095152e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.011421415387148359 0.99837948880152494 -0.055748969595498743 0
		 0.94160776459445139 -0.029501446191893987 -0.33541687841852436 0 -0.33651800683766475 -0.048662727142982878 -0.94041882693883461 0
		 -2.7036014268749429 4.3701938215788516 -0.12681314054623599 1;
	setAttr ".sd" 2;
	setAttr ".typ" 20;
	setAttr ".radi" 0.05;
createNode joint -n "RightArmElbowBind0" -p "RightArmElbow";
	rename -uid "8BA1C7DD-4272-F8C8-ADCD-6AA757AE5707";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 0 -2.1423834928313568e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782183 0.68973772012602552 -0.13158050428926046 0
		 0.69932141695006 -0.71342757457696682 0.044392022123202271 0 -0.06325430790565964 -0.12362432312687886 -0.99031102147900874 0
		 -1.5697510578392371 5.8233574407661388 -0.41307373289832983 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightArmElbowBind2" -p "RightArmElbow";
	rename -uid "39EEA376-49AB-44EB-7715-0292D105FB43";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.071390366126785842 0.000287528261409431 -3.8351066334804673e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782183 0.68973772012602552 -0.13158050428926046 0
		 0.69932141695006 -0.71342757457696682 0.044392022123202271 0 -0.06325430790565964 -0.12362432312687886 -0.99031102147900874 0
		 -1.9438759075878318 5.4579768539882707 -0.3435650451543612 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode transform -n "transform3" -p "RightArmElbow";
	rename -uid "6F770CA5-4B08-CD92-C48F-41B72B992FBF";
	setAttr ".t" -type "double3" 0.25641262321685965 0.87458742097329101 -0.004705656141013816 ;
	setAttr ".r" -type "double3" 0 0 180 ;
	setAttr ".s" -type "double3" 1 1 -1 ;
createNode joint -n "RightArmElbowBind1" -p "transform3";
	rename -uid "19DC3F6B-47E6-FB77-BACB-57A988593251";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.29210758317950103 0.87430048529679372 -0.004705694065633613 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782216 -0.68973772012602541 0.1315805042892606 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 1.9438798689384276 5.4579801779158599 -0.34356509123075385 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode transform -n "transform4" -p "RightArmElbow";
	rename -uid "D8D4C9A9-440A-C0B1-ABC2-EBBA7210816B";
	setAttr ".t" -type "double3" 0.25641262321685965 0.87458742097329101 -0.004705656141013816 ;
	setAttr ".r" -type "double3" 0 0 180 ;
	setAttr ".s" -type "double3" 1 1 -1 ;
createNode joint -n "RightArmElbowBind3" -p "transform4";
	rename -uid "E9296BA5-42B1-273E-EFB9-1AB5EA3D128A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.36349811727072623 0.87430048529679372 -0.004705694065633613 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71200312381782216 -0.68973772012602541 0.1315805042892606 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 -0.063254307905659474 0.12362432312687939 0.9903110214790084 0
		 1.9438798689384276 5.4579801779158599 -0.34356509123075385 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightArmShoulderBind0" -p "RightArmShoulder";
	rename -uid "681E9558-468F-3741-449D-D2BFADAAF2CC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -4.8572257327350599e-16 -1.2212453270876722e-15 6.7654215563095477e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71199450919617557 0.70072897459233585 0.045196493683368102 0
		 0.69932141695006 -0.71342757457696682 0.044392022123202271 0 0.063351201010380331 -7.7053258005012518e-15 -0.99799129521782048 0
		 -0.81291869197594202 6.5682111507043457 -0.36503114437397088 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightArmShoulderBind2" -p "RightArmShoulder";
	rename -uid "CB4D3ACF-4F11-363A-8E93-FDB5793EE6BA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.071924401088533457 -2.9334632856148346e-07 -2.0981898238812968e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.71199450919617557 0.70072897459233585 0.045196493683368102 0
		 0.69932141695006 -0.71342757457696682 0.044392022123202271 0 0.063351201010380331 -7.7053258005012518e-15 -0.99799129521782048 0
		 -1.1913361053385891 6.1957842957352423 -0.38905243863615113 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode transform -n "transform1" -p "RightArmShoulder";
	rename -uid "3256D62D-4E25-DD5C-36F8-F3A159ADF5F6";
	setAttr ".t" -type "double3" 0.11256405814846668 0.8745870671689111 -0.004705677007570068 ;
	setAttr ".r" -type "double3" 0 0 180 ;
	setAttr ".s" -type "double3" 1 1 -1 ;
createNode joint -n "RightArmShoulderBind3" -p "transform1";
	rename -uid "D1CA38B6-4CB7-0664-1546-178013271741";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.22045026324902292 0.87458676826427562 -0.0047057949765325633 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.7119945091961758 -0.70072897459233585 -0.045196493683368158 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 0.06335120101038072 8.0622012025724807e-15 0.99799129521782015 0
		 1.1913333955958183 6.1957818708598635 -0.38905273745851066 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode transform -n "transform2" -p "RightArmShoulder";
	rename -uid "C121F624-4CB4-8BA7-4885-12A6780088C2";
	setAttr ".t" -type "double3" 0.11256405814846668 0.8745870671689111 -0.004705677007570068 ;
	setAttr ".r" -type "double3" 0 0 180 ;
	setAttr ".s" -type "double3" 1 1 -1 ;
createNode joint -n "RightArmShoulderBind1" -p "transform2";
	rename -uid "9BFB6DDD-40F1-0F33-1BE6-5E8F86F78228";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.14852615747929296 0.87458676826427562 -0.0047057949765325633 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.7119945091961758 -0.70072897459233585 -0.045196493683368158 0
		 0.69932141695005978 0.71342757457696704 -0.044392022123202729 0 0.06335120101038072 8.0622012025724807e-15 0.99799129521782015 0
		 1.1913333955958183 6.1957818708598635 -0.38905273745851066 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightArmCollarBind0" -p "RightArmCollar";
	rename -uid "70E95820-4962-5206-A011-B19676D54168";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.7347234759768071e-17 5.5511151231257827e-16 -7.5460471204991109e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.97305201972346023 -6.2450045135165055e-17 0.2305857040496983 0
		 -1.110695460328729e-16 -1 4.9960036108132044e-16 0 0.23058570404969828 -4.9960036108132044e-16 -0.97305201972346034 0
		 -0.13133128317689333 6.5682111507043421 -0.20351410762673219 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "CenterHip" -p "CenterCOG";
	rename -uid "69C1E02D-4957-8B88-000D-D688789FDE72";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 2.2204460492503131e-16 1 0 0 -1 2.2204460492503131e-16 0 0
		 0 0 1 0 -1.0313815813703893e-16 4.7304898132489202 0 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegHip" -p "CenterHip";
	rename -uid "A1D4F741-492B-35AD-D798-00B9562BBCD1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.053038488960513989 -0.027861754627403257 -0.0070961645183506214 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 0 90 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593302 0.98737947534752035 0 0 0.98179675697694502 -0.15747680786670104 0.10618937316731988 0
		 0.10484920756543037 -0.01681745065607796 -0.99434592422674117 0 -0.39192918631329426 4.5246047091595409 -0.052437277911385576 1;
	setAttr ".sd" 2;
	setAttr ".typ" 2;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegKnee" -p "RightLegHip";
	rename -uid "BF31B4F5-4F36-5B72-A300-33AB4966D629";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -0.29037262145467985 -9.2326273327947295e-08 -9.8598173046277049e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757777 0.98535134714841321 0.082789661117107824 0
		 0.98179675697694502 -0.15747680786670104 0.10618937316731988 0 0.11767129346035228 0.065450574152726287 -0.9908933792484671 0
		 -0.73175166177217843 2.4059694216789218 -0.052437277911385145 1;
	setAttr ".sd" 2;
	setAttr ".typ" 3;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegKneeBind2" -p "RightLegKnee";
	rename -uid "2BE40310-4694-D1D5-C094-538CB14FA6C8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.12633410139734416 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757777 0.98535134714841321 0.082789661117107824 0
		 0.98179676048382236 -0.15747680591612184 0.1061893436363959 0 0.11767126420052876 0.065450578845900859 -0.99089338241315661 0
		 -0.87093645034962086 1.4860957219033666 -0.12972549369145339 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegFoot" -p "RightLegKnee";
	rename -uid "23C05901-41BD-3258-3A72-58A5FC078C99";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -0.25266820279468832 -3.9238995800522369e-07 2.0816681711721685e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -62.776262225551974 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.17284131982600565 0.50896552144784857 -0.84325558174145787 0
		 0.98179675463011684 -0.15747683308720148 0.10618935746390287 0 -0.078746496801923221 -0.84625950217303059 -0.52691920084893418 0
		 -1.0101249113879749 0.56622260014647408 -0.20701397538429972 1;
	setAttr ".sd" 2;
	setAttr ".typ" 4;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegFootBind0" -p "RightLegFoot";
	rename -uid "55AECD42-482B-1185-899A-4E90DF3E6CD9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -2.7408630920433552e-16 9.0205620750793969e-17 5.620504062164855e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.17284131982600565 0.50896552144784857 -0.84325558174145787 0
		 0.98179675152555379 -0.15747686645078487 0.1061893366902362 0 -0.078746535509031226 -0.84625949596454253 -0.52691920503542433 0
		 -1.0101249113879747 0.56622260014646986 -0.20701397538430008 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegToe" -p "RightLegFoot";
	rename -uid "4466A361-4DB0-0211-2841-EC99A3427463";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.11113143888731444 6.1189862238242299e-07 1.2260212463310882e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.17284131982600565 0.50896552144784857 -0.84325558174145787 0
		 0.98179675152555379 -0.15747686645078487 0.1061893366902362 0 -0.078746535509031226 -0.84625949596454253 -0.52691920503542433 0
		 -1.1520592286323765 0.14825503301893078 0.48547505207149538 1;
	setAttr ".sd" 2;
	setAttr ".typ" 5;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegToeBind0" -p "RightLegToe";
	rename -uid "2C6EE0B5-4A5E-DFB8-6B12-DDBD9365C125";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.3877787807814457e-16 7.6327832942979512e-17 9.0205620750793969e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.17284131982600565 0.50896552144784857 -0.84325558174145787 0
		 0.98179674542830853 -0.15747693197556115 0.10618929589156428 0 -0.078746611528281871 -0.84625948377131022 -0.52691921325752555 0
		 -1.1520592286323763 0.14825503301893 0.48547505207149566 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegBigToe0" -p "RightLegToe";
	rename -uid "4C83D6DF-42D9-E1A0-496E-78B97BC5622E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 0.035297807546159535 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.8379659785122067e-14 -27.223737774448029 6.4162580973492658e-15 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33586554333643248 -0.89175006831631209 0.30327570370403234 0
		 0.77282429731831681 0.4449626700159679 0.45249400854233496 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.5525955922138412 4.743714447219582 -0.067546450606751435 1;
	setAttr ".sd" 2;
	setAttr ".typ" 24;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegBigToe1" -p "RightLegBigToe0";
	rename -uid "76955C14-4F46-2CFA-1501-B7A9836B9A15";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.019999999999999976 1.0061396160665481e-16 -1.2186432418736648e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6248067147488707 4.551988100973607 -0.0023421465732985092 1;
	setAttr ".sd" 2;
	setAttr ".typ" 24;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegBigToe2" -p "RightLegBigToe1";
	rename -uid "0D742C4B-4388-B874-7D41-C4A0928482D3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.019999999999999962 -5.2041704279304213e-17 -1.1102230246251791e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6247826867638016 4.3851846204334235 0.014032435983179822 1;
	setAttr ".sd" 2;
	setAttr ".typ" 24;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegIndexToe0" -p "RightLegToe";
	rename -uid "E4374D50-4758-76CD-5EA8-0EA707A96E08";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 0.015299541151940703 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.8379659785122067e-14 -27.223737774448029 6.4162580973492658e-15 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33586554333643248 -0.89175006831631209 0.30327570370403234 0
		 0.77282429731831681 0.4449626700159679 0.45249400854233496 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.5525955922138412 4.743714447219582 -0.067546450606751435 1;
	setAttr ".sd" 2;
	setAttr ".typ" 25;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegIndexToe1" -p "RightLegIndexToe0";
	rename -uid "16ADB7B6-4615-4CB5-2160-DCA38E9DC363";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.019999999999999976 9.7144514654701197e-17 -1.2186432418736664e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6248067147488707 4.551988100973607 -0.0023421465732985092 1;
	setAttr ".sd" 2;
	setAttr ".typ" 25;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegIndexToe2" -p "RightLegIndexToe1";
	rename -uid "7317AF20-480F-60AA-43DB-3ABDABCF6CA3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.019999999999999948 -6.2450045135165055e-17 -1.1102230246251837e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6247826867638016 4.3851846204334235 0.014032435983179822 1;
	setAttr ".sd" 2;
	setAttr ".typ" 25;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegMiddleToe0" -p "RightLegToe";
	rename -uid "79FCA280-4593-3BD9-EE2B-05844DF12D7E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.8379659785122067e-14 -27.223737774448029 6.4162580973492658e-15 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.37445221034305071 -0.90939875232994727 0.18105096362610004 0
		 0.86402614152767931 0.41306881781095889 0.28780718981472242 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.618713781902053 4.7461154051879859 -0.17664051722583043 1;
	setAttr ".sd" 2;
	setAttr ".typ" 26;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegMiddleToe1" -p "RightLegMiddleToe0";
	rename -uid "82614FE9-46F6-194E-B4F0-8085B5A27399";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.019999999999999976 -3.6082248300317588e-16 -7.3985956250412296e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.01142141538714897 -0.99837948880152516 0.05574896959549859 0
		 0.94160776459445139 0.029501446191894265 0.33541687841852452 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.7016009767525628 4.5448146530516302 -0.13656382363067343 1;
	setAttr ".sd" 2;
	setAttr ".typ" 26;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegMiddleToe2" -p "RightLegMiddleToe1";
	rename -uid "2B3ED855-4EB0-0233-7890-068C5A4F8FD2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.019999999999999962 -9.7144514654701197e-17 -1.1102230246251945e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.01142141538714897 -0.99837948880152516 0.05574896959549859 0
		 0.94160776459445139 0.029501446191894265 0.33541687841852452 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.7035986491926174 4.370192233509953 -0.1268130023578857 1;
	setAttr ".sd" 2;
	setAttr ".typ" 26;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegRingToe0" -p "RightLegToe";
	rename -uid "0EE58258-42DD-5B59-8361-F5A35833BDDF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -0.018657091790105801 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.8379659785122067e-14 -27.223737774448029 6.4162580973492658e-15 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.39895292243837926 -0.91675711659422954 0.01982308885393691 0
		 0.91549560634568683 0.39944375549094641 0.048088262196011998 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.6352499107880449 4.7601588327315936 -0.31769820346088251 1;
	setAttr ".sd" 2;
	setAttr ".typ" 27;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegRingToe1" -p "RightLegRingToe0";
	rename -uid "8A449B94-40CE-D477-8C1D-1ABAA429F712";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.019999999999999976 2.4980018054066022e-16 4.961309141293769e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.096004506833477832 -0.9953729992529331 0.0039657314434298884 0
		 0.99402151597842237 0.096080783641149192 0.051862402440130614 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.7164306381824965 4.5736129888904449 -0.31366451256188488 1;
	setAttr ".sd" 2;
	setAttr ".typ" 27;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegRingToe2" -p "RightLegRingToe1";
	rename -uid "880461BB-4EEE-8B80-94F9-7CADC2AD5D4C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.019999999999999976 -1.1102230246251565e-16 -1.1102230246252037e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.096004506833477832 -0.9953729992529331 0.0039657314434298884 0
		 0.99402151597842237 0.096080783641149192 0.051862402440130614 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.7331816993029254 4.3999382886284364 -0.31297256369420051 1;
	setAttr ".sd" 2;
	setAttr ".typ" 27;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegPinkyToe0" -p "RightLegToe";
	rename -uid "5BCAB499-458E-F9B2-29EF-5E84B6D66204";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -0.035800061310019227 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.8379659785122067e-14 -27.223737774448029 6.4162580973492658e-15 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33127684384618067 -0.92729159809668693 -0.1743156471192594 0
		 0.93121877117526597 0.35107632841835718 -0.097862208411182511 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.629090201304674 4.7587767521231896 -0.44583689027085693 1;
	setAttr ".sd" 2;
	setAttr ".typ" 28;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegPinkyToe1" -p "RightLegPinkyToe0";
	rename -uid "DD0B70BC-4874-5E1E-1601-59A623CAAA1F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.019999999999999976 3.8857805861880479e-16 -1.2186432418735539e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.14108966550627738 -0.98402387587804507 -0.10858507258954506 0
		 0.97826706647274286 -0.12174279435913848 -0.16784587774635135 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.6808296105534977 4.613950693863611 -0.47306181942697717 1;
	setAttr ".sd" 2;
	setAttr ".typ" 28;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegPinkyToe2" -p "RightLegPinkyToe1";
	rename -uid "3C5E00AC-491D-441D-54C3-60AA209C276C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.019999999999999976 -9.7144514654701197e-17 -1.1102230246251883e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.14108966550627738 -0.98402387587804507 -0.10858507258954506 0
		 0.97826706647274286 -0.12174279435913848 -0.16784587774635135 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.6621091056886419 4.4833853282898861 -0.48746944717468027 1;
	setAttr ".sd" 2;
	setAttr ".typ" 28;
	setAttr ".radi" 0.05;
createNode joint -n "RightLegKneeBind0" -p "RightLegKnee";
	rename -uid "954F1880-47ED-4C3B-D366-398CAEE8C4A3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 6.6613381477509392e-16 -1.1102230246251565e-16 3.903127820947816e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757777 0.98535134714841321 0.082789661117107824 0
		 0.98179676048382236 -0.15747680591612184 0.1061893436363959 0 0.11767126420052876 0.065450578845900859 -0.99089338241315661 0
		 -0.73175166177217843 2.4059694216789258 -0.052437277911385173 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegKneeBind1" -p "RightLegKnee";
	rename -uid "6E7FE791-441B-E30B-86C4-4B9C0B0578D0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.063360706447884774 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 -2.5444437451708134e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757716 -0.98535134714841321 -0.082789661117107921 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 0.11767129346035049 -0.065450574152726759 0.9908933792484671 0
		 0.87118413200564815 1.4845347091478451 -0.12975039721741705 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegKneeBind3" -p "RightLegKnee";
	rename -uid "AE053CD2-4D3F-9E62-EDA2-A9A32666E963";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.1897355582262869 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 -2.5444437451708134e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757716 -0.98535134714841321 -0.082789661117107921 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 0.11767129346035049 -0.065450574152726759 0.9908933792484671 0
		 0.87118413200564815 1.4845347091478451 -0.12975039721741705 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegHipBind0" -p "RightLegHip";
	rename -uid "65EC342A-4CD0-415A-D3EF-4BA32B0D33FD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 1.1796119636642288e-16 -1.9081958235744878e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593302 0.98737947534752035 0 0 0.98179675697694502 -0.15747680786670104 0.10618937316731988 0
		 0.10484920756543037 -0.01681745065607796 -0.99434592422674117 0 -0.39192918631329343 4.5246047091595409 -0.05243727791138536 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegHipBind2" -p "RightLegHip";
	rename -uid "FDFB7CFB-4969-4F86-8E02-CCA8A7958C05";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.14518631072733956 -1.3356811097431365e-07 -1.4264164677549318e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593302 0.98737947534752035 0 0 0.98179675697694502 -0.15747680786670104 0.10618937316731988 0
		 0.10484920756543037 -0.01681745065607796 -0.99434592422674117 0 -0.56184106539880674 3.4652871682905317 -0.052437277911385367 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegHipBind1" -p "RightLegHip";
	rename -uid "1BFECE8E-438B-4C37-6815-01B88AA709CC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.072636059763409033 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 -2.5444437451708134e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593227 -0.98737947534752046 0 0 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0
		 0.10484920756542861 0.0168174506560776 0.99434592422674117 0 0.56194141724383373 3.4646569314679541 -0.05243727218320602 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "RightLegHipBind3" -p "RightLegHip";
	rename -uid "033618E3-4C87-E509-AB75-A9A569F2E54D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.21790928808509857 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 180 -2.5444437451708134e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593227 -0.98737947534752046 0 0 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0
		 0.10484920756542861 0.0168174506560776 0.99434592422674117 0 0.56194141724383373 3.4646569314679541 -0.05243727218320602 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegHip" -p "CenterHip";
	rename -uid "DD9D9A09-4585-9842-A723-68B990E964CD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.053038436651876658 -0.027861201263751578 -0.0070961637431748922 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -90 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593227 -0.98737947534752046 0 0 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0
		 0.10484920756542861 0.0168174506560776 0.99434592422674117 0 0.39192879977736383 4.5246087982535173 -0.052437272183205937 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegHipBind0" -p "LeftLegHip";
	rename -uid "0F317AA4-4A92-0DC0-AC50-88965776462A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.3783787444765494e-09 -6.9301367422447413e-10 -2.493227412719845e-11 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593227 -0.98737947534752046 0 0 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0
		 0.10484920756542861 0.0168174506560776 0.99434592422674117 0 0.3919287931171147 4.5246088075009885 -0.052437271822601744 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegHipBind2" -p "LeftLegHip";
	rename -uid "056776E5-4FD7-B71E-F550-2BBF46558287";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.14527322763250022 2.1510571102112408e-16 9.540979117872439e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593227 -0.98737947534752046 0 0 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0
		 0.10484920756542861 0.0168174506560776 0.99434592422674117 0 0.56194141724383373 3.4646569314679541 -0.05243727218320602 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegKnee" -p "LeftLegHip";
	rename -uid "AE742407-45B1-6E8B-7CD3-02B427807FC7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0.2905464552650005 3.4694469519536142e-17 -1.7347234759768071e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757716 -0.98535134714841321 -0.082789661117107921 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 0.11767129346035049 -0.065450574152726759 0.9908933792484671 0
		 0.73195403471030085 2.4047050646823904 -0.052437272183205985 1;
	setAttr ".sd" 1;
	setAttr ".typ" 3;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegFoot" -p "LeftLegKnee";
	rename -uid "1A515935-4A73-6D9D-0ED7-19BF9F16E6A2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.25274970400486341 -2.4176783700036175e-09 7.8062556418956319e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -62.776262225551974 0 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.17284131982600376 -0.5089655214478489 0.84325558174145776 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 -0.078746467542097867 0.84625950686620566 0.52691919768424433 0
		 1.0104142117607156 0.56436435079989855 -0.20706352035450307 1;
	setAttr ".sd" 1;
	setAttr ".typ" 4;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegToe" -p "LeftLegFoot";
	rename -uid "5D8D1989-4B03-325C-2A71-ABBD9BB19734";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.11113154726155085 1.0408340855860843e-16 4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.17284131982600376 -0.5089655214478489 0.84325558174145776 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 -0.078746467542097867 0.84625950686620566 0.52691919768424433 0
		 1.1523530996191509 0.14639716479761444 0.4854257499964213 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegToeBind0" -p "LeftLegToe";
	rename -uid "E49F0339-48CF-495A-37C5-91B5B66775E2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.7239750038932087e-09 6.7607562534433008e-09 -1.5650342133355366e-11 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.17284131982600376 -0.5089655214478489 0.84325558174145776 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 -0.078746467542097867 0.84625950686620566 0.52691919768424433 0
		 1.1523531521567185 0.14639716232218838 0.4854257616041826 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegPinkyToe0" -p "LeftLegToe";
	rename -uid "B8D5FA91-4D49-1580-8EBA-71ACC33C0E30";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 0.035799988853943782 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 -27.223737774448029 1.4307055304326102e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33127684384618067 -0.92729159809668693 -0.1743156471192594 0
		 0.93121877117526597 0.35107632841835718 -0.097862208411182511 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.629090201304674 4.7587767521231896 -0.44583689027085693 1;
	setAttr ".sd" 1;
	setAttr ".typ" 28;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegPinkyToe1" -p "LeftLegPinkyToe0";
	rename -uid "88938A75-4F06-C393-DC6F-57931F88A54D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.02 0 3.8857805861880479e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.14108966550627738 -0.98402387587804507 -0.10858507258954506 0
		 0.97826706647274286 -0.12174279435913848 -0.16784587774635135 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.6808296105534977 4.613950693863611 -0.47306181942697717 1;
	setAttr ".sd" 1;
	setAttr ".typ" 28;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegPinkyToe2" -p "LeftLegPinkyToe1";
	rename -uid "6F02E391-4176-B21B-7ECE-E4BB1E775144";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.02 0 -1.0408340855860843e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.14108966550627738 -0.98402387587804507 -0.10858507258954506 0
		 0.97826706647274286 -0.12174279435913848 -0.16784587774635135 0 0.15194490100737604 -0.12990651917274426 0.97981480052828362 0
		 2.6621091056886419 4.4833853282898861 -0.48746944717468027 1;
	setAttr ".sd" 1;
	setAttr ".typ" 28;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegRingToe0" -p "LeftLegToe";
	rename -uid "129CC321-42F7-0AA8-5995-01B32462B58D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 0.018657019334030356 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 -27.223737774448029 1.4307055304326102e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.39895292243837926 -0.91675711659422954 0.01982308885393691 0
		 0.91549560634568683 0.39944375549094641 0.048088262196011998 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.6352499107880449 4.7601588327315936 -0.31769820346088251 1;
	setAttr ".sd" 1;
	setAttr ".typ" 27;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegRingToe1" -p "LeftLegRingToe0";
	rename -uid "9D81CDFA-4E82-EE57-89E7-42A90EA2F03E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.02 0 2.3939183968479938e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.096004506833477832 -0.9953729992529331 0.0039657314434298884 0
		 0.99402151597842237 0.096080783641149192 0.051862402440130614 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.7164306381824965 4.5736129888904449 -0.31366451256188488 1;
	setAttr ".sd" 1;
	setAttr ".typ" 27;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegRingToe2" -p "LeftLegRingToe1";
	rename -uid "476E861B-439F-8327-4D86-C98519B5308A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.02 0 -1.1102230246251565e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.096004506833477832 -0.9953729992529331 0.0039657314434298884 0
		 0.99402151597842237 0.096080783641149192 0.051862402440130614 0 -0.052003465650090529 -0.00103700198810254 0.99864636593103207 0
		 2.7331816993029254 4.3999382886284364 -0.31297256369420051 1;
	setAttr ".sd" 1;
	setAttr ".typ" 27;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegMiddleToe0" -p "LeftLegToe";
	rename -uid "E4ECACD5-4BAE-37A6-8620-2D96E9CB8E44";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 -27.223737774448029 1.4307055304326102e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.37445221034305071 -0.90939875232994727 0.18105096362610004 0
		 0.86402614152767931 0.41306881781095889 0.28780718981472242 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.618713781902053 4.7461154051879859 -0.17664051722583043 1;
	setAttr ".sd" 1;
	setAttr ".typ" 26;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegMiddleToe1" -p "LeftLegMiddleToe0";
	rename -uid "18AF1BBE-4B0E-81BE-2853-BFBC5A6F04E6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.02 0 -3.7560829013044694e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.01142141538714897 -0.99837948880152516 0.05574896959549859 0
		 0.94160776459445139 0.029501446191894265 0.33541687841852452 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.7016009767525628 4.5448146530516302 -0.13656382363067343 1;
	setAttr ".sd" 1;
	setAttr ".typ" 26;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegMiddleToe2" -p "LeftLegMiddleToe1";
	rename -uid "E2C68EEB-414E-1E62-1596-97BA90F7A69F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.02 0 -9.0144634378591659e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.01142141538714897 -0.99837948880152516 0.05574896959549859 0
		 0.94160776459445139 0.029501446191894265 0.33541687841852452 0 -0.33651800683766486 0.048662727142982851 0.94041882693883427 0
		 2.7035986491926174 4.370192233509953 -0.1268130023578857 1;
	setAttr ".sd" 1;
	setAttr ".typ" 26;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegIndexToe0" -p "LeftLegToe";
	rename -uid "B9FEA9E8-4437-0E89-CEDD-DCB2FA394243";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -0.015299613608016141 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 -27.223737774448029 1.4307055304326102e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33586554333643248 -0.89175006831631209 0.30327570370403234 0
		 0.77282429731831681 0.4449626700159679 0.45249400854233496 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.5525955922138412 4.743714447219582 -0.067546450606751435 1;
	setAttr ".sd" 1;
	setAttr ".typ" 25;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegIndexToe1" -p "LeftLegIndexToe0";
	rename -uid "1B0EE797-4CD0-5026-287E-889E459E8342";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.02 0 9.0205620750793969e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6248067147488707 4.551988100973607 -0.0023421465732985092 1;
	setAttr ".sd" 1;
	setAttr ".typ" 25;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegIndexToe2" -p "LeftLegIndexToe1";
	rename -uid "04C66A69-4A7D-A072-2AEF-AFB769BAC81A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.02 0 -6.0715321659188248e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6247826867638016 4.3851846204334235 0.014032435983179822 1;
	setAttr ".sd" 1;
	setAttr ".typ" 25;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegBigToe0" -p "LeftLegToe";
	rename -uid "B664AB81-4260-9B25-3934-868CB605C0A7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -0.03529788000223498 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999986 -27.223737774448029 1.4307055304326102e-14 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.33586554333643248 -0.89175006831631209 0.30327570370403234 0
		 0.77282429731831681 0.4449626700159679 0.45249400854233496 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.5525955922138412 4.743714447219582 -0.067546450606751435 1;
	setAttr ".sd" 1;
	setAttr ".typ" 24;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegBigToe1" -p "LeftLegBigToe0";
	rename -uid "A409210A-4935-560A-EDE3-84949B0C05F6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.02 0 9.0205620750793969e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6248067147488707 4.551988100973607 -0.0023421465732985092 1;
	setAttr ".sd" 1;
	setAttr ".typ" 24;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegBigToe2" -p "LeftLegBigToe1";
	rename -uid "693B5C90-48F3-23FD-6C54-BE970058F9D3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	addAttr -s false -ci true -sn "ch" -ln "Character" -at "message";
	setAttr -k off -cb on ".v";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.02 0 -6.0715321659188248e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" -0.00014336055280844695 -0.9952161662141048 0.097697297577012704 0
		 0.84265238216834049 0.052485660479656415 0.53589384981546051 0 -0.5384579299014669 0.082401686573235378 0.83861374885945761 0
		 2.6247826867638016 4.3851846204334235 0.014032435983179822 1;
	setAttr ".sd" 1;
	setAttr ".typ" 24;
	setAttr ".radi" 0.05;
createNode joint -n "LeftLegFootBind0" -p "LeftLegFoot";
	rename -uid "26C5B11C-480E-9C60-44E4-1E93106DAC4B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -3.6820938659198887e-11 -1.4475677601044623e-11 4.8493250387471321e-10 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.17284131982600376 -0.5089655214478489 0.84325558174145776 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 -0.078746467542097867 0.84625950686620566 0.52691919768424433 0
		 1.0104142113264847 0.56436435395404017 -0.20706351868441197 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegKneeBind2" -p "LeftLegKnee";
	rename -uid "8F6F0926-49E0-15AE-7C2F-C38C064AB206";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.12637485200243165 -1.7347234759768071e-16 9.540979117872439e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757716 -0.98535134714841321 -0.082789661117107921 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 0.11767129346035049 -0.065450574152726759 0.9908933792484671 0
		 0.87118413200564815 1.4845347091478451 -0.12975039721741705 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegKneeBind0" -p "LeftLegKnee";
	rename -uid "AF13E9E0-43B3-3B88-4689-7F963578F532";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.6653345369377348e-16 -3.4694469519536142e-17 9.540979117872439e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757716 -0.98535134714841321 -0.082789661117107921 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 0.11767129346035049 -0.065450574152726759 0.9908933792484671 0
		 0.73195403471030041 2.4047050646823918 -0.052437272183205784 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegKneeBind3" -p "LeftLegKnee";
	rename -uid "530A8F1A-48A5-3C74-A68E-4BBF54EDBBC6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.18956227777961787 -1.7444062164346633e-16 9.540979117872439e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757716 -0.98535134714841321 -0.082789661117107921 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 0.11767129346035049 -0.065450574152726759 0.9908933792484671 0
		 0.87118413200564815 1.4845347091478451 -0.12975039721741705 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegKneeBind1" -p "LeftLegKnee";
	rename -uid "08D41399-46C0-8FEB-E607-B4AB10F9F6E2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.063187426001215741 -1.6433952547494893e-16 9.540979117872439e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.14909257085757716 -0.98535134714841321 -0.082789661117107921 0
		 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0 0.11767129346035049 -0.065450574152726759 0.9908933792484671 0
		 0.87118413200564815 1.4845347091478451 -0.12975039721741705 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegHipBind1" -p "LeftLegHip";
	rename -uid "7C30D0B5-4040-6394-54D6-8FAF270BE861";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.072636613127060712 2.095819189617544e-16 9.540979117872439e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593227 -0.98737947534752046 0 0 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0
		 0.10484920756542861 0.0168174506560776 0.99434592422674117 0 0.56194141724383373 3.4646569314679541 -0.05243727218320602 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode joint -n "LeftLegHipBind3" -p "LeftLegHip";
	rename -uid "5823C30E-4292-BA24-4A19-AE9511570CBD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.21790984144875025 2.0920488739599999e-16 9.540979117872439e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".ssc" no;
	setAttr ".bps" -type "matrix" 0.15837225660593227 -0.98737947534752046 0 0 0.98179675697694502 0.15747680786670035 -0.10618937316731809 0
		 0.10484920756542861 0.0168174506560776 0.99434592422674117 0 0.56194141724383373 3.4646569314679541 -0.05243727218320602 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Bind";
	setAttr ".radi" 0.060000000000000005;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "CBCC62DD-4B65-8718-0002-FBB8A5DCAAE7";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "23964192-4C99-F61B-73AD-538F8D72ADA1";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "28FF5333-4E79-578C-BA61-E19661EFBF93";
createNode displayLayerManager -n "layerManager";
	rename -uid "D152A122-42FB-546A-277D-0B970311CE9B";
createNode displayLayer -n "defaultLayer";
	rename -uid "8737D406-4F54-FCF4-18D4-76A25CCB3C48";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "B2B6539A-4C3E-6DEC-4E2D-A3BFE20424F3";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "DEF09B1E-4AF0-19A7-F860-71BE83D8E571";
	setAttr ".g" yes;
createNode renderLayerManager -n "skeleton_biped_T_renderLayerManager";
	rename -uid "F694A46A-43C9-A169-D4BB-1FB7FCD3A020";
createNode renderLayer -n "skeleton_biped_T_defaultRenderLayer";
	rename -uid "DEE468DE-4C7E-29CC-4BE8-01A078E2C48C";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "BF4B5C1C-4690-DBDC-FCD0-178CDC4EFBF2";
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
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 951\n            -height 613\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n"
		+ "            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n"
		+ "            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n"
		+ "            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n"
		+ "                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n"
		+ "                -animLayerFilterOptions \"selected\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"on\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 951\\n    -height 613\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 951\\n    -height 613\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 1 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "BBDF0610-490F-3728-15DA-81B44C64BF22";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "F6419168-4935-28E1-3466-0E94C17BA8D1";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 475.66950197069349 -2380.1811942755112 ;
	setAttr ".tgi[0].vh" -type "double2" 2195.7145736506313 -1361.2071248837242 ;
	setAttr -s 107 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 2965.71435546875;
	setAttr ".tgi[0].ni[0].y" -138.57142639160156;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 2965.71435546875;
	setAttr ".tgi[0].ni[1].y" -341.42855834960938;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 2965.71435546875;
	setAttr ".tgi[0].ni[2].y" -1715.7142333984375;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 2965.71435546875;
	setAttr ".tgi[0].ni[3].y" 267.14285278320313;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 2965.71435546875;
	setAttr ".tgi[0].ni[4].y" -37.142856597900391;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" 2965.71435546875;
	setAttr ".tgi[0].ni[5].y" -544.28570556640625;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" 1062.857177734375;
	setAttr ".tgi[0].ni[6].y" -2105.71435546875;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" 1062.857177734375;
	setAttr ".tgi[0].ni[7].y" -1975.7142333984375;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" 2965.71435546875;
	setAttr ".tgi[0].ni[8].y" -1072.857177734375;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" 2965.71435546875;
	setAttr ".tgi[0].ni[9].y" -240;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 2965.71435546875;
	setAttr ".tgi[0].ni[10].y" 165.71427917480469;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 2965.71435546875;
	setAttr ".tgi[0].ni[11].y" 470;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" -478.57144165039063;
	setAttr ".tgi[0].ni[12].y" -1571.4285888671875;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" -171.42857360839844;
	setAttr ".tgi[0].ni[13].y" -1571.4285888671875;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" 2592.857177734375;
	setAttr ".tgi[0].ni[14].y" -620;
	setAttr ".tgi[0].ni[14].nvs" 18304;
	setAttr ".tgi[0].ni[15].x" 135.71427917480469;
	setAttr ".tgi[0].ni[15].y" -1642.857177734375;
	setAttr ".tgi[0].ni[15].nvs" 18304;
	setAttr ".tgi[0].ni[16].x" -91.428573608398438;
	setAttr ".tgi[0].ni[16].y" 32.857143402099609;
	setAttr ".tgi[0].ni[16].nvs" 18304;
	setAttr ".tgi[0].ni[17].x" 2965.71435546875;
	setAttr ".tgi[0].ni[17].y" 368.57144165039063;
	setAttr ".tgi[0].ni[17].nvs" 18304;
	setAttr ".tgi[0].ni[18].x" 2285.71435546875;
	setAttr ".tgi[0].ni[18].y" -922.85711669921875;
	setAttr ".tgi[0].ni[18].nvs" 18304;
	setAttr ".tgi[0].ni[19].x" 2592.857177734375;
	setAttr ".tgi[0].ni[19].y" -1525.7142333984375;
	setAttr ".tgi[0].ni[19].nvs" 18304;
	setAttr ".tgi[0].ni[20].x" 2965.71435546875;
	setAttr ".tgi[0].ni[20].y" -747.14288330078125;
	setAttr ".tgi[0].ni[20].nvs" 18304;
	setAttr ".tgi[0].ni[21].x" 2285.71435546875;
	setAttr ".tgi[0].ni[21].y" -1442.857177734375;
	setAttr ".tgi[0].ni[21].nvs" 18304;
	setAttr ".tgi[0].ni[22].x" 2285.71435546875;
	setAttr ".tgi[0].ni[22].y" -2552.857177734375;
	setAttr ".tgi[0].ni[22].nvs" 18304;
	setAttr ".tgi[0].ni[23].x" 2592.857177734375;
	setAttr ".tgi[0].ni[23].y" -2635.71435546875;
	setAttr ".tgi[0].ni[23].nvs" 18304;
	setAttr ".tgi[0].ni[24].x" 2965.71435546875;
	setAttr ".tgi[0].ni[24].y" -1208.5714111328125;
	setAttr ".tgi[0].ni[24].nvs" 18304;
	setAttr ".tgi[0].ni[25].x" 2592.857177734375;
	setAttr ".tgi[0].ni[25].y" -1208.5714111328125;
	setAttr ".tgi[0].ni[25].nvs" 18304;
	setAttr ".tgi[0].ni[26].x" 2965.71435546875;
	setAttr ".tgi[0].ni[26].y" -1310;
	setAttr ".tgi[0].ni[26].nvs" 18304;
	setAttr ".tgi[0].ni[27].x" 2965.71435546875;
	setAttr ".tgi[0].ni[27].y" -1512.857177734375;
	setAttr ".tgi[0].ni[27].nvs" 18304;
	setAttr ".tgi[0].ni[28].x" 2965.71435546875;
	setAttr ".tgi[0].ni[28].y" -1918.5714111328125;
	setAttr ".tgi[0].ni[28].nvs" 18304;
	setAttr ".tgi[0].ni[29].x" 442.85714721679688;
	setAttr ".tgi[0].ni[29].y" -1641.4285888671875;
	setAttr ".tgi[0].ni[29].nvs" 18304;
	setAttr ".tgi[0].ni[30].x" 2965.71435546875;
	setAttr ".tgi[0].ni[30].y" -2020;
	setAttr ".tgi[0].ni[30].nvs" 18304;
	setAttr ".tgi[0].ni[31].x" 750;
	setAttr ".tgi[0].ni[31].y" -1691.4285888671875;
	setAttr ".tgi[0].ni[31].nvs" 18304;
	setAttr ".tgi[0].ni[32].x" 2965.71435546875;
	setAttr ".tgi[0].ni[32].y" -2121.428466796875;
	setAttr ".tgi[0].ni[32].nvs" 18304;
	setAttr ".tgi[0].ni[33].x" 1057.142822265625;
	setAttr ".tgi[0].ni[33].y" -1535.7142333984375;
	setAttr ".tgi[0].ni[33].nvs" 18304;
	setAttr ".tgi[0].ni[34].x" 1364.2857666015625;
	setAttr ".tgi[0].ni[34].y" -1161.4285888671875;
	setAttr ".tgi[0].ni[34].nvs" 18304;
	setAttr ".tgi[0].ni[35].x" 1671.4285888671875;
	setAttr ".tgi[0].ni[35].y" -1105.7142333984375;
	setAttr ".tgi[0].ni[35].nvs" 18304;
	setAttr ".tgi[0].ni[36].x" 2285.71435546875;
	setAttr ".tgi[0].ni[36].y" -1024.2857666015625;
	setAttr ".tgi[0].ni[36].nvs" 18304;
	setAttr ".tgi[0].ni[37].x" 2285.71435546875;
	setAttr ".tgi[0].ni[37].y" -821.4285888671875;
	setAttr ".tgi[0].ni[37].nvs" 18304;
	setAttr ".tgi[0].ni[38].x" 1978.5714111328125;
	setAttr ".tgi[0].ni[38].y" -1785.7142333984375;
	setAttr ".tgi[0].ni[38].nvs" 18304;
	setAttr ".tgi[0].ni[39].x" 2285.71435546875;
	setAttr ".tgi[0].ni[39].y" -1988.5714111328125;
	setAttr ".tgi[0].ni[39].nvs" 18304;
	setAttr ".tgi[0].ni[40].x" 2592.857177734375;
	setAttr ".tgi[0].ni[40].y" -2071.428466796875;
	setAttr ".tgi[0].ni[40].nvs" 18304;
	setAttr ".tgi[0].ni[41].x" 2965.71435546875;
	setAttr ".tgi[0].ni[41].y" -2222.857177734375;
	setAttr ".tgi[0].ni[41].nvs" 18304;
	setAttr ".tgi[0].ni[42].x" 2285.71435546875;
	setAttr ".tgi[0].ni[42].y" -2090;
	setAttr ".tgi[0].ni[42].nvs" 18304;
	setAttr ".tgi[0].ni[43].x" 2592.857177734375;
	setAttr ".tgi[0].ni[43].y" -2172.857177734375;
	setAttr ".tgi[0].ni[43].nvs" 18304;
	setAttr ".tgi[0].ni[44].x" 2965.71435546875;
	setAttr ".tgi[0].ni[44].y" -2324.28564453125;
	setAttr ".tgi[0].ni[44].nvs" 18304;
	setAttr ".tgi[0].ni[45].x" 2965.71435546875;
	setAttr ".tgi[0].ni[45].y" -2425.71435546875;
	setAttr ".tgi[0].ni[45].nvs" 18304;
	setAttr ".tgi[0].ni[46].x" 2285.71435546875;
	setAttr ".tgi[0].ni[46].y" -2248.571533203125;
	setAttr ".tgi[0].ni[46].nvs" 18304;
	setAttr ".tgi[0].ni[47].x" 2592.857177734375;
	setAttr ".tgi[0].ni[47].y" -2331.428466796875;
	setAttr ".tgi[0].ni[47].nvs" 18304;
	setAttr ".tgi[0].ni[48].x" 2285.71435546875;
	setAttr ".tgi[0].ni[48].y" -2350;
	setAttr ".tgi[0].ni[48].nvs" 18304;
	setAttr ".tgi[0].ni[49].x" 2965.71435546875;
	setAttr ".tgi[0].ni[49].y" -2527.142822265625;
	setAttr ".tgi[0].ni[49].nvs" 18304;
	setAttr ".tgi[0].ni[50].x" 2592.857177734375;
	setAttr ".tgi[0].ni[50].y" -2432.857177734375;
	setAttr ".tgi[0].ni[50].nvs" 18304;
	setAttr ".tgi[0].ni[51].x" 2965.71435546875;
	setAttr ".tgi[0].ni[51].y" -2628.571533203125;
	setAttr ".tgi[0].ni[51].nvs" 18304;
	setAttr ".tgi[0].ni[52].x" 2285.71435546875;
	setAttr ".tgi[0].ni[52].y" -2451.428466796875;
	setAttr ".tgi[0].ni[52].nvs" 18304;
	setAttr ".tgi[0].ni[53].x" 2592.857177734375;
	setAttr ".tgi[0].ni[53].y" -2534.28564453125;
	setAttr ".tgi[0].ni[53].nvs" 18304;
	setAttr ".tgi[0].ni[54].x" 2965.71435546875;
	setAttr ".tgi[0].ni[54].y" -2730;
	setAttr ".tgi[0].ni[54].nvs" 18304;
	setAttr ".tgi[0].ni[55].x" 2285.71435546875;
	setAttr ".tgi[0].ni[55].y" -1284.2857666015625;
	setAttr ".tgi[0].ni[55].nvs" 18304;
	setAttr ".tgi[0].ni[56].x" 2965.71435546875;
	setAttr ".tgi[0].ni[56].y" 64.285713195800781;
	setAttr ".tgi[0].ni[56].nvs" 18304;
	setAttr ".tgi[0].ni[57].x" 2965.71435546875;
	setAttr ".tgi[0].ni[57].y" -848.5714111328125;
	setAttr ".tgi[0].ni[57].nvs" 18304;
	setAttr ".tgi[0].ni[58].x" 2285.71435546875;
	setAttr ".tgi[0].ni[58].y" -504.28570556640625;
	setAttr ".tgi[0].ni[58].nvs" 18304;
	setAttr ".tgi[0].ni[59].x" 2965.71435546875;
	setAttr ".tgi[0].ni[59].y" -2831.428466796875;
	setAttr ".tgi[0].ni[59].nvs" 18304;
	setAttr ".tgi[0].ni[60].x" 2285.71435546875;
	setAttr ".tgi[0].ni[60].y" -2654.28564453125;
	setAttr ".tgi[0].ni[60].nvs" 18304;
	setAttr ".tgi[0].ni[61].x" 2965.71435546875;
	setAttr ".tgi[0].ni[61].y" -2932.857177734375;
	setAttr ".tgi[0].ni[61].nvs" 18304;
	setAttr ".tgi[0].ni[62].x" 2592.857177734375;
	setAttr ".tgi[0].ni[62].y" -2794.28564453125;
	setAttr ".tgi[0].ni[62].nvs" 18304;
	setAttr ".tgi[0].ni[63].x" 2965.71435546875;
	setAttr ".tgi[0].ni[63].y" -3034.28564453125;
	setAttr ".tgi[0].ni[63].nvs" 18304;
	setAttr ".tgi[0].ni[64].x" 2965.71435546875;
	setAttr ".tgi[0].ni[64].y" -3135.71435546875;
	setAttr ".tgi[0].ni[64].nvs" 18304;
	setAttr ".tgi[0].ni[65].x" 1057.142822265625;
	setAttr ".tgi[0].ni[65].y" -1694.2857666015625;
	setAttr ".tgi[0].ni[65].nvs" 18304;
	setAttr ".tgi[0].ni[66].x" 1364.2857666015625;
	setAttr ".tgi[0].ni[66].y" -1521.4285888671875;
	setAttr ".tgi[0].ni[66].nvs" 18304;
	setAttr ".tgi[0].ni[67].x" 1671.4285888671875;
	setAttr ".tgi[0].ni[67].y" -845.71429443359375;
	setAttr ".tgi[0].ni[67].nvs" 18304;
	setAttr ".tgi[0].ni[68].x" 1978.5714111328125;
	setAttr ".tgi[0].ni[68].y" -1092.857177734375;
	setAttr ".tgi[0].ni[68].nvs" 18304;
	setAttr ".tgi[0].ni[69].x" 2285.71435546875;
	setAttr ".tgi[0].ni[69].y" 225.71427917480469;
	setAttr ".tgi[0].ni[69].nvs" 18304;
	setAttr ".tgi[0].ni[70].x" 2592.857177734375;
	setAttr ".tgi[0].ni[70].y" 334.28570556640625;
	setAttr ".tgi[0].ni[70].nvs" 18304;
	setAttr ".tgi[0].ni[71].x" 1577.142822265625;
	setAttr ".tgi[0].ni[71].y" -1958.5714111328125;
	setAttr ".tgi[0].ni[71].nvs" 18304;
	setAttr ".tgi[0].ni[72].x" 1597.142822265625;
	setAttr ".tgi[0].ni[72].y" -2088.571533203125;
	setAttr ".tgi[0].ni[72].nvs" 18304;
	setAttr ".tgi[0].ni[73].x" 1530;
	setAttr ".tgi[0].ni[73].y" -1828.5714111328125;
	setAttr ".tgi[0].ni[73].nvs" 18304;
	setAttr ".tgi[0].ni[74].x" 2965.71435546875;
	setAttr ".tgi[0].ni[74].y" -442.85714721679688;
	setAttr ".tgi[0].ni[74].nvs" 18304;
	setAttr ".tgi[0].ni[75].x" 2965.71435546875;
	setAttr ".tgi[0].ni[75].y" -645.71429443359375;
	setAttr ".tgi[0].ni[75].nvs" 18304;
	setAttr ".tgi[0].ni[76].x" 2965.71435546875;
	setAttr ".tgi[0].ni[76].y" -971.4285888671875;
	setAttr ".tgi[0].ni[76].nvs" 18304;
	setAttr ".tgi[0].ni[77].x" 2965.71435546875;
	setAttr ".tgi[0].ni[77].y" -3237.142822265625;
	setAttr ".tgi[0].ni[77].nvs" 18304;
	setAttr ".tgi[0].ni[78].x" 2592.857177734375;
	setAttr ".tgi[0].ni[78].y" -2952.857177734375;
	setAttr ".tgi[0].ni[78].nvs" 18304;
	setAttr ".tgi[0].ni[79].x" 2285.71435546875;
	setAttr ".tgi[0].ni[79].y" -1772.857177734375;
	setAttr ".tgi[0].ni[79].nvs" 18304;
	setAttr ".tgi[0].ni[80].x" 1978.5714111328125;
	setAttr ".tgi[0].ni[80].y" -705.71429443359375;
	setAttr ".tgi[0].ni[80].nvs" 18304;
	setAttr ".tgi[0].ni[81].x" 2965.71435546875;
	setAttr ".tgi[0].ni[81].y" -1817.142822265625;
	setAttr ".tgi[0].ni[81].nvs" 18304;
	setAttr ".tgi[0].ni[82].x" 2965.71435546875;
	setAttr ".tgi[0].ni[82].y" -1411.4285888671875;
	setAttr ".tgi[0].ni[82].nvs" 18304;
	setAttr ".tgi[0].ni[83].x" 1671.4285888671875;
	setAttr ".tgi[0].ni[83].y" -1004.2857055664063;
	setAttr ".tgi[0].ni[83].nvs" 18304;
	setAttr ".tgi[0].ni[84].x" 2965.71435546875;
	setAttr ".tgi[0].ni[84].y" -3338.571533203125;
	setAttr ".tgi[0].ni[84].nvs" 18304;
	setAttr ".tgi[0].ni[85].x" 2965.71435546875;
	setAttr ".tgi[0].ni[85].y" -3440;
	setAttr ".tgi[0].ni[85].nvs" 18304;
	setAttr ".tgi[0].ni[86].x" 2965.71435546875;
	setAttr ".tgi[0].ni[86].y" -3541.428466796875;
	setAttr ".tgi[0].ni[86].nvs" 18304;
	setAttr ".tgi[0].ni[87].x" 2965.71435546875;
	setAttr ".tgi[0].ni[87].y" -3642.857177734375;
	setAttr ".tgi[0].ni[87].nvs" 18304;
	setAttr ".tgi[0].ni[88].x" 2592.857177734375;
	setAttr ".tgi[0].ni[88].y" -3288.571533203125;
	setAttr ".tgi[0].ni[88].nvs" 18304;
	setAttr ".tgi[0].ni[89].x" 2965.71435546875;
	setAttr ".tgi[0].ni[89].y" -3744.28564453125;
	setAttr ".tgi[0].ni[89].nvs" 18304;
	setAttr ".tgi[0].ni[90].x" 2285.71435546875;
	setAttr ".tgi[0].ni[90].y" -2984.28564453125;
	setAttr ".tgi[0].ni[90].nvs" 18304;
	setAttr ".tgi[0].ni[91].x" 2965.71435546875;
	setAttr ".tgi[0].ni[91].y" -3845.71435546875;
	setAttr ".tgi[0].ni[91].nvs" 18304;
	setAttr ".tgi[0].ni[92].x" 1978.5714111328125;
	setAttr ".tgi[0].ni[92].y" -1525.7142333984375;
	setAttr ".tgi[0].ni[92].nvs" 18304;
	setAttr ".tgi[0].ni[93].x" 1671.4285888671875;
	setAttr ".tgi[0].ni[93].y" -1207.142822265625;
	setAttr ".tgi[0].ni[93].nvs" 18304;
	setAttr ".tgi[0].ni[94].x" 1364.2857666015625;
	setAttr ".tgi[0].ni[94].y" -1262.857177734375;
	setAttr ".tgi[0].ni[94].nvs" 18304;
	setAttr ".tgi[0].ni[95].x" 2965.71435546875;
	setAttr ".tgi[0].ni[95].y" -3947.142822265625;
	setAttr ".tgi[0].ni[95].nvs" 18304;
	setAttr ".tgi[0].ni[96].x" 2965.71435546875;
	setAttr ".tgi[0].ni[96].y" -4048.571533203125;
	setAttr ".tgi[0].ni[96].nvs" 18304;
	setAttr ".tgi[0].ni[97].x" 2965.71435546875;
	setAttr ".tgi[0].ni[97].y" -4150;
	setAttr ".tgi[0].ni[97].nvs" 18304;
	setAttr ".tgi[0].ni[98].x" 2285.71435546875;
	setAttr ".tgi[0].ni[98].y" -1182.857177734375;
	setAttr ".tgi[0].ni[98].nvs" 18304;
	setAttr ".tgi[0].ni[99].x" 594.28570556640625;
	setAttr ".tgi[0].ni[99].y" -2170;
	setAttr ".tgi[0].ni[99].nvs" 18304;
	setAttr ".tgi[0].ni[100].x" 2965.71435546875;
	setAttr ".tgi[0].ni[100].y" -1614.2857666015625;
	setAttr ".tgi[0].ni[100].nvs" 18304;
	setAttr ".tgi[0].ni[101].x" 2285.71435546875;
	setAttr ".tgi[0].ni[101].y" -720;
	setAttr ".tgi[0].ni[101].nvs" 18304;
	setAttr ".tgi[0].ni[102].x" 594.28570556640625;
	setAttr ".tgi[0].ni[102].y" -2040;
	setAttr ".tgi[0].ni[102].nvs" 18304;
	setAttr ".tgi[0].ni[103].x" 594.28570556640625;
	setAttr ".tgi[0].ni[103].y" -1910;
	setAttr ".tgi[0].ni[103].nvs" 18304;
	setAttr ".tgi[0].ni[104].x" 594.28570556640625;
	setAttr ".tgi[0].ni[104].y" -1780;
	setAttr ".tgi[0].ni[104].nvs" 18304;
	setAttr ".tgi[0].ni[105].x" 1398.5714111328125;
	setAttr ".tgi[0].ni[105].y" -2311.428466796875;
	setAttr ".tgi[0].ni[105].nvs" 18304;
	setAttr ".tgi[0].ni[106].x" 1398.5714111328125;
	setAttr ".tgi[0].ni[106].y" -2181.428466796875;
	setAttr ".tgi[0].ni[106].nvs" 18304;
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
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "CenterRoot.s" "CenterCOG.is";
connectAttr "CenterCOG.s" "CenterSpine0.is";
connectAttr "CenterSpine0.s" "CenterSpine0Bind0.is";
connectAttr "CenterSpine0.s" "CenterSpine1.is";
connectAttr "CenterSpine1.s" "CenterSpine1Bind0.is";
connectAttr "CenterSpine1.s" "CenterSpine2.is";
connectAttr "CenterSpine2.s" "CenterSpine2Bind0.is";
connectAttr "CenterSpine2.s" "CenterSpine3.is";
connectAttr "CenterSpine3.s" "CenterSpine3Bind0.is";
connectAttr "CenterSpine3.s" "CenterSpine4.is";
connectAttr "CenterSpine4.s" "CenterSpine5.is";
connectAttr "CenterSpine5.s" "CenterSpine5Bind0.is";
connectAttr "CenterSpine5.s" "CenterHead.is";
connectAttr "CenterHead.s" "CenterHeadBind0.is";
connectAttr "CenterSpine4.s" "CenterSpine4Bind0.is";
connectAttr "CenterSpine4.s" "LeftArmCollar.is";
connectAttr "LeftArmCollar.s" "LeftArmCollarBind0.is";
connectAttr "LeftArmCollar.s" "LeftArmShoulder.is";
connectAttr "LeftArmShoulder.s" "LeftArmElbow.is";
connectAttr "LeftArmElbow.s" "LeftArmElbowBind0.is";
connectAttr "LeftArmElbow.s" "LeftArmElbowBind2.is";
connectAttr "LeftArmElbow.s" "LeftArmHand.is";
connectAttr "LeftArmHand.s" "LeftArmMiddleFinger0.is";
connectAttr "LeftArmMiddleFinger0.s" "LeftArmMiddleFinger1.is";
connectAttr "LeftArmMiddleFinger1.s" "LeftArmMiddleFinger2.is";
connectAttr "LeftArmHand.s" "LeftArmThumb0.is";
connectAttr "LeftArmThumb0.s" "LeftArmThumb1.is";
connectAttr "LeftArmThumb1.s" "LeftArmThumb2.is";
connectAttr "LeftArmHand.s" "LeftArmRingFinger0.is";
connectAttr "LeftArmRingFinger0.s" "LeftArmRingFinger1.is";
connectAttr "LeftArmRingFinger1.s" "LeftArmRingFinger2.is";
connectAttr "LeftArmHand.s" "LeftArmIndexFinger0.is";
connectAttr "LeftArmIndexFinger0.s" "LeftArmIndexFinger1.is";
connectAttr "LeftArmIndexFinger1.s" "LeftArmIndexFinger2.is";
connectAttr "LeftArmHand.s" "LeftArmPinkyFinger0.is";
connectAttr "LeftArmPinkyFinger0.s" "LeftArmPinkyFinger1.is";
connectAttr "LeftArmPinkyFinger1.s" "LeftArmPinkyFinger2.is";
connectAttr "LeftArmHand.s" "LeftArmHandBind0.is";
connectAttr "LeftArmElbow.s" "LeftArmElbowBind1.is";
connectAttr "LeftArmElbow.s" "LeftArmElbowBind3.is";
connectAttr "LeftArmShoulder.s" "LeftArmShoulderBind0.is";
connectAttr "LeftArmShoulder.s" "LeftArmShoulderBind2.is";
connectAttr "LeftArmShoulder.s" "LeftArmShoulderBind1.is";
connectAttr "LeftArmShoulder.s" "LeftArmShoulderBind3.is";
connectAttr "CenterSpine4.s" "RightArmCollar.is";
connectAttr "RightArmCollar.s" "RightArmShoulder.is";
connectAttr "RightArmShoulder.s" "RightArmElbow.is";
connectAttr "RightArmElbow.s" "RightArmHand.is";
connectAttr "RightArmHand.s" "RightArmPinkyFinger0.is";
connectAttr "RightArmPinkyFinger0.s" "RightArmPinkyFinger1.is";
connectAttr "RightArmPinkyFinger1.s" "RightArmPinkyFinger2.is";
connectAttr "RightArmHand.s" "RightArmIndexFinger0.is";
connectAttr "RightArmIndexFinger0.s" "RightArmIndexFinger1.is";
connectAttr "RightArmIndexFinger1.s" "RightArmIndexFinger2.is";
connectAttr "RightArmHand.s" "RightArmHandBind0.is";
connectAttr "RightArmHand.s" "RightArmRingFinger0.is";
connectAttr "RightArmRingFinger0.s" "RightArmRingFinger1.is";
connectAttr "RightArmRingFinger1.s" "RightArmRingFinger2.is";
connectAttr "RightArmHand.s" "RightArmThumb0.is";
connectAttr "RightArmThumb0.s" "RightArmThumb1.is";
connectAttr "RightArmThumb1.s" "RightArmThumb2.is";
connectAttr "RightArmHand.s" "RightArmMiddleFinger0.is";
connectAttr "RightArmMiddleFinger0.s" "RightArmMiddleFinger1.is";
connectAttr "RightArmMiddleFinger1.s" "RightArmMiddleFinger2.is";
connectAttr "RightArmElbow.s" "RightArmElbowBind0.is";
connectAttr "RightArmElbow.s" "RightArmElbowBind2.is";
connectAttr "RightArmShoulder.s" "RightArmShoulderBind0.is";
connectAttr "RightArmShoulder.s" "RightArmShoulderBind2.is";
connectAttr "RightArmCollar.s" "RightArmCollarBind0.is";
connectAttr "CenterCOG.s" "CenterHip.is";
connectAttr "CenterHip.s" "RightLegHip.is";
connectAttr "RightLegHip.s" "RightLegKnee.is";
connectAttr "RightLegKnee.s" "RightLegKneeBind2.is";
connectAttr "RightLegKnee.s" "RightLegFoot.is";
connectAttr "RightLegFoot.s" "RightLegFootBind0.is";
connectAttr "RightLegFoot.s" "RightLegToe.is";
connectAttr "RightLegToe.s" "RightLegToeBind0.is";
connectAttr "RightLegToe.s" "RightLegBigToe0.is";
connectAttr "RightLegBigToe0.s" "RightLegBigToe1.is";
connectAttr "RightLegBigToe1.s" "RightLegBigToe2.is";
connectAttr "RightLegToe.s" "RightLegIndexToe0.is";
connectAttr "RightLegIndexToe0.s" "RightLegIndexToe1.is";
connectAttr "RightLegIndexToe1.s" "RightLegIndexToe2.is";
connectAttr "RightLegToe.s" "RightLegMiddleToe0.is";
connectAttr "RightLegMiddleToe0.s" "RightLegMiddleToe1.is";
connectAttr "RightLegMiddleToe1.s" "RightLegMiddleToe2.is";
connectAttr "RightLegToe.s" "RightLegRingToe0.is";
connectAttr "RightLegRingToe0.s" "RightLegRingToe1.is";
connectAttr "RightLegRingToe1.s" "RightLegRingToe2.is";
connectAttr "RightLegToe.s" "RightLegPinkyToe0.is";
connectAttr "RightLegPinkyToe0.s" "RightLegPinkyToe1.is";
connectAttr "RightLegPinkyToe1.s" "RightLegPinkyToe2.is";
connectAttr "RightLegKnee.s" "RightLegKneeBind0.is";
connectAttr "RightLegKnee.s" "RightLegKneeBind1.is";
connectAttr "RightLegKnee.s" "RightLegKneeBind3.is";
connectAttr "RightLegHip.s" "RightLegHipBind0.is";
connectAttr "RightLegHip.s" "RightLegHipBind2.is";
connectAttr "RightLegHip.s" "RightLegHipBind1.is";
connectAttr "RightLegHip.s" "RightLegHipBind3.is";
connectAttr "CenterHip.s" "LeftLegHip.is";
connectAttr "LeftLegHip.s" "LeftLegHipBind0.is";
connectAttr "LeftLegHip.s" "LeftLegHipBind2.is";
connectAttr "LeftLegHip.s" "LeftLegKnee.is";
connectAttr "LeftLegKnee.s" "LeftLegFoot.is";
connectAttr "LeftLegFoot.s" "LeftLegToe.is";
connectAttr "LeftLegToe.s" "LeftLegToeBind0.is";
connectAttr "LeftLegToe.s" "LeftLegPinkyToe0.is";
connectAttr "LeftLegPinkyToe0.s" "LeftLegPinkyToe1.is";
connectAttr "LeftLegPinkyToe1.s" "LeftLegPinkyToe2.is";
connectAttr "LeftLegToe.s" "LeftLegRingToe0.is";
connectAttr "LeftLegRingToe0.s" "LeftLegRingToe1.is";
connectAttr "LeftLegRingToe1.s" "LeftLegRingToe2.is";
connectAttr "LeftLegToe.s" "LeftLegMiddleToe0.is";
connectAttr "LeftLegMiddleToe0.s" "LeftLegMiddleToe1.is";
connectAttr "LeftLegMiddleToe1.s" "LeftLegMiddleToe2.is";
connectAttr "LeftLegToe.s" "LeftLegIndexToe0.is";
connectAttr "LeftLegIndexToe0.s" "LeftLegIndexToe1.is";
connectAttr "LeftLegIndexToe1.s" "LeftLegIndexToe2.is";
connectAttr "LeftLegToe.s" "LeftLegBigToe0.is";
connectAttr "LeftLegBigToe0.s" "LeftLegBigToe1.is";
connectAttr "LeftLegBigToe1.s" "LeftLegBigToe2.is";
connectAttr "LeftLegFoot.s" "LeftLegFootBind0.is";
connectAttr "LeftLegKnee.s" "LeftLegKneeBind2.is";
connectAttr "LeftLegKnee.s" "LeftLegKneeBind0.is";
connectAttr "LeftLegKnee.s" "LeftLegKneeBind3.is";
connectAttr "LeftLegKnee.s" "LeftLegKneeBind1.is";
connectAttr "LeftLegHip.s" "LeftLegHipBind1.is";
connectAttr "LeftLegHip.s" "LeftLegHipBind3.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "skeleton_biped_T_renderLayerManager.rlmi[0]" "skeleton_biped_T_defaultRenderLayer.rlid"
		;
connectAttr "LeftArmShoulderBind1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "LeftLegKneeBind1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "LeftLegHipBind3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "RightLegHipBind3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "RightLegKneeBind3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "LeftLegHipBind1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn";
connectAttr "transform2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn";
connectAttr "transform1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn";
connectAttr "LeftLegKneeBind3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "RightLegKneeBind1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "RightLegHipBind1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "RightArmPinkyFinger2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "CenterRoot.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn";
connectAttr "CenterCOG.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn";
connectAttr "RightArmIndexFinger1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn"
		;
connectAttr "CenterSpine0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn";
connectAttr "defaultRenderLayer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn"
		;
connectAttr "RightArmElbowBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn"
		;
connectAttr "RightArmMiddleFinger0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[18].dn"
		;
connectAttr "RightArmRingFinger1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[19].dn"
		;
connectAttr "RightArmIndexFinger2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[20].dn"
		;
connectAttr "RightArmRingFinger0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[21].dn"
		;
connectAttr "RightArmThumb0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[22].dn";
connectAttr "RightArmThumb1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[23].dn";
connectAttr "RightArmMiddleFinger2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[24].dn"
		;
connectAttr "RightArmMiddleFinger1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[25].dn"
		;
connectAttr "RightArmShoulderBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[26].dn"
		;
connectAttr "RightArmRingFinger2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[27].dn"
		;
connectAttr "RightArmElbowBind2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[28].dn"
		;
connectAttr "CenterSpine2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[29].dn";
connectAttr "CenterSpine2Bind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[30].dn"
		;
connectAttr "CenterSpine4.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[31].dn";
connectAttr "LeftArmCollarBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[32].dn"
		;
connectAttr "LeftArmCollar.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[33].dn";
connectAttr "LeftArmShoulder.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[34].dn"
		;
connectAttr "LeftArmElbow.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[35].dn";
connectAttr "LeftArmElbowBind2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[36].dn"
		;
connectAttr "LeftArmElbowBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[37].dn"
		;
connectAttr "LeftArmHand.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[38].dn";
connectAttr "LeftArmMiddleFinger0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[39].dn"
		;
connectAttr "LeftArmMiddleFinger1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[40].dn"
		;
connectAttr "LeftArmMiddleFinger2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[41].dn"
		;
connectAttr "LeftArmThumb0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[42].dn";
connectAttr "LeftArmThumb1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[43].dn";
connectAttr "LeftArmThumb2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[44].dn";
connectAttr "RightArmHandBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[45].dn"
		;
connectAttr "LeftArmRingFinger0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[46].dn"
		;
connectAttr "LeftArmRingFinger1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[47].dn"
		;
connectAttr "LeftArmIndexFinger0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[48].dn"
		;
connectAttr "LeftArmRingFinger2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[49].dn"
		;
connectAttr "LeftArmIndexFinger1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[50].dn"
		;
connectAttr "LeftArmIndexFinger2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[51].dn"
		;
connectAttr "LeftArmPinkyFinger0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[52].dn"
		;
connectAttr "LeftArmPinkyFinger1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[53].dn"
		;
connectAttr "LeftArmPinkyFinger2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[54].dn"
		;
connectAttr "LeftArmHandBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[55].dn"
		;
connectAttr "LeftArmShoulderBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[56].dn"
		;
connectAttr "LeftArmShoulderBind2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[57].dn"
		;
connectAttr "RightArmIndexFinger0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[58].dn"
		;
connectAttr "RightArmThumb2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[59].dn";
connectAttr "CenterSpine5.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[60].dn";
connectAttr "CenterSpine5Bind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[61].dn"
		;
connectAttr "CenterHead.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[62].dn";
connectAttr "CenterHeadBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[63].dn"
		;
connectAttr "CenterSpine4Bind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[64].dn"
		;
connectAttr "RightArmCollar.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[65].dn";
connectAttr "RightArmShoulder.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[66].dn"
		;
connectAttr "RightArmElbow.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[67].dn";
connectAttr "RightArmHand.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[68].dn";
connectAttr "RightArmPinkyFinger0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[69].dn"
		;
connectAttr "RightArmPinkyFinger1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[70].dn"
		;
connectAttr "sceneConfigurationScriptNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[71].dn"
		;
connectAttr "uiConfigurationScriptNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[72].dn"
		;
connectAttr "skeleton_biped_T_defaultRenderLayer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[73].dn"
		;
connectAttr "LeftLegKneeBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[74].dn"
		;
connectAttr "LeftLegKneeBind2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[75].dn"
		;
connectAttr "LeftLegFootBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[76].dn"
		;
connectAttr "LeftLegToeBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[77].dn"
		;
connectAttr "LeftLegToe.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[78].dn";
connectAttr "LeftLegFoot.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[79].dn";
connectAttr "LeftLegKnee.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[80].dn";
connectAttr "LeftLegHipBind2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[81].dn"
		;
connectAttr "LeftLegHipBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[82].dn"
		;
connectAttr "LeftLegHip.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[83].dn";
connectAttr "RightLegHipBind2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[84].dn"
		;
connectAttr "RightLegHipBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[85].dn"
		;
connectAttr "RightLegKneeBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[86].dn"
		;
connectAttr "RightLegToeBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[87].dn"
		;
connectAttr "RightLegToe.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[88].dn";
connectAttr "RightLegFootBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[89].dn"
		;
connectAttr "RightLegFoot.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[90].dn";
connectAttr "RightLegKneeBind2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[91].dn"
		;
connectAttr "RightLegKnee.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[92].dn";
connectAttr "RightLegHip.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[93].dn";
connectAttr "CenterHip.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[94].dn";
connectAttr "CenterSpine0Bind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[95].dn"
		;
connectAttr "RightArmCollarBind0.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[96].dn"
		;
connectAttr "RightArmShoulderBind2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[97].dn"
		;
connectAttr "LeftArmElbowBind3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[98].dn"
		;
connectAttr "RightArmShoulderBind1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[99].dn"
		;
connectAttr "LeftArmShoulderBind3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[100].dn"
		;
connectAttr "LeftArmElbowBind1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[101].dn"
		;
connectAttr "RightArmElbowBind1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[102].dn"
		;
connectAttr "RightArmShoulderBind3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[103].dn"
		;
connectAttr "RightArmElbowBind3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[104].dn"
		;
connectAttr "transform3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[105].dn";
connectAttr "transform4.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[106].dn";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "skeleton_biped_T_defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
// End of skeleton_biped_T_advanced.ma
