# cli.api.AdminsApi

All URIs are relative to *https://localhost/apitax/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**display_admin_dashboard**](AdminsApi.md#display_admin_dashboard) | **GET** /dashboard/admin | Displays the developer admin page
[**driver_status**](AdminsApi.md#driver_status) | **GET** /system/driver/{name}/status | Retrieve the status of a loaded driver
[**system_status**](AdminsApi.md#system_status) | **GET** /system/status | Retrieve the system status


# **display_admin_dashboard**
> display_admin_dashboard()

Displays the developer admin page

Displays the user admin page

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
api_instance = cli.api.AdminsApi(cli.api.ApiClient(configuration))

try:
    # Displays the developer admin page
    api_instance.display_admin_dashboard()
except ApiException as e:
    print("Exception when calling AdminsApi->display_admin_dashboard: %s\n" % e)
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

# **driver_status**
> Response driver_status(name)

Retrieve the status of a loaded driver

Retrieve the status of a loaded driver

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
api_instance = cli.api.AdminsApi(cli.api.ApiClient(configuration))
name = 'name_example' # str | Get status of a driver with this name

try:
    # Retrieve the status of a loaded driver
    api_response = api_instance.driver_status(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsApi->driver_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Get status of a driver with this name | 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_status**
> Response system_status()

Retrieve the system status

Retrieve the system status

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
api_instance = cli.api.AdminsApi(cli.api.ApiClient(configuration))

try:
    # Retrieve the system status
    api_response = api_instance.system_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsApi->system_status: %s\n" % e)
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

