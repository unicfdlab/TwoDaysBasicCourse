# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v5.1.4 with dump python functionality (SMESH component)
###

import salome, SMESH, SALOMEDS
import smesh

## import GEOM dump file ## 
import string, os, sys, re
sys.path.insert( 0, os.path.dirname(__file__) )
exec("from "+re.sub("SMESH$","GEOM",__name__)+" import *")


def RebuildData(theStudy):
	smesh.SetCurrentStudy(theStudy)
	import StdMeshers
	import NETGENPlugin
	Mesh_1 = smesh.Mesh(Cut_1)
	Regular_1D = Mesh_1.Segment()
	Max_Size_1 = Regular_1D.MaxSize(20.2301)
	MEFISTO_2D = Mesh_1.Triangle()
	Tetrahedron_Netgen = Mesh_1.Tetrahedron(algo=smesh.NETGEN)
	isDone = Mesh_1.Compute()
	Mesh_1.Clear()
	isDone = Mesh_1.Compute()
	Mesh_2 = smesh.Mesh(Y)
	Regular_1D_1 = Mesh_2.Segment()
	ns_1 = Regular_1D_1.NumberOfSegments(50,10,[  ])
	isDone = Mesh_2.Compute()
	Mesh_2.ExtrusionSweepObject1D( Mesh_2, SMESH.DirStruct( SMESH.PointStruct ( 0, 0, 100 )), 5 )
	Mesh_2.RotationSweepObject1D( Mesh_2, SMESH.AxisStruct( 0, 0, 0, 0, 0, 10 ), 0.0872665, 6, 1e-05 )

	## set object names
	smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
	smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
	smesh.SetName(Max_Size_1, 'Max Size_1')
	smesh.SetName(MEFISTO_2D.GetAlgorithm(), 'MEFISTO_2D')
	smesh.SetName(Tetrahedron_Netgen.GetAlgorithm(), 'Tetrahedron (Netgen)')
	smesh.SetName(Mesh_2.GetMesh(), 'Mesh_2')
	smesh.SetName(ns_1, 'ns_1')
	if salome.sg.hasDesktop():
		salome.sg.updateObjBrowser(0)

	### Store presentation parameters of displayed objects
	import iparameters
	ipar = iparameters.IParameters(theStudy.GetModuleParameters("Interface Applicative", "SMESH", 1))

	#Set up entries:
	# set up entry SMESH_4 (Mesh_2) parameters
	ipar.setParameter("SMESH_4", "VTKViewer_0_Visibility", "On")
	ipar.setParameter("SMESH_4", "VTKViewer_0_Representation", "2")
	ipar.setParameter("SMESH_4", "VTKViewer_0_IsShrunk", "0")
	ipar.setParameter("SMESH_4", "VTKViewer_0_Entities", "e:1:f:1:v:0")
	ipar.setParameter("SMESH_4", "VTKViewer_0_Colors", "surface:0:0.666667:1:backsurface:0:0:1:edge:0:0.666667:1:node:1:0:0")
	ipar.setParameter("SMESH_4", "VTKViewer_0_Sizes", "line:1:shrink:0.75")
	ipar.setParameter("SMESH_4", "VTKViewer_0_PointMarker", "std:1:9")
	ipar.setParameter("SMESH_4", "VTKViewer_0_Opacity", "1")
	ipar.setParameter("SMESH_4", "VTKViewer_0_ClippingPlane", "Off")


	pass
