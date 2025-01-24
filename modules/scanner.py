import os
import subprocess


def scan_ip(ip_address, output_folder):
    """주어진 IP 주소를 스캔하고 XML로 저장."""
    # Nmap 결과를 저장할 XML 파일 경로
    output_file = os.path.join(output_folder, f"{ip_address}.xml")
    
    # Nmap 명령 실행
    command = [
        "nmap", ip_address,
        "-sT",  # TCP 연결 스캔
        "-sV",  # 서비스와 버전 정보 스캔
        "-T4",  # 빠른 스캔 속도
        "-A",   # 추가 정보 수집 (OS, 서비스 버전 등)
        "-oX", output_file  # 결과를 XML로 저장
    ]
    print(f"Running Nmap scan: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Nmap 실행 결과 출력
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(f"Nmap scan failed: {result.stderr}")
    
    # 파일이 생성되었는지 확인
    if not os.path.exists(output_file):
        raise FileNotFoundError(f"Nmap did not create the expected XML file: {output_file}")
    
    print(f"Scan completed and saved to {output_file}")
    return output_file
