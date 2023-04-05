#!/usr/bin/python
import sqlite3
from sqlite3 import Error
import pandas as pd 
from tabulate import tabulate
"""
7.99 A deep-drawing operation will take place on aluminum-killed steel with an 
LDR of 2.4. A cylindrical cup will be produced with a diameter of 100 mm and a 
sheet thickness of 2 mm. Find 
 (a) the largest permissible blank diameter; 
 (b) the deepest cup that can be deep drawn; 
 (c) the deepest cup that can be drawn if LDR = 2.0. 
 Comment on your results.
 """

#  Given
LDR = 2.4
# cylindrincal cup with diameter in mm
Dp = 100 
# sheet thickness in mm
t = 2
# Assume material thickness remains constant

# a) the largest permissible blank diameter
# LDR < Do/Dp
Do = LDR * Dp
# print("the largest permissible blank diameter is "+ str(Do) + "mm")

# b) the deepest cup that can be deep drawn; 
# LDR < Do/Dp
# normal anisotropy for aluminum-killed steel, r̄: 1.4 - 1.8
Dp = Do/LDR
# print("the deepest cup that can be deep drawn is "+ str(Dp) + "mm")

# c) the deepest cup that can be drawn if LDR = 2.0.
LDR = 2.0
Dp = Do/LDR
# print("the deepest cup that can be deep drawn is "+ str(Dp) + "mm")

"""
8.85 The accompanying illustration shows a part that is to be machined from a 
rectangular blank. Suggest the type of operations required and their sequence, 
and specify the machine tools that are needed.
"""
answer = """
1. On a milling machine, clamp the rectangular block to secure the block. 

2. Using a corner radius end mill, machine the stepped cavity and machine
   the step down labeled "A".

3. Using the appropriate drill bit, drill the four holes on the block

4. Using the appropriate tap, tap the four holes on the top.

5. Using a square end mill, machine the angles on the corners (label "B").

6. Using  T-Slot cutter, machine the slots on the sides of the block.

"""
print("Prob 8.85" + answer)

"""
9.1 Why are grinding operations necessary for parts that have been machined by other processes?
"""
answer = """
Grinding operations may be necessary for parts that have been machined by other processes in a 
situation where the hardness or brittleness of the material prevent future machining, or the 
shape is difficult to produce with to dimensional accuracy, and/or there is a particular surface 
finish required for the part.
"""
print("Prob 9.1" + answer)

"""
9.100 Prepare a comprehensive table of the capabilities of abrasive machining processes, including 
the shapes of parts ground, types of machines involved, typical maximum and minimum workpiece dimensions, 
and production rates
"""
def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
      conn = sqlite3.connect(db_file)
      print("sqlite version: " + sqlite3.version)
      print("Opened database successfully")
   except Error as e:
      print(e)
   finally:
      if conn:
         conn.close()

create_connection('hw14.db')   



# print("Prob 9.100")
# dict = {'Process': ['Surface grinding', 'Cylindrical grinding', 'Internal grinding','Centerless grinding'],
# 'Characteristics': [
#     'This process involves the grinding of flat surfaces', """In cylindrical grinding, also called center-type grinding, 
#                                                               the external cylindrical surfaces and shoulders of the 
#                                                               workpiece are ground, such as crankshaft bearings, spindles, 
#                                                               pins, bearing rings, and rolls for rolling mills.""", 'Internal grinding','Centerless grinding'],
# 'Type of machines': ['Surface grinder, vertical spindles, rotary tables', 'Cylindrical grinding', 'Internal grinding','Centerless grinding'],
# 'Dimension of piece': [' The surface grinder can cut steel in pieces \nno bigger than 18” long by 6” high by 8” wide.', 'Cylindrical grinding', 'Internal grinding','Centerless grinding']

# }
# df = pd.DataFrame(dict)
# print(tabulate(df, headers = 'keys', tablefmt = 'psql'))