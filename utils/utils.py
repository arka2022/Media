import requests
from utils.constants import s3_url, s3_bucket_name, cloud_front
import wget as wget

def upload_file_to_s3(file_path, file_name):
    url = s3_url + "upload"
    payload = {'file_path': f'{s3_bucket_name}/thumbnails'}
    print(f"file path {file_path} {file_name.split('/')[1]}")
    files = [
        ('file',
         (file_name.split("/")[1], open(file_name, 'rb'), 'application/octet-stream'))
    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(f'{file_name}: {response.status_code}')
def download_file_from_s3(file_name, path_to_save):
    print(f'proceeding to download file:{file_name}')
    url = f'{cloud_front}{file_name}'
    response = wget.download(url, path_to_save)
    print('Download complete')
    return response