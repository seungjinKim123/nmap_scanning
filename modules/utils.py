def read_ip_ranges(file_path):
    """IP 대역 파일 읽기."""
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]
