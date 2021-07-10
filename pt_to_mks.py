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
    print(points)
    for subject in subjects:
        for i in range(len(category)):
            if(str(subject).lower() == str(category.loc[i,"Subjects"]).lower()):
                # if((math.ceil((points/len(subjects))/category.loc[i,"Credits"]) == 0) or (math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 1) or (math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 2) or (math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 3)):
                #     marks = 20
                # elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 4)):
                #     marks = 42
                # elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 5) or (math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 6)):
                #     marks = 52
                # elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 7)):
                #     marks = 65
                # elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 8)):
                #     marks = 75
                # elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 9)):
                #     marks = 85
                # elif((math.ceil((points/(len(subjects)))/category.loc[i,"Credits"]) == 10)):
                #     marks = 95
                if category.loc[i, "Credits"] == 4:
                    if ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 6)):
                        marks = 95
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 5)):
                        marks = 80
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 4)):
                        marks = 75
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 3)):
                        marks = 60
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 2)):
                        marks = 55
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 1) or (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 0)):
                        marks = 39
                elif category.loc[i, "Credits"] == 3:
                    if ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 8)):
                        marks = 95
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) >=6) and (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <8)):
                        marks = 85
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) >=4) and (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <6)):
                        marks = 70
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) >=2) and (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <4)):
                        marks = 50
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) >=0) and (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <2)):
                        marks = 39
                elif category.loc[i, "Credits"] == 1:
                    if ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) == 25)):
                        marks = 95
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) >=20) and (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <25)):
                        marks = 90
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) >=15) and (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <20)):
                        marks = 80
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) >=10) and (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <15)):
                        marks = 65
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) >=5) and (math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <10)):
                        marks = 45
                    elif ((math.floor((points/(len(subjects)))/category.loc[i,"Credits"]) <5)):
                        marks = 39
                else:
                    marks = 40
                    
                    
                final_marks[subject] = marks
    
    return final_marks


    
