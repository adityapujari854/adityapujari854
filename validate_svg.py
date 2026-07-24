import xml.etree.ElementTree as ET
for name in ['dark.svg', 'light.svg']:
    ET.parse(name)
    print(name, 'OK')
