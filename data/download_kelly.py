import requests

url = 'https://svn.spraakbanken.gu.se/sb-arkiv/pub/lmf/kelly/kelly.xml'
output_file = 'kelly.xml'

response = requests.get(url)

if response.status_code == 200:
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f"✅ File downloaded and saved as '{output_file}'")
else:
    print(f"❌ Failed to download file. Status code: {response.status_code}")