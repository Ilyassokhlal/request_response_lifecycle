import requests
import json


def anatomy_func(response):
    print(f"=== {response.request.method} Anatomy ===")
    print(f"1.Method: {response.request.method}")
    print(f"  URL:    {response.request.url}")

    print("\n2.Request Headers:")
    for key, value in response.request.headers.items():
        print(f"   {key}: {value}")
    if response.request.body:
        print(f"\n3.Request Body: {response.request.body.decode('utf-8')}")

    print(f"\n4.Status: {response.status_code} {response.reason}")

    print("\n5.Response Headers:")
    print(f"Content-Type: {response.headers.get('Content-Type')}") 
    print(f"Content-Length: {response.headers.get('Content-Length')}")

    print("\n6.Response Body:")
    print(json.dumps(response.json(), indent=3))

    print(f"\n7.Total time elapsed: {response.elapsed.total_seconds()*1000:.3f} milliseconds")

# GET
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print("="*60)
anatomy_func(response=response)

# POST
new_post = {
    "title": "New Post Title",
    "body": "New Post Body...",
    "userId": 100
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post, headers={"X-Custom-Header": "For Testing Purposes"})

print("="*60)
anatomy_func(response=response)

# PATCH
new_title = {
    "title": "New Post Updated title"
}
response = requests.patch("https://jsonplaceholder.typicode.com/posts/101", json=new_title)

print("="*60)
anatomy_func(response=response)