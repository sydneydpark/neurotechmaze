class EEGAcquisition:

    def __init__(self):

        self.connected = False
        self.board = None

    def connect(self):

        print("EEG connection has not been configured yet.")

        print("Waiting for headset selection...")

    def get_latest_data(self):

        if not self.connected:
            return None

        # Actual EEG data retrieval will go here.
        return None

    def disconnect(self):

        if self.connected:

            self.connected = False

            print("EEG disconnected.")