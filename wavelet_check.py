import numpy as np
import pywt

# Define functions for calculating wavelet amplitude and phase variances

WAVELET_NAME = 'db4'
LEVEL = 2


def calculate_wavelet_variance(csi):
    variances = []

    for i in range(64):
        amplitudes = csi[:, i+1].tolist()
        amplitudes = [float(i) for i in amplitudes]

        phases = csi[:, i+65].tolist()
        phases = [float(i) for i in phases]

        amplitude_coeffs = pywt.wavedec(amplitudes, WAVELET_NAME, LEVEL)
        phase_coeffs = pywt.wavedec(phases, WAVELET_NAME, LEVEL)

        amplitude_variances = [np.var(coeff) for coeff in amplitude_coeffs]
        phase_variances = [np.var(coeff) for coeff in phase_coeffs]

        # variances.append(
        # [np.sum(amplitude_variances), np.sum(phase_variances)])

        variances.append(np.sum(amplitude_variances))
        variances.append(np.sum(phase_variances))

    return variances


# def wavelet_amplitude_variance(csi):
#     """
#     Calculates the wavelet amplitude variance of a CSI signal.

#     Args:
#       csi: Complex-valued CSI signal.
#       wavelet_name: Name of the wavelet function.
#       level: Decomposition level.

#     Returns:
#       wavelet_amplitude_variance: Wavelet amplitude variance.
#     """
#     # Perform wavelet decomposition
#     coeffs = pywt.wavedec(np.abs(csi), WAVELET_NAME, LEVEL)

#     # Calculate variance of each wavelet coefficient
#     variances = [np.var(coeff) for coeff in coeffs]

#     # Return total wavelet amplitude variance
#     return np.sum(variances)


# def wavelet_phase_variance(csi, wavelet_name, level):
#     """
#     Calculates the wavelet phase variance of a CSI signal.

#     Args:
#       csi: Complex-valued CSI signal.
#       wavelet_name: Name of the wavelet function.
#       level: Decomposition level.

#     Returns:
#       wavelet_phase_variance: Wavelet phase variance.
#     """
#     # Extract phase information from the CSI signal
#     phase = np.angle(csi)

#     # Perform wavelet decomposition on the phase
#     coeffs = pywt.wavedec(phase, wavelet_name, level)

#     # Calculate variance of each wavelet coefficient
#     variances = [np.var(coeff) for coeff in coeffs]

#     # Return total wavelet phase variance
#     return np.sum(variances)

# # Example usage

# # Define sample CSI signal
# csi = np.array([1.2+0.3j, 1.4+0.2j, 1.5+0.1j])

# # Choose wavelet and level
# wavelet_name = 'db4'
# level = 2

# # Calculate wavelet amplitude and phase variances
# wav_amp_var = wavelet_amplitude_variance(csi, wavelet_name, level)
# wav_phase_var = wavelet_phase_variance(csi, wavelet_name, level)

# # Print results
# print("Wavelet amplitude variance:", wav_amp_var)
# print("Wavelet phase variance:", wav_phase_var)
