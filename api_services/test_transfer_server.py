import requests
import concurrent.futures
import time

# Endpoint URL and headers
url = "https://stagingapi.finecore.co/v1/transfers/bank"
headers = {
    "X-API-Key": "flk_6f1025328641a6b2b3b309cee58a27aa_1784140885",
    "Content-Type": "application/json"
}

# JSON data to be sent in the POST request
data = {
    "amount": 10,
    "sortCode": "000013",
    "narration": "Testing",
    "accountNumber": "1700263070",
    "accountName": "Obagunwa Emmanuel",
    "metadata": {
        "reason": "testing"
    }
}

# Function to send a POST request and return the status code and response time
def send_request():
    response = requests.post(url, headers=headers, json=data)
    return response.status_code, response.elapsed.total_seconds()

# Function to perform load test with concurrent requests
def load_test(concurrent_requests):
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(concurrent_requests)]
        for future in concurrent.futures.as_completed(futures):
            try:
                status_code, response_time = future.result()
                print(f"Status Code: {status_code}, Response Time: {response_time:.4f} seconds")
            except Exception as e:
                print(f"Request generated an exception: {e}")

# Parameters for load test
concurrent_requests = 1  # Number of concurrent requests

# Perform load test
start_time = time.time()
load_test(concurrent_requests)
end_time = time.time()

print(f"Load test completed in {end_time - start_time:.2f} seconds")


# 50 concurrent requests
# lots of 500s

# if you change the value of the account number it will come up as 500 error

"""
Status Code: 500, Response Time: 1.8663 seconds
Status Code: 500, Response Time: 1.9860 seconds
Status Code: 500, Response Time: 2.0844 seconds
Status Code: 500, Response Time: 2.1289 seconds
Status Code: 500, Response Time: 2.1203 seconds
Status Code: 500, Response Time: 2.1789 seconds
Status Code: 500, Response Time: 2.2293 seconds
Status Code: 500, Response Time: 2.2254 seconds
Status Code: 500, Response Time: 2.2190 seconds
Status Code: 500, Response Time: 2.3277 seconds
Status Code: 500, Response Time: 2.3704 seconds
Status Code: 500, Response Time: 2.3983 seconds
Status Code: 500, Response Time: 2.3947 seconds
Status Code: 500, Response Time: 2.4568 seconds
Status Code: 500, Response Time: 2.5029 seconds
Status Code: 500, Response Time: 2.5637 seconds
Status Code: 500, Response Time: 2.5790 seconds
Status Code: 500, Response Time: 2.5551 seconds
Status Code: 500, Response Time: 2.5789 seconds
Status Code: 500, Response Time: 2.5847 seconds
Status Code: 500, Response Time: 2.6187 seconds
Status Code: 500, Response Time: 2.6451 seconds
Status Code: 500, Response Time: 2.6358 seconds
Status Code: 500, Response Time: 2.6542 seconds
Status Code: 500, Response Time: 2.7401 seconds
Status Code: 500, Response Time: 2.7483 seconds
Status Code: 500, Response Time: 2.7260 seconds
Status Code: 500, Response Time: 2.7436 seconds
Status Code: 500, Response Time: 2.7400 seconds
Status Code: 500, Response Time: 2.7539 seconds
Status Code: 500, Response Time: 2.7509 seconds
Status Code: 500, Response Time: 2.7126 seconds
Status Code: 500, Response Time: 2.7026 seconds
Status Code: 500, Response Time: 2.7736 seconds
Status Code: 500, Response Time: 2.7333 seconds
Status Code: 500, Response Time: 2.7504 seconds
Status Code: 500, Response Time: 2.7460 seconds
Status Code: 500, Response Time: 2.7499 seconds
Status Code: 500, Response Time: 2.8047 seconds
Status Code: 500, Response Time: 2.7816 seconds
Status Code: 500, Response Time: 2.7700 seconds
Status Code: 500, Response Time: 2.7714 seconds
Status Code: 500, Response Time: 2.8048 seconds
Status Code: 500, Response Time: 2.7941 seconds
Status Code: 500, Response Time: 2.7861 seconds
Status Code: 500, Response Time: 2.8659 seconds
Status Code: 500, Response Time: 2.8565 seconds
Status Code: 500, Response Time: 2.8912 seconds
Status Code: 201, Response Time: 3.1057 seconds
Status Code: 201, Response Time: 3.2982 seconds
Load test completed in 3.38 seconds
"""
