map = {}
vif_number = 0 
target_hosts = ["130.230.112.34", "130.230.112.35"

physPortId = 1

packet in loop

packet = event.parsed
src_mac = packet.src

src_ip = 0
dst_ip = 0 

if packet.type == ethernet.IP_TYPE:
     ipv4_packet = event.parsed.find("ipv4")
    # Do more processing of the IPv4 packet
    src_ip = ipv4_packet.srcip
    dst_ip = ipv4_packet.dstip
else :
    return fail 
    
    
outport = 0 
if dst ip in target_hosts: 
    setup = 1
    if dst_ip in keys map: 
        #¿vif exists?
if src_ip in keys(map[dst_ip]): 
# make a function that matches certain vif to switchport 
try: 
outport = getPortFromOvs(map[dst_ip][src_ip])
setup =0 
catch :
pass 
# reuse old negotiator? 
else: 
try: 
outport =getPortFromOvs(map[dst_ip]keys(map[dst_ip])[0])
setup = 0
catch: 
pass 
if (setup) 
create a virtual ike negotiator bound to interface "vi"+vifnumber with ip address dst_ip 
rewMac= askmacfrommaincontroller(dst_ip)
# this is ovs rule for the return packets in the local ovs (the rule in main sdn is static) 
create rule to forward from "vi"+vifnumber to outport physPortId with action rewrite mac to rewMac 
map[dst_ip][src_ip]="vi"+vifnumber
++vifnumber 

outport = getPortFromOvs("vi"+vifnumber)

msg = of.ofp_packet_out()  
msg.buffer_id = event.ofp.buffer_id  
msg.in_port = packet_in.in_port
msg.match = of.ofp_match.from_packet(packet)
action = of.ofp_action_output(outport) 
msg.actions.append(action)
self.connection.send(msg)

