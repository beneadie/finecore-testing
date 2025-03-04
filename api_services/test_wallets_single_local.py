import requests
import concurrent.futures
import time

# Base URL and headers
base_url = "http://localhost:8080/v1/wallets"
headers = {
    "X-API-Key": "fsk_5b0c0b7d6359fc06b70ae27d4f8468d210b9ed8a2c0105dcd7a587c90f779d8f_438241922",
}

# Array of customer IDs
customer_ids = [
     "34231443-3895-4604-b6f4-a70ed87b302e",
     "d80fdb1d-3df1-4213-8633-ec8949d2192d",
     "46d9d71d-40a2-4228-a300-7cb9c02b7cf0",
     "4a8fc71b-c999-4d14-b272-19cc5db27937",
     "6717ba2d-d4c2-4b60-8a32-0d53da089bb9",
     "6d21af05-592a-41ab-96b2-1283783eaef9",
]

times_arr = []

# Function to send a request for a specific customer ID
def send_request(customer_id):
     url = f"{base_url}/{customer_id}"
     response = requests.get(url, headers=headers)
     return response.status_code, response.elapsed.total_seconds()

# Function to perform load test
def load_test(customer_ids, concurrent_requests):
     with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
          futures = [executor.submit(send_request, customer_id) for customer_id in customer_ids]
          for future in concurrent.futures.as_completed(futures):
               try:
                    status_code, response_time = future.result()
                    times_arr.append(response_time)
                    print(f"Status Code: {status_code}, Response Time: {response_time:.4f} seconds")
               except Exception as e:
                    print(f"Request generated an exception: {e}")

# Parameters for load test
concurrent_requests = 2  # Number of concurrent requests

times_arr = []
# Perform load test
for i in range(200):
    start_time = time.time()
    load_test(customer_ids, concurrent_requests)
    end_time = time.time()
    latency = end_time - start_time
    times_arr.append(latency)
    print(f"Load test completed in {end_time - start_time:.2f} seconds")

print(f"Average latency: {sum(times_arr)/len(times_arr)}")


# 10 concurrent requests local
#"""
#Status Code: 200, Response Time: 0.2264 seconds
#Status Code: 200, Response Time: 0.2257 seconds
#Status Code: 200, Response Time: 0.2248 seconds
#Status Code: 200, Response Time: 0.2152 seconds
#Status Code: 200, Response Time: 0.2082 seconds
#Status Code: 200, Response Time: 0.2383 seconds
#Status Code: 200, Response Time: 0.2257 seconds
#Status Code: 200, Response Time: 0.2384 seconds
#Status Code: 200, Response Time: 0.2334 seconds
#Status Code: 200, Response Time: 0.2244 seconds
#Status Code: 200, Response Time: 0.2043 seconds
#Status Code: 200, Response Time: 0.2057 seconds
#Status Code: 200, Response Time: 0.2331 seconds
#Status Code: 200, Response Time: 0.2322 seconds
#Status Code: 200, Response Time: 0.2357 seconds
#Status Code: 200, Response Time: 0.2063 seconds
#Status Code: 200, Response Time: 0.1993 seconds
#Status Code: 200, Response Time: 0.1896 seconds
#Status Code: 200, Response Time: 0.1896 seconds
#Status Code: 404, Response Time: 0.1992 seconds
#0.22947199249999997
#Load test completed in 27.90 seconds
#"""
#
## 100 concurrent request
#"""
#Status Code: 200, Response Time: 2.2108 seconds
#Status Code: 200, Response Time: 2.2681 seconds
#Status Code: 200, Response Time: 2.2120 seconds
#Status Code: 200, Response Time: 2.2707 seconds
#Status Code: 200, Response Time: 2.2095 seconds
#Status Code: 200, Response Time: 2.2198 seconds
#Status Code: 200, Response Time: 2.2241 seconds
#Status Code: 200, Response Time: 2.2073 seconds
#Status Code: 200, Response Time: 2.2112 seconds
#Status Code: 200, Response Time: 2.2122 seconds
#Status Code: 200, Response Time: 2.2683 seconds
#Status Code: 200, Response Time: 2.2121 seconds
#Status Code: 200, Response Time: 2.2167 seconds
#Status Code: 200, Response Time: 2.1730 seconds
#Status Code: 200, Response Time: 2.2095 seconds
#Status Code: 200, Response Time: 2.2096 seconds
#Status Code: 200, Response Time: 2.2072 seconds
#Status Code: 200, Response Time: 2.2052 seconds
#Status Code: 200, Response Time: 2.2071 seconds
#Status Code: 200, Response Time: 2.2248 seconds
#Status Code: 200, Response Time: 2.2173 seconds
#Status Code: 404, Response Time: 2.1650 seconds
#2.23806706833333
#Load test completed in 27.36 seconds
#"""
#
