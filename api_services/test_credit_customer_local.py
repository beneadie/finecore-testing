import requests
import concurrent.futures
import time

# Endpoint URL and headers
url = "http://localhost:8080/v1/wallets/credit"
headers = {
    "X-API-Key": "flk_6f1025328641a6b2b3b309cee58a27aa_1784140885",
    "Content-Type": "application/json"
}

# Array of customer IDs
customer_ids =[
    "4d12f338-401d-4be4-8596-f9736c96d07e",
    "207177e0-f8a1-45b0-93f9-92935c4dafbb",
    "73a11ec8-b5a4-4bf1-bb4f-4b79352b7a36",
    "090558fd-63d0-45a7-b846-b4f18bbeeae3",
    "d14d275c-5d79-4cb3-b5a6-21754ab773cb",
    "2715cc19-72e7-48ed-9832-72966f890a75",
    "5a6ca30a-328e-4779-93ec-0112e978e943",
    "be6bd533-3de7-4d78-acb7-4cce5b0f8ba3",
    "99332140-f1ba-4a9e-8caa-dbf6c90cbd85",
    "a3eb2310-7d48-4267-843a-4a7a9e98ee6f",
    "e593cb90-c29d-43b3-80ad-dd72cdde7542",
    "c848116f-ca1d-4edf-9497-54d8bd8d9cea",
    "ec9a9272-ce5e-4450-bdad-3993cafd16c4",
    "efc51969-4ac8-400d-a0b7-363b6dc98999",
    "b4d90203-02fb-4b4b-9a8e-b91f63994c13",
    "71755d38-1420-48f2-898c-174d46e241c5",
    "30f4142b-49e5-43a5-84ef-2d38d349b82c",
    "e48ab0c9-ba33-487b-890c-75e4b6aa382c",
    "b7f13129-fc6a-453b-bdca-09f45d895b0d",
    "976cb9b1-22e3-428c-b1f2-a430a1a423b7"
]

# Function to send POST request and print response
def send_request(customer_id):
    data = {
        "amount": 1,
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



# test that ran indefinitely
# only 2 concurrent requests

#"""
#Status Code: 400
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Status Code: 400
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Status Code: 400
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Status Code: 400
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Status Code: 400
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Status Code: 400
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Status Code: 400
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Request generated an exception: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
#Request generated an exception: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
#
#"""
