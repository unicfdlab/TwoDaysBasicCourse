#  File   : faceSelects.py
#  Author : Matvej Kraposhin, RRC KI
#  Module : GEOM
#  Purpose: Script for selecting faces from BREP file, with various conditions
#

import geompy
import salome
import math
geom = geompy.geom

#
# returns list of normalized vector coordinates 
#
def VectorNorm (aVector):
	vectorNorm = [1., 1., 1.]
	vectorMag = 0.
	edgePoints = geompy.SubShapeAll(aVector, geompy.ShapeType["VERTEX"])
	pointCoords0 = geompy.PointCoordinates(edgePoints[0])
	pointCoords1 = geompy.PointCoordinates(edgePoints[1])
	vLen = len(pointCoords0)
	for j in range (0, vLen):
		vectorNorm[j] = pointCoords1[j] - pointCoords0[j]
	for j in range (0, vLen):
		vectorMag = vectorMag + vectorNorm[j]*vectorNorm[j]
	vectorMag = math.sqrt(vectorMag)
	if vectorMag > 1.0E-30:
		for j in range (0, vLen):
			vectorNorm[j] = vectorNorm[j] / vectorMag
	return vectorNorm
	

#
# returns scalar product of two lists (vector coordinates)
#
def VectorMul(aList1, aList2):
	mult = 0.
	vLen = len(aList1)
	for j in range (0, vLen):
		mult = mult + aList1[j]*aList2[j]
	return mult
#
# If two vectors are parallel (their normalized scalar product is 1 or -1)
# returns 1, otherwise - 0
#
def VectorsAreParallel (aVector1, aVector2, aTol):
	v1Norm = VectorNorm(aVector1)
	v2Norm = VectorNorm(aVector2)
	mult = VectorMul(v1Norm, v2Norm)
	ramult = math.fabs(math.fabs(mult) - 1.0)
	if ramult <= aTol:
		return 1
	return 0

#
# If some vectors of aVector2Vec is parallel to aVector returns 1,
# otherwise - returns 0
#
def VectorsAreParallelVec(aVector1, aVector2Vec, aTol):
	isParallel = 0
	nVector2 = len(aVector2Vec)
	for jVector in range (0, nVector2):
		isParallel = isParallel + VectorsAreParallel(aVector1, aVector2Vec[jVector], aTol)
	if isParallel:
		return 1
	return 0

#
# If point aPoint in radius aRadius of center aCenter if tolerance aTol,
# returns 1, otherwise - 0
#
def PointOnRadius (aPoint, aCenter, aRadius, aTol):
    pointCoords = geompy.PointCoordinates(aPoint)
    centrCoords = geompy.PointCoordinates(aCenter)
    radVect = [0,0,0]
    rad = 0
    for jC in range(0,3):
	radVect[jC] = math.pow(pointCoords[jC]-centrCoords[jC],2)
	rad = rad + radVect[jC]
    rad = math.sqrt(rad)
    if math.fabs(rad-aRadius) <= aTol:
	return 1
    return 0

#
#
#
def PointLessRadius (aPoint, aCenter, aRadius, aTol):
    pointCoords = geompy.PointCoordinates(aPoint)
    centrCoords = geompy.PointCoordinates(aCenter)
    radVect = [0,0,0]
    rad = 0
    for jC in range(0,3):
	radVect[jC] = math.pow(pointCoords[jC]-centrCoords[jC],2)
	rad = rad + radVect[jC]
    rad = math.sqrt(rad)
    if rad < aRadius:
	return 1
    return 0

#
#
#
def PointGreaterRadius (aPoint, aCenter, aRadius, aTol):
    pointCoords = geompy.PointCoordinates(aPoint)
    centrCoords = geompy.PointCoordinates(aCenter)
    radVect = [0,0,0]
    rad = 0
    for jC in range(0,3):
	radVect[jC] = math.pow(pointCoords[jC]-centrCoords[jC],2)
	rad = rad + radVect[jC]
    rad = math.sqrt(rad)
    if rad > aRadius:
	return 1
    return 0

#
# Calculates Points distance
#
def PointsDistance(aPoint1, aPoint2):
	point1Coords = geompy.PointCoordinates(aPoint1)
	point2Coords = geompy.PointCoordinates(aPoint2)
	diffCoords = 0
	for jCoord in range(0,3):
		diffCoords = diffCoords+math.pow((point1Coords[jCoord]-point2Coords[jCoord]),2)
	diffCoords = math.sqrt(diffCoords)
	return diffCoords

def PointsAreNear(aPoint1, aPoint2, aTol):
	distance = PointsDistance(aPoint1,aPoint2)
	if (distance <= aTol):
		return 1
	return 0
#
#
#
def PointOnCoordinate (aPoint, aCoordValue, aCoord, aTol):
    pointCoords = geompy.PointCoordinates(aPoint)
    if math.fabs(pointCoords[aCoord] - aCoordValue) <= aTol:
	return 1
    return 0

#
#
#
def PointOnCoordinateVec (aPoint, aCoordVALUES, aCoord, aTol):
    nCoords = len(aCoordVALUES)
    for jCoord in range(0, nCoords):
	if PointOnCoordinate(aPoint,aCoordVALUES[jCoord],aCoord,aTol):
	    return 1
    return 0

#
#
#
def EdgeEndsOnCoordinate (aEdge, aCoordValue, aCoord, aTol):
    edgePoints = geompy.SubShapeAll(aEdge, geompy.ShapeType["EDGE"])
    edgeCoord1 = geompy.PointCoordinates(edgePoints[0])
    edgeCoord2 = geompy.PointCoordinates(edgePoints[1])
    tol = math.fabs(aCoordValue - edgeCoord1[aCoord]) + fabs(aCoordValue - edgeCoord2[aCoord])
    if aTol >= tol:
	return 1
    return 0

# Selects faces with Center Of Mass (COM) on radius
# aObject - object, which contains faces for selection, any type
# aCenter - center point (of type Point)
# aRadius - radius, real
def SelectFacesWithCOM_OnRadius(aObject, aCenter, aRadius, aTol):
    # all Faces
    allFacesList = []
    selectedFacesList = []
    allFacesList = geompy.SubShapeAll(aObject, geompy.ShapeType["FACE"])

    facesGroup = geompy.CreateGroup(aObject, geompy.ShapeType["FACE"])


    nFaces = len(allFacesList)

    nSelected = 0
    for jFace in range (0,nFaces):
	jFaceCOM = geompy.MakeCDG(allFacesList[jFace])
	isOnRadius = PointOnRadius(jFaceCOM, aCenter, aRadius, aTol)
	if isOnRadius:
	    faceID = geompy.GetSubShapeID(aObject, allFacesList[jFace])
	    geompy.AddObject(facesGroup, faceID)
	    nSelected = nSelected + 1
    print nSelected
    print "done"
    return facesGroup

#
# Selects all faces in aObject, with normal, parallel to aVector
#
def SelectFacesWithNormalParallelTo(aObject, aVector, aTol):
	allFacesList = []
	allFacesList = geompy.SubShapeAll(aObject, geompy.ShapeType["FACE"])
	
	facesGroup = geompy.CreateGroup(aObject, geompy.ShapeType["FACE"])
	
	nFaces = len(allFacesList)
	nSelected = 0
	for jFace in range (0, nFaces):
		jFaceCOM = geompy.MakeCDG(allFacesList[jFace])
		jFaceNormal = geompy.GetNormal(allFacesList[jFace], jFaceCOM)
		isParallel = VectorsAreParallel(jFaceNormal, aVector, aTol)
		if isParallel:
			faceID = geompy.GetSubShapeID(aObject, allFacesList[jFace])
			geompy.AddObject(facesGroup,faceID)
			nSelected = nSelected + 1
	print nSelected
	print "done"
	return facesGroup
	
#
# Vector version of SelectFacesWithNormalParallelTo
#
def SelectFacesWithNormalParallelToVec(aObject, aVectors, aTol):
	allFacesList = []
	allFacesList = geompy.SubShapeAll(aObject, geompy.ShapeType["FACE"])
	
	facesGroup = geompy.CreateGroup(aObject, geompy.ShapeType["FACE"])
	
	nFaces = len(allFacesList)
	nSelected = 0
	for jFace in range (0, nFaces):
		jFaceCOM = geompy.MakeCDG(allFacesList[jFace])
		jFaceNormal = geompy.GetNormal(allFacesList[jFace], jFaceCOM)
		isParallel = VectorsAreParallelVec(jFaceNormal, aVectors, aTol)
		if isParallel:
			faceID = geompy.GetSubShapeID(aObject, allFacesList[jFace])
			geompy.AddObject(facesGroup,faceID)
			nSelected = nSelected + 1
	print nSelected
	print "done"
	return facesGroup

#
#
#
def SelectFacesWithCOM_OnCoordinate(aObject, aCoordValue, aCoordID, aTol):
    # 0 - X, 1 - Y, 2 - Z
    # all Faces
    allFacesList = []
    selectedFacesList = []
    allFacesList = geompy.SubShapeAll(aObject, geompy.ShapeType["FACE"])

    facesGroup = geompy.CreateGroup(aObject, geompy.ShapeType["FACE"])


    nFaces = len(allFacesList)

    nSelected = 0
    for jFace in range (0,nFaces):
	jFaceCOM = geompy.MakeCDG(allFacesList[jFace])
	isOnCoordinate = PointOnCoordinate(jFaceCOM, aCoordValue, aCoordID, aTol)
	if isOnCoordinate:
	    faceID = geompy.GetSubShapeID(aObject, allFacesList[jFace])
	    geompy.AddObject(facesGroup, faceID)
	    nSelected = nSelected + 1
    print nSelected
    print "done"
    return facesGroup

#
#
#
def SelectFacesWithCOM_OnCoordinateVec(aObject, aCoordVALUES, aCoordID, aTol):
    # 0 - X, 1 - Y, 2 - Z
    # all Faces
    allFacesList = []
    selectedFacesList = []
    allFacesList = geompy.SubShapeAll(aObject, geompy.ShapeType["FACE"])

    facesGroup = geompy.CreateGroup(aObject, geompy.ShapeType["FACE"])

    nFaces = len(allFacesList)

    nSelected = 0
    for jFace in range (0,nFaces):
	jFaceCOM = geompy.MakeCDG(allFacesList[jFace])
	isOnCoordinate = PointOnCoordinateVec(jFaceCOM, aCoordVALUES, aCoordID, aTol)
	if isOnCoordinate:
	    faceID = geompy.GetSubShapeID(aObject, allFacesList[jFace])
	    geompy.AddObject(facesGroup, faceID)
	    nSelected = nSelected + 1
	    print nSelected
    print nSelected
    print "done"
    return facesGroup

#
# Selects faces with COM on coordinate and radius is less then aRadius
#
def SelectFacesWithCoordinateAndLessRadius(aObject, aCoord, aCoordID, aCenter, aRadius, aTol):
	allFacesList = []
	allFacesList = geompy.SubShapeAll(aObject, geompy.ShapeType["FACE"])
	facesGroup = geompy.CreateGroup(aObject, geompy.ShapeType["FACE"])
	nFaces = len(allFacesList)
	nSelected = 0
	for jFace in range (0, nFaces):
		jFaceCOM = geompy.MakeCDG(allFacesList[jFace])
		isOnCoordinate = PointOnCoordinate(jFaceCOM, aCoord, aCoordID, aTol)
		isLessRadius   = PointLessRadius (jFaceCOM, aCenter, aRadius, aTol)
		if (isOnCoordinate and isLessRadius):
			faceID = geompy.GetSubShapeID(aObject, allFacesList[jFace])
			geompy.AddObject(facesGroup, faceID)
			nSelected = nSelected + 1
	print nSelected
	print "done"
	return facesGroup

#
# Selects faces with COM on coordinate and radius is greater then aRadius
#
def SelectFacesWithCoordinateAndGreaterRadius(aObject, aCoord, aCoordID, aCenter, aRadius, aTol):
	allFacesList = []
	allFacesList = geompy.SubShapeAll(aObject, geompy.ShapeType["FACE"])
	facesGroup = geompy.CreateGroup(aObject, geompy.ShapeType["FACE"])
	nFaces = len(allFacesList)
	nSelected = 0
	for jFace in range (0, nFaces):
		jFaceCOM = geompy.MakeCDG(allFacesList[jFace])
		isOnCoordinate = PointOnCoordinate(jFaceCOM, aCoord, aCoordID, aTol)
		isGreaterRadius   = PointGreaterRadius (jFaceCOM, aCenter, aRadius, aTol)
		if (isOnCoordinate and isGreaterRadius):
			faceID = geompy.GetSubShapeID(aObject, allFacesList[jFace])
			geompy.AddObject(facesGroup, faceID)
			nSelected = nSelected + 1
	print nSelected
	print "done"
	return facesGroup
#
#
#