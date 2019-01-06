//Maya ASCII 2018 scene
//Name: skeleton_biped_male_face.ma
//Last modified: Tue, Apr 24, 2018 02:00:00 PM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 7 Ultimate Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode joint -n "CenterFaceRoot";
	rename -uid "C4E64781-4B89-D510-1B08-B0B280C64166";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.8791971549544119e-17 0.91520452499389648 5.0306980803327406e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 -4.7161628985784021e-14 1.6901488304138184 0.031516246497631073 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftZygomaticus1" -p "CenterFaceRoot";
	rename -uid "8CD7BF7F-4DEC-8931-9715-84AF8F9E140E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.025875614629529781 -0.0012911727204070189 0.030137783293604434 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99977266877401283 -3.4125427891361438e-12 -0.021321604692944231 0
		 9.742367378152865e-05 0.99998962054340368 0.0045682078965685229 0 0.021321382114249224 -0.0045692463567309927 0.99976223203233516 0
		 0.047396149486303329 1.6740075349807739 0.055203128606081009 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftZygomaticus0" -p "CenterFaceRoot";
	rename -uid "6935318E-4054-5385-A534-66A44AB5DB5F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.021512652989375089 -0.0078866645187437578 0.035627082394081334 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99986224699104098 0.0019415241467081864 -0.01648385752348995 0
		 -0.0018318852308002965 0.99997617835082642 0.0066637929348080669 0 0.016496401781913209 -0.0066326780465827085 0.99984192564511898 0
		 0.039404548704624176 1.6619266271591189 0.065257832407951355 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftCheeck1" -p "CenterFaceRoot";
	rename -uid "D6771550-41B7-7736-74B1-DFB721056C71";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.019562088534470105 0.006431465988312568 0.039949313171539644 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.9999609813207091 -1.4138563552889919e-12 -0.0088337899809045085 0
		 0 1.0000000596046483 -1.6005094558707578e-10 0 0.0088337905073572788 1.6004470060907094e-10 0.99996104091372984 0
		 0.035831715911626816 1.6881530284881592 0.073174826800823226 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftNasolabial1" -p "CenterFaceRoot";
	rename -uid "FA11E525-4C00-E849-0352-1A8EF1BB3E86";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.011182807754756038 -0.0042481517620472919 0.043726266531994233 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99991611273346548 -0.0072160238672589871 -0.010756231474902973 0
		 0.0071792046443295661 0.99996831045247458 -0.0034577904295217269 0 0.010780842112912492 0.0033802791779274036 0.99993623114249675 0
		 0.020483456552028656 1.6685912609100344 0.080093041062355042 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "UpperLip0" -p "CenterFaceRoot";
	rename -uid "22CC2807-444F-7F9D-9717-05876019F720";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.8791971549544119e-17 -0.0082472161632188845 0.047740409507457351 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0 1.6612662076950075 0.087445713579654694 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Mouth";
	setAttr ".radi" 0.005;
createNode joint -n "CenterUpperTeeth" -p "CenterFaceRoot";
	rename -uid "C5F36726-49F6-6E06-D894-BB8721D41605";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.8679168694736419e-09 -0.0072317491439047865 0.038147909465887704 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046421 -1.1007430377728526e-07 0
		 0 1.1007430377728526e-07 1.0000000596046421 0 5.2531397010113778e-09 1.6631262302398684 0.069875210523605347 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "UpperLip1" -p "CenterFaceRoot";
	rename -uid "2F9C4753-4700-EF0E-5C21-9A9849B558F8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.007717181522819078 -0.0086865815308192484 0.045195437190309835 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990910197999294 -0.0054797845958873114 -0.012319081135268431 0
		 0.0054480029865535884 0.99998180786220547 -0.0026119750871369564 0 0.012333169350356396 0.0025446231212391825 0.99992070576061853 0
		 0.014135497622191906 1.6604614257812502 0.082784108817577362 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Mouth";
	setAttr ".radi" 0.005;
createNode joint -n "UpperLip2" -p "CenterFaceRoot";
	rename -uid "89338BA2-4517-0C01-7706-23860158993A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.014072400977591673 -0.010316287970284055 0.038295449280128666 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99990812596593193 -2.1695000269955365e-12 -0.013555059911392433 0
		 0 1.0000000596046483 -1.6005094558707578e-10 0 0.013555060719040111 1.6003624105754294e-10 0.99990818554320282 0
		 0.025776300579309464 1.6574763059616091 0.070145457983016968 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftBrow1" -p "CenterFaceRoot";
	rename -uid "3D4B9A1C-456E-2009-0BC0-C2A9335DFFAA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.015846785679640416 0.028333676640450278 0.0491194097209421 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99998653201289356 -8.2881941589821039e-13 -0.0051784727810232191 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.0051784724723787428 1.6004877094421391e-10 0.99998647241224836 0
		 0.029026426374912262 1.7282711267471313 0.089971616864204421 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "LeftBrow2" -p "CenterFaceRoot";
	rename -uid "A269F656-4826-02DD-A96E-D1A104868F47";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.021438018718018155 0.028550853686378108 0.045401017527558415 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99994413568560103 -1.6917428961667926e-12 -0.010570028129462937 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.010570027499580945 1.6004198537437016e-10 0.99994407609760416 0
		 0.039267841726541519 1.7286689281463623 0.083160668611526475 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "LeftBrow3" -p "CenterFaceRoot";
	rename -uid "E72F991C-4AC4-2D41-A27F-B8B9665A6356";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.025767050512434841 0.025925790419978334 0.038804769156964306 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99985163413431433 -2.7569194582230784e-12 -0.017225262946343481 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.017225261920247068 1.6002718041891199e-10 0.99985157457387808 0
		 0.047197293490171432 1.7238606214523315 0.071078374981880202 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "LeftBrow0" -p "CenterFaceRoot";
	rename -uid "7CB7CB14-4E42-5C6F-E8D3-4EBECEE175FC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0075321166165990584 0.027960303937498043 0.050387157130960245 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.013796515762805939 1.7275872230529785 0.092293739318847656 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "CenterBrow" -p "CenterFaceRoot";
	rename -uid "9F47171F-4520-1545-6901-3B8D58FF84E3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.8791971549544119e-17 0.028221020522291806 0.050661740148030598 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0 1.7280647754669189 0.092796690762043013 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "LeftCheek0" -p "CenterFaceRoot";
	rename -uid "08CD9EA5-423A-E7A9-6E96-F4AFA41189AB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0092006319834028218 0.010100827387727218 0.045685114646912668 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99994816586230739 -0.0086531904711334481 -0.0053543124346693933 0
		 0.0086175796177977004 0.99994077194053121 -0.0066385790702577548 0 0.0054114405208526006 0.0065920941444742595 0.99996357003667125 0
		 0.016852721571922302 1.6948741674423218 0.083681046962738037 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftOribital0" -p "CenterFaceRoot";
	rename -uid "1EB1C622-4A80-2980-214F-61A08C2B699E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0097655121547911578 0.015585833142918282 0.042937026962143264 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.999980758340001 -0.0060252382038528934 -0.001476295957994878 0
		 0.00600719336928357 0.99991065104098542 -0.011936681181657069 0 0.0015480853999712079 0.011927583104809699 0.99992760587148111 0
		 0.017887407913804054 1.7049210071563721 0.0786473974585533 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftOribital1" -p "CenterFaceRoot";
	rename -uid "65A4906E-4E7D-23A2-06A7-448484CA449A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.01803920324643335 0.014495847780675808 0.040257885015728037 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.033042259514331818 1.7029244899749756 0.073740035295486464 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftCheeck2" -p "CenterFaceRoot";
	rename -uid "EBC35FF3-43E1-783B-B513-BEAB46372B7C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.027633661835276095 0.015423194416058772 0.034030372289872213 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99982527945173671 -2.9917566372197209e-12 -0.018692528210741851 0
		 0 1.0000000596046483 -1.6005094558707578e-10 0 0.018692529324124824 1.6002298139144732e-10 0.99982533900432524 0
		 0.050616350024938583 1.7046231031417847 0.062333151698112488 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftOribital2" -p "CenterFaceRoot";
	rename -uid "C2ECA5FC-453D-7199-1195-D6AEFC60AB87";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.022765830273284618 0.016859283322405383 0.037467254351789263 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99991486868810864 0.0087068661444996889 -0.0097183248601810188 0
		 -0.0086693756568399991 0.99995478206393806 0.0038931417718950246 0 0.0097517824819888677 -0.0038085585347036642 0.99994513770624549 0
		 0.041699983179569244 1.7072535753250122 0.068628460168838501 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "CenterJaw" -p "CenterFaceRoot";
	rename -uid "4BD4DD89-478A-D8B4-16E9-958A88039E46";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.6599177684984373e-06 0.0016931405620610462 0.011677983581001196 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 -1.0367224604124203e-05 1.679473876953125 0.021390466019511223 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Jaw";
	setAttr ".radi" 0.005;
createNode joint -n "CenterTongue0" -p "CenterJaw";
	rename -uid "7A83EA46-40BC-0913-CFF4-4DB056E43E6D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -0.017135184272950132 0.013567662232959087 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99962421681471014 4.3873376402637159e-12 0.027412133590816557 0
		 -0.000751425027667022 0.99962415727726572 0.027401830941119202 0 -0.027401830942224328 -0.027412131959500902 0.9992485154167966 0
		 -1.0367224604124203e-05 1.6480875015258787 0.046242240816354752 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Tongue";
	setAttr ".radi" 0.005;
createNode joint -n "CenterTongue1" -p "CenterTongue0";
	rename -uid "C3587538-4572-2FF8-A636-A6B60D937E6E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00016259377673133208 0.0038391677828594206 0.0058261734637325042 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99962421690425329 4.3873376406567195e-12 0.027412133593272048 0
		 -0.00075142511724382317 0.99962427644169471 0.02740183420767045 0 -0.0274018342063247 -0.02741213522482833 0.99924863444707079 0
		 -1.0367224604123986e-05 1.6548244953155518 0.057106833904981613 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "CenterTongue2" -p "CenterTongue1";
	rename -uid "2C660B81-4084-CF12-EDAB-E287BC5C6A3C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00026701740678021708 0.00078164858328144682 0.0097194125639332753 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99962421681470992 4.387337640263715e-12 0.02741213359081655 0
		 -0.00075142502766702189 0.9996241572772655 0.027401830941119198 0 -0.027401830942224325 -0.027412131959500902 0.99924851541679649 0
		 -1.0367224604125233e-05 1.6557676792144782 0.074949063360691084 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "CenterLowerTeeth" -p "CenterJaw";
	rename -uid "5D2E8E9B-42D7-8DF4-F8B4-79B2B7FC4374";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.6627856853679112e-06 -0.018194451158394354 0.026469925883402908 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039534912 -1.1007708443210324e-07 0
		 0 1.1007708443210324e-07 0.99999994039534912 0 5.2531397010113778e-09 1.6461472511291504 0.069875210523605347 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Teeth";
	setAttr ".radi" 0.005;
createNode joint -n "LowerLip0" -p "CenterJaw";
	rename -uid "8F61C6CE-4D5A-EC32-BF20-E0B6E3481AA9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.6599177684596457e-06 -0.016619217954908061 0.036208729191167272 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0 1.6490325927734375 0.08771369606256485 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Mouth";
	setAttr ".radi" 0.005;
createNode joint -n "LowerLip1" -p "CenterJaw";
	rename -uid "90DF7271-44FF-6AF0-4F16-39A7990256A2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0082701394315284459 -0.016006410325078657 0.032676181357005812 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99992804128312041 0.0029193118987892782 -0.011635714700185155 0
		 -0.0028719884605426923 0.99998748599532938 0.0040817063491259036 0 0.011647484864897785 -0.0040479949964907077 0.99992391242519885 0
		 0.015137978829443455 1.6501550674438477 0.081243157386779785 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Mouth";
	setAttr ".radi" 0.005;
createNode joint -n "LeftDepressor" -p "CenterJaw";
	rename -uid "1B666085-45C1-EAAA-4EC0-EDB04CBC6530";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.014500594554243199 -0.017055264163820416 0.027615381042615589 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99991615622929153 0.0070893804979241335 -0.010836105195396644 0
		 -0.0070063364599608291 0.99994588454384814 0.0076824494659618551 0 0.010889982602195317 -0.0076058839416233981 0.99991171590958061 0
		 0.026550251990556717 1.648233890533447 0.071973331272602081 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Mouth";
	setAttr ".radi" 0.005;
createNode joint -n "LowerLip2" -p "CenterJaw";
	rename -uid "F537F324-40B6-002A-CB2D-3F8EE9B09ACC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.013781372531971401 -0.013234718383142163 0.025921252029164153 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99991017889838973 -2.1451251097327785e-12 -0.013402765161578819 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.013402764362998769 1.600365505604112e-10 0.99991011932051077 0
		 0.025232858955860138 1.6552319526672363 0.068870209157466888 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "MouthCorner" -p "CenterJaw";
	rename -uid "C787B78C-41D2-5A20-C37F-8E90F8E6340D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.014879781884395532 -0.012756824752914508 0.025562762657493607 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99991017889838973 -2.1451251097327785e-12 -0.013402765161578819 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.013402764362998769 1.600365505604112e-10 0.99991011932051077 0
		 0.027244806289672852 1.6561073064804075 0.068213567137718201 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "CenterChin" -p "CenterJaw";
	rename -uid "122BBB0D-491D-ECD5-AD18-38BC33410FCF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.6599177684596457e-06 -0.024322462370676923 0.033760053122692535 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0 1.6349226236343382 0.083228476345539093 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Chin";
	setAttr ".radi" 0.005;
createNode joint -n "MouthCorner1" -p "CenterJaw";
	rename -uid "9F936CEC-46FA-693A-39B6-7C9E8E1FD0A0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.01487974008223154 -0.012756665555957558 0.025562716418998755 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99991017889838973 -2.1451251097327785e-12 -0.013402765161578819 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.013402764362998769 1.600365505604112e-10 0.99991011932051077 0
		 0.027244806289672852 1.6561073064804075 0.068213567137718201 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LowerLip3" -p "CenterJaw";
	rename -uid "3345A10A-4DB7-83E9-0492-96963A76C061";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.013781340082231541 -0.013234665555957537 0.025921216418998753 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99991017889838973 -2.1451251097327785e-12 -0.013402765161578819 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.013402764362998769 1.600365505604112e-10 0.99991011932051077 0
		 0.025232858955860138 1.6552319526672363 0.068870209157466888 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LowerLip4" -p "CenterJaw";
	rename -uid "4A609AE9-48AF-7860-F39B-9B9220120B2B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0082701400822315398 -0.016006665555957533 0.03267621641899876 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99992804128312041 0.0029193118987892782 -0.011635714700185155 0
		 -0.0028719884605426923 0.99998748599532938 0.0040817063491259036 0 0.011647484864897785 -0.0040479949964907077 0.99992391242519885 0
		 0.015137978829443455 1.6501550674438477 0.081243157386779785 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Mouth";
	setAttr ".radi" 0.005;
createNode joint -n "RightDepressor" -p "CenterJaw";
	rename -uid "A4FB12DF-4598-9F77-BA75-E1A2FAEA7443";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.01450064008223154 -0.0170556655559575 0.027615416418998753 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99991615622929153 0.0070893804979241335 -0.010836105195396644 0
		 -0.0070063364599608291 0.99994588454384814 0.0076824494659618551 0 0.010889982602195317 -0.0076058839416233981 0.99991171590958061 0
		 0.026550251990556717 1.648233890533447 0.071973331272602081 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Mouth";
	setAttr ".radi" 0.005;
createNode joint -n "LeftEye" -p "CenterFaceRoot";
	rename -uid "CC671BBB-4FCF-A417-F251-61AB167BF0AF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.014930026995677347 0.023083224700537808 0.032759564015598264 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.027347207069396973 1.7186539173126221 0.060005422681570053 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftEyeAim" -p "LeftEye";
	rename -uid "B11E880F-462F-71C9-0ABF-ED831C3836B0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.027347207069396973 1.7186539173126221 0.060005422681570053 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftLowerLid" -p "LeftEye";
	rename -uid "09AF11A0-4435-3C3F-75A2-AFBFCA6A57DB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -9.2611008543186379e-05 -1.4814538484841933e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.027347207069396973 1.7184842824935913 0.060005422681570053 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftLowerLid0" -p "LeftLowerLid";
	rename -uid "00135E3C-4EB2-10E2-E9B8-58B5EE64EBFB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0021927470420077966 -0.0038288111353110832 0.0085340893865391079 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.023330770432949066 1.7114710807800293 0.075637243688106537 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftLowerLid1" -p "LeftLowerLid";
	rename -uid "92304231-4B0B-EF70-C2CA-87918C51B438";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0033613569869715681 -0.0037612565133783304 0.0079089203353357382 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.033504176884889603 1.711594820022583 0.074492126703262329 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftLowerLid2" -p "LeftLowerLid";
	rename -uid "518F3961-4C92-2E44-0107-66BB44610E59";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0069097359019255119 -0.0026313761761551646 0.0054907512326138955 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.040003713220357895 1.7136644124984739 0.070062786340713501 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftUpperLid" -p "LeftEye";
	rename -uid "72F494BE-47BB-4E61-3100-668F10B8DEB1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 9.2611008543297402e-05 1.4828416272649747e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.027347207069396973 1.7188235521316528 0.060005422681570053 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftUpperLid0" -p "LeftUpperLid";
	rename -uid "9BD6F6B1-4C12-3BDA-8E74-8CADB4889D01";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0020672068161569305 -0.00020565761709234742 0.0093334572723050083 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.023560721427202225 1.7184468507766724 0.077101439237594604 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftUpperLid1" -p "LeftUpperLid";
	rename -uid "4EB8119A-4C77-7748-55CC-51B0448FEDEE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0034662623021434313 0.00018274891779823665 0.0086171822228505307 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.033696331083774567 1.7191582918167116 0.075789444148540497 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftUpperLid2" -p "LeftUpperLid";
	rename -uid "37E8B974-46CE-D5C1-FE5B-2E9374BB964B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00686390630629761 -0.00021144987222421197 0.0062264449822185264 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.039919767528772354 1.7184362411499023 0.071410350501537323 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftEyeInnerCorner" -p "LeftEye";
	rename -uid "AA85D736-4AA2-2E29-15CC-F38A1417F27E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0058602617540990075 -0.0015945624188230534 0.0073258875036135776 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.016613014042377472 1.7157331705093384 0.073424190282821655 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftEyeOutterCorner" -p "LeftEye";
	rename -uid "5D89E14D-4002-A39F-CEA1-A285202A14D9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0085600406448164221 -0.0011557177024149601 0.0036291023762080044 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.04302656278014183 1.7165369987487793 0.066652819514274597 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftInnerBrow" -p "CenterFaceRoot";
	rename -uid "C1486FC6-4878-2C68-8421-C6B733F0D5BB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.005916731670438961 0.021537538505599474 0.043721580666398752 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.01083762850612402 1.715822696685791 0.080084457993507371 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightBrow0" -p "CenterFaceRoot";
	rename -uid "AA56967E-4906-4390-C236-FF8141EBA032";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0075321200000000388 0.027960475006103547 0.050387199999999951 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.013796515762805939 1.7275872230529785 0.092293739318847656 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "RightBrow1" -p "CenterFaceRoot";
	rename -uid "E68A3343-4C44-37C1-FA12-50AAB7CD24E0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.015846800000000039 0.028333475006103503 0.049119399999999952 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99998653201289356 -8.2881941589821039e-13 -0.0051784727810232191 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.0051784724723787428 1.6004877094421391e-10 0.99998647241224836 0
		 0.029026426374912262 1.7282711267471313 0.089971616864204421 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "RightBrow2" -p "CenterFaceRoot";
	rename -uid "AC4F98A4-46E5-E917-569C-A983CAF2ABFC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.021438000000000037 0.028550475006103526 0.045400999999999948 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99994413568560103 -1.6917428961667926e-12 -0.010570028129462937 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.010570027499580945 1.6004198537437016e-10 0.99994407609760416 0
		 0.039267841726541519 1.7286689281463623 0.083160668611526475 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "RightBrow3" -p "CenterFaceRoot";
	rename -uid "20CC3817-4FB5-4E81-6E69-C7B758E65C01";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.025767100000000039 0.025925475006103538 0.038804799999999952 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99985163413431433 -2.7569194582230784e-12 -0.017225262946343481 0
		 0 0.99999994039535522 -1.6005092650751683e-10 0 0.017225261920247068 1.6002718041891199e-10 0.99985157457387808 0
		 0.047197293490171432 1.7238606214523315 0.071078374981880202 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Brow";
	setAttr ".radi" 0.005;
createNode joint -n "RightInnerBrow" -p "CenterFaceRoot";
	rename -uid "EB2DF292-45BC-F537-40F2-0AA1DE60A444";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0059167300000000393 0.021537475006103479 0.043721599999999951 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.01083762850612402 1.715822696685791 0.080084457993507371 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightEye" -p "CenterFaceRoot";
	rename -uid "924C86AA-46DF-3D55-B83B-729AAC90356E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.014930000000000039 0.023083475006103527 0.032759599999999951 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.027347207069396973 1.7186539173126221 0.060005422681570053 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightEyeAim" -p "RightEye";
	rename -uid "F12C3CB8-4CC4-869E-1F3C-C0A6B2A44BB2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.027347207069396973 1.7186539173126221 0.060005422681570053 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightLowerLid" -p "RightEye";
	rename -uid "B39732EC-4B5B-493D-E2BD-EAB6E4392905";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 9.3000000000009742e-05 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.027347207069396973 1.7184842824935913 0.060005422681570053 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightLowerLid0" -p "RightLowerLid";
	rename -uid "4D11DA89-461C-08ED-7800-38B05D71121C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0021927000000000006 0.0038289999999999713 -0.0085341000000000097 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.023330770432949066 1.7114710807800293 0.075637243688106537 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightLowerLid1" -p "RightLowerLid";
	rename -uid "C8EFDCD8-4506-E29A-F81C-FCA461CC4296";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0033613999999999988 0.0037610000000000143 -0.0079089000000000104 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.033504176884889603 1.711594820022583 0.074492126703262329 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightLowerLid2" -p "RightLowerLid";
	rename -uid "2A05C56B-4C60-42FD-E12F-2D963A9BF192";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0069097999999999989 0.00263100000000005 -0.0054907000000000011 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.040003713220357895 1.7136644124984739 0.070062786340713501 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightUpperLid" -p "RightEye";
	rename -uid "2ACB26C8-484B-BE92-8687-95BF47CE1069";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -9.1999999999980986e-05 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.027347207069396973 1.7188235521316528 0.060005422681570053 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightUpperLid0" -p "RightUpperLid";
	rename -uid "A3F226D8-4ADB-1F4E-BA8D-A9B6C13D4A65";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0020671999999999999 0.00020500000000001073 -0.0093333999999999986 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.023560721427202225 1.7184468507766724 0.077101439237594604 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightUpperLid1" -p "RightUpperLid";
	rename -uid "6FBF7B79-40AC-8D17-F06A-438BC536F658";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0034663000000000003 -0.00018300000000004424 -0.0086171000000000025 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.033696331083774567 1.7191582918167116 0.075789444148540497 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightUpperLid2" -p "RightUpperLid";
	rename -uid "33C01A68-489B-815B-18C5-E69EBD1053B7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0068639000000000009 0.00021099999999996122 -0.0062264 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000596046483 -1.6005094558707578e-10 0
		 0 1.6005094558707578e-10 1.0000000596046483 0 0.039919767528772354 1.7184362411499023 0.071410350501537323 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightEyeInnerCorner" -p "RightEye";
	rename -uid "B8B4E46C-4641-9EDB-AB38-4EABAC5F24CA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.005860230000000001 0.0015950000000000131 -0.0073259000000000032 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.016613014042377472 1.7157331705093384 0.073424190282821655 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightEyeOutterCorner" -p "RightEye";
	rename -uid "95822850-471D-A3FD-35BB-47A1BD6CE6C7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0085600999999999993 0.0011560000000000459 -0.0036291000000000032 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.04302656278014183 1.7165369987487793 0.066652819514274597 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightOribital0" -p "CenterFaceRoot";
	rename -uid "85F8B499-45BC-6B71-050F-6DB085AE0202";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.009765510000000038 0.015585475006103522 0.042936999999999954 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.999980758340001 -0.0060252382038528934 -0.001476295957994878 0
		 0.00600719336928357 0.99991065104098542 -0.011936681181657069 0 0.0015480853999712079 0.011927583104809699 0.99992760587148111 0
		 0.017887407913804054 1.7049210071563721 0.0786473974585533 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightOribital1" -p "CenterFaceRoot";
	rename -uid "6DE28F28-4B57-0971-3AE6-0CABD6B5364B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.018039200000000036 0.014495475006103486 0.040257899999999951 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99999994039535522 -1.6005092650751683e-10 0
		 0 1.6005092650751683e-10 0.99999994039535522 0 0.033042259514331818 1.7029244899749756 0.073740035295486464 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightOribital2" -p "CenterFaceRoot";
	rename -uid "21111C72-4D47-BA1A-9A51-B38FFEF1CA15";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.022765800000000037 0.016859475006103519 0.037467299999999953 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99991486868810864 0.0087068661444996889 -0.0097183248601810188 0
		 -0.0086693756568399991 0.99995478206393806 0.0038931417718950246 0 0.0097517824819888677 -0.0038085585347036642 0.99994513770624549 0
		 0.041699983179569244 1.7072535753250122 0.068628460168838501 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightCheeck2" -p "CenterFaceRoot";
	rename -uid "CCA9BFCB-4D89-28A7-C63B-648C7C41E7ED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.027633700000000039 0.015423475006103526 0.034030399999999954 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99982527945173671 -2.9917566372197209e-12 -0.018692528210741851 0
		 0 1.0000000596046483 -1.6005094558707578e-10 0 0.018692529324124824 1.6002298139144732e-10 0.99982533900432524 0
		 0.050616350024938583 1.7046231031417847 0.062333151698112488 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightCheek0" -p "CenterFaceRoot";
	rename -uid "5303F32F-447C-FEFA-AD6D-7BAD7F6654F0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0092006300000000377 0.01010047500610356 0.045685099999999951 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99994816586230739 -0.0086531904711334481 -0.0053543124346693933 0
		 0.0086175796177977004 0.99994077194053121 -0.0066385790702577548 0 0.0054114405208526006 0.0065920941444742595 0.99996357003667125 0
		 0.016852721571922302 1.6948741674423218 0.083681046962738037 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightCheeck1" -p "CenterFaceRoot";
	rename -uid "472A1B72-40D6-BFDC-F6CF-14B3EE7FCA92";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.019562100000000037 0.0064314750061035264 0.039949299999999952 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.9999609813207091 -1.4138563552889919e-12 -0.0088337899809045085 0
		 0 1.0000000596046483 -1.6005094558707578e-10 0 0.0088337905073572788 1.6004470060907094e-10 0.99996104091372984 0
		 0.035831715911626816 1.6881530284881592 0.073174826800823226 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightZygomaticus1" -p "CenterFaceRoot";
	rename -uid "A5BD3700-4A14-9465-3EE1-AC9995944A3B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.025875600000000037 -0.001291524993896509 0.030137799999999951 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99977266877401283 -3.4125427891361438e-12 -0.021321604692944231 0
		 9.742367378152865e-05 0.99998962054340368 0.0045682078965685229 0 0.021321382114249224 -0.0045692463567309927 0.99976223203233516 0
		 0.047396149486303329 1.6740075349807739 0.055203128606081009 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightZygomaticus0" -p "CenterFaceRoot";
	rename -uid "443C659F-416E-675D-6227-A18A1F12D941";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.021512700000000037 -0.0078865249938965265 0.035627099999999953 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99986224699104098 0.0019415241467081864 -0.01648385752348995 0
		 -0.0018318852308002965 0.99997617835082642 0.0066637929348080669 0 0.016496401781913209 -0.0066326780465827085 0.99984192564511898 0
		 0.039404548704624176 1.6619266271591189 0.065257832407951355 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "UpperLip3" -p "CenterFaceRoot";
	rename -uid "B29BBF66-4049-002E-D59F-73A4D93567C4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.014072400000000039 -0.010316524993896459 0.038295399999999952 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99990812596593193 -2.1695000269955365e-12 -0.013555059911392433 0
		 0 1.0000000596046483 -1.6005094558707578e-10 0 0.013555060719040111 1.6003624105754294e-10 0.99990818554320282 0
		 0.025776300579309464 1.6574763059616091 0.070145457983016968 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "UpperLip4" -p "CenterFaceRoot";
	rename -uid "1DF681EB-4219-E463-5953-0AAF06003377";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0077171800000000387 -0.0086865249938964384 0.045195399999999948 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99990910197999294 -0.0054797845958873114 -0.012319081135268431 0
		 0.0054480029865535884 0.99998180786220547 -0.0026119750871369564 0 0.012333169350356396 0.0025446231212391825 0.99992070576061853 0
		 0.014135497622191906 1.6604614257812502 0.082784108817577362 1;
	setAttr ".sd" 3;
	setAttr ".otp" -type "string" "Mouth";
	setAttr ".radi" 0.005;
createNode joint -n "RightNasolabial1" -p "CenterFaceRoot";
	rename -uid "24CD156F-43ED-97DC-9620-B685BCD73930";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.011182800000000038 -0.0042485249938964964 0.043726299999999954 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99991611273346548 -0.0072160238672589871 -0.010756231474902973 0
		 0.0071792046443295661 0.99996831045247458 -0.0034577904295217269 0 0.010780842112912492 0.0033802791779274036 0.99993623114249675 0
		 0.020483456552028656 1.6685912609100344 0.080093041062355042 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "CenterNose" -p "CenterFaceRoot";
	rename -uid "F503107E-43DA-7A66-0431-7099675A11CF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.8791971549544119e-17 0.00016450572072224112 0.04837420744940877 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99999956330308104 0.00015751349743468838 -0.00092118567138740036 0
		 -0.00015751355502527739 0.99999992799009596 -1.6005092452204348e-10 0 0.00092118560502779136 1.4525928079321933e-07 0.99999951610382043 0
		 0 1.6766738891601563 0.10634275525808334 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "RightNasolabial0" -p "CenterNose";
	rename -uid "A2CC9FF8-4938-DDF3-274A-B9AC1A11820A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0071524400000000004 0.00050196928538126517 -0.00025920744940882007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 0.99999956330318518 0.00015751349743470478 -0.00092118567138749631 0
		 -0.00016083174426011996 0.99999355522109146 -0.0036031734247140199 0 0.00092061218610142714 0.0036033200071176161 0.99999314386016092 0
		 0.013101068325340748 1.6775926351547243 0.088131770491600037 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "LeftNasolabial0" -p "CenterNose";
	rename -uid "CE058CB4-49BF-EC74-7CAF-44A45B2C5B52";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.0071524416845672005 0.00050158330646998817 -0.00025924970275065934 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99999956330318518 0.00015751349743470478 -0.00092118567138749631 0
		 -0.00016083174426011996 0.99999355522109146 -0.0036031734247140199 0 0.00092061218610142714 0.0036033200071176161 0.99999314386016092 0
		 0.013101068325340748 1.6775926351547243 0.088131770491600037 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
createNode joint -n "CenterNoseTip" -p "CenterNose";
	rename -uid "43C93901-449D-27AF-50EE-C99733B1766C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0 0.0096829170965623407 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99999956330308104 0.00015751349743468838 -0.00092118567138740036 0
		 -0.00015751355502527739 0.99999992799009596 -1.6005092452204348e-10 0 0.00092118560502779136 1.4525928079321933e-07 0.99999951610382043 0
		 0 1.6766738891601563 0.10634275525808334 1;
	setAttr ".sd" 3;
	setAttr ".radi" 0.005;
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
connectAttr "CenterFaceRoot.s" "LeftZygomaticus1.is";
connectAttr "CenterFaceRoot.s" "LeftZygomaticus0.is";
connectAttr "CenterFaceRoot.s" "LeftCheeck1.is";
connectAttr "CenterFaceRoot.s" "LeftNasolabial1.is";
connectAttr "CenterFaceRoot.s" "UpperLip0.is";
connectAttr "CenterFaceRoot.s" "CenterUpperTeeth.is";
connectAttr "CenterFaceRoot.s" "UpperLip1.is";
connectAttr "CenterFaceRoot.s" "UpperLip2.is";
connectAttr "CenterFaceRoot.s" "LeftBrow1.is";
connectAttr "CenterFaceRoot.s" "LeftBrow2.is";
connectAttr "CenterFaceRoot.s" "LeftBrow3.is";
connectAttr "CenterFaceRoot.s" "LeftBrow0.is";
connectAttr "CenterFaceRoot.s" "CenterBrow.is";
connectAttr "CenterFaceRoot.s" "LeftCheek0.is";
connectAttr "CenterFaceRoot.s" "LeftOribital0.is";
connectAttr "CenterFaceRoot.s" "LeftOribital1.is";
connectAttr "CenterFaceRoot.s" "LeftCheeck2.is";
connectAttr "CenterFaceRoot.s" "LeftOribital2.is";
connectAttr "CenterFaceRoot.s" "CenterJaw.is";
connectAttr "CenterJaw.s" "CenterTongue0.is";
connectAttr "CenterTongue0.s" "CenterTongue1.is";
connectAttr "CenterTongue1.s" "CenterTongue2.is";
connectAttr "CenterJaw.s" "CenterLowerTeeth.is";
connectAttr "CenterJaw.s" "LowerLip0.is";
connectAttr "CenterJaw.s" "LowerLip1.is";
connectAttr "CenterJaw.s" "LeftDepressor.is";
connectAttr "CenterJaw.s" "LowerLip2.is";
connectAttr "CenterJaw.s" "MouthCorner.is";
connectAttr "CenterJaw.s" "CenterChin.is";
connectAttr "CenterJaw.s" "MouthCorner1.is";
connectAttr "CenterJaw.s" "LowerLip3.is";
connectAttr "CenterJaw.s" "LowerLip4.is";
connectAttr "CenterJaw.s" "RightDepressor.is";
connectAttr "CenterFaceRoot.s" "LeftEye.is";
connectAttr "LeftEye.s" "LeftEyeAim.is";
connectAttr "LeftEye.s" "LeftLowerLid.is";
connectAttr "LeftLowerLid.s" "LeftLowerLid0.is";
connectAttr "LeftLowerLid.s" "LeftLowerLid1.is";
connectAttr "LeftLowerLid.s" "LeftLowerLid2.is";
connectAttr "LeftEye.s" "LeftUpperLid.is";
connectAttr "LeftUpperLid.s" "LeftUpperLid0.is";
connectAttr "LeftUpperLid.s" "LeftUpperLid1.is";
connectAttr "LeftUpperLid.s" "LeftUpperLid2.is";
connectAttr "LeftEye.s" "LeftEyeInnerCorner.is";
connectAttr "LeftEye.s" "LeftEyeOutterCorner.is";
connectAttr "CenterFaceRoot.s" "LeftInnerBrow.is";
connectAttr "CenterFaceRoot.s" "RightBrow0.is";
connectAttr "CenterFaceRoot.s" "RightBrow1.is";
connectAttr "CenterFaceRoot.s" "RightBrow2.is";
connectAttr "CenterFaceRoot.s" "RightBrow3.is";
connectAttr "CenterFaceRoot.s" "RightInnerBrow.is";
connectAttr "CenterFaceRoot.s" "RightEye.is";
connectAttr "RightEye.s" "RightEyeAim.is";
connectAttr "RightEye.s" "RightLowerLid.is";
connectAttr "RightLowerLid.s" "RightLowerLid0.is";
connectAttr "RightLowerLid.s" "RightLowerLid1.is";
connectAttr "RightLowerLid.s" "RightLowerLid2.is";
connectAttr "RightEye.s" "RightUpperLid.is";
connectAttr "RightUpperLid.s" "RightUpperLid0.is";
connectAttr "RightUpperLid.s" "RightUpperLid1.is";
connectAttr "RightUpperLid.s" "RightUpperLid2.is";
connectAttr "RightEye.s" "RightEyeInnerCorner.is";
connectAttr "RightEye.s" "RightEyeOutterCorner.is";
connectAttr "CenterFaceRoot.s" "RightOribital0.is";
connectAttr "CenterFaceRoot.s" "RightOribital1.is";
connectAttr "CenterFaceRoot.s" "RightOribital2.is";
connectAttr "CenterFaceRoot.s" "RightCheeck2.is";
connectAttr "CenterFaceRoot.s" "RightCheek0.is";
connectAttr "CenterFaceRoot.s" "RightCheeck1.is";
connectAttr "CenterFaceRoot.s" "RightZygomaticus1.is";
connectAttr "CenterFaceRoot.s" "RightZygomaticus0.is";
connectAttr "CenterFaceRoot.s" "UpperLip3.is";
connectAttr "CenterFaceRoot.s" "UpperLip4.is";
connectAttr "CenterFaceRoot.s" "RightNasolabial1.is";
connectAttr "CenterFaceRoot.s" "CenterNose.is";
connectAttr "CenterNose.s" "RightNasolabial0.is";
connectAttr "CenterNose.s" "LeftNasolabial0.is";
connectAttr "CenterNose.s" "CenterNoseTip.is";
// End of skeleton_biped_male_face.ma
