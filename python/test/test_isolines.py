# This file is part of libigl, a simple c++ geometry processing library.
#
# Copyright (C) 2017 Sebastian Koch <s.koch@tu-berlin.de> and Daniele Panozzo <daniele.panozzo@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
import numpy as np
import sys
import os

# Add the igl library to the modules search path
# sys.path.insert(0, os.getcwd() + "/../")
import pyigl as igl
from test_iglhelpers import e2p, p2e

# from shared import TUTORIAL_SHARED_PATH, check_dependencies

# dependencies = ["glfw"]
# check_dependencies(dependencies)


# V = igl.eigen.MatrixXd()
# F = igl.eigen.MatrixXi()

# mesh_file = sys.argv[1]
# mesh_file = '/media/maiqi/e60ff36e-3f59-4df8-930c-7639804532d1/yalong2019/Datasets2/ToothSegmentDataPipeline/Train-Samples-with-normal/raw/train_data/22054603/33.obj'

# print('mesh_file: ', mesh_file)
# igl.readOBJ(mesh_file, V, F)


V = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0]]).astype(np.float64)
F = np.array([[0, 1, 2]]).astype(np.int64)
z = np.array([0, 1, 2]).astype(np.float64)

V, F, z = p2e(V), p2e(F), p2e(z)


#
# n = 3
values = [0.5, 1.0]
isoV = igl.eigen.MatrixXd()
isoE = igl.eigen.MatrixXi()
# igl.isolines(V, F, z, n, isoV, isoE)
igl.isolines(V, F, z, values, isoV, isoE)

isoV, isoE = e2p(isoV), e2p(isoE)
isoV1, isoV2 = isoV[isoE[:, 0]], isoV[isoE[:, 1]]
isoV1, isoV2 = p2e(isoV1), p2e(isoV2)


#
red = igl.eigen.MatrixXd([[0.8, 0.2, 0.2]])
blue = igl.eigen.MatrixXd([[0.2, 0.2, 0.8]])

viewer = igl.glfw.Viewer()
viewer.data().set_mesh(V, F)
viewer.data().set_colors(blue)

# # Draw a red segment parallel to the maximal curvature direction
# viewer.data().add_edges(V + PD2 * avg, V - PD2 * avg, red)

viewer.data().add_edges(isoV1, isoV2, red)


# # Hide wireframe
viewer.data().show_lines = False

viewer.launch()
