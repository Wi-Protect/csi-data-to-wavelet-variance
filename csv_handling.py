import csv


CSV_HEADERS = ["amplitude1", "phase1", "amplicude2", "phase2", "amplitude3", "phase3", "amplitude4", "phase4", "amplitude5", "phase5", "amplitude6", "phase6", "amplitude7", "phase7", "amplitude8", "phase8", "amplitude9", "phase9", "amplitude10", "phase10", "amplitude11", "phase11", "amplitude12", "phase12", "amplitude13", "phase13", "amplitude14", "phase14", "amplitude15", "phase15", "amplitude16", "phase16", "amplitude17", "phase17", "amplitude18", "phase18", "amplitude19", "phase19", "amplitude20", "phase20", "amplitude21", "phase21", "amplitude22", "phase22", "amplitude23", "phase23", "amplitude24", "phase24", "amplitude25", "phase25", "amplitude26", "phase26", "amplitude27", "phase27", "amplitude28", "phase28", "amplitude29", "phase29", "amplitude30", "phase30", "amplitude31", "phase31", "amplitude32", "phase32",
               "amplitude33", "phase33", "amplitude34", "phase34", "amplitude35", "phase35", "amplitude36", "phase36", "amplitude37", "phase37", "amplitude38", "phase38", "amplitude39", "phase39", "amplitude40", "phase40", "amplitude41", "phase41", "amplitude42", "phase42", "amplitude43", "phase43", "amplitude44", "phase44", "amplitude45", "phase45", "amplitude46", "phase46", "amplitude47", "phase47", "amplitude48", "phase48", "amplitude49", "phase49", "amplitude50", "phase50", "amplitude51", "phase51", "amplitude52", "phase52", "amplitude53", "phase53", "amplitude54", "phase54", "amplitude55", "phase55", "amplitude56", "phase56", "amplitude57", "phase57", "amplitude58", "phase58", "amplitude59", "phase59", "amplitude60", "phase60", "amplitude61", "phase61", "amplitude62", "phase62", "amplitude63", "phase63", "amplitude64", "phase64", "activity"]


file = open("wavelet_test.csv", "w")

writer = csv.writer(file, lineterminator='\n')

writer.writerow(CSV_HEADERS)

file.close()


def write_to_csv(data, activityNum=0):
    f = open("wavelet_test.csv", "a")
    w = csv.writer(f, lineterminator='\n')
    data.append(activityNum)
    w.writerow(data)
    f.close()


# file.close()
