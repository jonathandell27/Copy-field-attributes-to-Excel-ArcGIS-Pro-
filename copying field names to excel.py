import arcpy
import os
import pandas as pd
import time
from datetime import datetime

arcpy.AddMessage("All rights reserved to Jonathan Dell!")
username = os.getlogin()
arcpy.AddMessage("Hello {}!".format(username))
#Start Time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
arcpy.AddMessage("start time = {}".format(current_time))

#The input layer - The user inserts a layer or table by the input button
Layer = arcpy.GetParameter(0)

#Output layer - The location and name of the output file by the Output button
Outputpath = arcpy.GetParameter(1)

#list fields 
fields = arcpy.Describe(Layer).fields

field_domains = []
field_aliasName = []
field_basename = []
field_type = []

for field in fields:
    field_aliasName.append(field.aliasName) #list of aliasName
    field_basename.append(field.baseName)   #list of baseName
    field_type.append(field.type)           #list of field type (integer, text...)
    field_domains.append(field.domain)      #list of domains (if any)
    

#The column names of the output table        
columns = ["BaseName","AliasName","Type","Domains"]

# Converting to excel
df = pd.DataFrame(list(zip(field_basename,field_aliasName,field_type,field_domains)), columns = columns)
df.to_excel(r'{}'.format(Outputpath), index=True)

arcpy.AddMessage("Done!")
arcpy.AddMessage("Your Excel is waiting for you in - {}".format(Outputpath))
#End Time
end = datetime.now()
End_time = end.strftime("%H:%M:%S")
arcpy.AddMessage("End time = {}".format(End_time))


