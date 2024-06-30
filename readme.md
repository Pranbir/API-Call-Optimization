# FastAPI App

This is a FastAPI app and the scripts demonstrates concurrency using `asyncio.gather`. The app has a single API endpoint that takes 2 seconds to respond and returns a sample JSON output. The business logic is implemented as an async function, and it doesn't matter how many tabs in the browser call the API, each tab will receive the response at the same time.

## Installation

To install the required dependencies, run the following command:

`pip install -r requirements.txt`


## Usage

To run the FastAPI app, execute the following command:

`python main.py`


You can then access the API at http://localhost:8000/.


To run the scripts, execute any of the following commands:

`python script_requests.py`
OR

`python script_aiohttp.py`
OR

`python script_aiohttp_optimized.py`

## API Endpoint

The app has a single API endpoint at `/`. When you access this endpoint, it will take 2 seconds to respond and return a JSON object with the message `{"PING":"PONG!"}`.

## Concurrent Requests

Instead of using a browser it is suggested to use non-browser clients such as curl or Postman.

## Scripts Description

`script_requests.py` -> Sync implementation using requests library that shows it takes 20.07 seconds to complete 10 API calls

`script_aiohttp.py` -> Used aiohttp library for the API calls but used `await` keyword means it is a blocking call, which is not benificial enough since it is blocking the event loop. Hence it takes 20.06 seconds to complete 10 API calls

`script_aiohttp_optimized.py` -> Completely non-blocking method, used asyncio's gather method to run all async tasks concurrently where each tasks takes 2 seconds to complete. But in total it takes 2.01 seconds to complete 10 API calls. But remember this method is only benificial when the non-blocking calls are non dependent on each other.