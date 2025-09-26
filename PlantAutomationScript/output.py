import pandas as pd
from datetime import datetime

def getTemperature():
    #HOOK INTO WEATHER API
    return 90

temperature = getTemperature()
curr_day = datetime.today().strftime("%a")  # 'Thu' style

df = pd.read_csv("./schedule.csv")
zones = pd.read_csv("./zone.csv")

today_rows = df[df["Day"] == curr_day].copy()
print(today_rows)

#algo explained in readme
def computeZoneWaterBuff(paramZone):
    thisZone = zones.loc[zones["Zone"] == paramZone]
    #one match per zone, iloc[0] safe, weird series conflict 
    row = thisZone.iloc[0]
    baseline_temp   = float(row["BaselineTemp"])
    threshold_temp  = float(row["ThresholdTemp"])
    threshold_bonus = float(row["ThresholdBonus"])
    newWaterAmount = (((temperature - baseline_temp) / threshold_temp) * threshold_bonus )
    return newWaterAmount

#return CURRENT DAY SCHEDULE + WATERING AMOUNT BASED ON ZONE + TEMPERATURE
today_rows["WateringAmount_L"] += today_rows["Zone"].apply(computeZoneWaterBuff)
print(today_rows)


