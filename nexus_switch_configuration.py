#!/usr/bin/python3
import sys

# arguments to this script in this order
# 1st argument = no of switches attached to nexus
# 2nd argument = no of cu attached for vodafone
# 3rd argument = no of cu attached for O2
# 4th argument = no of cu attached for EE
# 5th argument = no of cu attached for 3UK

__no_of_switches = int(sys.argv[1]) + 1         #1 because of range function in for
__voda = int(sys.argv[2])
__o2 = int(sys.argv[3])
__ee = int(sys.argv[4])
__3uk = int(sys.argv[5])
__voda_s1 = __voda
__o2_s1 = __o2
__ee_s1 = __ee
__3uk_s1 = __3uk

def module_start():

    #Starting of the configuration
    temp_text = ("version 6.0(2)A7(2)\n"
                 "hostname nexus\n"
                 "\n"
                 "feature telnet\n"
                  "feature scp-server\n"
                 "cfs eth distribute\n"
                 "feature interface-vlan\n"
                 "feature lacp\n"
                 "feature vpc\n"
                 "feature lldp\n"
                 "\n"
                 "no password strength-check\n"
                 "\n"
                 "ip domain-lookup\n"
                 "errdisable recovery interval 100\n"
                 "errdisable recovery cause link-flap\n"
                 "ip access-list RU_CU_PTP\n"
                 "  10 permit udp any range 319 320 any\n"
                 "ip access-list copp-system-acl-bfd\n"
                 "  10 permit udp any any eq 3784\n"
                 "  20 permit udp any any eq 3785\n"
                 "ip access-list copp-system-acl-eigrp\n"
                 "  10 permit eigrp any any\n"
                 "ip access-list copp-system-acl-ftp\n"
                 "  10 permit tcp any any eq ftp-data\n"
                 "  20 permit tcp any any eq ftp\n"
                 "  30 permit tcp any eq ftp-data any\n"
                 "  40 permit tcp any eq ftp any\n"
                 "ip access-list copp-system-acl-http\n"
                 "  10 permit tcp any any eq www\n"
                 "  20 permit tcp any any eq 443\n"
                 "ip access-list copp-system-acl-icmp\n"
                 "  10 permit icmp any any\n"
                 "ip access-list copp-system-acl-ntp\n"
                 "  10 permit udp any any eq ntp\n"
                 "  20 permit udp any eq ntp any\n"
                 "ip access-list copp-system-acl-ping\n"
                 "  10 permit icmp any any echo\n"
                 "  20 permit icmp any any echo-reply\n"
                 "ip access-list copp-system-acl-routingproto1\n"
                 "  10 permit tcp any any eq bgp\n"
                 "  20 permit tcp any eq bgp any\n"
                 "  30 permit tcp any any eq 639\n"
                 "  40 permit tcp any eq 639 any\n"
                 "  50 permit ospf any any\n"
                 "ip access-list copp-system-acl-routingproto2\n"
                 "  10 permit 112 any 224.0.0.0/24\n"
                 "ip access-list copp-system-acl-snmp\n"
                 "  10 permit udp any any eq snmp\n"
                 "  20 permit udp any eq snmp any\n"
                 "  30 permit udp any any eq snmptrap\n"
                 "ip access-list copp-system-acl-ssh\n"
                 "  10 permit tcp any any eq 22\n"
                 "  20 permit tcp any eq 22 any\n"
                 "ip access-list copp-system-acl-stftp\n"
                 "  10 permit udp any any eq tftp\n"
                 "  20 permit udp any any eq 1758\n"
                 "  30 permit udp any eq tftp any\n"
                 "  40 permit udp any eq 1758 any\n"
                 "  50 permit tcp any any eq 115\n"
                 "  60 permit tcp any eq 115 any\n"
                 "ip access-list copp-system-acl-tacacsradius\n"
                 "  10 permit tcp any any eq tacacs\n"
                 "  20 permit tcp any eq tacacs any\n"
                 "  30 permit udp any any eq 1812\n"
                 "  40 permit udp any any eq 1813\n"
                 "  50 permit udp any any eq 1645\n"
                 "  60 permit udp any any eq 1646\n"
                 "  70 permit udp any eq 1812 any\n"
                 "  80 permit udp any eq 1813 any\n"
                 "  90 permit udp any eq 1645 any\n"
                 "  100 permit udp any eq 1646 any\n"
                 "ip access-list copp-system-acl-telnet\n"
                 "  10 permit tcp any any eq telnet\n"
                 "  20 permit tcp any any eq 107\n"
                 "  30 permit tcp any eq telnet any\n"
                 "  40 permit tcp any eq 107 any\n"
                 "ip access-list copp-system-dhcp-relay\n"
                 "  10 permit udp any eq bootps any eq bootps\n"
                 "class-map type qos match-all RU_CU_PTP\n"
                 "  match access-group name RU_CU_PTP\n"
                 "policy-map type qos RU_CU_PTP_Policy\n"
                 "  class RU_CU_PTP\n"
                 "    set dscp 46\n"
                 "policy-map type network-qos jumbo\n"
                 "  class type network-qos class-default\n"
                 "    mtu 9216\n"
                 "system qos\n"
                 "  service-policy type network-qos jumbo\n"
                 "class-map type control-plane match-any copp-ftp\n"
                 "  match access-group name copp-system-acl-ftp\n"
                 "class-map type control-plane match-any copp-http\n"
                 "  match access-group name copp-system-acl-http\n"
                 "class-map type control-plane match-any copp-icmp\n"
                 "  match access-group name copp-system-acl-icmp\n"
                 "class-map type control-plane match-any copp-ntp\n"
                 "  match access-group name copp-system-acl-ntp\n"
                 "class-map type control-plane match-any copp-s-arp\n"
                 "class-map type control-plane match-any copp-s-bfd\n"
                 "  match access-group name copp-system-acl-bfd\n"
                 "class-map type control-plane match-any copp-s-bpdu\n"
                 "class-map type control-plane match-any copp-s-cdp\n"
                 "class-map type control-plane match-any copp-s-default\n"
                 "class-map type control-plane match-any copp-s-dhcpreq\n"
                 "class-map type control-plane match-any copp-s-dhcpresp\n"
                 "  match access-group name copp-system-dhcp-relay\n"
                 "class-map type control-plane match-any copp-s-dpss\n"
                 "class-map type control-plane match-any copp-s-eigrp\n"
                 "  match access-group name copp-system-acl-eigrp\n"
                 "class-map type control-plane match-any copp-s-glean\n"
                 "class-map type control-plane match-any copp-s-igmp\n"
                 "class-map type control-plane match-any copp-s-ip-nat\n"
                 "class-map type control-plane match-any copp-s-ip-options\n"
                 "class-map type control-plane match-any copp-s-ipmc-g-hit\n"
                 "class-map type control-plane match-any copp-s-ipmc-rpf-fail-g\n"
                 "class-map type control-plane match-any copp-s-ipmc-rpf-fail-sg\n"
                 "class-map type control-plane match-any copp-s-ipmcmiss\n"
                 "class-map type control-plane match-any copp-s-l3destmiss\n"
                 "class-map type control-plane match-any copp-s-l3mtufail\n"
                 "class-map type control-plane match-any copp-s-lacp\n"
                 "class-map type control-plane match-any copp-s-lldp\n"
                 "class-map type control-plane match-any copp-s-pimautorp\n"
                 "class-map type control-plane match-any copp-s-pimreg\n"
                 "class-map type control-plane match-any copp-s-ping\n"
                 "  match access-group name copp-system-acl-ping\n"
                 "class-map type control-plane match-any copp-s-ptp\n"
                 "class-map type control-plane match-any copp-s-routingProto1\n"
                 "  match access-group name copp-system-acl-routingproto1\n"
                 "class-map type control-plane match-any copp-s-routingProto2\n"
                 "  match access-group name copp-system-acl-routingproto2\n"
                 "class-map type control-plane match-any copp-s-ttl1\n"
                 "class-map type control-plane match-any copp-snmp\n"
                 "  match access-group name copp-system-acl-snmp\n"
                 "class-map type control-plane match-any copp-ssh\n"
                 "  match access-group name copp-system-acl-ssh\n"
                 "class-map type control-plane match-any copp-stftp\n"
                 "  match access-group name copp-system-acl-stftp\n"
                 "class-map type control-plane match-any copp-tacacsradius\n"
                 "  match access-group name copp-system-acl-tacacsradius\n"
                 "class-map type control-plane match-any copp-telnet\n"
                 "  match access-group name copp-system-acl-telnet\n"
                 "policy-map type control-plane copp-system-policy \n"
                 "  class copp-s-default\n"
                 "    police pps 400 \n"
                 "  class copp-s-ping\n"
                 "    police pps 100 \n"
                 "  class copp-s-l3destmiss\n"
                 "    police pps 100 \n"
                 "  class copp-s-glean\n"
                 "    police pps 500 \n"
                 "  class copp-s-l3mtufail\n"
                 "    police pps 100 \n"
                 "  class copp-s-ttl1\n"
                 "    police pps 100 \n"
                 "  class copp-s-ip-options\n"
                 "    police pps 100 \n"
                 "  class copp-s-ip-nat\n"
                 "    police pps 100 \n"
                 "  class copp-s-ipmcmiss\n"
                 "    police pps 400 \n"
                 "  class copp-s-ipmc-g-hit\n"
                 "    police pps 400 \n"
                 "  class copp-s-ipmc-rpf-fail-g\n"
                 "    police pps 400 \n"
                 "  class copp-s-ipmc-rpf-fail-sg\n"
                 "    police pps 400 \n"
                 "  class copp-s-dhcpreq\n"
                 "    police pps 300 \n"
                 "  class copp-s-dhcpresp\n"
                 "    police pps 300 \n"
                 "  class copp-s-igmp\n"
                 "    police pps 400 \n"
                 "  class copp-s-routingProto2\n"
                 "    police pps 1300 \n"
                 "  class copp-s-eigrp\n"
                 "    police pps 200 \n"
                 "  class copp-s-pimreg\n"
                 "    police pps 200 \n"
                 "  class copp-s-pimautorp\n"
                 "    police pps 200 \n"
                 "  class copp-s-routingProto1\n"
                 "    police pps 1000 \n"
                 "  class copp-s-arp\n"
                 "    police pps 200 \n"
                 "  class copp-s-ptp\n"
                 "    police pps 1000 \n"
                 "  class copp-s-bfd\n"
                 "    police pps 350 \n"
                 "  class copp-s-bpdu\n"
                 "    police pps 12000 \n"
                 "  class copp-s-dpss\n"
                 "    police pps 6400 \n"
                 "  class copp-s-cdp\n"
                 "    police pps 400 \n"
                 "  class copp-s-lacp\n"
                 "    police pps 400 \n"
                 "  class copp-s-lldp\n"
                 "    police pps 500 \n"
                 "  class copp-icmp\n"
                 "    police pps 200 \n"
                 "  class copp-telnet\n"
                 "    police pps 500 \n"
                 "  class copp-ssh\n"
                 "    police pps 500 \n"
                 "  class copp-snmp\n"
                 "    police pps 500 \n"
                 "  class copp-ntp\n"
                 "    police pps 100 \n"
                 "  class copp-tacacsradius\n"
                 "    police pps 400 \n"
                 "  class copp-stftp\n"
                 "    police pps 400 \n"
                 "  class copp-ftp\n"
                 "    police pps 100 \n"
                 "  class copp-http\n"
                 "    police pps 100 \n"
                 "control-plane\n"
                 "  service-policy input copp-system-policy \n"
                 "snmp-server user admin network-admin auth md5 0x4d7055f9e1d238eab9a6cfc555ce6f19 priv 0x4d7055f9e1d238eab9a6cfc555ce6f19 localizedkey\n"
                 "ntp master 15\n"
                 "\n")
    
    return temp_text

def module_vlan_conf():

    __iq_oper = [ "VF", "O2", "EE", "3UK"]
    __total_iq_vlans = __voda + __o2 + __ee + __3uk
    __iq_vlans = [__voda, __o2, __ee, __3uk]
    __s1_conn = [__voda_s1, __o2_s1, __ee_s1, __3uk_s1]

    temp_text = ("vlan configuration " + str(101) + "-" + str(100 +__total_iq_vlans) + "\n"
                 "  ip igmp snooping querier 1.1.1.5\n"
                 #"vlan configuration 300,111-130\n"
                 "vlan 1\n"
                 "vlan 222\n"
                 "  name mgmt_for_snmp\n"
                 "vlan 300\n"
                 "  name N1-N2_interconnect/mgmt\n")
        
    vlan1=101
    for j,k in zip(__iq_vlans,range(4)):
        if( j == 2):
            temp_text = temp_text + ("vlan " + str(vlan1) + "\n"
                                     "  name IQ_for_" + __iq_oper[k] + "_BC1\n"
                                     "vlan " + str(vlan1+1) + "\n"
                                     "  name IQ_for_" + __iq_oper[k] + "_BC2\n")
            vlan1+=2
        if( j == 1):
            temp_text = temp_text + ("vlan " + str(vlan1) + "\n"
                                     "  name IQ_for_" + __iq_oper[k] + "_BC1\n")
            vlan1+=1

    vlan2=111
    for j,k in zip(__iq_vlans,range(4)):
        if( j == 2):
            temp_text = temp_text + ("vlan " + str(vlan2) + "\n"
                                     "  name 1588_" + __iq_oper[k] + "_BC1\n"
                                     "vlan " + str(vlan2+1) + "\n"
                                     "  name 1588_" + __iq_oper[k] + "_BC2\n")
            vlan2+=2
        if( j == 1):
            temp_text = temp_text + ("vlan " + str(vlan2) + "\n"
                                     "  name 1588_" + __iq_oper[k] + "_BC1\n")
            vlan2+=1
    
    vlan3=500
    for j,k in zip(__s1_conn,range(4)):
        if( j == 2):
            temp_text = temp_text + ("vlan " + str(vlan3) + "\n"
                                     "  name s1_for_" + __iq_oper[k] + "_BC1\n"
                                     "vlan " + str(vlan3+20) + "\n"
                                     "  name s1_for_" + __iq_oper[k] + "_BC2\n")
            vlan3+=100
        if( j == 1):
            temp_text = temp_text + ("vlan " + str(vlan3) + "\n"
                                     "  name s1_for_" + __iq_oper[k] + "_BC1\n")
            vlan3+=100
    
    temp_text = temp_text + ("key chain Vfone-QES\n"
                             "  key 0\n"
                             "    key-string 7 07392743400c543402170e02490f272d32323727070f5b3015574d514659\n"
                             "vrf context management\n"
                             "vrf context vpc_keepalive\n"
                             "\n"
                             "\n"
                             "interface port-channel 1\n"
                             "  switchport trunk allowed vlan 101-" + str(__total_iq_vlans+100)+ ",300\n"
                             "  switchport mode trunk\n"
                             "  no shut\n"
                             "\n"
                             "interface Vlan1\n"
                             "  no shutdown\n"
                             "\n"
                             "interface Vlan300\n"
                             "  description \"MGMT Vlan\"\n"
                             "  no shutdown\n"
                             "  management\n"
                             "  vrf member vpc_keepalive\n"
                             "  ip address 192.168.100.101/24\n"
                             "\n")

    for i,j in zip(range(111,vlan2),range(11,11+__total_iq_vlans)):
        temp_text = temp_text + ("interface Vlan" + str(i) + "\n"
                                 "  no shutdown\n"
                                 "  ip address 10.0." + str(j) + ".201/24\n"
                                 "\n")
    
    return temp_text

def module_interfaces():

    vlan1=100
    vlan2=110
    __total_iq_vlans = __voda + __o2 + __ee + __3uk

    temp_text = ""
    for i in range(1,__no_of_switches):
        temp_text = temp_text + ("interface Ethernet1/" + str(i*2-1) + "\n"
                                 "  switchport mode trunk\n"
                                 "  switchport trunk allowed vlan 101-" + str(__total_iq_vlans+100) + ",300\n"
                                 "  no shutdown\n"
                                 "\n"
                                 "interface Ethernet1/" + str(i*2) + "\n"
                                 "  speed 1000\n"
                                 "  switchport mode trunk\n"
                                 "  switchport trunk allowed vlan 111-" + str(__total_iq_vlans+110) + "\n"
                                 "  service-policy type qos input RU_CU_PTP_Policy\n"
                                 "  no negotiate auto\n"
                                 "  no shutdown\n"
                                 "\n")
    
    for i in range(__no_of_switches*2-1,23):
        temp_text = temp_text + ("interface Ethernet1/" + str(i) + "\n"
                                  "  shutdown\n"
                                  "\n")
    
    __interface = 23
    __cu_conn = [__voda,__o2,__ee,__3uk]
    for k in __cu_conn:
        if(k==0):
            i=1
        else:
            i=k
        for j in range(0,i):
            vlan1=vlan1+1
            vlan2=vlan2+1
            if(k==0):
                temp_text = temp_text + ("interface Ethernet1/" + str(__interface) + "\n"
                                         "  shutdown\n"
                                         "\n"
                                         "interface Ethernet1/" + str(__interface+1) + "\n"
                                         "  shutdown\n"
                                         "\n"
                                         "interface Ethernet1/" + str(__interface+2) + "\n"
                                         "  shutdown\n"
                                         "\n"
                                         "interface Ethernet1/" + str(__interface+3) + "\n"
                                         "  shutdown\n"
                                         "\n")
                __interface=__interface+4
                break
            temp_text = temp_text + ("interface Ethernet1/" + str(__interface) + "\n"
                                     "  switchport access vlan " + str(vlan1) + "\n"
                                     "  no shutdown\n"
                                     "\n"
                                     "interface Ethernet1/" + str(__interface+1) + "\n"
                                     "  speed 1000\n"
                                     "  switchport access vlan " + str(vlan2) + "\n"
                                     "  no negotiate auto\n"
                                     "  service-policy type qos input RU_CU_PTP_Policy\n"
                                     "  no negotiate auto\n"
                                     "  no shutdown\n"
                                     "\n")
            __interface = __interface + 2
            if(i==1):
                temp_text = temp_text + ("interface Ethernet1/" + str(__interface) + "\n"
                                         "  shutdown\n"
                                         "\n"
                                         "interface Ethernet1/" + str(__interface+1) + "\n"
                                         "  shutdown\n"
                                         "\n")
                j=2
                __interface = __interface + 2
    
    __s1_conn = [__voda_s1, __o2_s1, __ee_s1, __3uk_s1]
    vlan3=500
    j=39
    for i in __s1_conn:
        if(i==0):
            temp_text = temp_text + ("interface Ethernet1/" + str(j) + "\n"
                                     "  shutdown\n"
                                     "\n"
                                     "interface Ethernet1/" + str(j+1) + "\n"
                                     "  shutdown\n"
                                     "\n")
            j+=2
        else:
            for k in range(i):
                temp_text = temp_text + ("interface Ethernet1/" + str(j) + "\n"
                                         "  switchport mode trunk\n"
                                         "  switchport trunk allowed vlan " + str(str(vlan3) + "," + str(vlan3+20) if (i == 2) else str(vlan3)) + "\n"
                                         "  no shutdown\n"
                                         "\n")
                j+=1
            if(i==1):
                temp_text = temp_text + ("interface Ethernet1/" + str(j) + "\n"
                                         "  shutdown\n"
                                         "\n")
                j+=1
            vlan3+=100

    backhaul_vlan_list = []
    backhaul_vlan = ""
    i=500
    for k,j in zip(range(3),__s1_conn):
        if(j!=0):
            backhaul_vlan_list.append(i)
            if(j==2):
                backhaul_vlan_list.append(i+20)
            i+=100
    if(__s1_conn[3] == 2):
        backhaul_vlan_list.append(i)
        backhaul_vlan_list.append(i+20)
    elif(__s1_conn[3] == 1):
        backhaul_vlan_list.append(i)

    for i,j in zip(backhaul_vlan_list,range(len(backhaul_vlan_list))):
        backhaul_vlan = backhaul_vlan + "," + str(i)
    #backhaul_vlan = backhaul_vlan + str(backhaul_vlan_list[len(backhaul_vlan_list)-1])
    temp_text = temp_text +("interface Ethernet1/47\n"
                            "  description \"equinix backhaul\"\n"
                            "  switchport mode trunk\n"
                            "  switchport trunk allowed vlan 300" + str(backhaul_vlan) + "\n"
                            "\n"
                            "interface Ethernet1/48\n"
                            "  speed 1000\n"
                            "  switchport access vlan 222\n"
                            "  no negotiate auto\n"
                            "  no shutdown\n"
                            "\n"
                            "interface mgmt0\n"
                            "  vrf member management\n"
                            "  ip address 192.168.2.101/24\n"
                            "line console\n"
                            "line vty\n"
                            "boot kickstart bootflash:/n3500-uk9-kickstart.6.0.2.A7.2.bin \n"
                            "boot system bootflash:/n3500-uk9.6.0.2.A7.2.bin \n"
                            "\n")
    return temp_text

temp_text=module_start()+module_vlan_conf()+module_interfaces()
print(temp_text)
