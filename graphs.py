import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flows.csv')

def srcIP():
    counts = df['src_ip'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('IP address')
    plt.ylabel('Connections count')
    plt.title('Count of ergress connections per IP')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def destIP():
    counts = df['dst_ip'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('IP address')
    plt.ylabel('Connections count')
    plt.title('Count of ingress connections per IP')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def srcPort():
    counts = df['src_port'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('Port number')
    plt.ylabel('Connections count')
    plt.title('Count of ergress connections per port')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def destPort():
    counts = df['dst_port'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('Port number')
    plt.ylabel('Connections count')
    plt.title('Count of ingress connections per port')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def srcMac():
    counts = df['src_mac'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('Mac address')
    plt.ylabel('Connections count')
    plt.title('Count of ingress connections per mac address')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def destMac():
    counts = df['dst_mac'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index.astype(str), counts.values, color='lightblue')
    plt.xlabel('Port number')
    plt.ylabel('Connections count')
    plt.title('Count of ingress connections per port')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def flowDur():
    df['flow_duration_ms'] = df['flow_duration'] / 1000
    # Ustawienia wykresu
    plt.plot(df['flow_duration_ms'], marker='o')
    plt.xlabel('Indeks połączenia')
    plt.ylabel('Connection lenght (ms)')
    plt.title('Czas trwania połączenia dla różnych indeksów')   
    plt.show()

def flowPkt():
    df['flow_kbyts_s'] = df['flow_byts_s'] / 1024
    # Ustawienia wykresu
    plt.plot(df['flow_kbyts_s'], marker='o')
    plt.xlabel('Indeks połączenia')
    plt.ylabel('Connection speed [kilobytes/s]')
    plt.title('Connection speed per connection')   
    plt.show()

def flag_count():
    # Wybierz konkretne kolumny
    wybrane_kolumny = ['fwd_psh_flags', 'bwd_psh_flags', 'fwd_urg_flags', 'bwd_urg_flags', 'fin_flag_cnt', 'syn_flag_cnt', 'rst_flag_cnt', 'psh_flag_cnt', 'ack_flag_cnt', 'urg_flag_cnt', 'ece_flag_cnt']

    # Oblicz sumę dla wybranych kolumn
    sumy_kolumn = df[wybrane_kolumny].sum()

    # Generuj wykres słupkowy
    plt.bar(sumy_kolumn.index, sumy_kolumn.values)
    plt.xlabel('Flag name')
    plt.ylabel('Sum')
    plt.title('Sums of flags')
    plt.show()


while True:
    print("Which graph you would like to see?")
    print("1. Source IP graph")
    print("2. Destiation IP graph")
    print("3. Source port graph")
    print("4. Destiation port graph")
    print("5. Source mac adress graph")
    print("6. Destiation mac adress graph")
    print("7. Destiation time of connection in ms")
    print("8. Speed of connection in kbytes/s")
    print("9. Count of tcp flags in capture")
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
        flowPkt()
    elif(int(x) == 9): 
        flag_count()
    else:
        break


