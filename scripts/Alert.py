class Alert:
    def __init__(self, alert_id, alert_type, alert_severity):
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.alert_severity = alert_severity
    def alert_banner(self):
        alert_dictionary = {
            "Alert Severity" : self.alert_severity,
            "Alert ID": self.alert_id,
            "Alert Type" : self.alert_type,
        }
        return alert_dictionary