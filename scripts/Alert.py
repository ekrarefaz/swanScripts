class Alert:
    def __init__(self, alert_id, alert_type, alert_severity):
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.alert_severity = alert_severity
    def alert_banner(self):
        return "Alert SEVERITY: {}\nAlert ID: {}\nAlert Type: {}\n".format(self.alert_severity,self.alert_id,self.alert_type)