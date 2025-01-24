from modules.utils import read_ip_ranges


def test_read_ip_ranges(tmpdir):
    """Test reading IP ranges from a file."""
    # Create a temporary file with IP ranges
    ip_file = tmpdir.join("ip_ranges.txt")
    ip_file.write("192.168.1.1\n192.168.1.0/24\n")
    
    # Read IP ranges
    ip_ranges = read_ip_ranges(str(ip_file))
    
    # Assertions
    assert len(ip_ranges) == 2, "Number of IP ranges read is incorrect."
    assert ip_ranges[0] == "192.168.1.1", "First IP range is incorrect."
    assert ip_ranges[1] == "192.168.1.0/24", "Second IP range is incorrect."
