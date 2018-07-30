from __future__ import print_function
import time
import cli.api
from cli.api.rest import ApiException
from pprint import pprint
from cli.api.models.command import Command
from cli.api.models.response import Response
import json
import ast

url = "http://127.0.0.1:5085/apitax/2"


def authenticate(username, password):
    # create an instance of the API class

    api_instance = cli.api.AnyApi()
    api_instance.api_client.configuration.host = url
    # api_instance.api_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
    # print(cli.api.configuration.host)

    user = cli.api.UserAuth(username=username,
                            password=password)  # UserAuth | The user authentication object. (optional)

    try:
        # Authenticate
        return api_instance.authenticate(user=user)
    except ApiException as e:
        print("Exception when calling AnyApi->authenticate: %s\n" % e)


def doScript(user_auth, script):
    # create an instance of the API class
    api_instance = cli.api.UsersApi()

    api_instance = setup_api_config(api_instance, user_auth)

    execute = cli.api.Execute(auth=user_auth.auth, command=Command(command='script ' + script, parameters={},
                                                                   options={'debug': True,
                                                                            'sensitive': False}))  # Execute | The data needed to execute this command (optional)

    try:
        # Execute a Command
        return api_instance.command(execute=execute)
    except ApiException as e:
        print("Exception when calling UsersApi->command: %s\n" % e)


def setup_api_config(api_instance, user_auth):
    api_instance.api_client.configuration.host = url
    # Configure API key authorization: Bearer
    api_instance.api_client.configuration.api_key['Authorization'] = user_auth.access_token
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    api_instance.api_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
    return api_instance


def log_printer(response: Response):
    for line in ast.literal_eval(response.log):
        content = line['line']
        #if(content.strip() != ""):
        print(content)
