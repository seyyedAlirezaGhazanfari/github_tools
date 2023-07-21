import requests

def get_dirs(content_resp, file_count):
    for item in content_resp:
        if item.get("type") == "dir":
            dir_url = item.get("url")
            dir_extractor(file_count, dir_url)

def count_file_number(file_count, contents_data):
    for item in contents_data:
        if item.get("type") == "file":
            file_count += 1
            print(item.get("path"))

def count_files_in_github_repo(file_count):
    contents_url = f"{base_url}/contents"
    contents_response = requests.get(contents_url, headers=headers)
    if contents_response.status_code != 200:
        print(f"Error: Unable to access the repository contents. Status code: {contents_response.status_code}")
        return -1
    contents_data = contents_response.json()
    count_file_number(file_count, contents_data)
    get_dirs(contents_data, file_count)

def dir_extractor(file_count, url):
    contents_response = requests.get(url, headers=headers)
    if contents_response.status_code != 200:
        print(url)
        print(f"Error: Unable to access the repository contents. Status code: {contents_response.status_code}")
        return -1
    contents_data = contents_response.json()
    count_file_number(file_count, contents_data)
    get_dirs(contents_data, file_count)


# Replace these variables with your repository details

repo_owner = "owner"
repo_name = "name"
access_token = "your token"
base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
headers = {"Authorization": f"token {access_token}",}
file_count = 0
num_files = count_files_in_github_repo(file_count=file_count)
print(f"Number of files in the repository: {num_files}")
