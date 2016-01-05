#!/bin/bash

cp polyMesh.initial/* constant/polyMesh

blockMesh

snappyHexMesh -overwrite

simpleFoam

#
# END_OF_FILE
#

