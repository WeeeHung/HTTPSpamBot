# HTTPSpamBot
to spam websites at high volume.


## Sending concurrent requests to Example Domain
This is a simple Python script that sends concurrent HTTP requests to the Example Domain using the requests library and concurrent.futures module. The script sends a total of MAX_REQUESTS requests concurrently, each with a unique user agent.

## Prerequisites
- Python 3.x
- requests library
- concurrent.futures module

## Usage
1. Clone the repository or copy the script to your local machine. 
2. Install the requests library and concurrent.futures module by running pip install requests futures. 
3. Open a terminal and navigate to the directory containing the script. 
4. Run the script using python spam.py. 

## Configuration
The script uses the following configuration variable:

- MAX_REQUESTS: The maximum number of requests to send concurrently.