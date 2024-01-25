import pandas as pd
import matplotlib.pyplot as plt
import os
import platform
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test.py <filename>")
        exit()
    else:
        filename = sys.argv[1]


df = pd.read_csv(filename)

def srcIP():
    counts = df['src_ip'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('IP address')
    plt.ylabel('Connection count')
    plt.title('Count of ergress connections per IP')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def destIP():
    counts = df['dst_ip'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('IP address')
    plt.ylabel('Connection count')
    plt.title('Count of ingress connections per IP')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def srcPort():
    counts = df['src_port'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('Port number')
    plt.ylabel('Connection count')
    plt.title('Count of ergress connections per port')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def destPort():
    counts = df['dst_port'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('Port number')
    plt.ylabel('Connection count')
    plt.title('Count of ingress connections per port')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def srcMac():
    counts = df['src_mac'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('Mac address')
    plt.ylabel('Connection count')
    plt.title('Count of ingress connections per mac address')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def destMac():
    counts = df['dst_mac'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('Port number')
    plt.ylabel('Connection count')
    plt.title('Count of ingress connections per mac address')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def flowDur():
    df['flow_duration_ms'] = df['flow_duration'] / 1000
    # Ustawienia wykresu
    plt.plot(df['flow_duration_ms'], marker='o')
    plt.xlabel('Connection index')
    plt.ylabel('Connection lenght (ms)')
    plt.title('Time of connection per connection')   
    plt.show()

def flowSpeed():
    df['flow_kbyts_s'] = df['flow_byts_s'] / 1024
    # Ustawienia wykresu
    plt.plot(df['flow_kbyts_s'], marker='o')
    plt.xlabel('Connection index')
    plt.ylabel('Connection speed [kilobytes/s]')
    plt.title('Connection speed per connection')   
    plt.show()

def flag_count():
    plt.figure(figsize=(14, 5))
    choosen_cols = ['fwd_psh_flags', 'bwd_psh_flags', 'fwd_urg_flags', 'bwd_urg_flags', 'fin_flag_cnt', 'syn_flag_cnt', 'rst_flag_cnt', 'psh_flag_cnt', 'ack_flag_cnt', 'urg_flag_cnt', 'ece_flag_cnt']
    col_sum = df[choosen_cols].sum()
    plt.bar(col_sum.index, col_sum.values)
    plt.xlabel('Flag name')
    plt.ylabel('Sum')
    plt.title('Sums of flags')
    plt.show()

def flowPkt():
    plt.plot(df['flow_pkts_s'], marker='o')
    plt.xlabel('Connection index')
    plt.ylabel('Connection speed [packets/s]')
    plt.title('Connection speed per connection')   
    plt.show()

def maxPkt():
    plt.plot(df['pkt_len_max'], marker='o')
    plt.xlabel('Connection index')
    plt.ylabel('Length of packet in IP header')
    plt.title('Maximal lenght of packet per connection')   
    plt.show()

def minPkt():
    plt.plot(df['pkt_len_min'], marker='o')
    plt.xlabel('Connection index')
    plt.ylabel('Length of packet in IP header')
    plt.title('Minimal lenght of packet per connection')   
    plt.show()

def avgPkt():
    plt.plot(df['pkt_len_mean'], marker='o')
    plt.xlabel('Connection index')
    plt.ylabel('Length of packet in IP header')
    plt.title('Averege lenght of packet per connection')   
    plt.show()

def stdPkt():
    plt.plot(df['pkt_len_mean'], marker='o')
    plt.xlabel('Connection index')
    plt.ylabel('Length of packet in IP header')
    plt.title('Standard Deviation of Packet Length')   
    plt.show()

def varPkt():
    plt.plot(df['pkt_len_mean'], marker='o')
    plt.xlabel('Connection index')
    plt.ylabel('Length of packet in IP header')
    plt.title('Variance of Packet Length')   
    plt.show()

def subflow_forward():
    subflow_forward = df['subflow_fwd_byts'] / 1024
    plt.plot(subflow_forward, marker='o')
    plt.xlabel('Subflow index')
    plt.ylabel('Subflow forward speed [kilobytes/s]')
    plt.title('Subflow forward speed per connection')   
    plt.show()


def subflow_backward():
    subflow_backward = df['subflow_bwd_byts'] / 1024
    plt.plot(subflow_backward, marker='o')
    plt.xlabel('Subflow index')
    plt.ylabel('Subflow response speed [kilobytes/s]')
    plt.title('Subflow response speed per connection')   
    plt.show()

def subflow_packets_forward():
    plt.plot(df['subflow_fwd_pkts'], marker='o')
    plt.xlabel('Subflow index')
    plt.ylabel('Length of subflow packet forwarded')
    plt.title('Average length of subflow packet forwarded')   
    plt.show()

def subflow_packets_backward():
    plt.plot(df['subflow_bwd_pkts'], marker='o')
    plt.xlabel('Subflow index')
    plt.ylabel('Length of subflow packet backwarded')
    plt.title('Average length of subflow packet backwarder')   
    plt.show()




while True:
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

    print("Which graph you would like to see?")
    print("1. Source IP graph")
    print("2. Destiation IP graph")
    print("3. Source port graph")
    print("4. Destiation port graph")
    print("5. Source mac adress graph")
    print("6. Destiation mac adress graph")
    print("7. Time of connection in ms")
    print("8. Speed of connection in kbytes/s")
    print("9. Speed of connection in packet/s")
    print("10. Maximal lenght of packet per connection")
    print("11. Minimal lenght of packet per connection")
    print("12. Averege lenght of packet per connection")
    print("13. Standard Deviation of Packet Length")
    print("14. Variance of Packet Length ")
    print("15. Count of tcp flags in capture")
    print("16. Speed of subflow forward in kbytes/s")
    print("17. Speed of subflow response in kbytes/s")
    print("18. Average length of subflow packet forwarded")
    print("19. Average length of subflow packet backwarded")
    print("Type anything to exit the program")
    x = input("Please insert number: ")
    if (int(x) == 1):
        srcIP()
    elif(int(x) == 2): 
        destIP()
    elif(int(x) == 3):
        srcPort()
    elif(int(x) == 4):
        destPort()
    elif(int(x) == 5): 
        srcMac()
    elif(int(x) == 6): 
        destMac()
    elif(int(x) == 7): 
        flowDur()
    elif(int(x) == 8): 
        flowSpeed()
    elif(int(x) == 9 ):
        flowPkt() 
    elif(int(x) == 10): 
        maxPkt()
    elif(int(x) == 11): 
        minPkt()
    elif(int(x) == 12): 
        avgPkt()
    elif(int(x) == 13): 
        stdPkt()
    elif(int(x) == 14): 
        varPkt()
    elif(int(x) == 15):
        flag_count()
    elif(int(x) == 16): 
        subflow_forward()
    elif(int(x) == 17):
        subflow_backward()
    elif(int(x) == 18): 
        subflow_packets_forward()
    elif(int(x) == 19):
        subflow_packets_backward()
    else:
        break


