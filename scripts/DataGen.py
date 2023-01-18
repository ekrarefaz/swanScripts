from DER import DER
from FroniusDER import FroniusData

import random
import os
import time

DER_folder = "/Users/ekrar/SwanForesight/"
DER_path = os.listdir(DER_folder)
DER_list = []
    
# Instantiate a DER Object
newDER = FroniusData()

en_day = random.randint(0, 99)
en_total = random.randint(0, 999)
en_year = random.randint(0, 99999)

# Generate Port Info

src_port_no , dest_port_no = newDER.generate_port()
dest_IP = "Dest_IP: " + newDER.gen_dest_IP_addr()
src_port = "Source Port: " + str(src_port_no)
dest_port = "Destination Port: " + str(dest_port_no)

# File Write

flag = True
while flag:

    # try:
    total_der = int(input("Enter the number of DERs: "))
    flag = False
    for der in range(total_der):

        der_ID = "DER ID: " + str(der + 1)
        sourceIP = newDER.gen_src_IP_addr()
        ap = "connectedViaAP : " + str(False)
        remote_address = "remoteAddr :" + sourceIP
        wireless = "wlanAvailable : " + str(True)
        salt = {"admin": newDER.gen_salt(), "service": newDER.gen_salt(), "user": ""}
        salt_data = "salt:" + str(salt)
        product_name = "product_Name: Fronius Datamanager"
        platform = "platform: arm-wilma"
        system_date = "systemDate: " + newDER.time_gen()
        pcb_name = "PCBname: WILMA2O"
        hw_version = "hwVersion: 2.4E"
        software_version, update = newDER.gen_sw_vr()
        sw_version = "swVersion: " + software_version
        isWlanCapable = "isWlanCapable: " + str(True)
        new_sw_version = "newSWVersion: " + newDER.new_sw_vr(update)
        time_stmp = "Timestamp: " + newDER.time_gen()

        # storing a der object in the der list
        der_list_item = DER(der_ID,sourceIP,ap,remote_address,wireless,salt_data,product_name,platform,system_date,pcb_name,hw_version,sw_version,isWlanCapable,new_sw_version,time_stmp)
        DER_list.append(der_list_item)

        # Fronius Ad
        str2 = der_ID + newDER.get_FroAd(ap,remote_address,wireless,salt_data,product_name,platform,system_date,pcb_name,hw_version,sw_version,isWlanCapable,new_sw_version,time_stmp) + "\n\n" + "******************************************************"
        
        #setting the file name of the DER
        filename = DER_folder + "DER" + str(der + 1) + ".txt"

        #Opening the DER file adn writing the data into the respective files
        with open(filename, "w") as file:
            # Writing Fronius Ad into the file
            file.write(str2)

    # Get a Random File to keep updating the data
    while True:
        rand_file = random.randint(1,len(DER_list))
        # print(rand_file)
        DER_file = DER_folder + "DER" + str(rand_file) + ".txt"
        with open(DER_file,"a") as file:

            # Fronius Data Tx
            en_day = float(random.randint(0, 99))
            en_total = float(random.randint(0, 999))
            en_year = float(random.randint(0, 99999))
            str3 = newDER.FroDataTx(en_day, en_total, en_year) + "\n" + "---------------------------------------" + "\n"
            # Writing Fronius Data Tx into the file
            file.write(str3)

            src_port_no , dest_port_no = newDER.generate_port()
            source_IP = "Src_IP: " + DER_list[rand_file-1].src_IP
            dest_IP = "Dest_IP: " + newDER.gen_dest_IP_addr()
            src_port = "Source Port: " + str(src_port_no)
            dest_port = "Destination Port: " + str(dest_port_no)
            TTL = "TTL: " + str(newDER.gen_TTL())
            # Writing Source and Destination port info
            str4 = newDER.FroSDInfo(source_IP,dest_IP,src_port,dest_port,TTL) + "\n" + "...................................." + "\n"
            file.write(str4)
            
            time.sleep(2)            
           