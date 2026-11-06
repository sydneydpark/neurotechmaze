FREQUENCIES = {
    "UP": 8,
    "DOWN": 10,
    "LEFT": 12,
    "RIGHT": 15
}


def classify_ssvep(eeg_data):

    if eeg_data is None:
        return None

    # SSVEP classification will be implemented here.
    # We will compare EEG data with frequency references
    # using FFT and eventually CCA.

    return None