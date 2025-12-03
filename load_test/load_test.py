import threading
import requests

class LoadTestThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        try:
            response = requests.get(self.url)
            print(f"Response Code: {response.status_code} for URL: {self.url}")
        except Exception as e:
            print(f"Error: {e}")

def generate_load(url, num_requests):
    threads = []
    for _ in range(num_requests):
        thread = LoadTestThread(url)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_url = "https://ca-clouds-lab.mangoriver-5484e137.westeurope.azurecontainerapps.io"  # Replace with your server URL
    number_of_requests = 10000  # Adjust the number of requests as needed
    generate_load(target_url, number_of_requests)