import xml.etree.ElementTree as ET


def parse_and_update_xml(xml_file):
    """XML 파일을 파싱하고 취약점 의심 사항 표시."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for host in root.findall("host"):
        for port in host.findall(".//port"):
            service = port.find("service")
            if service is not None:
                product = service.get("product", "Unknown")
                version = service.get("version", "Unknown")
                
                if "EOS" in product or "outdated" in version.lower():
                    comment = ET.Comment(f"Service {product} version {version} might be vulnerable.")
                    port.append(comment)
    
    tree.write(xml_file)
    print(f"Updated XML file: {xml_file}")
