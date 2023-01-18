from datetime import datetime
import random
from faker import Faker  
import string

class FroniusData:

    def time_gen(self):
        today = datetime.now()
        # print("Current date and time is", today)
        d_t = datetime.isoformat(today)
        # print("Date & Time:", date_as_string)
        return d_t

    def gen_src_IP_addr(self):
        faker = Faker()  
        ip_addr = faker.ipv4()  
        return ip_addr

    def gen_salt(self):
        characters = string.ascii_lowercase + string.digits
        salt = ""
        for i in range(8):
            salt += "".join(random.choice(characters))
        return salt

    def gen_sw_vr(self):
        update = random.randint(1, 9)
        sw = "3.23." + str(update) + "-" + str(random.randint(0, 9))
        return sw, update

    def new_sw_vr(self,update):
        update += 1
        sw = "3.23." + str(update) + "-" + str(random.randint(0, 9))
        return sw

    def get_FroAd(self,ap,rm_addr,wlan_avail,salt_data,product_name,platform,system_date,pcb_name,hw_version,sw_version,isWlanCapable,new_sw_version,time_stmp):
        final_output = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(ap,rm_addr,wlan_avail,salt_data,
                        product_name,platform,system_date,pcb_name,hw_version,sw_version,isWlanCapable,new_sw_version,time_stmp)
        return final_output

    def FroDataTx(self,en_day,en_total,en_year):
        day = 0
        mt_loc = "location: unknown"
        mode = "operationMode: produce-only"
        P_Akku = "P_Akku: null"
        P_Grid = "P_Grid: null"
        P_Load = "P_Load: null"
        P_PV = "P_PV: null"
        rel_Autonomy = "rel_Autonomy: null"
        rel_SelfConsumption = "rel_SelfConsumption: null"

        # inv_num = "Inverter No: " + str(num)
        inv_day = "Inverter Day: " + str(day)
        per_day = "E_Day: " + str("%.2f" % en_day)
        per_month = "E_Total: " + str("%.2f" % en_total)
        per_year = "E_Year: " + str("%.2f" % en_year)

        final_DER_output = "\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(mt_loc,mode,inv_day,
                            per_day, per_month, per_year, P_Akku, P_Grid, P_Load, P_PV, rel_Autonomy,rel_SelfConsumption)
        return final_DER_output

    def generate_port(self):
        src_port = random.randint(0,65535)
        dest_port = random.randint(0,65535) 
        return src_port,dest_port

    def gen_dest_IP_addr(self):
        faker = Faker()  
        ip_addr = faker.ipv4()  
        return ip_addr
    
    def gen_TTL(self):
        return 100

    def FroSDInfo(self,source_IP,dest_IP,src_port,dest_port,TTL):
        return ("{}\n{}\n{}\n{}\n{}\n").format(source_IP,dest_IP,src_port,dest_port,TTL)
