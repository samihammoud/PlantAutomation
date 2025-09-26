# PlantAutomation
Simple Python Script to adjust the watering amount of a plant given the temperature and zone that certain plant is located in

Two Testing Schedule and Zone scripts


Algorithm Explained

newWaterAmount = (((temperature - baseline_temp) / threshold_temp) * threshold_bonus )

Baseline Temp of a Zone: When no water bonus buffs need to be applied
Threshold Temp: The temperature change per threshold bonus (Every 10 degrees above baseline, bonus is applied) In this case, would be 70
Threshold Bonus: The amount of water added per Threshold Temp change (Every _ above baseline, 5L water is added)


Example: Fri,Cal,Peace Lily,upstairs,0.55|
Current Temperature is 90 degrees|

Baseline temperature of upstairs zone is 60 degrees|
Threshold Temperature: 10 Degrees|
Bonus: 5L |

90(current temperature) - 60(baseline temperature) = 30|
30 / 10(threshold_temp) = 3|
3 * 5L(Bonus) = 15|
new waterAmount = 15 + oldWaterAmount|
