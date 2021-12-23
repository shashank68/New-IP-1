# Sending LBF contract packet with min delay as 500ms and max delay as 800ms

from setup import setup
from sender import sender

setup_obj = setup()
setup_obj.setup_topology (pcap=False)
setup_obj.start_receiver ()

with setup_obj.h1:
    sender_obj = sender()
    delay = 500
    
    sender_obj.make_packet(src_addr_type='ipv4', src_addr='10.0.1.2',
                        dst_addr_type='ipv6', dst_addr='10::2:2', content='ipv4 to ipv6 from h1 to h2 more latency')
    sender_obj.insert_contract(
        contract_type='latency_based_forwarding', params=[500,800,300,3])   #min_delay, max_delay, fib_todelay, fib_tohops
    sender_obj.send_packet(iface='h1_r1', show_pkt=True)

setup_obj.show_stats()