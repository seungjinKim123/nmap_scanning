import os

from modules.scanner import scan_ip
from modules.utils import read_ip_ranges
from modules.xml_manager import parse_and_update_xml

IP_RANGES_FILE = "ip_ranges.txt"
OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def main():
    ip_addresses = read_ip_ranges(IP_RANGES_FILE)
    
    for ip in ip_addresses:
        try:
            xml_file = scan_ip(ip, OUTPUT_FOLDER)
            parse_and_update_xml(xml_file)
        except Exception as e:
            print(f"Error processing {ip}: {e}")

if __name__ == "__main__":
    main()
