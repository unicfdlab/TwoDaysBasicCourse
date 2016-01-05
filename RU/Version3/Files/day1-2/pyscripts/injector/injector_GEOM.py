##############################################################################################
# Script for generating In(-E)jector hexahedral geomtry and mesh, using
# base dimensions, for CFD simulation
#
# Authors: Kraposhin M., Gusha E.
# Moscow, RRC "Kurchatovsky Institute", 2009
# Published under GPL (see www.fsf.org)
#
# www.os-cfd.ru, os-cfd@yandex.ru
#
##############################################################################################

import geompy
import math
import SALOMEDS

def CreateGEOM(injLens, injRads, injAngs, wallS):
	L1 = injLens[0]
	L2 = injLens[1]
	L3 = injLens[2]
	L4 = injLens[3]
	L5 = injLens[4]
	L6 = injLens[5]
	#
	R0 = injRads[0]
	R1 = injRads[1]
	R2 = injRads[2]
	R3 = injRads[3]
	R4 = injRads[4]
	#
	A1 = injAngs[0]
	#
	S  = wallS
	#
	# Printing input
	#
	LSUMM = L1 + L2 + L3 + L4 + L5 + L6
	DX1= math.tan(A1*math.pi/180.)*L3 + R3 - R0
	#
	print "Input Data"
	print "L1, L2, L3, L4, L5, L6"
	print L1, L2, L3, L4, L5, L6
	print "R0, R1, R2, R3, R4"
	print R0, R1, R2, R3, R4
	print "A1 = ", A1
	print "S = ", S
	#
	print "Intermediate variables: "
	print "LSUMM = ", LSUMM
	print "DX1 = ", DX1
	#
	#
	#
	#
	oXYZ = geompy.MakeVertex(0, 0, 0)
	xPnt = geompy.MakeVertex(1, 0, 0)
	yPnt = geompy.MakeVertex(0, 1, 0)
	zPnt = geompy.MakeVertex(0, 0, 1)
	oX   = geompy.MakeVector(oXYZ, xPnt)
	oY   = geompy.MakeVector(oXYZ, yPnt)
	oZ   = geompy.MakeVector(oXYZ, zPnt)
	#
	# Inlet and nozzle points and faces
	#
	P000 = geompy.MakeVertexWithRef(oXYZ, -(L1+L2), R1, 0)
	P001 = geompy.MakeVertexWithRef(oXYZ, -L2, R1, 0)
	P002 = geompy.MakeVertexWithRef(oXYZ, -L2, 0, 0)
	P003 = geompy.MakeVertexWithRef(oXYZ, -(L1+L2), 0, 0)
	#
	P004 = geompy.MakeVertexWithRef(oXYZ, 0, R2, 0)
	P005 = geompy.MakeVertexWithRef(oXYZ, 0, 0, 0)
	#
	P006 = geompy.MakeVertexWithRef(P000, 0, S, 0)
	P007 = geompy.MakeVertexWithRef(P006, L1,0, 0)
	P008 = geompy.MakeVertexWithRef(oXYZ, DX1,R0,0)
	P009 = geompy.MakeVertexWithRef(oXYZ, -(L1+L2), R0, 0)
	#
	F000 = geompy.MakeQuad4Vertices(P000, P001, P002, P003)
	F001 = geompy.MakeQuad4Vertices(P001, P002, P005, P004)
	F002 = geompy.MakeQuad4Vertices(P006, P007, P008, P009)
	#
	# Mixing chamber
	#
	P009 = geompy.MakeVertexWithRef(P004, 0, S, 0)
	P010 = geompy.MakeVertexWithRef(P005, L3,0, 0)
	P011 = geompy.MakeVertexWithRef(P010, 0,R3, 0)
	E000 = geompy.MakeLineTwoPnt(P008, P011)
	P012 = geompy.MakeVertexOnCurve(E000,0.9)
	P013 = geompy.MakeVertexWithRef(P010, L4, 0, 0)
	P014 = geompy.MakeVertexWithRef(P013, 0, R3, 0)
	#
	F003 = geompy.MakeQuad4Vertices(P009, P007, P008, P012)
	F004 = geompy.MakeQuad4Vertices(P004, P009, P012, P011)
	F005 = geompy.MakeQuad4Vertices(P004, P005, P010, P011)
	F006 = geompy.MakeQuad4Vertices(P010, P011, P014, P013)
	#
	# Diffusor and out tube
	#
	P015 = geompy.MakeVertexWithRef(P013, L5, 0, 0)
	P016 = geompy.MakeVertexWithRef(P015, 0, R4, 0)
	P017 = geompy.MakeVertexWithRef(P016, L6, 0, 0)
	P018 = geompy.MakeVertexWithRef(P017, 0, -R4,0)
	#
	F007 = geompy.MakeQuad4Vertices(P013, P014, P016, P015)
	F008 = geompy.MakeQuad4Vertices(P015, P016, P017, P018)
	#
	faceComp = geompy.MakeShell([F000, F001, F002, F003, F004, F005, F006, F007, F008])
	# 
	# Solid geomtry
	#
	sBase1 = geompy.MakeRotation(faceComp, oX, 0)
	sBase2 = geompy.MakeRotation(sBase1, oX, 45.*math.pi/180.)
	sBase3 = geompy.MakeRotation(sBase2, oX, 90.*math.pi/180.)
	#
	solid1 = geompy.MakeRevolution(sBase1, oX, 45.*math.pi/180.)
	solid2 = geompy.MakeRevolution(sBase2, oX, 90.*math.pi/180.)
	solid3 = geompy.MakeRevolution(sBase3, oX, 45.*math.pi/180.)
	#
	# Cutters
	#
	E002 = geompy.MakeLineTwoPnt(P005, P004)
	E003 = geompy.MakeRotation(E002, oX, 45.*math.pi/180.)
	E004 = geompy.MakeRotation(E003, oX, 90.*math.pi/180.)
	E005 = geompy.MakeRotation(E004, oX, 45.*math.pi/180.)
	P019 = geompy.MakeVertexOnCurve(E002,0.5)
	P020 = geompy.MakeVertexOnCurve(E003,0.5)
	P021 = geompy.MakeVertexOnCurve(E004,0.5)
	P022 = geompy.MakeVertexOnCurve(E005,0.5)
	zmin = geompy.PointCoordinates(oXYZ)[2]
	zmax = geompy.PointCoordinates(P020)[2]
	ymin = geompy.PointCoordinates(P022)[1]
	ymax = geompy.PointCoordinates(P019)[1]
	print "ymin, ymax, zmin, zmax"
	print ymin, ymax, zmin, zmax
	#
	E006 = geompy.MakeLineTwoPnt(P019, P020)
	E007 = geompy.MakeLineTwoPnt(P020, P021)
	E008 = geompy.MakeLineTwoPnt(P021, P022)
	E009 = geompy.MakeLineTwoPnt(P021, P022)
	edgeComp1 = geompy.MakeCompound([E006, E007, E008, E009])
	edgeComp2 = geompy.MakeTranslation(edgeComp1, -(2*L1 + 2*L2), 0, 0)
	cutter1 = geompy.MakePrismVecH(edgeComp2, oX, LSUMM*2)
	#
	# Hexa solid
	#
	solid1_hex_v1 = geompy.MakePartition([solid1], [cutter1], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
	solid2_hex_v1 = geompy.MakePartition([solid2], [cutter1], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
	solid3_hex_v1 = geompy.MakePartition([solid3], [cutter1], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
	dom_v1 = geompy.MakeCompound([solid1_hex_v1, solid2_hex_v1, solid3_hex_v1])
	hsolids1 = geompy.SubShapeAll(dom_v1, geompy.ShapeType["SOLID"])
	nSolids = len(hsolids1)
	hsolids2 = []
	for jSolid in xrange(0,nSolids):
		solidCDG = geompy.MakeCDG(hsolids1[jSolid])
		coordCDG = geompy.PointCoordinates(solidCDG)
		ys = coordCDG[1]
		zs = coordCDG[2]
		zOk = (zs >= zmin) * (zs <= zmax)
		yOk = (ys >= ymin) * (ys <= ymax)
		if not(zOk and yOk):
			hsolids2.append(hsolids1[jSolid])
	
	# Creasting hexahedrons near the center
	sBase4 = geompy.MakeQuad4Vertices(P019, P020, P021, P022)
	sBase5 = geompy.MakeTranslation(sBase4, -(L1 + L2), 0, 0)
	hsolids2.append(geompy.MakePrismVecH(sBase5, oX, L1))
	sBase6 = geompy.MakeTranslation(sBase5, L1, 0, 0)
	hsolids2.append(geompy.MakePrismVecH(sBase6, oX, L2))
	sBase7 = geompy.MakeTranslation(sBase6, L2, 0, 0)
	hsolids2.append(geompy.MakePrismVecH(sBase7, oX, L3))
	sBase8 = geompy.MakeTranslation(sBase7, L3, 0, 0)
	hsolids2.append(geompy.MakePrismVecH(sBase8, oX, L4))
	sBase9 = geompy.MakeTranslation(sBase8, L4, 0, 0)
	hsolids2.append(geompy.MakePrismVecH(sBase9, oX, L5))
	sBase10= geompy.MakeTranslation(sBase9,L5, 0, 0)
	hsolids2.append(geompy.MakePrismVecH(sBase10, oX, L6))
	#
	# Domain 
	#
	dom_v2   = geompy.MakeCompound(hsolids2)
	dom_comp = geompy.MakeGlueFaces(dom_v2,1.0E-6)
	return dom_comp

#END_OF_FILE


