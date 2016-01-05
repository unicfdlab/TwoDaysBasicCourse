#
#
#
#
import geompy
import faceSelect
import edgeSelect
import salome
import geompy
import math
#
def injectorFaceGroups (injGeom, aInjLens, aInjRads, aWallS ,aTol):
	#
	L1=     aInjLens[0]
	L2=     aInjLens[1]
	L3=     aInjLens[2]
	L4=     aInjLens[3]
	L5=     aInjLens[4]
	L6=     aInjLens[5]
	#
	R0=     aInjRads[0]
	R1=     aInjRads[1]
	R2=     aInjRads[2]
	R3=     aInjRads[3]
	R4=     aInjRads[4]
	#
	S =     aWallS
	#
	RMAX  = R0
	LSUMM = L1 + L2 + L3 + L4 + L5 + L6
	XMIN  = -L1 -L2
	XMAX  = LSUMM + XMIN
	HALFR2= R2*0.5
	#
	vertex1 = geompy.MakeVertex(0, 0, 0)
	vertex2 = geompy.MakeVertex(0, 0, 1)
	vector1 = geompy.MakeVector(vertex1, vertex2)
	#
	vertex3 = geompy.MakeVertex(1, 0, 0)
	vertex4 = geompy.MakeVertex(XMIN, 0, 0)
	Xvector = geompy.MakeVector(vertex1, vertex3)
	#
	symmWalls = faceSelect.SelectFacesWithNormalParallelToVec(injGeom, [vector1], aTol)
	#
	# now, remove all faces which are in small quadrangle 
	#
	selGroup0faces = []
	selGroup0faces = geompy.SubShapeAll(symmWalls, geompy.ShapeType["FACE"])
	nFaces = len(selGroup0faces)
	idsToRemove = []
	nToRemove=0
	for jFace in range(0,nFaces):
		jFaceCOM  = geompy.MakeCDG(selGroup0faces[jFace])
		COMCoords = geompy.PointCoordinates(jFaceCOM)
		jFaceID   = geompy.GetSubShapeID(injGeom, selGroup0faces[jFace])
		ZCoord = COMCoords[2]
		Cond   = (ZCoord >= aTol)
		if Cond:
			idsToRemove.append (jFaceID)
			nToRemove = nToRemove + 1
	print  "---"
	print nToRemove
	print  "---"
	#
	for jFace in range(0,nToRemove):
		geompy.RemoveObject(symmWalls, idsToRemove[jFace])
	#
	id_symmWalls = geompy.addToStudyInFather(injGeom,symmWalls,"symm-walls")
	#
	activeInlet    = faceSelect.SelectFacesWithCoordinateAndLessRadius(injGeom,XMIN,0,vertex4,R1, aTol)
	id_activeInlet = geompy.addToStudyInFather(injGeom,activeInlet,"active-inlet")
	#
	passiveInlet    = faceSelect.SelectFacesWithCoordinateAndGreaterRadius(injGeom,XMIN,0,vertex4,R1+S, aTol)
	id_passiveInlet = geompy.addToStudyInFather(injGeom,passiveInlet,"passive-inlet")
	
	Outlet = faceSelect.SelectFacesWithCOM_OnCoordinate(injGeom, XMAX, 0, aTol)
	id_Outlet = geompy.addToStudyInFather(injGeom,Outlet,"outlet")
	#
	faceGroups = [symmWalls, activeInlet, passiveInlet, Outlet]
	return faceGroups
#
#
#
#
def injectorEdgeGroups (aInjGeom, aInjLens, aInjRads, aWallS ,aTol):
	#
	L1=     aInjLens[0]
	L2=     aInjLens[1]
	L3=     aInjLens[2]
	L4=     aInjLens[3]
	L5=     aInjLens[4]
	L6=     aInjLens[5]
	#
	R0=     aInjRads[0]
	R1=     aInjRads[1]
	R2=     aInjRads[2]
	R3=     aInjRads[3]
	R4=     aInjRads[4]
	#
	S =     aWallS
	#
	RMAX  = R4
	LSUMM = L1 + L2 + L3 + L4 + L5 + L6
	X = [-(L1+L2), -L2, 0, L3, L3+L4, L3+L4+L5, L3+L4+L5+L6]
	Sqrt2By2 = math.sqrt(2.0)/2.0
	YL1 = R2 * Sqrt2By2 * 0.5
	ZL1 = R2 * Sqrt2By2 * 0.5
	YL2 = (R1+S) * Sqrt2By2
	ZL2 = (R1+S) * Sqrt2By2
	YL2b= (R1) * Sqrt2By2
	ZL2b= (R1) * Sqrt2By2
	YL3 = (R2+S) * Sqrt2By2
	ZL3 = (R2+S) * Sqrt2By2
	YL3b= (R2) * Sqrt2By2
	ZL3b= (R2) * Sqrt2By2
	#
	v0 = geompy.MakeVertex(X[0],  YL1, ZL1)
	v0a= geompy.MakeVertex(X[0],  YL2, ZL2)
	v0b= geompy.MakeVertex(X[0],  YL2b, ZL2b)
	v1 = geompy.MakeVertex(X[1],  YL1, ZL1)
	v1a= geompy.MakeVertex(X[1],  YL2, ZL2)
	v2 = geompy.MakeVertex(X[2],  YL1, ZL1)
	v2a= geompy.MakeVertex(X[2],  YL3, ZL3)
	v2b= geompy.MakeVertex(X[2],  YL3b, ZL3b)
	v3 = geompy.MakeVertex(X[3],  YL1, ZL1)
	v4 = geompy.MakeVertex(X[4],  YL1, ZL1)
	v5 = geompy.MakeVertex(X[5],  YL1, ZL1)
	v6 = geompy.MakeVertex(X[6],  YL1, ZL1)
	#
	Edge_L1 = edgeSelect.EdgeOnEnds (aInjGeom, v0, v1, aTol)
	Edge_L1a= edgeSelect.EdgeOnEnds (aInjGeom, v0a,v1a,aTol)
	Edge_L2a= edgeSelect.EdgeOnEnds (aInjGeom, v1a,v2a,aTol)
	Edge_L2 = edgeSelect.EdgeOnEnds (aInjGeom, v1, v2, aTol)
	Edge_L3 = edgeSelect.EdgeOnEnds (aInjGeom, v2, v3, aTol)
	Edge_L4 = edgeSelect.EdgeOnEnds (aInjGeom, v3, v4, aTol)
	Edge_L5 = edgeSelect.EdgeOnEnds (aInjGeom, v4, v5, aTol)
	Edge_L6 = edgeSelect.EdgeOnEnds (aInjGeom, v5, v6, aTol)
	#
	Edge_L1_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_L1_ID    = geompy.GetSubShapeID(aInjGeom, Edge_L1)
	geompy.AddObject(Edge_L1_Group, Edge_L1_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_L1_Group,"LE1")
	#
	Edge_L1a_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_L1a_ID   = geompy.GetSubShapeID(aInjGeom, Edge_L1a)
	geompy.AddObject(Edge_L1a_Group, Edge_L1a_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_L1a_Group,"LE1a")
	#
	Edge_L2_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_L2_ID    = geompy.GetSubShapeID(aInjGeom, Edge_L2)
	geompy.AddObject(Edge_L2_Group, Edge_L2_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_L2_Group,"LE2")
	#
	Edge_L2a_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_L2a_ID   = geompy.GetSubShapeID(aInjGeom, Edge_L2a)
	geompy.AddObject(Edge_L2a_Group, Edge_L2a_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_L2a_Group,"LE2a")
	#
	Edge_L3_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_L3_ID    = geompy.GetSubShapeID(aInjGeom, Edge_L3)
	geompy.AddObject(Edge_L3_Group, Edge_L3_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_L3_Group,"LE3")
	#
	Edge_L4_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_L4_ID    = geompy.GetSubShapeID(aInjGeom, Edge_L4)
	geompy.AddObject(Edge_L4_Group, Edge_L4_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_L4_Group,"LE4")
	#
	Edge_L5_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_L5_ID    = geompy.GetSubShapeID(aInjGeom, Edge_L5)
	geompy.AddObject(Edge_L5_Group, Edge_L5_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_L5_Group,"LE5")
	#
	Edge_L6_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_L6_ID    = geompy.GetSubShapeID(aInjGeom, Edge_L6)
	geompy.AddObject(Edge_L6_Group, Edge_L6_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_L6_Group,"LE6")
	#
	YL5 = R2 * 0.5
	ZL5 = 0.0
	YL6 = -R2 * 0.5
	ZL6 = 0.0
	YL7 = YL5 * Sqrt2By2
	ZL7 = YL7
	YL8 = YL6 * Sqrt2By2
	ZL8 = YL7
	#
	v7       = geompy.MakeVertex(X[0], YL5, ZL5)
	v8       = geompy.MakeVertex(X[0], YL7, ZL7)
	v9       = geompy.MakeVertex(X[0], YL6, ZL6)
	v10      = geompy.MakeVertex(X[0], YL8, ZL8)
	#
	Edge_A11 = edgeSelect.EdgeOnEnds (aInjGeom, v7, v8, aTol)
	Edge_A12 = edgeSelect.EdgeOnEnds (aInjGeom, v9, v10, aTol)
	Edge_A2  = edgeSelect.EdgeOnEnds (aInjGeom, v8, v10, aTol)
	#
	Edge_A1_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_A11_ID    = geompy.GetSubShapeID(aInjGeom, Edge_A11)
	Edge_A12_ID    = geompy.GetSubShapeID(aInjGeom, Edge_A12)
	geompy.AddObject(Edge_A1_Group, Edge_A11_ID)
	geompy.AddObject(Edge_A1_Group, Edge_A12_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_A1_Group,"AE1")
	#
	Edge_A2_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_A2_ID    = geompy.GetSubShapeID(aInjGeom, Edge_A2)
	geompy.AddObject(Edge_A2_Group, Edge_A2_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_A2_Group,"AE2")
	#
	Edge_R1 = edgeSelect.EdgeOnEnds (aInjGeom, v8, v0b, aTol)
	Edge_R2 = edgeSelect.EdgeOnEnds (aInjGeom, v2a,v2b,aTol)
	#
	Edge_R1_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_R1_ID    = geompy.GetSubShapeID(aInjGeom, Edge_R1)
	geompy.AddObject(Edge_R1_Group, Edge_R1_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_R1_Group,"RE1")
	#
	Edge_R2_Group = geompy.CreateGroup(aInjGeom, geompy.ShapeType["EDGE"])
	Edge_R2_ID    = geompy.GetSubShapeID(aInjGeom, Edge_R2)
	geompy.AddObject(Edge_R2_Group, Edge_R2_ID)
	geompy.addToStudyInFather(aInjGeom,Edge_R2_Group,"RE2")
	#	
	subMeshEdges  = [Edge_L1_Group, Edge_L1a_Group,
			 Edge_L2_Group, Edge_L2a_Group,
			 Edge_L3_Group, Edge_L4_Group,
			 Edge_L5_Group, Edge_L6_Group,
			 Edge_A1_Group, Edge_A2_Group,
			 Edge_R1_Group, Edge_R2_Group]
	return subMeshEdges
#
#END_OF_FILE
#

