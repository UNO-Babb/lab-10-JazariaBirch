#MapPlot.py
#Name:
#Date:
#Assignment:


import smoking
report = smoking.get_report()

num_items = len(report)
total = []
percent = []

for spot in range(25):
    smoke = report[0]["Data"]["Smokers"]["Total"]
    smoking_total = report[0]["Data"]["Percentage"]["Total"]

    
    total.append(smoke)
    percent.append(smoking_total)

    import matplotlib.pyplot as plt
    plt.plot(total, percent, 'ro')
    plt.ylabel('Total Score')
    plt.savefig("output")