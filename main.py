from serial_read import csi_data_read_parse
from wavelet_check import calculate_wavelet_variance


test = csi_data_read_parse()
print(calculate_wavelet_variance(test))
