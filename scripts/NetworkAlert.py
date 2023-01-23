import Alert

class NetworkAlert(Alert.Alert):
    def __init__(self,alert_id,alert_type,alert_severity,source_ip,destination_ip,device_macaddr):
        super().__init__(alert_id,alert_type,alert_severity)
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.device_macaddr = device_macaddr
    def alert_details(self):
        return("Source IP: {}\nDestination IP: {}\nDevice MAC: {}\n".format(self.source_ip, self.destination_ip,self.device_macaddr))