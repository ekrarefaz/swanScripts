from datetime import datetime
import os
import random
import string
from UserAlert import UserAlert


def generate_alert_severity():
    severity_array = ["SEVERE", "CRITICAL", "WARNING", "LOW IMPACT"]
    for severity in severity_array:
        severity = random.choice(severity_array)
        return severity

def generate_alert_type():
    alert_type_array = ["WARNING","ERROR","NOTIFICATION"]
    for alert in alert_type_array:
        alert = random.choice(alert_type_array)
        return alert

def generate_alert_id():
    id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return id

def generate_alert_details():
    values = [True, False]
    privilege_values = ["Root", "Admin", "SuperUser", "Reperesentative", "GuestUser"]
    profile_change = random.choice(values)
    credential_change = random.choice(values)
    privilege_change = random.choice(values)
    if(privilege_change):
        updated_privilege = random.choice(privilege_values)
    else:
        updated_privilege = "null"
    return profile_change,credential_change,privilege_change, updated_privilege

def write_to_file(alert_message, id, alert_folder):
    filename = alert_folder + "Alert-{}".format(id)
    with open(filename, "w") as file:
        file.write(alert_message) 
    
def generate_alert():

    alert_folder = "/Users/ekrar/SwanForesight/data/"
    alert_path = os.listdir(alert_folder)
    alert_list = []

    severity = generate_alert_severity()
    id = generate_alert_id()
    type = generate_alert_type()
    profile,credential,pirivilege, updated_privilege = generate_alert_details()
    new_alert = UserAlert(id,type,severity,profile,credential,pirivilege,updated_privilege)

    alert_banner = new_alert.alert_banner()
    alert_details = new_alert.alert_details()

    alert_message = alert_banner + alert_details
    write_to_file(alert_message, id, alert_folder)

def main():
    total_alerts = int(input("Enter the number of Alerts to Generate: "))
    for i in range(total_alerts):
        generate_alert()

main()