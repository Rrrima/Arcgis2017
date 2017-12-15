
# -*- coding:utf-8 -*-
# Name: Table2shp.py
# Copyright: Rima 2017/12/14
# Description: Display XY & define coordinate system as WGS1984 & converse to .shp
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env


print ("begin")
# set xy position and make .shp
env.workspace = "C:\Users\hero\Desktop\workspace\geodata.gdb"
outLocation = "C:\Users\hero\Desktop\workspace\geodata.gdb"
tableList = arcpy.ListTables()
for table in tableList:
    print table
    # excute MakeXYEventLayer & define coordinate system as GCS_WGS_1984
    arcpy.MakeXYEventLayer_management(table, "东经", "北纬", table + "layer", 4326)
    # excute FeatureClassToFeatureClass
    arcpy.FeatureClassToFeatureClass_conversion(table + "layer", outLocation, table + "conv")
    print(table + "success")