#  GEOM GEOM_SWIG : binding of C++ omplementaion with Python
#
#  Copyright (C) 2003  CEA
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
#
#  File   : Spiral.py
#  Author : Matvej Kraposhin, RRC KI
#  Module : GEOM
#  $Header: /home/server/cvs/GEOM/GEOM_SRC/src/GEOM_SWIG/GEOM_TestAll.py,v 1.6.2.2 2007/02/23 14:16:34 nge Exp $
#
import geompy
import salome
import math
geom = geompy.geom
# Initialization
#
startX = 0.0              # X-coordinate of spiral center start
startY = 0.0              # Y-coordinate of spiral center start
startZ = 0.0              # Z-coordinate of spiral center start
spiralLength = 100.0      # Length of spiral
spiralDirectionX =  0.0   #
spiralDirectionY =  0.0   # Direction of spiral
spiralDirectionZ =  100.0 # 
spiralRadius     = 50.0   # Radius of spiral
spiralStep       =  20.0  # Step between two segments of spiral
tubeRadius       = 5.0    # tube radius
nStepPoints      = 10     # Number of interpolation points in spiral
rotTolerance     = 1.0E-6 # rot. tolerance
#
#
directionLength  = math.sqrt(spiralDirectionX*spiralDirectionX + spiralDirectionY*spiralDirectionY + spiralDirectionZ*spiralDirectionZ)
normalSDX        = spiralDirectionX / directionLength
normalSDY        = spiralDirectionY / directionLength
normalSDZ        = spiralDirectionZ / directionLength
#
#base elements
#
baseOX           = geompy.MakeVectorDXDYDZ(1,0,0)
baseOY           = geompy.MakeVectorDXDYDZ(0,1,0)
baseOZ           = geompy.MakeVectorDXDYDZ(0,0,1)
#
startingPoint = geompy.MakeVertex(startX, startY, startZ)
endingPoint   = geompy.MakeVertexWithRef(startingPoint, normalSDX*spiralLength, normalSDY*spiralLength, normalSDZ*spiralLength)
endingPoint0  = geompy.MakeVertexWithRef(startingPoint, 0, 0, spiralLength)
baseDirectionVector = geompy.MakeVectorDXDYDZ(normalSDX*spiralLength, normalSDY*spiralLength, normalSDZ*spiralLength)


realStartingPoint = geompy.MakeVertex(startX+spiralRadius, startY, startZ)
startingVector    = geompy.MakeVectorDXDYDZ(0,1,0)
tubeCircle        = geompy.MakeCircle(realStartingPoint, startingVector, tubeRadius)
#id_sVector        = geompy.addToStudy(startingVector, "Starting Vector")
#id_rsPoint        = geompy.addToStudy(realStartingPoint, "Starting Point")
#
id_sPoint     = geompy.addToStudy(startingPoint, "Start Center Point")
id_bVector    = geompy.addToStudy(baseDirectionVector, "Base Vector")
#
iVertices = []
id_iVertices = []
hStep = 0
I     = 0
x     = [None]*(nStepPoints)
y     = [None]*(nStepPoints)
z     = [None]*(nStepPoints)
hamma = 2.0*math.pi/nStepPoints # radians in one segment of spiral step
#creating points for spiral skeleton
while (hStep < spiralLength):
    M = nStepPoints
    for J in range (0, M):
	x[J] = startX + math.cos(hamma*J)*spiralRadius
	y[J] = startY + math.sin(hamma*J)*spiralRadius
	z[J] = startZ + hStep + J*spiralStep/nStepPoints
	iVertices.append(geompy.MakeVertex(x[J], y[J], z[J]))
    I+=(nStepPoints)
    hStep+=spiralStep
#spiral skeleton
spiralSkeleton = geompy.MakeInterpol(iVertices)

#
#rotating spiral according to direction
if (math.fabs(normalSDX)>=rotTolerance) or (math.fabs(normalSDY)>=rotTolerance) or (math.fabs(normalSDZ-1)>=rotTolerance):
    spiralSkeleton = geompy.MakeRotationThreePoints(spiralSkeleton, startingPoint, endingPoint0, endingPoint)
    tubeCircle = geompy.MakeRotationThreePoints(tubeCircle, startingPoint, endingPoint0, endingPoint)
id_sSkel = geompy.addToStudy(spiralSkeleton, "spiral")
id_sCircle = geompy.addToStudy(tubeCircle,"Base Circle")
#creating pipe
spiralPipe = geompy.MakePipe(tubeCircle,spiralSkeleton)
#exploding pipe into edges and obtaining bound faces
spiralPipeExplosion = geompy.SubShapeAll(spiralPipe, geompy.ShapeType["EDGE"])
startingCircle = geompy.MakeFace(spiralPipeExplosion[1], 1)
endingCircle = geompy.MakeFace(spiralPipeExplosion[2], 2)
id_startingCircle = geompy.addToStudy(startingCircle, "Pipe Start")
id_endingCircle = geompy.addToStudy(endingCircle, "Pipe End")
id_pipeWall = geompy.addToStudy(spiralPipe, "Pipe Wall")
#creating pipe shell
pipeFacesList = []
pipeFacesList.append(spiralPipe)
pipeFacesList.append(startingCircle)
pipeFacesList.append(endingCircle)
spiralPipeShell = geompy.MakeShell(pipeFacesList)
id_spiralPipeShell = geompy.addToStudy(spiralPipeShell, "Pipe Shell")
#creating pipe solid
spiralPipeSolid = geompy.MakeSolid([spiralPipeShell])
id_spiralPipeSolid = geompy.addToStudy(spiralPipeSolid, "Pipe Solid")
#
#end of script

