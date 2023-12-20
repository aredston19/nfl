import pandas as pd
import numpy as np

##turn the csv data into a dataframe
df = pd.read_csv("NFL_data.csv")

def function(team, year):
     
    
    df["Win Count"] = np.where(df["Team Score"] > df["Opponent Score"],1, 0)
    df["Loss Count"] = np.where(df["Team Score"] < df["Opponent Score"],1, 0)
    df["Ties"] = np.where(df["Team Score"] == df["Opponent Score"],1, 0)
    
    df_1 = df.loc[(df["Team ID"] == team) & (df["Schedule Season"] == year)]
    df_playoffcheck = df_1.loc[df_1["Schedule Playoff"] == True]

    if ((sum(df_1["Ties"]) > 0) & (len(df_playoffcheck) > 0)):
        print("In " + str(year) + " " + str(team) + " went " + str(sum(df_1[("Win Count")])) + "-" 
        + str(sum(df_1[("Loss Count")])) + "-" + str(sum(df_1[("Ties")])) + "; scored "
        + str(sum(df_1[("Team Score")])) + " points and " + str(team) + " made the playoffs.")
    
    elif ((sum(df_1["Ties"]) > 0) & (len(df_playoffcheck) == 0)):
        print("In " + str(year) + " " + str(team) + " went " + str(sum(df_1[("Win Count")])) + "-" 
        + str(sum(df_1[("Loss Count")])) + "-" + str(sum(df_1[("Ties")])) + "; scored "
        + str(sum(df_1[("Team Score")])) + " points and " + str(team) + " didn't make the playoffs.")
    
    elif len(df_playoffcheck) > 0:
        print("In " + str(year) + " " + str(team) + " went " + str(sum(df_1[("Win Count")])) + "-" 
        + str(sum(df_1[("Loss Count")])) + "; scored "
        + str(sum(df_1[("Team Score")])) + " points and " + str(team) + " made the playoffs.")
    
    else:
        print("In " + str(year) + " " + str(team) + " went " + str(sum(df_1[("Win Count")])) + "-" 
        + str(sum(df_1[("Loss Count")])) + "; scored "
        + str(sum(df_1[("Team Score")])) + " points and " + str(team) + " didn't make the playoffs.")   
    
## function to itterate the above function for every team and year combination
def function2():

    IDs = df["Team ID"].tolist()
    ID_unique = []
    for id in (IDs):
        if id not in ID_unique:
            ID_unique.append(id)
            ID_sorted = sorted(ID_unique)

    years = df["Schedule Season"].tolist()
    year_unique = []
    for y in (years):
        if y not in year_unique:
            year_unique.append(y)
            year_sorted = sorted(year_unique)
            
    for ids in(ID_sorted):
        for ys in(year_sorted):
            function(ids,ys)

function2()


------------------------

import pandas as pd
import numpy as np
df = pd.read_csv("NFL_data.csv")

def function3(year):
     
    ##turn the csv data into a dataframe

    
    ##to retrieve each team-year combination
    teamseason = df["Team_Season"].tolist() 
    ts_unique = []
    for t in teamseason:
        if t not in ts_unique:
            ts_unique.append(t)

    ##print(len(ts_unique))


    playoffcheck = df.loc[df["Schedule Playoff"] == True] 

    ## to retreive the team-year combinations for playoff teams
    playoff_teams = playoffcheck["Team_Season"].tolist()
    pt_unique = []  
    for p in playoff_teams:
        if p not in pt_unique:
            pt_unique.append(p)  

    pt_sorted = sorted(pt_unique)
    ##print(len(pt_sorted))

    
    ##and now the non-playoff teams
    non_playoff = []
    for u in ts_unique:
        if u not in pt_sorted:
            non_playoff.append(u)
    
    np_sorted = sorted(non_playoff)
    ##print(len(np_sorted))

    ##data frame filtered on non-playoff teams
    df_n = df.loc[df["Team_Season"].isin(np_sorted)]

    ##filtered again for the desired year
    df_np = df_n.loc[df_n["Schedule Season"] == year]

    ##print(df_np)

    ##to retrieve every team abreviation
    IDs = df_np["Team ID"].tolist() 
    ID_unique = []
    for id in (IDs):
        if id not in ID_unique:
            ID_unique.append(id)
            ID_sorted = sorted(ID_unique)

    ## team name and total points in a year for each team
    t = []
    p = []
    for ids in ID_sorted:
        t.append(ids)
        test = df_np.loc[df_np["Team ID"] == ids]
        p.append(sum(test["Team Score"]))

    c = []

    c.append(t)
    c.append(p) 
    
    ##print(c)

    df2 = pd.DataFrame(c).T
    df2.columns = ["Teams", "Points"]

    pmax = max(p)

    ts = df2.loc[df2["Points"] == pmax]
    top_scorer =ts.reset_index(drop=True)

    print("In " + str(year) + " for teams that missed the playoffs " + str(top_scorer.at[0,"Teams"]) 
    + " led the leage in scoring with " + str(top_scorer.at[0,"Points"]) + " points.")


## function to itterate the above function for every year combination
def function4():
    
    years = df["Schedule Season"].tolist()
    year_unique = []
    for y in (years):
        if y not in year_unique:
            year_unique.append(y)
            year_sorted = sorted(year_unique)
            
    for ys in(year_sorted):
            function3(ys)

function4()


