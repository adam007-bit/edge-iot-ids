import pyshark
import pandas as pd

# Load PCAP file
cap = pyshark.FileCapture('traffic.pcap')

data = []

for pkt in cap:
    try:
        packet_size = int(pkt.length)
        protocol = pkt.transport_layer
        src_ip = pkt.ip.src
        dst_ip = pkt.ip.dst
        src_port = pkt[pkt.transport_layer].srcport
        dst_port = pkt[pkt.transport_layer].dstport

        data.append([packet_size, protocol, src_ip, dst_ip, src_port, dst_port])
    except AttributeError:
        # Skip packets that do not have the fields
        pass

# Create DataFrame
df = pd.DataFrame(data, columns=['packet_size', 'protocol', 'src_ip', 'dst_ip', 'src_port', 'dst_port'])

# Save to CSV
df.to_csv('raw_dataset.csv', index=False)
print("CSV dataset created: raw_dataset.csv")
