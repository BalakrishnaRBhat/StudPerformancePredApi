import pandas as pd
import math

# get predicted marks of each from predicted points
def points_to_marks(points):
    
    marks = 0
    category = pd.read_excel('datasets\category_dataset.xlsx')
    subjects = ['Advanced Calculus And Numerical Methods','Engineering Chemistry','C Programming For Problem Solving','Basic Electronics','Elements Of Mechanical Engineering','Engineering Chemistry Laboratory','C Programming Laboratory','Technical English 2']
    final_marks = dict()
    for i in range(len(subjects)):
        final_marks[subjects[i]] = ""
    points = int(round(points, 0))
    
    if points < 0:
        points = 0
    elif points > 200:
        points = 200
    
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


    
