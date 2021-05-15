from typing import final
import numpy as np
import pandas as pd
import math

# get predicted marks of each from predicted points
def points_to_marks(points):
    
    marks = 0
    category = pd.read_excel('datasets\category_dataset.xlsx')
    subjects =['Transform Calculus, Fourier Series And Numerical Techniques','Data Structures and Applications','Analog and Digital Electronics','Computer Organization','Software Engineering','Discrete Mathematical Structures','Analog and Digital Electronics Laboratory','Data Structures Laboratory','Constitution of India, Professional Ethics and Cyber Law']
    predicted_marks = list()
    final_marks = dict()
    for i in range(len(subjects)):
        final_marks[subjects[i]] = ""
    points = int(round(points, 0))
    
    if points < 0:
        points = 0
    elif points > 400:
        points = 400
    
    for subject in subjects:
        for i in range(len(category)):
            if(str(subject).lower() == str(category.loc[i,"Subjects"]).lower()):
                if((math.ceil((points/len(subjects))/category.loc[i,"Credits"]) == 0) or (math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 1) or (math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 2) or (math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 3)):
                    marks = 20
                elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 4)):
                    marks = 42
                elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 5) or (math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 6)):
                    marks = 52
                elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 7)):
                    marks = 65
                elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 8)):
                    marks = 75
                elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 9)):
                    marks = 85
                elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 10)):
                    marks = 95
                final_marks[subject] = marks
    
    return final_marks

# print(points_to_marks(370))
    
