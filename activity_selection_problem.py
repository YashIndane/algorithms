#Activity Selection Problem -> In the given timeframe calculate max number
#of events the person can attend

activities = [["A1", 0, 1],
              ["A2", 2, 7],
              ["A3", 3, 4]]

activities.sort(key = lambda x : x[2])
i = 0
firstActivity = activities[i][0]
print(firstActivity)

for j in range(len(firstActivity)):
  if activities[j][1] > activities[i][2]:
    print(activities[j][0])
    i = j
