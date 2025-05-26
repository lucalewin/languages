import xml.etree.ElementTree as ET
import json

input_file = 'kelly.xml'
output_file = 'kelly.json'

tree = ET.parse(input_file)
root = tree.getroot()

entries = []

# Iterate over all LexicalEntry elements
for entry in root.findall('.//LexicalEntry'):
    entry_data = {}

    # FormRepresentation
    form_repr = entry.find('.//FormRepresentation')
    if form_repr is not None:
        for feat in form_repr.findall('feat'):
            key = feat.attrib.get('att')
            val = feat.attrib.get('val')
            if key:
                entry_data[key] = val

    # Sense
    sense = entry.find('Sense')
    if sense is not None:
        entry_data['sense_id'] = sense.attrib.get('id')
        saldo_senses = [
            feat.attrib.get('val')
            for feat in sense.findall('feat')
            if feat.attrib.get('att') == 'saldoSense'
        ]
        if saldo_senses:
            entry_data['saldoSense'] = saldo_senses

    # Multiple karp:saldoLink elements (namespace-aware)
    saldo_links = [
        link.attrib.get('ref')
        for link in entry.findall('{http://spraakbanken.gu.se/eng/research/infrastructure/karp/karp}saldoLink')
    ]
    if saldo_links:
        entry_data['saldoLinks'] = saldo_links

    entries.append(entry_data)

# Save as JSON
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"✅ Saved to '{output_file}' with {len(entries)} entries.")