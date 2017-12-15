
# -*- coding:utf-8 -*-
# Name: KrigingInsertion.py
# Copyright: Rima 2017/12/14
# Description: KrigingInsertion and Variation analysis
# Requirements: Spacial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
import os

#Check out the ArcGIS Spatial Anapyst extension license
arcpy.CheckOutExtension("Spatial")
#Setting initial
env.workspace = "C:\Users\hero\Desktop\workspace\geodata.gdb"
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    print(fc)
    fieldList = arcpy.ListFields(env.workspace + "\\" + fc)
    print (env.workspace + "\\" + fc)
    for field in fieldList:
        if (field.type == u"Double"):
            print(field.name)
            inFeatures = fc
            print(inFeatures)

            #Output settings
            outRaster = env.workspace + "\\" + "KRe_" + field.name + fc
            outVarRaster = env.workspace + "\\" + "KVar_" + field.name + fc
            print (outRaster)
            print (outVarRaster)

            #Model setting
            kModel = "Gaussian"

            # Execute Kriging
            arcpy.Kriging_3d(inFeatures, field.name
                              , outRaster, kModel, out_variance_prediction_raster = outVarRaster)
            print(field.name + "success")

