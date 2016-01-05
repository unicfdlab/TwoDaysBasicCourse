# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v5.1.4 with dump python functionality
###

import sys
import salome

salome.salome_init()

import salome_notebook
notebook = salome_notebook.notebook
sys.path.insert( 0, r'/lustre/unicluster/home/matvey.kraposhin/BasicCourse/Files/day1-2')

import iparameters
ipar = iparameters.IParameters(salome.myStudy.GetCommonParameters("Interface Applicative", 1))

#Set up visual properties:
ipar.setProperty("AP_ACTIVE_VIEW", "OCCViewer_0_0")
ipar.setProperty("AP_WORKSTACK_INFO", "0000000100000000000000020100000001000002f8000000040000000200000001000000080000001a004f00430043005600690065007700650072005f0030005f00300000000102000000080000001a00560054004b005600690065007700650072005f0030005f00300000000202")
ipar.setProperty("AP_ACTIVE_MODULE", "Geometry")
ipar.setProperty("AP_SAVEPOINT_NAME", "GUI state: 1")
#Set up lists:
# fill list AP_VIEWERS_LIST
ipar.append("AP_VIEWERS_LIST", "OCCViewer_1")
ipar.append("AP_VIEWERS_LIST", "VTKViewer_2")
# fill list OCCViewer_1
ipar.append("OCCViewer_1", "OCC scene:1 - viewer:1")
ipar.append("OCCViewer_1", "1.728000000000e+00*1.629682843763e+02*-6.430041152263e+01*4.831644594669e-01*-4.608648419380e-01*7.444163560867e-01*2.570241421262e-01*-6.878357696533e+01*1.568929767609e+01*-5.629996871948e+01*-6.600971796882e+01*1.304346133002e+01*-5.202625618533e+01*1.000000000000e+00*1.000000000000e+00*1.000000000000e+00*1*100.00")
# fill list VTKViewer_2
ipar.append("VTKViewer_2", "VTK scene:1 - viewer:1")
ipar.append("VTKViewer_2", """<?xml version="1.0"?>
<ViewState>
    <Position X="3321.87" Y="-2032.02" Z="4441.18"/>
    <FocalPoint X="-183.207" Y="155.044" Z="211.432"/>
    <ViewUp X="-0.446677" Y="0.588111" Z="0.674244"/>
    <ViewScale Parallel="109.56" X="1" Y="1" Z="1"/>
    <DisplayCubeAxis Show="0"/>
    <GraduatedAxis Axis="X">
        <Title isVisible="1" Text="X" Font="0" Bold="0" Italic="0" Shadow="0">
            <Color R="1" G="0" B="0"/>
        </Title>
        <Labels isVisible="1" Number="3" Offset="2" Font="0" Bold="0" Italic="0" Shadow="0">
            <Color R="1" G="0" B="0"/>
        </Labels>
        <TickMarks isVisible="1" Length="5"/>
    </GraduatedAxis>
    <GraduatedAxis Axis="Y">
        <Title isVisible="1" Text="Y" Font="0" Bold="0" Italic="0" Shadow="0">
            <Color R="0" G="1" B="0"/>
        </Title>
        <Labels isVisible="1" Number="3" Offset="2" Font="0" Bold="0" Italic="0" Shadow="0">
            <Color R="0" G="1" B="0"/>
        </Labels>
        <TickMarks isVisible="1" Length="5"/>
    </GraduatedAxis>
    <GraduatedAxis Axis="Z">
        <Title isVisible="1" Text="Z" Font="0" Bold="0" Italic="0" Shadow="0">
            <Color R="0" G="0" B="1"/>
        </Title>
        <Labels isVisible="1" Number="3" Offset="2" Font="0" Bold="0" Italic="0" Shadow="0">
            <Color R="0" G="0" B="1"/>
        </Labels>
        <TickMarks isVisible="1" Length="5"/>
    </GraduatedAxis>
    <Trihedron isShown="1" Size="105"/>
</ViewState>
""")
# fill list AP_MODULES_LIST
ipar.append("AP_MODULES_LIST", "Geometry")
ipar.append("AP_MODULES_LIST", "Mesh")


import u_case_1_GEOM
u_case_1_GEOM.RebuildData(salome.myStudy)
import u_case_1_SMESH
u_case_1_SMESH.RebuildData(salome.myStudy)

if salome.sg.hasDesktop():
	salome.sg.updateObjBrowser(1)
	iparameters.getSession().restoreVisualState(1)
