# test_username_generator.py
import requests
import json

def test_username_generator():
    print("Testing Username Generator Microservice")
    print("======================================")
    
    base_url = "http://localhost:5000"
    
    # Test 1: Health check
    print("\nTest 1: Health Check")
    health_response = requests.get(f"{base_url}/health")
    print(f"Response Status: {health_response.status_code}")
    print(f"Response Body: {health_response.json()}")
    
    # Test 2: Generate username with full information
    print("\nTest 2: Generate Username with Full Information")
    full_data = {
        "first_name": "John",
        "last_name": "Smith",
        "favorite_genre": "rock"
    }
    full_response = requests.post(
        f"{base_url}/generate", 
        headers={"Content-Type": "application/json"},
        data=json.dumps(full_data)
    )
    print(f"Request: {full_data}")
    print(f"Response Status: {full_response.status_code}")
    print(f"Response Body: {full_response.json()}")
    
    # Test 3: Generate username with partial information
    print("\nTest 3: Generate Username with Partial Information")
    partial_data = {
        "first_name": "Alice"
    }
    partial_response = requests.post(
        f"{base_url}/generate", 
        headers={"Content-Type": "application/json"},
        data=json.dumps(partial_data)
    )
    print(f"Request: {partial_data}")
    print(f"Response Status: {partial_response.status_code}")
    print(f"Response Body: {partial_response.json()}")
    
    # Test 4: Generate username with no information
    print("\nTest 4: Generate Username with No Information")
    empty_data = {}
    empty_response = requests.post(
        f"{base_url}/generate", 
        headers={"Content-Type": "application/json"},
        data=json.dumps(empty_data)
    )
    print(f"Request: {empty_data}")
    print(f"Response Status: {empty_response.status_code}")
    print(f"Response Body: {empty_response.json()}")

if __name__ == "__main__":
    test_username_generator()