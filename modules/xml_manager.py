from lxml import etree


def load_eos_services(eos_file):
    """EOS 서비스와 버전을 텍스트 파일에서 읽어오기."""
    eos_services = {}
    try:
        with open(eos_file, "r") as file:
            for line in file:
                line = line.strip()
                # 빈 줄 및 주석(#) 무시
                if not line or line.startswith("#"):
                    continue
                parts = line.split()  # 공백 또는 탭으로 분리
                if len(parts) == 2:
                    service, eos_version = parts
                    eos_services[service.lower()] = eos_version
        return eos_services
    except FileNotFoundError:
        print(f"Error: EOS file '{eos_file}' not found.")
        return {}



def parse_and_update_xml(xml_file, eos_file):
    """XML 파일을 파싱하고 취약점 의심 사항 표시."""
    # EOS 서비스 목록 로드
    eos_services = load_eos_services(eos_file)
    print(f"Loaded EOS services: {eos_services}")  # 디버깅 출력
    
    tree = etree.parse(xml_file)
    root = tree.getroot()

    for port in root.xpath(".//port"):
        service = port.find("service")
        if service is not None:
            product = service.get("product", "Unknown")
            version = service.get("version", "Unknown")
            
            # 버전 정보가 없는 경우 로그를 남기고 다음 포트로 넘어감
            if version == "Unknown":
                print(f"Skipping port with service {product}: version information not available.")
                continue
            
            # EOS 및 취약점 의심 로직 (서비스와 버전 비교)
            if product.lower() in eos_services:
                eos_version = eos_services[product.lower()]
                if version <= eos_version:
                    comment_text = f"Service {product} version {version} might be vulnerable (EOS latest: {eos_version})."
                    comment = etree.Comment(comment_text)
                    
                    # 주석을 <service> 태그 바로 뒤에 추가
                    service_index = list(port).index(service)
                    port.insert(service_index + 1, comment)

    # 디버깅: XML 출력
    print(etree.tostring(root, pretty_print=True, encoding="unicode"))
    
    # XML 파일 업데이트
    tree.write(xml_file, pretty_print=True, encoding="UTF-8", xml_declaration=True)
    print(f"Updated XML file: {xml_file}")
