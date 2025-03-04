import requests
import concurrent.futures
import time

# Base URLs and headers
local_url = "http://localhost:8080/v1/transactions/customer/" #2da3424b-1d1e-4155-a65e-d2347c37a73c/TXN-1736445726-87dc1349d8f78a0a
#server_url = "https://stagingapi.finecore.co/v1/transactions/customer/2da3424b-1d1e-4155-a65e-d2347c37a73c/TXN-1736445726-87dc1349d8f78a0a"
headers = {
    "X-API-Key": "fsk_5b0c0b7d6359fc06b70ae27d4f8468d210b9ed8a2c0105dcd7a587c90f779d8f_438241922",
}

# Function to send a GET request and return the status code and response time
def send_request(url):
    response = requests.get(url, headers=headers)
    return response.status_code, response.elapsed.total_seconds()

# Function to perform load test with concurrent requests
def load_test(url, concurrent_requests):
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(send_request, url) for _ in range(concurrent_requests)]
        for future in concurrent.futures.as_completed(futures):
            try:
                status_code, response_time = future.result()
                print(f"Status Code: {status_code}, Response Time: {response_time:.4f} seconds")
            except Exception as e:
                print(f"Request generated an exception: {e}")

# Parameters for load test
concurrent_requests = 1  # Number of concurrent requests

time_arr= []
# Perform load test for local endpoint
for i in range(50):
    start_time = time.time()
    load_test(local_url, concurrent_requests)
    end_time = time.time()
    latency = end_time - start_time
    time_arr.append(latency)
    print(f"Load test for local endpoint completed in {end_time - start_time:.2f} seconds\n")

print(f"Average latency: {sum(time_arr)/len(time_arr)}")


# not sure why 500 local

"""
Starting load test for local endpoint...
Status Code: 500, Response Time: 2.3403 seconds
Status Code: 500, Response Time: 2.3643 seconds
Status Code: 500, Response Time: 2.4153 seconds
Status Code: 500, Response Time: 2.4143 seconds
Status Code: 500, Response Time: 2.5320 seconds
Status Code: 500, Response Time: 2.5606 seconds
Status Code: 500, Response Time: 2.6158 seconds
Status Code: 500, Response Time: 2.6142 seconds
Status Code: 500, Response Time: 2.7603 seconds
Status Code: 500, Response Time: 2.7719 seconds
Load test for local endpoint completed in 2.79 seconds

Starting load test for server endpoint...
Status Code: 200, Response Time: 0.7920 seconds
Status Code: 200, Response Time: 0.7980 seconds
Status Code: 200, Response Time: 0.8229 seconds
Status Code: 200, Response Time: 0.8174 seconds
Status Code: 200, Response Time: 0.8270 seconds
Status Code: 200, Response Time: 0.8252 seconds
Status Code: 200, Response Time: 0.8427 seconds
Status Code: 200, Response Time: 0.9024 seconds
Status Code: 200, Response Time: 0.9130 seconds
Status Code: 200, Response Time: 0.9322 seconds
Load test for server endpoint completed in 0.93 seconds

"""
