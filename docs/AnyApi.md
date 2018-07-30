# cli.api.AnyApi

All URIs are relative to *https://localhost/apitax/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AnyApi.md#authenticate) | **POST** /auth | Authenticate
[**display_login**](AnyApi.md#display_login) | **GET** /login | Displays the login page
[**get_asset**](AnyApi.md#get_asset) | **GET** /assets/{name} | Displays the user dashboard page
[**refresh_token**](AnyApi.md#refresh_token) | **POST** /token/refresh | Refreshes login token using refresh token


# **authenticate**
> AuthResponse authenticate(user=user)

Authenticate

Authenticate with the API

### Example
```python
from __future__ import print_function
import time
import cli.api
from cli.api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cli.api.AnyApi()
user = cli.api.UserAuth() # UserAuth | The user authentication object. (optional)

try:
    # Authenticate
    api_response = api_instance.authenticate(user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnyApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserAuth**](UserAuth.md)| The user authentication object. | [optional] 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_login**
> display_login()

Displays the login page

Displays the login page

### Example
```python
from __future__ import print_function
import time
import cli.api
from cli.api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cli.api.AnyApi()

try:
    # Displays the login page
    api_instance.display_login()
except ApiException as e:
    print("Exception when calling AnyApi->display_login: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> get_asset(name)

Displays the user dashboard page

Displays the user dashboard page

### Example
```python
from __future__ import print_function
import time
import cli.api
from cli.api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cli.api.AnyApi()
name = 'name_example' # str | Get an asset such as a JavaScript file

try:
    # Displays the user dashboard page
    api_instance.get_asset(name)
except ApiException as e:
    print("Exception when calling AnyApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Get an asset such as a JavaScript file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> UserAuth refresh_token()

Refreshes login token using refresh token

Refreshes login token using refresh token

### Example
```python
from __future__ import print_function
import time
import cli.api
from cli.api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = cli.api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cli.api.AnyApi(cli.api.ApiClient(configuration))

try:
    # Refreshes login token using refresh token
    api_response = api_instance.refresh_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnyApi->refresh_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAuth**](UserAuth.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

