import requests
import concurrent.futures
import time

# Endpoint URL and headers
url = "http://localhost:8080/v1/transfers/bank"
headers = {
    "X-API-Key": "fsk_5b0c0b7d6359fc06b70ae27d4f8468d210b9ed8a2c0105dcd7a587c90f779d8f_438241922",
    "Content-Type": "application/json"
}

# JSON data to be sent in the POST request
#AMOUNT MUST BE GREATER THAN 50
data = {
    "amount": 60,
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

# 50 concurrent requests
# lots of 500s

#"""
#Status Code: 500, Response Time: 1.2394 seconds
#Status Code: 500, Response Time: 1.7160 seconds
#Status Code: 500, Response Time: 1.8374 seconds
#Status Code: 500, Response Time: 1.8332 seconds
#Status Code: 500, Response Time: 1.8545 seconds
#Status Code: 500, Response Time: 1.8644 seconds
#Status Code: 500, Response Time: 1.8868 seconds
#Status Code: 500, Response Time: 1.8992 seconds
#Status Code: 500, Response Time: 1.9106 seconds
#Status Code: 201, Response Time: 1.9513 seconds
#Status Code: 500, Response Time: 1.9448 seconds
#Status Code: 201, Response Time: 1.9653 seconds
#Status Code: 500, Response Time: 1.9535 seconds
#Status Code: 500, Response Time: 1.9529 seconds
#Status Code: 500, Response Time: 1.9516 seconds
#Status Code: 500, Response Time: 1.9574 seconds
#Status Code: 500, Response Time: 1.9646 seconds
#Status Code: 500, Response Time: 1.9920 seconds
#Status Code: 500, Response Time: 2.0194 seconds
#Status Code: 500, Response Time: 2.0315 seconds
#Status Code: 500, Response Time: 2.0659 seconds
#Status Code: 500, Response Time: 2.0673 seconds
#Status Code: 500, Response Time: 2.0721 seconds
#Status Code: 500, Response Time: 2.0817 seconds
#Status Code: 500, Response Time: 2.0790 seconds
#Status Code: 500, Response Time: 2.0914 seconds
#Status Code: 500, Response Time: 2.0924 seconds
#Status Code: 500, Response Time: 2.1020 seconds
#Status Code: 500, Response Time: 2.1057 seconds
#Status Code: 201, Response Time: 2.1726 seconds
#Status Code: 500, Response Time: 2.1201 seconds
#Status Code: 500, Response Time: 2.1232 seconds
#Status Code: 500, Response Time: 2.1199 seconds
#Status Code: 500, Response Time: 2.1272 seconds
#Status Code: 500, Response Time: 2.1447 seconds
#Status Code: 500, Response Time: 2.1461 seconds
#Status Code: 500, Response Time: 2.1740 seconds
#Status Code: 500, Response Time: 2.1786 seconds
#Status Code: 500, Response Time: 2.1710 seconds
#Status Code: 500, Response Time: 2.1721 seconds
#Status Code: 500, Response Time: 2.1705 seconds
#Status Code: 500, Response Time: 2.1769 seconds
#Status Code: 500, Response Time: 2.1943 seconds
#Status Code: 500, Response Time: 2.1915 seconds
#Status Code: 500, Response Time: 2.2037 seconds
#Status Code: 500, Response Time: 2.2019 seconds
#Status Code: 500, Response Time: 2.2069 seconds
#Status Code: 500, Response Time: 2.2284 seconds
#Status Code: 201, Response Time: 2.3781 seconds
#Status Code: 201, Response Time: 2.5622 seconds
#Load test completed in 2.66 seconds
#
#"""
#
