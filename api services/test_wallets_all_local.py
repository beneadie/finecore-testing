import requests
import concurrent.futures
import time

# Endpoint and headers
url_template = "http://localhost:8080/v1/wallets/2da3424b-1d1e-4155-a65e-d2347c37a73c"
headers = {
    "X-API-Key": "flk_6f1025328641a6b2b3b309cee58a27aa_1784140885"
}

# Function to send a request
def send_request(customer_id):
    url = url_template.format(customer_id)
    response = requests.get(url, headers=headers)
    return response.status_code, response.elapsed.total_seconds()

# Function to perform load test
def load_test(customer_ids, concurrent_requests):
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(send_request, customer_id) for customer_id in customer_ids]
        for future in concurrent.futures.as_completed(futures):
            try:
                status_code, response_time = future.result()
                print(f"Status Code: {status_code}, Response Time: {response_time:.4f} seconds")
            except Exception as e:
                print(f"Request generated an exception: {e}")

# Parameters for load test
customer_ids = [f"customer_{i}" for i in range(1, 1001)]  # Example customer IDs
concurrent_requests = 100  # Number of concurrent requests

# Perform load test
start_time = time.time()
load_test(customer_ids, concurrent_requests)
end_time = time.time()

print(f"Load test completed in {end_time - start_time:.2f} seconds")



# 10 concurrent requests local
"""
Status Code: 200, Response Time: 0.2360 seconds
Status Code: 200, Response Time: 0.2175 seconds
Status Code: 200, Response Time: 0.2070 seconds
Status Code: 200, Response Time: 0.2115 seconds
Status Code: 200, Response Time: 0.2320 seconds
Status Code: 200, Response Time: 0.2359 seconds
Status Code: 200, Response Time: 0.2151 seconds
Status Code: 200, Response Time: 0.2080 seconds
Status Code: 200, Response Time: 0.2400 seconds
Status Code: 200, Response Time: 0.1854 seconds
Status Code: 200, Response Time: 0.1875 seconds
Status Code: 200, Response Time: 0.2056 seconds
Status Code: 200, Response Time: 0.2027 seconds
Status Code: 200, Response Time: 0.2129 seconds
Load test completed in 23.02 seconds
"""


# 100 concurrent requests local

"""
Status Code: 200, Response Time: 2.2218 seconds
Status Code: 200, Response Time: 2.1960 seconds
Status Code: 200, Response Time: 2.1888 seconds
Status Code: 200, Response Time: 2.1824 seconds
Status Code: 200, Response Time: 2.2413 seconds
Status Code: 200, Response Time: 2.2107 seconds
Status Code: 200, Response Time: 2.2141 seconds
Status Code: 200, Response Time: 2.2176 seconds
Status Code: 200, Response Time: 2.2188 seconds
Status Code: 200, Response Time: 2.2139 seconds
Status Code: 200, Response Time: 2.1744 seconds
Status Code: 200, Response Time: 2.1831 seconds
Load test completed in 22.93 seconds
"""

