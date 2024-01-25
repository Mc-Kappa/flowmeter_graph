How to run?
Download repo with CiC flow meter: https://gitlab.com/hieulw/cicflowmeter and install

git clone https://gitlab.com/hieulw/cicflowmeter
cd cicflowmeter
python setup.py install
pip install pandas matpotlib

How to use?
1. Collect data with tcp dump or wireshark (it has to be in .pcap format)
2. Prepare .csv with cic flowmeter:
   - cicflowmeter -f example.pcap -c flows.csv
3. run out script with python graphs.py file_name.csv

Enjoy beautyful graphs.


