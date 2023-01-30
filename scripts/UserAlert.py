import Alert 

class UserAlert(Alert.Alert):
    def __init__(self,alert_id,alert_type,alert_severity,profile_update,credential_update,privilege_update,new_privilege):
        super().__init__(alert_id,alert_type,alert_severity)
        self.profile_update = profile_update
        self.credential_update = credential_update
        self.privilege_update = privilege_update
        self.new_privilege = new_privilege

    def alert_heading(self):
        return("-----USER ALERT-----\n")

    def alert_details(self):
        details_dictionary = {
            "Profile Updated" : self.profile_update,
            "Credentails Updated" : self.credential_update,
            "Priviledge Changed" : self.privilege_update,
            "Privilege " : self.new_privilege
        }
        return details_dictionary
