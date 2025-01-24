import requests

class UpicMediaClient:
    BASE_URL = "https://upic.media/api/"

    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }

    def get_classes_files(self, slug):
        """Retrieve files of a specific class by slug."""
        url = f"{self.BASE_URL}classes/files"
        params = {"slug": slug}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def get_classes_index(self):
        """Retrieve the index of all classes."""
        url = f"{self.BASE_URL}classes/index"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def search_labels(self, name, scan=None, class_id=None):
        """Search labels by name, scan, or class."""
        url = f"{self.BASE_URL}labels"
        params = {
            "name": name,
            "scan": scan or "",
            "class": class_id or "",
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
