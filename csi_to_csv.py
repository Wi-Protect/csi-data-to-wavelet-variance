# from csv_handling import write_to_csv
import csv
from serial_read import csi_data_read_parse

AMP_AND_PHASE_COLUMNS_NAMES = ['id', 'amplitude1', 'amplitude2', 'amplitude3', 'amplitude4', 'amplitude5', 'amplitude6', 'amplitude7', 'amplitude8', 'amplitude9', 'amplitude10', 'amplitude11', 'amplitude12', 'amplitude13', 'amplitude14', 'amplitude15', 'amplitude16', 'amplitude17', 'amplitude18', 'amplitude19', 'amplitude20', 'amplitude21', 'amplitude22', 'amplitude23', 'amplitude24', 'amplitude25', 'amplitude26', 'amplitude27', 'amplitude28', 'amplitude29', 'amplitude30', 'amplitude31', 'amplitude32', 'amplitude33', 'amplitude34', 'amplitude35', 'amplitude36', 'amplitude37', 'amplitude38', 'amplitude39', 'amplitude40', 'amplitude41', 'amplitude42', 'amplitude43', 'amplitude44', 'amplitude45', 'amplitude46', 'amplitude47', 'amplitude48', 'amplitude49', 'amplitude50', 'amplitude51', 'amplitude52', 'amplitude53', 'amplitude54',
                               'amplitude55', 'amplitude56', 'amplitude57', 'amplitude58', 'amplitude59', 'amplitude60', 'amplitude61', 'amplitude62', 'amplitude63', 'amplitude64', 'phase1', 'phase2', 'phase3', 'phase4', 'phase5', 'phase6', 'phase7', 'phase8', 'phase9', 'phase10', 'phase11', 'phase12', 'phase13', 'phase14', 'phase15', 'phase16', 'phase17', 'phase18', 'phase19', 'phase20', 'phase21', 'phase22', 'phase23', 'phase24', 'phase25', 'phase26', 'phase27', 'phase28', 'phase29', 'phase30', 'phase31', 'phase32', 'phase33', 'phase34', 'phase35', 'phase36', 'phase37', 'phase38', 'phase39', 'phase40', 'phase41', 'phase42', 'phase43', 'phase44', 'phase45', 'phase46', 'phase47', 'phase48', 'phase49', 'phase50', 'phase51', 'phase52', 'phase53', 'phase54', 'phase55', 'phase56', 'phase57', 'phase58', 'phase59', 'phase60', 'phase61', 'phase62', 'phase63', 'phase64', 'activity']

file = open("csi_data.csv", "w")

writer = csv.writer(file, lineterminator='\n')

writer.writerow(AMP_AND_PHASE_COLUMNS_NAMES)

file.close()

while True:
    csi_data = csi_data_read_parse()
    f = open("csi_data.csv", "a")
    w = csv.writer(f, lineterminator='\n')
    w.writerows(csi_data)
    f.close()
    print(csi_data)
    # print(wavelet_variances)
