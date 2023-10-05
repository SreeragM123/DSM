import numpy as np
import matplotlib.pyplot as plt 
 
data = {'AOS':30, 'NSA':10, 'JAVA':40, 
        'ADMBS':55}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values, color ='yellow', 
        width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()