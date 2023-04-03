import json
import urllib.request

metadata_url = 'http://169.254.169.254/latest/meta-data/'

def get_instance_metadata():
    metadata = {}
    response = urllib.request.urlopen(metadata_url)
    for line in response:
        key = line.decode('utf-8').split('/')[0]
        value = urllib.request.urlopen(metadata_url + line.decode('utf-8')).read().decode('utf-8')
        metadata[key] = value
    return metadata

metadata = get_instance_metadata()
json_output = json.dumps(metadata, indent=4)
print(json_output)
