import requests
import concurrent.futures

# experiment with max no of terminals and send all concurrently (10000*10)
MAX_REQUESTS = 10000

print(f"Sending {MAX_REQUESTS} requests concurrently...")

def send_request(num):
    # Set a different user agent for each request
    user_agent = f"CustomUserAgent-{num}"
    headers = {'User-Agent': user_agent}

    # Send a GET request to a URL using requests library
    url = "https://example.com"
    response = requests.get(url, headers=headers)

    # Get the response status code
    status_code = response.status_code

    # Print the user agent and status code
    print(f"User agent: {user_agent}, Status code: {status_code}")

# Create a ThreadPoolExecutor with 10 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(send_request, num) for num in range(MAX_REQUESTS)]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)

    