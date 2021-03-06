# cli.api
The API for the frontend of Apitax

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import cli.api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cli.api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cli.api
from cli.api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
cli.api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# cli.api.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = cli.api.AdminsApi()

try:
    # Displays the developer admin page
    api_instance.display_admin_dashboard()
except ApiException as e:
    print("Exception when calling AdminsApi->display_admin_dashboard: %s\n" % e)

```


## Documentation for API Endpoints

All URIs are relative to *https://localhost/apitax/2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminsApi* | [**display_admin_dashboard**](docs/AdminsApi.md#display_admin_dashboard) | **GET** /dashboard/admin | Displays the developer admin page
*AdminsApi* | [**driver_status**](docs/AdminsApi.md#driver_status) | **GET** /system/driver/{name}/status | Retrieve the status of a loaded driver
*AdminsApi* | [**system_status**](docs/AdminsApi.md#system_status) | **GET** /system/status | Retrieve the system status
*AnyApi* | [**authenticate**](docs/AnyApi.md#authenticate) | **POST** /auth | Authenticate
*AnyApi* | [**display_login**](docs/AnyApi.md#display_login) | **GET** /login | Displays the login page
*AnyApi* | [**get_asset**](docs/AnyApi.md#get_asset) | **GET** /assets/{name} | Displays the user dashboard page
*AnyApi* | [**refresh_token**](docs/AnyApi.md#refresh_token) | **POST** /token/refresh | Refreshes login token using refresh token
*DevelopersApi* | [**create_script**](docs/DevelopersApi.md#create_script) | **POST** /system/script | Create a new script
*DevelopersApi* | [**delete_script**](docs/DevelopersApi.md#delete_script) | **DELETE** /system/script | Delete a script
*DevelopersApi* | [**display_developer_dashboard**](docs/DevelopersApi.md#display_developer_dashboard) | **GET** /dashboard/developer | Displays the developer dashboard page
*DevelopersApi* | [**rename_script**](docs/DevelopersApi.md#rename_script) | **PATCH** /system/script | Rename a script
*DevelopersApi* | [**save_script**](docs/DevelopersApi.md#save_script) | **PUT** /system/script | Save a script
*UsersApi* | [**command**](docs/UsersApi.md#command) | **POST** /command | Execute a Command
*UsersApi* | [**display_dashboard**](docs/UsersApi.md#display_dashboard) | **GET** /dashboard | Displays the user dashboard page
*UsersApi* | [**endpoint_catalog**](docs/UsersApi.md#endpoint_catalog) | **GET** /system/endpoint/catalog | Retrieve the endpoint catalog
*UsersApi* | [**get_script**](docs/UsersApi.md#get_script) | **GET** /system/script | Retrieve the contents of a script
*UsersApi* | [**script_catalog**](docs/UsersApi.md#script_catalog) | **GET** /system/script/catalog | Retrieve the script catalog


## Documentation For Models

 - [AuthResponse](docs/AuthResponse.md)
 - [Command](docs/Command.md)
 - [Create](docs/Create.md)
 - [Delete](docs/Delete.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Execute](docs/Execute.md)
 - [Rename](docs/Rename.md)
 - [Response](docs/Response.md)
 - [Save](docs/Save.md)
 - [Script](docs/Script.md)
 - [UserAuth](docs/UserAuth.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

shawn.clake@nopatience.net

