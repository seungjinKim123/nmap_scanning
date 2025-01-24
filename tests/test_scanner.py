import os

from lxml import etree
from modules.scanner import scan_ip


def test_scan_ip_matches_zenmap_format(tmpdir):
    """Test that the generated XML file matches Zenmap's format."""
    output_folder = tmpdir.mkdir("outputs")
    ip_address = "127.0.0.1"
    
    # Perform the scan
    xml_file = scan_ip(ip_address, str(output_folder))
    
    # Assertions
    assert os.path.exists(xml_file), "XML file was not created."
    
    # Validate the structure of the XML file
    tree = etree.parse(xml_file)
    root = tree.getroot()
    
    # Check root element
    assert root.tag == "nmaprun", "Root element is not <nmaprun>."
    
    # Check required attributes in <nmaprun>
    required_attributes = ["start", "args", "scanner", "version", "startstr"]
    for attr in required_attributes:
        assert root.get(attr) is not None, f"Missing attribute '{attr}' in <nmaprun>."
    
    # Check for <host> element
    hosts = root.findall("host")
    assert len(hosts) > 0, "No <host> elements found in the XML."
    
    # Check for <ports> and <port> elements
    for host in hosts:
        ports = host.find("ports")
        assert ports is not None, "<ports> element is missing."
        for port in ports.findall("port"):
            assert port.get("portid") is not None, "<port> is missing 'portid' attribute."
            state = port.find("state")
            assert state is not None, "No <state> element in <port>."
            service = port.find("service")
            assert service is not None, "No <service> element in <port>."
