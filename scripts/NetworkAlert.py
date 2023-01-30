import Alert

class NetworkAlert(Alert.Alert):
    def __init__(self,alert_id,alert_type,alert_severity,device_id,source_ip,destination_ip,device_macaddr):
        super().__init__(alert_id,alert_type,alert_severity)
        self.device_id = device_id
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.device_macaddr = device_macaddr

    def alert_heading(self):
        return("-----NETWORK ALERT-----\n")

    def alert_details(self):
        details_dictionary = {
            "Device ID" : self.device_id,
            "Source IP": self.source_ip,
            "Destination IP":self.destination_ip,
            "Device MAC":self.device_macaddr
        }
        return details_dictionary