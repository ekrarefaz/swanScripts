from datetime import datetime
import os
import random
from random import randint
import string
from faker import Faker
from UserAlert import UserAlert
from NetworkAlert import NetworkAlert

# USER ALERT FUNCTIONS
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

def generate_user_alert_details():
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

# NETWORK ALERT FUNCTIONS
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generate_device_id():
    device_id = random_with_N_digits(15)
    return device_id

def generate_ipaddr():
    faker = Faker()  
    source_ip = faker.ipv4()  
    destination_ip = faker.ipv4()
    return source_ip, destination_ip

def generate_macaddr():
    return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))


# ALERT GENERATOR
def generate_network_alert():
    alert_folder = "/Users/ekrar/SwanForesight/data/"
    alert_path = os.listdir(alert_folder)
    alert_list = []

    severity = generate_alert_severity()
    id = generate_alert_id()
    type = generate_alert_type()
    device_id = generate_device_id()
    source_ip,destination_ip = generate_ipaddr()
    device_macaddr = generate_macaddr()

    new_alert = NetworkAlert(id,type,severity,device_id,source_ip,destination_ip,device_macaddr)
    alert_banner = new_alert.alert_banner()
    alert_details = new_alert.alert_details()
    alert_message = alert_banner + alert_details
    write_to_file(alert_message, id, alert_folder)
    
def generate_user_alert():

    alert_folder = "/Users/ekrar/SwanForesight/data/"
    alert_path = os.listdir(alert_folder)
    alert_list = []

    severity = generate_alert_severity()
    id = generate_alert_id()
    type = generate_alert_type()
    profile,credential,pirivilege, updated_privilege = generate_user_alert_details()
    new_alert = UserAlert(id,type,severity,profile,credential,pirivilege,updated_privilege)

    alert_banner = new_alert.alert_banner()
    alert_details = new_alert.alert_details()

    alert_message = alert_banner + alert_details
    write_to_file(alert_message, id, alert_folder)

def main_menu(total_alerts):
    selection = int(input("Select the type of Alert:\n1.User Alert\n2.Network Alert\n"))
    match selection:
        case 1: 
            for i in range(total_alerts):
                generate_user_alert()
        case 2:
            for i in range(total_alerts):
                generate_network_alert()
        case _:
            print("ERROR 404")
        
def write_to_file(alert_message, id, alert_folder):
    filename = alert_folder + "Alert-{}".format(id)
    with open(filename, "w") as file:
        file.write(alert_message)

def main():
    total_alerts = int(input("Enter the number of Alerts to Generate: "))
    main_menu(total_alerts)

main()