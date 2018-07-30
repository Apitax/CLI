# cli.api.UsersApi

All URIs are relative to *https://localhost/apitax/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**command**](UsersApi.md#command) | **POST** /command | Execute a Command
[**display_dashboard**](UsersApi.md#display_dashboard) | **GET** /dashboard | Displays the user dashboard page
[**endpoint_catalog**](UsersApi.md#endpoint_catalog) | **GET** /system/endpoint/catalog | Retrieve the endpoint catalog
[**get_script**](UsersApi.md#get_script) | **GET** /system/script | Retrieve the contents of a script
[**script_catalog**](UsersApi.md#script_catalog) | **GET** /system/script/catalog | Retrieve the script catalog


# **command**
> Response command(execute=execute)

Execute a Command

Execute a command

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
api_instance = cli.api.UsersApi(cli.api.ApiClient(configuration))
execute = cli.api.Execute() # Execute | The data needed to execute this command (optional)

try:
    # Execute a Command
    api_response = api_instance.command(execute=execute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute** | [**Execute**](Execute.md)| The data needed to execute this command | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_dashboard**
> display_dashboard()

Displays the user dashboard page

Displays the user dashboard page

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
api_instance = cli.api.UsersApi(cli.api.ApiClient(configuration))

try:
    # Displays the user dashboard page
    api_instance.display_dashboard()
except ApiException as e:
    print("Exception when calling UsersApi->display_dashboard: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_catalog**
> Response endpoint_catalog(catalog=catalog)

Retrieve the endpoint catalog

Retrieve the endpoint catalog

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
api_instance = cli.api.UsersApi(cli.api.ApiClient(configuration))
catalog = cli.api.UserAuth() # UserAuth | The data needed to get a catalog (optional)

try:
    # Retrieve the endpoint catalog
    api_response = api_instance.endpoint_catalog(catalog=catalog)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->endpoint_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | [**UserAuth**](UserAuth.md)| The data needed to get a catalog | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_script**
> Response get_script(name=name)

Retrieve the contents of a script

Retrieve the contents of a script

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
api_instance = cli.api.UsersApi(cli.api.ApiClient(configuration))
name = 'name_example' # str | The script name. (optional)

try:
    # Retrieve the contents of a script
    api_response = api_instance.get_script(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The script name. | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_catalog**
> Response script_catalog()

Retrieve the script catalog

Retrieve the script catalog

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
api_instance = cli.api.UsersApi(cli.api.ApiClient(configuration))

try:
    # Retrieve the script catalog
    api_response = api_instance.script_catalog()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->script_catalog: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

