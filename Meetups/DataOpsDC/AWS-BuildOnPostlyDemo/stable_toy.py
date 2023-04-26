'''
'''

import requests
import json
import boto3

def main():
    # Set the AWS credentials explicitly
    aws_access_key_id = 'your_access_key_id'
    aws_secret_access_key = 'your_secret_access_key'

    # Create an AWS Lambda client with the credentials and region
    client = boto3.client('lambda', 
                          region_name='us-east-1',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)

    # Define the function name and data for the push request
    function_name = 'arn:aws:lambda:us-east-1:180754357734:function:fm_create_image'
    payload = {
        "body": "{\"text\":\"clouds over the ocean\"}"
    }

    # Invoke the function and get the response
    response = client.invoke(FunctionName=function_name, Payload=json.dumps(payload))

    # Extract the response body from the response
    response_body = response['Payload'].read().decode('utf-8')

    # Save the response body as a JPG file
    with open("response.jpg", "wb") as f:
        f.write(response_body.encode('utf-8'))

def url_version():
    # Define the URL and data for the push request
    url = "https://zkozgdvhtkkxktrmpdvsg4scdy0yqyeb.lambda-url.us-east-1.on.aws/"
    data = {
        "body": "{\"text\":\"clouds over the ocean\"}"
    }

    # Make the push request and get the response
    response = requests.get(url, data=json.dumps(data))

    # Save the response as a JPG file
    with open("response.jpg", "wb") as f:
        f.write(response.content)
    # TODO This just results in writing "Internal Server Error" to a file.

if __name__ == '__main__':
    main()