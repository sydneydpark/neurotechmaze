import numpy as np

from scipy.signal import butter, sosfiltfilt


def filter_eeg(data, sampling_rate):

    if data is None:
        return None

    data = np.asarray(data)

    # Bandpass filter
    low_frequency = 6
    high_frequency = 35

    sos = butter(
        4,
        [low_frequency, high_frequency],
        btype="bandpass",
        fs=sampling_rate,
        output="sos"
    )

    filtered_data = sosfiltfilt(
        sos,
        data,
        axis=-1
    )

    return filtered_data