# nmap scanning tool

## Feature
- Scans IP addresses and saves results as XML
- Parses XML to detect End of Service (EOS) or outdated services
- Modular design for scalability

## Requirements
- Python 3.x
- Nmap installed on your system

## Installation
1. Clone the repository
```
git clone <repository-url>
cd project
```
2. Create and active a virtual environment
```
python -m venv venv
source venv/bin/activate    # Linux / macOS
.\venv\Scripts\activate     # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```

## Usage
1. Add IP ranges to 'ip_ranges.txt' (one per line):
```
192.168.1.1
192.168.1.0/24
```
2. Run the script:
```
python main.py
```
3. Check the 'outputs' folder for XML results.

## License
MIT License

## dir structure
```
project/
│
├── venv/                   # 가상환경 폴더 (Git에서 제외됨)
├── ip_ranges.txt           # 입력 파일: IP 대역 목록
├── requirements.txt        # 필요한 패키지 목록
├── main.py                 # 실행 스크립트
├── modules/                # 모듈 폴더
│   ├── __init__.py         # 모듈 초기화 파일
│   ├── scanner.py          # Nmap 스캔 모듈
│   ├── xml_manager.py      # XML 생성 및 분석 모듈
│   └── utils.py            # 기타 유틸리티 함수 모듈
├── outputs/                # 결과 XML 저장 폴더 (Git에서 제외됨)
│
├── .gitignore              # Git 무시 파일
└── README.md               # 프로젝트 설명 파일
```
