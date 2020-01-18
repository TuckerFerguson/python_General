#@author Tucker Ferguson
#1/18/2020
#Nested Dictionary Basketball Statistics

import pandas as pd

nba_Stats = {"Guards": {"Trey Burke" : {"Shot Attempts":20,
                                        "Shots Made":15,
                                        "Shots missed":5,
                                        "FG Percentage(%)":75},
                        "Mike Conley" : {"Shot Attempts":24,
                                        "Shots Made":19,
                                        "Shots missed":5,
                                        "FG Percentage(%)":79},
                        "Steph Curry" : {"Shot Attempts":30,
                                        "Shots Made":25,
                                        "Shots missed":5,
                                        "FG Percentage(%)":85}},
                                        
                                        
            "Forwards": {"De'Aaron Fox": {"Shot Attempts":23,
                                        "Shots Made":15,
                                        "Shots Missed":8,
                                        "FG Percentage(%)":65},
                        "Kyle Lowry" : {"Shot Attempts":26,
                                        "Shots Made":20,
                                        "Shots Missed":6,
                                        "FG Percentage(%)":76},
                        "Tucker Ferg" : {"Shot Attempts":5,
                                             "Shots Made":1,
                                             "Shots Missed":4,
                                             "FG Percentage(%)":20}}} 
                                        
                                        
guardTable = pd.DataFrame(nba_Stats["Guards"])
forwardTable = pd.DataFrame(nba_Stats["Forwards"])
print("============================[Guard Stats]============================\n")
print(guardTable)
print("\n\n\n==========================[Forward Stats]==========================\n")
print(forwardTable)



                                        