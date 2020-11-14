from mother import Mother


class DeviceInfo(Mother):
    def __init__(self, device_id: str, device_name: str = '', notes: str = '') -> None:
        self.device_name = device_name
        self.device_id = device_id
        self.notes = notes
    def publish(self):
        pass