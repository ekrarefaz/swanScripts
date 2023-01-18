from time import time


class DER:
    def __init__(self,ID,src_IP,ap,rm_addr,wlan_avail,salt_data,product_name,platform,system_date,pcb_name,hw_version,sw_version,isWlanCapable,new_sw_version,time_stmp):
        
        self.ID = ID
        self.src_IP = src_IP
        self.ap = ap
        self.rm_addr = rm_addr
        self.wlan_avail = wlan_avail
        self.salt_data = salt_data
        self.product_name = product_name
        self.platform = platform
        self.system_date = system_date
        self.pcb_name = pcb_name
        self.hw_version = hw_version
        self.sw_version = sw_version
        self.isWlanCapable = isWlanCapable
        self.new_sw_version = new_sw_version
        self.time_stmp = time_stmp
    
    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.ID,self.src_IP,self.ap,self.rm_addr,self.wlan_avail,self.salt_data,self.product_name,self.platform,self.system_date,self.pcb_name,self.hw_version,self.sw_version,self.isWlanCapable,self.new_sw_version,self.time_stmp)
