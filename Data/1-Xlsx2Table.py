
# -*- coding:utf-8 -*-
# Name: Xlsx2Table.py
# Copyright: Rima 2017/12/9
# Description: converse .xlsx to database table
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env
import glob

#converse .xlsx data to table
outLocation = "C:\Users\hero\Desktop\workspace\geodata.gdb"
print ("begin")
# Set environment settings
env.workspace = "C:\Users\hero\Desktop\workspace\Data"

fnames = glob.glob("*xlsx")
for fname in fnames:
    print fname

    # Set local variables
    intable = env.workspace +"\\" + fname + "\\'" + fname.replace(".xlsx", "") + "$'"
    outtable = "O" + fname.replace("-","").replace(".xlsx", "")
    print (intable)
    print (outtable)


    try:
    # Execute TableToGeodatabase
    # print ("Importing" + intable + "to gdb: " + outLocation)
        arcpy.TableToGeodatabase_conversion(intable, outLocation)
    except:
        print arcpy.GetMessages()
   # arcpy.TableToTable_conversion(intable, outLocation, outtable)
   # fields = arcpy.ListFields(outLocation + "/" + outtable)
   # for debugging
   # for field in fields:
   #     print("%s is a type of %s with a length of %s" % ((field.name, field.type, field.length)))
'''
# set xy position and make .shp
env.workspace = outLocation
tableList = arcpy.ListTables()
for table in tableList:
    print table
    # excute MakeXYEventLayer
    arcpy.MakeXYEventLayer_management(table, "东经", "北纬", table + "layer", 4326)
    # excute FeatureClassToFeatureClass
    arcpy.FeatureClassToFeatureClass_conversion(table + "layer", outLocation, table + "conv")
    print(table + "success")
'''
