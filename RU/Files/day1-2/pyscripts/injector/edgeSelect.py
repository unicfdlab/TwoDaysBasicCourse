#  File   : edgeSelects.py
#  Author : Matvej Kraposhin, RRC KI
#  Module : GEOM
#  Purpose: Script for selecting edges from BREP file, with various conditions

import geompy
import salome
import math
from faceSelect import *

#
#
#
def SelectEdgesParalletTo (aObject, aVector, aTol):
	allEdgesList = []
	allEdgesList = geompy.SubShapeAll(aObject, geompy.ShapeType["EDGE"])
	
	edgeGroup = geompy.CreateGroup(aObject, geompy.ShapeType["EDGE"])
	
	nEdges = len(allEdgesList)
	nSelected = 0
	for jEdge in range (0, nEdges):
		isParallel = VectorsAreParallel(aVector, allEdgesList[jEdge], aTol)
		if isParallel:
			edgeID = geompy.GetSubShapeID(aObject, allEdgesList[jEdge])
			geompy.AddObject(edgeGroup,edgeID)
			nSelected = nSelected + 1
	print nSelected
	print "done"
	return edgeGroup

#
#
#
def SelectEdgesWithLenEqualAndParallelTo (aObject, aLen, aVector, aTol):
	allEdgesList = []
	allEdgesList = geompy.SubShapeAll(aObject, geompy.ShapeType["EDGE"])
	
	edgeGroup = geompy.CreateGroup(aObject, geompy.ShapeType["EDGE"])
	
	nEdges = len(allEdgesList)
	nSelected = 0
	for jEdge in range (0, nEdges):
		edgeProps = geompy.BasicProperties(allEdgesList[jEdge])
		edgeLen   = edgeProps[0]
		lenDiff   = math.fabs(edgeLen - aLen)
		isParallel = VectorsAreParallel(aVector, allEdgesList[jEdge], aTol)
		if (isParallel and (lenDiff <= aTol)):
			edgeID = geompy.GetSubShapeID(aObject, allEdgesList[jEdge])
			geompy.AddObject(edgeGroup,edgeID)
			nSelected = nSelected + 1
	return edgeGroup

#
# Selects edge with points aPoint1 and aPoint 2 at ends
#
def EdgeHasEnds (aObject, aPoint1, aPoint2, aTol):
	edgeEnds = geompy.SubShapeAll(aObject, geompy.ShapeType["VERTEX"])
	areNear1 = PointsAreNear(aPoint1, edgeEnds[0], aTol)
	areNear2 = PointsAreNear(aPoint2, edgeEnds[1], aTol)
	areNear3 = PointsAreNear(aPoint1, edgeEnds[1], aTol)
	areNear4 = PointsAreNear(aPoint2, edgeEnds[0], aTol)
	cond1 = areNear1 * areNear2
	cond2 = areNear3 * areNear4
	if (cond1 or cond2):
		return 1
	return 0

def EdgeOnEnds (aObject, aPoint1, aPoint2, aTol):
	allEdgesList = []
	allEdgesList = geompy.SubShapeAll(aObject, geompy.ShapeType["EDGE"])
	nEdges = len(allEdgesList)
	nSelected = 0
	for jEdge in range (0, nEdges):
		isEdgeHasEnds = EdgeHasEnds(allEdgesList[jEdge], aPoint1, aPoint2, aTol)
		if isEdgeHasEnds:
			return allEdgesList[jEdge]
	print "Serious error: can\'t find edge with specified points"
	return 0
#
#
#