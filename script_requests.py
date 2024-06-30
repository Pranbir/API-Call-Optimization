import time
import requests

url= "http://localhost:8000/"

def my_function():
    requests.get(url)
    print("Received Response")
    return True

start_time = time.time()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
my_function()
end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

"""
Execution time: 20.07779598236084 seconds
"""