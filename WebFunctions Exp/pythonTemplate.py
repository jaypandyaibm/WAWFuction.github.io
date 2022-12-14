#
# main() will be run when you invoke this action
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
# @return The output of this action, which must be a JSON object.
#
import sys
import json
import requests

def local_function(name):
    # This function is a local function that let you know that the code is working in of itself.
    print(f"Function Name: ", "local_function()")
    print(f"Hi, {name}")
    return({"name": name})

def get_json_value(name):
    # This function fetchs a single row of data and shows how to dereference a single json field
    print(f"Function Name: ", "get_jason_value()")
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url).json()
    title = response["title"]
    print(f"Title: {title}")
    return({"title": title})

def get_sample_json():
    # This function fetchs a single row of data and displays the entire contents of the row
    print(f"Function Name: ", "get_sample_json()")
    headers = {"Content-Type": "text", "apiKey": "APIKEY"}
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    print("Sample Data: ", response.json())
    return(response.json())

def get_project_count():
    # This function illustrates use of the 'len' function to determine the number of rows in a list
    print(f"Function Name: ", "get_project_count()")
    headers = {"Content-Type": "text", "apiKey": "APIKEY"}
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url, headers=headers)
    responseJSON = response.json()
    print("Project Count: ", len(responseJSON))
    return({"record_count": len(responseJSON)})

def get_html_link_list():
    # This function illustrates the building of links from data in a result set
    print(f"Function Name: ", "get_html_link_list()")
    link = ""
    headers = {"Content-Type": "text", "apiKey": "APIKEY"}
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url, headers=headers)
    responseJSON = response.json()

    for i in responseJSON:
        userId = str(i["userId"])
        link = link + "<a target='_blank' href=https://jsonplaceholder.typicode.com/todos/"+ userId +">"+userId+"</a>\n"
    #print("Link: ", link) # <-- See entire list
    return({"link_list": link})

def main(dict):
    if 'function_name' in dict:
        function_name = dict['function_name']
    else:
        function_name = "None"
    if 'name' in dict:
        name = dict['name']
    else:
        name = "Sonya"

    if function_name == "local_function":
        api_return = local_function(name)
    if function_name == "get_json_value":
        api_return = get_json_value(name)
    if function_name == "get_sample_json":
        api_return = get_sample_json()
    if function_name == "get_project_count":
        api_return = get_project_count()
    if function_name == "get_html_link_list":
        api_return = get_html_link_list()
    if function_name == "None":
        api_return = "Function requested is not recognized."

    return {"extract":api_return}
