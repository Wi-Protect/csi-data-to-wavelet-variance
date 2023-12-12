import serial
import csv
import json
import numpy as np
from io import StringIO
from math import sqrt, atan2

CSI_VAID_SUBCARRIER_INTERVAL = 3

# Remove invalid subcarriers
# secondary channel : below, HT, 40 MHz, non STBC, v, HT-LFT: 0~63, -64~-1, 384
csi_vaid_subcarrier_index = []
csi_vaid_subcarrier_color = []
color_step = 255 // (28 // CSI_VAID_SUBCARRIER_INTERVAL + 1)

# LLTF: 52
# 26  red
csi_vaid_subcarrier_index += [i for i in range(
    6, 32, CSI_VAID_SUBCARRIER_INTERVAL)]
csi_vaid_subcarrier_color += [(i * color_step, 0, 0)
                              for i in range(1,  26 // CSI_VAID_SUBCARRIER_INTERVAL + 2)]
# 26  green
csi_vaid_subcarrier_index += [i for i in range(
    33, 59, CSI_VAID_SUBCARRIER_INTERVAL)]
csi_vaid_subcarrier_color += [(0, i * color_step, 0)
                              for i in range(1,  26 // CSI_VAID_SUBCARRIER_INTERVAL + 2)]
CSI_DATA_LLFT_COLUMNS = len(csi_vaid_subcarrier_index)

# HT-LFT: 56 + 56
# 28  blue
csi_vaid_subcarrier_index += [i for i in range(
    66, 94, CSI_VAID_SUBCARRIER_INTERVAL)]
csi_vaid_subcarrier_color += [(0, 0, i * color_step)
                              for i in range(1,  28 // CSI_VAID_SUBCARRIER_INTERVAL + 2)]
# 28  White
csi_vaid_subcarrier_index += [i for i in range(
    95, 123, CSI_VAID_SUBCARRIER_INTERVAL)]
csi_vaid_subcarrier_color += [(i * color_step, i * color_step, i * color_step)
                              for i in range(1,  28 // CSI_VAID_SUBCARRIER_INTERVAL + 2)]

CSI_DATA_INDEX = 200  # buffer size
CSI_DATA_COLUMNS = len(csi_vaid_subcarrier_index)
DATA_COLUMNS_NAMES = ["type", "id", "mac", "rssi", "rate", "sig_mode", "mcs", "bandwidth", "smoothing", "not_sounding", "aggregation", "stbc", "fec_coding",
                      "sgi", "noise_floor", "ampdu_cnt", "channel", "secondary_channel", "local_timestamp", "ant", "sig_len", "rx_state", "len", "first_word", "data"]

AMP_AND_PHASE_COLUMNS_NAMES = ['id', 'amplitude1', 'amplitude2', 'amplitude3', 'amplitude4', 'amplitude5', 'amplitude6', 'amplitude7', 'amplitude8', 'amplitude9', 'amplitude10', 'amplitude11', 'amplitude12', 'amplitude13', 'amplitude14', 'amplitude15', 'amplitude16', 'amplitude17', 'amplitude18', 'amplitude19', 'amplitude20', 'amplitude21', 'amplitude22', 'amplitude23', 'amplitude24', 'amplitude25', 'amplitude26', 'amplitude27', 'amplitude28', 'amplitude29', 'amplitude30', 'amplitude31', 'amplitude32', 'amplitude33', 'amplitude34', 'amplitude35', 'amplitude36', 'amplitude37', 'amplitude38', 'amplitude39', 'amplitude40', 'amplitude41', 'amplitude42', 'amplitude43', 'amplitude44', 'amplitude45', 'amplitude46', 'amplitude47', 'amplitude48', 'amplitude49', 'amplitude50', 'amplitude51', 'amplitude52', 'amplitude53', 'amplitude54',
                               'amplitude55', 'amplitude56', 'amplitude57', 'amplitude58', 'amplitude59', 'amplitude60', 'amplitude61', 'amplitude62', 'amplitude63', 'amplitude64', 'phase1', 'phase2', 'phase3', 'phase4', 'phase5', 'phase6', 'phase7', 'phase8', 'phase9', 'phase10', 'phase11', 'phase12', 'phase13', 'phase14', 'phase15', 'phase16', 'phase17', 'phase18', 'phase19', 'phase20', 'phase21', 'phase22', 'phase23', 'phase24', 'phase25', 'phase26', 'phase27', 'phase28', 'phase29', 'phase30', 'phase31', 'phase32', 'phase33', 'phase34', 'phase35', 'phase36', 'phase37', 'phase38', 'phase39', 'phase40', 'phase41', 'phase42', 'phase43', 'phase44', 'phase45', 'phase46', 'phase47', 'phase48', 'phase49', 'phase50', 'phase51', 'phase52', 'phase53', 'phase54', 'phase55', 'phase56', 'phase57', 'phase58', 'phase59', 'phase60', 'phase61', 'phase62', 'phase63', 'phase64']
csi_data_array = np.zeros(
    [CSI_DATA_INDEX, CSI_DATA_COLUMNS], dtype=np.complex64)


SERIAL_PORT = "COM3"

ser = serial.Serial(port=SERIAL_PORT, baudrate=921600,
                    bytesize=8, parity='N', stopbits=1)

serial_open = False

if ser.isOpen():
    print("open success")
    serial_open = True
else:
    print("open failed")


def csi_data_read_parse():
    count = 0

    csi_list = np.zeros((1, 129))

    while serial_open and count < 500:
        strings = str(ser.readline())
        if not strings:
            break

        strings = strings.lstrip('b\'').rstrip('\\r\\n\'')
        index = strings.find('CSI_DATA')

        if index == -1:
            continue

        csv_reader = csv.reader(StringIO(strings))
        csi_data = next(csv_reader)

        if len(csi_data) != len(DATA_COLUMNS_NAMES):
            print("element number is not equal")
            continue

        try:
            csi_raw_data = json.loads(csi_data[-1])
        except json.JSONDecodeError:
            print(f"data is incomplete")
            continue

        if len(csi_raw_data) != 128 and len(csi_raw_data) != 256 and len(csi_raw_data) != 384:
            print(f"element number is not equal: {len(csi_raw_data)}")
            continue

        imaginary = []
        real = []
        amplitudes = []
        phases = []

        # print(csi_raw_data[0])

        for i in range(len(csi_raw_data)):
            if i % 2 == 0:
                imaginary.append(csi_raw_data[i])
            else:
                real.append(csi_raw_data[i])

    # Transform imaginary and real into amplitude and phase
        for i in range(int(len(csi_raw_data) / 2)):
            amplitudes.append(sqrt(imaginary[i] ** 2 + real[i] ** 2))
            phases.append(atan2(imaginary[i], real[i]))

        # print([csi_data[1]] + amplitudes+phases)
        # csi_list.append([csi_data[1]] + amplitudes+phases)
        csi_list = np.vstack([csi_list, [csi_data[1]] + amplitudes+phases])
        count += 1
        print(count)

    # ser.close()

    csi_list = np.delete(csi_list, np.s_[:1], axis=0)

    return csi_list


# serial_port = "COM3"
# csv_file_name = "csi_data.csv"

# with open(csv_file_name, 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(AMP_AND_PHASE_COLUMNS_NAMES)
#     csi_data_read_parse(serial_port, csv_writer)

# print(csi_data_read_parse())

# matrix = csi_data_read_parse()
# a = matrix[:, 1].tolist()
# a = [float(i) for i in a]
# print(type(a[0]))
