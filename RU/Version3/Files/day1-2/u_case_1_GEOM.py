# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v5.1.4 with dump python functionality (GEOM component)
###

import GEOM
import geompy
import math
import SALOMEDS

def RebuildData(theStudy):
	geompy.init_geom(theStudy)

	global Edge_1, Edge_2, Vertex_3, Revolution_1, Vertex_5, Vertex_4, Vertex_6, Face_1, Cone_1, Edge_5, Edge_3, Cylinder_1, Edge_4, Translation_1, Y, Vertex_2, Common_1, Cut_1, Compound_1, Vector_1, Fillet_1, X, Box_1, Rotation_1, Partition_1, Cone_1_edge_7, Torus_1, Vertex_1, Circle_1
	Vertex_1 = geompy.MakeVertex(200, 200, 0)
	Vertex_2 = geompy.MakeVertexWithRef(Vertex_1, 0, 0, 200)
	Vector_1 = geompy.MakeVector(Vertex_1, Vertex_2)
	Cone_1 = geompy.MakeConeR1R2H(100, 0, 300)
	Cylinder_1 = geompy.MakeCylinder(Vertex_2, Vector_1, 100, 100)
	geomObj_1 = geompy.GetSubShape(Cone_1, [7])
	Circle_1 = geompy.MakeCircle(Vertex_1, Vector_1, 100)
	Cone_1_edge_7 = geompy.GetSubShape(Cone_1, [7])
	Revolution_1 = geompy.MakeRevolution2Ways(Circle_1, Cone_1_edge_7, 45*math.pi/180.0)
	Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
	Torus_1 = geompy.MakeTorusRR(200, 75)
	Common_1 = geompy.MakeCommon(Torus_1, Box_1)
	Cut_1 = geompy.MakeCut(Torus_1, Box_1)
	Translation_1 = geompy.MakeTranslation(Torus_1, 190, 190, 0)
	Y = geompy.MakeVectorDXDYDZ(0, 100, 0)
	X = geompy.MakeVectorDXDYDZ(100, 0, 0)
	Rotation_1 = geompy.MakeRotation(Translation_1, Y, -90*math.pi/180.0)
	Compound_1 = geompy.MakeCompound([Translation_1, Torus_1, Rotation_1])
	Fillet_1 = geompy.MakeFilletAll(Box_1, 35)
	Vertex_3 = geompy.MakeVertex(0, 0, 0)
	Vertex_4 = geompy.MakeVertex(0, 0, 200)
	Vertex_5 = geompy.MakeVertex(200, 0, 200)
	Vertex_6 = geompy.MakeVertex(200, 0, 0)
	Edge_1 = geompy.MakeEdge(Vertex_3, Vertex_4)
	Edge_2 = geompy.MakeEdge(Vertex_4, Vertex_5)
	Edge_3 = geompy.MakeEdge(Vertex_5, Vertex_6)
	Edge_4 = geompy.MakeEdge(Vertex_6, Vertex_3)
	Face_1 = geompy.MakeFaceWires([Edge_1, Edge_2, Edge_3, Edge_4], 1)
	Edge_5 = geompy.MakeEdge(Vertex_3, Vertex_5)
	Partition_1 = geompy.MakePartition([Face_1], [Edge_5], [], [], geompy.ShapeType["FACE"], 0, [], 0)
	geompy.addToStudy( Vertex_1, "Vertex_1" )
	geompy.addToStudy( Vertex_2, "Vertex_2" )
	geompy.addToStudy( Vector_1, "Vector_1" )
	geompy.addToStudy( Cone_1, "Cone_1" )
	geompy.addToStudy( Cylinder_1, "Cylinder_1" )
	geompy.addToStudy( Circle_1, "Circle_1" )
	geompy.addToStudyInFather( Cone_1, Cone_1_edge_7, "Cone_1:edge_7" )
	geompy.addToStudy( Revolution_1, "Revolution_1" )
	geompy.addToStudy( Box_1, "Box_1" )
	geompy.addToStudy( Torus_1, "Torus_1" )
	geompy.addToStudy( Common_1, "Common_1" )
	geompy.addToStudy( Cut_1, "Cut_1" )
	geompy.addToStudy( Translation_1, "Translation_1" )
	geompy.addToStudy( Y, "Y" )
	geompy.addToStudy( X, "X" )
	geompy.addToStudy( Rotation_1, "Rotation_1" )
	geompy.addToStudy( Compound_1, "Compound_1" )
	geompy.addToStudy( Fillet_1, "Fillet_1" )
	geompy.addToStudy( Vertex_3, "Vertex_3" )
	geompy.addToStudy( Vertex_4, "Vertex_4" )
	geompy.addToStudy( Vertex_5, "Vertex_5" )
	geompy.addToStudy( Vertex_6, "Vertex_6" )
	geompy.addToStudy( Edge_1, "Edge_1" )
	geompy.addToStudy( Edge_2, "Edge_2" )
	geompy.addToStudy( Edge_3, "Edge_3" )
	geompy.addToStudy( Edge_4, "Edge_4" )
	geompy.addToStudy( Face_1, "Face_1" )
	geompy.addToStudy( Edge_5, "Edge_5" )
	geompy.addToStudy( Partition_1, "Partition_1" )

	### Store presentation parameters of displayed objects
	import iparameters
	ipar = iparameters.IParameters(theStudy.GetModuleParameters("Interface Applicative", "GEOM", 1))

	#Set up entries:
	# set up entry GEOM_11 (Cut_1) parameters
	ipar.setParameter("GEOM_11", "OCCViewer_0_Visibility", "On")
	ipar.setParameter("GEOM_11", "OCCViewer_0_DisplayMode", "1")
	ipar.setParameter("GEOM_11", "OCCViewer_0_Transparency", "0")
	ipar.setParameter("GEOM_11", "OCCViewer_0_Isos", "1:1")

	pass
