#
# injector.py
#
import sys
sys.path.append('/home/m-11.3/tmp')
sys.path.append('/lustre/unicluster/home/matvey.kraposhin/BasicCourse/Files/day1-2/pyscripts/injector')
#
import edgeSelect
import injector_GROUPS
import injector_GEOM
import geompy
import salome
import math
import smesh
#
#
#	
injLens = []
injRads = []
injAngs = []
#
Rinner  = 25.00
dSinner = 1.0

Souter  = math.pi * 150. * 150. / 4.
Sinner  = math.pi * (Rinner+dSinner)*(Rinner+dSinner)
Rout    = math.sqrt((Souter - Sinner) / math.pi)
#
injLens.append(250.50)  # L1
injLens.append( 20.00)  # L2
injLens.append( 83.00)  # L3
injLens.append(480.00)  # L4
injLens.append(490.00)  # L5
injLens.append(450.00)  # L6
#

injRads.append(Rout)  # R0
#injRads.append(100.00)  # R0
#injRads.append( 25.00)  # R1
injRads.append( 25.00)  # R1
injRads.append(  4.75)  # R2
injRads.append( 39.50)  # R3
injRads.append( 75.00)  # R4
#
injAngs.append( 45.00)  # A1
#
wallS = 1.0        # wall thikness
#
#
#
injGeom    =  injector_GEOM.CreateGEOM (injLens, injRads, injAngs, wallS)
id_injGEOM =  geompy.addToStudy(injGeom,"injGeom")
#
# To Select Geometry From Tree
#
#id_selObj   = salome.sg.getSelected(0)
#print id_selObj
#injGeom = salome.IDToObject(id_selObj)
#
faceTol = 1.0E-3
edgeTol = 1.0E-3
print "Face Groups (BC)"
faceGroups = injector_GROUPS.injectorFaceGroups(injGeom, injLens, injRads, wallS ,faceTol)
print "Edge Groups (Mesh Options)"
edgeGroups = injector_GROUPS.injectorEdgeGroups(injGeom, injLens, injRads, wallS ,edgeTol)

print "Geometry done."
Edge_L1 = edgeGroups[0]   #1
Edge_L1a= edgeGroups[1]   #2
Edge_L2 = edgeGroups[2]   #3
Edge_L2a= edgeGroups[3]   #4
Edge_L3 = edgeGroups[4]   #5
Edge_L4 = edgeGroups[5]   #6
Edge_L5 = edgeGroups[6]   #7
Edge_L6 = edgeGroups[7]   #8
Edge_A1 = edgeGroups[8]
Edge_A2 = edgeGroups[9]
Edge_R1 = edgeGroups[10]
Edge_R2 = edgeGroups[11]
#
#        0   1   2   3   4   5    6  7
LenNS = [50, 50, 20, 40, 40, 40, 20, 20]
#
AzlNS = [5, 10]
#
RadNS = [15, 5]
#
#creating mesh
injMesh = smesh.Mesh(injGeom, "injMesh")
#default 1D hypothesis
default1D = injMesh.Segment()
default1D.NumberOfSegments(5)
#quadrangle 2D meshing
injMesh.Quadrangle()
# Parallel to X
algo_Edge_L1 = injMesh.Segment(Edge_L1)
algo_Edge_L1.NumberOfSegments(LenNS[0], 0.08)
algo_Edge_L1.Propagation()
#
algo_Edge_L1a= injMesh.Segment(Edge_L1a)
algo_Edge_L1a.NumberOfSegments(LenNS[1], 0.08)
algo_Edge_L1a.Propagation()
#
algo_Edge_L2 = injMesh.Segment(Edge_L2)
algo_Edge_L2.NumberOfSegments(LenNS[2], 0.4)
algo_Edge_L2.Propagation()
#
algo_Edge_L2a= injMesh.Segment(Edge_L2a)
algo_Edge_L2a.NumberOfSegments(LenNS[3], 2.5)
algo_Edge_L2a.Propagation()
#
algo_Edge_L3 = injMesh.Segment(Edge_L3)
algo_Edge_L3.NumberOfSegments(LenNS[4], 10)
algo_Edge_L3.Propagation()
#
algo_Edge_L4 = injMesh.Segment(Edge_L4)
algo_Edge_L4.NumberOfSegments(LenNS[5], 5)
algo_Edge_L4.Propagation()
#
algo_Edge_L5 = injMesh.Segment(Edge_L5)
algo_Edge_L5.NumberOfSegments(LenNS[6])
algo_Edge_L5.Propagation()
#
algo_Edge_L6 = injMesh.Segment(Edge_L6)
algo_Edge_L6.NumberOfSegments(LenNS[7])
algo_Edge_L6.Propagation()
#
# Azimuthal edges
#
algo_Edge_A1 = injMesh.Segment(Edge_A1)
algo_Edge_A1.NumberOfSegments(AzlNS[0])
algo_Edge_A1.Propagation()
#
algo_Edge_A2 = injMesh.Segment(Edge_A2)
algo_Edge_A2.NumberOfSegments(AzlNS[1])
algo_Edge_A2.Propagation()
#
# Parallel to radius
#
#
algo_Edge_R1 = injMesh.Segment(Edge_R1)
algo_Edge_R1.NumberOfSegments(RadNS[0])
algo_Edge_R1.Propagation()
#
algo_Edge_R2 = injMesh.Segment(Edge_R2)
algo_Edge_R2.NumberOfSegments(RadNS[1])
algo_Edge_R2.Propagation()
#
# Computing a mesh
#
print "Computing mesh"
injMesh.Hexahedron()
#
ret = injMesh.Compute()
if ret == 0:
    print "problem when computing the mesh"
else:
    print "mesh computed without problems"
    pass
#
print "Creating groups"
#
# Creating groups
#
symmWalls   = injMesh.Group(faceGroups[0], "symm-walls")
activeInlet = injMesh.Group(faceGroups[1], "active-inlet")
passiveInlet= injMesh.Group(faceGroups[2], "passive-inlet")
outlet      = injMesh.Group(faceGroups[3], "outlet")
#
# END__OF_FILE
#

