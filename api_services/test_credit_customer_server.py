import requests
import concurrent.futures
import time

# Endpoint URL and headers
#url = "https://stagingapi.finecore.co/v1/wallets/credit"
url = "http://localhost:8080/v1/wallets/credit"

headers = {
    "X-API-Key": "fsk_5b0c0b7d6359fc06b70ae27d4f8468d210b9ed8a2c0105dcd7a587c90f779d8f_438241922", #"flk_6f1025328641a6b2b3b309cee58a27aa_1784140885",
    "Content-Type": "application/json"
}

# Array of customer IDs
customer_ids =[
    "b196f725-a4f2-4d5f-93b5-8d6a9014e25d",
    "bd5f0399-d06a-42f6-82e1-a799cf13753a",
    "769f3502-d25d-44f4-8d8f-0e09a38465ba"

]

manual_ids=[
    "b196f725-a4f2-4d5f-93b5-8d6a9014e25d",
    "24ac422b-0686-4f64-9d9d-fe611c915066",
    "432c0d5c-1500-4d81-9cb3-ecb25c8d8cc4",
    "df902c6f-a989-4c95-880e-6ec66b171cf7",
    "7a7c30e8-1ecc-4dd3-be1f-ee80a9dd475c",
    "5a0e0b7b-5aea-4025-889a-eff3af43fe15",
    "5a923675-1ef1-4088-ad6e-5795ec3c8259",
    "6ff35d9e-4ad6-49cf-b21a-04f7b74ce0bd",
    "b155a179-a251-4166-ac9e-10654322b9c2",
    "da98471b-6a10-4927-94ce-3b4df6941d8f",
    "b49f7e33-67fb-4a63-a82f-7d626f1195c3",
    "b2d248ff-04d2-4249-878e-004b1d8263f5",
    "0cdb8e41-8bcf-4ad1-850c-f1f41d520583",
    "fc3b1570-d3f2-469c-9354-44d928af7c72",
    "4e7076e6-9aa1-4a73-a4d1-d72fc159e7f4",
    "cf56178d-4219-41ee-b4eb-218ce474b9bd",

    "b196f725-a4f2-4d5f-93b5-8d6a9014e25d",
    "24ac422b-0686-4f64-9d9d-fe611c915066",
    "432c0d5c-1500-4d81-9cb3-ecb25c8d8cc4",
    "df902c6f-a989-4c95-880e-6ec66b171cf7",
    "7a7c30e8-1ecc-4dd3-be1f-ee80a9dd475c",
    "5a0e0b7b-5aea-4025-889a-eff3af43fe15",
    "5a923675-1ef1-4088-ad6e-5795ec3c8259",
    "6ff35d9e-4ad6-49cf-b21a-04f7b74ce0bd",
    "b155a179-a251-4166-ac9e-10654322b9c2",
    "da98471b-6a10-4927-94ce-3b4df6941d8f",
    "b49f7e33-67fb-4a63-a82f-7d626f1195c3",
    "b2d248ff-04d2-4249-878e-004b1d8263f5",
    "0cdb8e41-8bcf-4ad1-850c-f1f41d520583",
    "fc3b1570-d3f2-469c-9354-44d928af7c72",
    "4e7076e6-9aa1-4a73-a4d1-d72fc159e7f4",
    "cf56178d-4219-41ee-b4eb-218ce474b9bd"

]

customer_ids_gemini=[
  "24ac422b-0686-4f64-9d9d-fe611c915066",
  "b196f725-a4f2-4d5f-93b5-8d6a9014e25d",
  "432c0d5c-1500-4d81-9cb3-ecb25c8d8cc4",
  "df902c6f-a989-4c95-880e-6ec66b171cf7",
  "7a7c30e8-1ecc-4dd3-be1f-ee80a9dd475c",
  "5a0e0b7b-5aea-4025-889a-eff3af43fe15",
  "5a923675-1ef1-4088-ad6e-5795ec3c8259",
  "6ff35d9e-4ad6-49cf-b21a-04f7b74ce0bd",
  "b155a179-a251-4166-ac9e-10654322b9c2",
  "da98471b-6a10-4927-94ce-3b4df6941d8f",
  "b49f7e33-67fb-4a63-a82f-7d626f1195c3",
  "b2d248ff-04d2-4249-878e-004b1d8263f5",
  "0cdb8e41-8bcf-4ad1-850c-f1f41d520583",
  "fc3b1570-d3f2-469c-9354-44d928af7c72",
  "4e7076e6-9aa1-4a73-a4d1-d72fc159e7f4",
  "cf56178d-4219-41ee-b4eb-218ce474b9bd",
  "7f44ad80-205b-46df-a7e3-70bda0884546",
  "f6703013-0a73-4046-a722-ecf6c3a67663",
  "c7804f67-1988-4975-8cc0-fa0738500478",
  "4d12f338-401d-4be4-8596-f9736c96d07e"
]

new_ids=[
    "34231443-3895-4604-b6f4-a70ed87b302e",
    "d80fdb1d-3df1-4213-8633-ec8949d2192d",
    "46d9d71d-40a2-4228-a300-7cb9c02b7cf0",
    "4a8fc71b-c999-4d14-b272-19cc5db27937",
    "6717ba2d-d4c2-4b60-8a32-0d53da089bb9",
    "6d21af05-592a-41ab-96b2-1283783eaef9",

    "34231443-3895-4604-b6f4-a70ed87b302e",
    "d80fdb1d-3df1-4213-8633-ec8949d2192d",
    "46d9d71d-40a2-4228-a300-7cb9c02b7cf0",
    "4a8fc71b-c999-4d14-b272-19cc5db27937",
    "6717ba2d-d4c2-4b60-8a32-0d53da089bb9",
    "6d21af05-592a-41ab-96b2-1283783eaef9",

    "34231443-3895-4604-b6f4-a70ed87b302e",
    "d80fdb1d-3df1-4213-8633-ec8949d2192d",
    "46d9d71d-40a2-4228-a300-7cb9c02b7cf0",
    "4a8fc71b-c999-4d14-b272-19cc5db27937",
    "6717ba2d-d4c2-4b60-8a32-0d53da089bb9",
    "6d21af05-592a-41ab-96b2-1283783eaef9",

    "34231443-3895-4604-b6f4-a70ed87b302e",
    "d80fdb1d-3df1-4213-8633-ec8949d2192d",
    "46d9d71d-40a2-4228-a300-7cb9c02b7cf0",
    "4a8fc71b-c999-4d14-b272-19cc5db27937",
    "6717ba2d-d4c2-4b60-8a32-0d53da089bb9",
    "6d21af05-592a-41ab-96b2-1283783eaef9",
]

print(len(new_ids))
print(new_ids)

# Function to send POST request and print response
def send_request(customer_id):
    print("customer_id:     ", customer_id)
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
    count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(send_request, customer_id) for customer_id in customer_ids]
        for future in concurrent.futures.as_completed(futures):
            count += 1
            print(f"Request {count} completed")
            try:
                future.result()
            except Exception as e:
                print(f"Request generated an exception: {e}")

# Parameters for load test
concurrent_requests = 1  # Number of concurrent requests

# Perform load test
start_time = time.time()
load_test(new_ids, concurrent_requests)
end_time = time.time()

print(f"Load test completed in {end_time - start_time:.2f} seconds")



 #test
 #first run on server worked fine but after doing a local test
 #issue is a t the DB level but not necessarily caused by the DB
 #could also be providus
 #after doing local test which ran indefinitely, the server test ended up having issues with performance
 #changes to test if providus
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
#Status Code: 400
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Request generated an exception: Extra data: line 2 column 1 (char 95)
#Request generated an exception: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
#Request generated an exception: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
#"""
## after local test
#"""
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#
#"""
#
#
#
##first server test
#"""
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Load test completed in 5.64 seconds
#(venv) PS C:\Users\User\Documents\GitHub\finecore-testing> python test_credit_customer.py
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Status Code: 400
#Response Body: {'statusCode': 400, 'status': 'error', 'error': {'message': 'insufficient merchant wallet balance'}}
#Load test completed in 2.49 seconds
#"""

