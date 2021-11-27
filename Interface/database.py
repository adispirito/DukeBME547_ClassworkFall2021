# print("This is the database.py module")
# print(f"It's name is {__name__}")

# import blood_calculator
import blood_calculator as bc
# from blood_calculator import hdl_analysis, ldl_analysis
# from blood_calculator import *

answer = bc.hdl_analysis(55)
print(f"The analysis of 55 HDL is {answer}")

answer2 = bc.ldl_analysis(200)
print(f"The analysis of 200 LDL is {answer2}")
