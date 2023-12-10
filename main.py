from csv_handling import write_to_csv
from serial_read import csi_data_read_parse
from wavelet_check import calculate_wavelet_variance

# delete_all_records("wavelet_test.csv")

NORMAL = 0
WALKING = 1
RUNNING = 2
BENDING = 3


while True:
    csi_data = csi_data_read_parse()
    wavelet_variances = calculate_wavelet_variance(csi_data)

    write_to_csv(wavelet_variances, NORMAL)

    print(wavelet_variances)

# test = csi_data_read_parse()
# print(calculate_wavelet_variance(test))
