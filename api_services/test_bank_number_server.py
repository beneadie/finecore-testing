import requests
import concurrent.futures
import time

# Base URL and headers
url = "https://api.finecore.co/v1/transfers/banks"
headers = {
    "X-API-Key": "fsk_5b0c0b7d6359fc06b70ae27d4f8468d210b9ed8a2c0105dcd7a587c90f779d8f_438241922"
}

# Function to send a POST request and return the status code and response time
def send_request():
    response = requests.get(url, headers=headers)
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

arr_times = []
# Perform load test
for i in range(50):
    start_time = time.time()
    load_test(concurrent_requests)
    end_time = time.time()
    latency = end_time - start_time
    arr_times.append(latency)
    print(f"Load test completed in {end_time - start_time:.2f} seconds")

print(f"Average latency: {sum(arr_times)/len(arr_times)}")


# Average latency: 0.5468312692642212 for single request

# Average latency: 0.5109046077728272 for 2 concucrrent requests

# Average latency: 0.785199384689331 for 4 concurrent requests
