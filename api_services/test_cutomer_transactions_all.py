import requests
import concurrent.futures
import time

# Base URLs and headers
# my code not up to date. works fine on staging url

local_url = "http://localhost:8080/v1/transactions/customer/2da3424b-1d1e-4155-a65e-d2347c37a73c" #34231443-3895-4604-b6f4-a70ed87b302e"
local_url = "https://stagingapi.finecore.co/v1/transactions/customer/2da3424b-1d1e-4155-a65e-d2347c37a73c"
headers = {
    #"X-API-Key": "flk_6f1025328641a6b2b3b309cee58a27aa_1784140885"
    "X-API-Key": "fsk_5b0c0b7d6359fc06b70ae27d4f8468d210b9ed8a2c0105dcd7a587c90f779d8f_438241922"
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

time_arr = []
# Perform load test for local endpoint

for i in range(50):
    start_time = time.time()
    load_test(local_url, concurrent_requests)
    end_time = time.time()
    latency = end_time - start_time
    time_arr.append(latency)
    print(f"Load test for local endpoint completed in {end_time - start_time:.2f} seconds")


print(f"Average latency for local endpoint: {sum(time_arr)/len(time_arr)}")

# gets 500 here and on postman for local but server is okay

"""
Starting load test for local endpoint...
Status Code: 500, Response Time: 0.6202 seconds
Status Code: 500, Response Time: 0.6255 seconds
Status Code: 500, Response Time: 0.6241 seconds
Status Code: 500, Response Time: 0.6266 seconds
Status Code: 500, Response Time: 0.8224 seconds
Status Code: 500, Response Time: 0.8227 seconds
Status Code: 500, Response Time: 0.8204 seconds
Status Code: 500, Response Time: 0.8300 seconds
Status Code: 500, Response Time: 1.0204 seconds
Status Code: 500, Response Time: 1.0221 seconds
Load test for local endpoint completed in 1.05 seconds

Starting load test for server endpoint...
Status Code: 200, Response Time: 0.4385 seconds
Status Code: 200, Response Time: 0.4533 seconds
Status Code: 200, Response Time: 0.4410 seconds
Status Code: 200, Response Time: 0.4419 seconds
Status Code: 200, Response Time: 0.4571 seconds
Status Code: 200, Response Time: 0.4536 seconds
Status Code: 200, Response Time: 0.4558 seconds
Status Code: 200, Response Time: 0.4670 seconds
Status Code: 200, Response Time: 0.7778 seconds
Status Code: 200, Response Time: 0.7876 seconds
Load test for server endpoint completed in 0.80 seconds

"""
