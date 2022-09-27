import arcpy
# import archook
# import numpy as np
import  matplotlib.pyplot as plt
from arcpy import PointGeometry
from arcpy.sa import  *
from typing import List

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("spatial")
f = open('.\\average.txt' ,'r')
data = f.readlines()
f.close()
fcpath = u"E:\\Programming\\Python\\Arcpy\\"
fcname = u"arcpy_points_test.shp"
pt = arcpy.Point()
ptGeoms = []  # type: List[PointGeometry]
sr = arcpy.SpatialReference("WGS 1984")
for i in range(len(data)):
    tmp = data[i].split()
    xp = float(tmp[0])
    yp = float(tmp[1])
    zp = float(tmp[-1])
    pt.X = xp
    pt.Y = yp
    pt.Z = zp

    ptGeoms.append(arcpy.PointGeometry(pt,sr,True))
# arcpy.CopyFeatures_management(ptGeoms,fcpath+fcname)
search_radius = RadiusFixed(distance=12)#RadiusVariable(numberOfPoints=3)
# search_radius = RadiusFixed(distance=0.025)
# outIDW = Idw(ptGeoms, "SHAPE", power=2, search_radius=search_radius)
# outIDW.save(u"E:\\Programming\\Python\\Arcpy\\test_interp_IDW.tif")
# arcpy.Kriging_3d(fcpath+fcname, "SHAPE", u"E:\\Programming\\Python\\Arcpy\\test_interp_Krig.tif","Spherical")
outIDW = Kriging(ptGeoms, "SHAPE", "Spherical", search_radius=search_radius)
var = arcpy.RasterToNumPyArray(outIDW)
plt.contourf(var, cmap = plt.cm.Blues)
plt.show()
