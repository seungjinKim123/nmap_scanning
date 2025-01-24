from lxml import etree
from modules.xml_manager import load_eos_services, parse_and_update_xml


def test_parse_and_update_xml_with_os_and_services(tmpdir):
    """Test parsing and updating an XML file with expanded EOS services."""
    # Sample XML content
    sample_xml_content = """
    <nmaprun>
        <host>
            <ports>
                <port>
                    <service product="windows" version="7" />
                </port>
                <port>
                    <service product="ssh" version="7.2" />
                </port>
                <port>
                    <service product="nginx" version="1.18.0" />
                </port>
            </ports>
        </host>
    </nmaprun>
    """
    
    # Write sample XML to a file
    xml_file = tmpdir.join("sample.xml")
    xml_file.write(sample_xml_content)
    
    # Write EOS services to a file
    eos_file = tmpdir.join("eos_services.txt")
    eos_file.write("windows 7\nssh 7.4\nnginx 1.18.0")
    
    # Parse and update XML
    parse_and_update_xml(str(xml_file), str(eos_file))
    
    # Validate the updated XML
    tree = etree.parse(str(xml_file))
    root = tree.getroot()

    # Verify comments were added for EOS services
    comments_windows = root.xpath(".//port[service/@product='windows']/*[name()='comment']")
    assert len(comments_windows) > 0, "No comments were added for Windows."

    comments_ssh = root.xpath(".//port[service/@product='ssh']/*[name()='comment']")
    assert len(comments_ssh) > 0, "No comments were added for SSH."

    comments_nginx = root.xpath(".//port[service/@product='nginx']/*[name()='comment']")
    assert len(comments_nginx) > 0, "No comments were added for Nginx."
