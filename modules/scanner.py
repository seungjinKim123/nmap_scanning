import os

from nmap import PortScanner


def scan_ip(ip_address, output_folder):
    """주어진 IP 주소를 스캔하고 XML로 저장."""
    scanner = PortScanner()
    print(f"Scanning {ip_address}...")
    scanner.scan(ip_address, arguments="-sV")
    output_file = os.path.join(output_folder, f"{ip_address}.xml")
    scanner.export_to_file(output_file)
    return output_file
