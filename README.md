# HTTPSpamBot
spam bot build in python to spam websites at high volume.

# Table of Contents

1. [Introduction](#Introduction)
2. [Prerequisites](#Prerequisites)
3. [Usage](#Usage)
4. [Configuration](#Configuration)



## Introduction
This is a simple Python script that sends concurrent HTTP requests to the Example Domain using the requests library and concurrent.futures module. The script sends a total of MAX_REQUESTS requests concurrently, each with a unique user agent. Current script sends HTTP GET requests only, feel free to edit for other request types.

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