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
        return "\nProfile Updated {}\nCredentails Updated {}\nPriviledge Changed {}\nPrivilege {}\n".format(self.profile_update,self.credential_update,self.privilege_update, self.new_privilege)

