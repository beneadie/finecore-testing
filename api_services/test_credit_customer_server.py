import requests
import concurrent.futures
import time

# Endpoint URL and headers
#url = "https://stagingapi.finecore.co/v1/wallets/credit"
url = "http://localhost:8080/v1/wallets/credit"

headers = {
    "X-API-Key": "fsk_ee792fd278a5bc0bba7dfd9e0346e4659dd50edb7f8f3ccd3d490b082a450906_748844942", #"flk_6f1025328641a6b2b3b309cee58a27aa_1784140885",
    "Content-Type": "application/json"
}

# Array of customer IDs
customer_ids =[
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546",
    "7f44ad80-205b-46df-a7e3-70bda0884546"

]

# Function to send POST request and print response
def send_request(customer_id):
    data = {
        "amount": 200,
        "customer_id": customer_id,
        "metadata": {
            "reason": "for completion of task"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")

# Function to perform load test with concurrent requests
def load_test(customer_ids, concurrent_requests):
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(send_request, customer_id) for customer_id in customer_ids]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Request generated an exception: {e}")

# Parameters for load test
concurrent_requests = 2  # Number of concurrent requests

# Perform load test
start_time = time.time()
load_test(customer_ids, concurrent_requests)
end_time = time.time()

print(f"Load test completed in {end_time - start_time:.2f} seconds")



 #test
 #first run on server worked fine but after doing a local test
 #issue is a t the DB level but not necessarily caused by the DB
 #could also be providus
 #after doing local test which ran indefinitely, the server test ended up having issues with performance
 #changes to test if providus
"""
Status Code: 400
Request generated an exception: Extra data: line 2 column 1 (char 95)
Status Code: 400
Request generated an exception: Extra data: line 2 column 1 (char 95)
Status Code: 400
Request generated an exception: Extra data: line 2 column 1 (char 95)
Status Code: 400
Request generated an exception: Extra data: line 2 column 1 (char 95)
Status Code: 400
Status Code: 400
Request generated an exception: Extra data: line 2 column 1 (char 95)
Request generated an exception: Extra data: line 2 column 1 (char 95)
Request generated an exception: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
Request generated an exception: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
"""
# after local test
"""
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}

"""



#first server test
"""
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Load test completed in 5.64 seconds
(venv) PS C:\Users\User\Documents\GitHub\finecore-testing> python test_credit_customer.py
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Status Code: 400
Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
Load test completed in 2.49 seconds
"""

