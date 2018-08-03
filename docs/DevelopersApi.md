# cli.api.DevelopersApi

All URIs are relative to *https://localhost/apitax/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_script**](DevelopersApi.md#create_script) | **POST** /system/script | Create a new script
[**delete_script**](DevelopersApi.md#delete_script) | **DELETE** /system/script | Delete a script
[**display_developer_dashboard**](DevelopersApi.md#display_developer_dashboard) | **GET** /dashboard/developer | Displays the developer dashboard page
[**rename_script**](DevelopersApi.md#rename_script) | **PATCH** /system/script | Rename a script
[**save_script**](DevelopersApi.md#save_script) | **PUT** /system/script | Save a script


# **create_script**
> Response create_script(create=create)

Create a new script

Create a new script

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
api_instance = cli.api.DevelopersApi(cli.api.ApiClient(configuration))
create = cli.api.Create() # Create | The data needed to create this script (optional)

try:
    # Create a new script
    api_response = api_instance.create_script(create=create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->create_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create** | [**Create**](Create.md)| The data needed to create this script | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_script**
> Response delete_script(delete=delete)

Delete a script

Delete a script

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
api_instance = cli.api.DevelopersApi(cli.api.ApiClient(configuration))
delete = cli.api.Delete() # Delete | The data needed to delete this script (optional)

try:
    # Delete a script
    api_response = api_instance.delete_script(delete=delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->delete_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete** | [**Delete**](Delete.md)| The data needed to delete this script | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_developer_dashboard**
> display_developer_dashboard()

Displays the developer dashboard page

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
api_instance = cli.api.DevelopersApi(cli.api.ApiClient(configuration))

try:
    # Displays the developer dashboard page
    api_instance.display_developer_dashboard()
except ApiException as e:
    print("Exception when calling DevelopersApi->display_developer_dashboard: %s\n" % e)
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

# **rename_script**
> Response rename_script(rename=rename)

Rename a script

Rename a script

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
api_instance = cli.api.DevelopersApi(cli.api.ApiClient(configuration))
rename = cli.api.Rename() # Rename | The data needed to save this script (optional)

try:
    # Rename a script
    api_response = api_instance.rename_script(rename=rename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->rename_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rename** | [**Rename**](Rename.md)| The data needed to save this script | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_script**
> Response save_script(save=save)

Save a script

Save a script

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
api_instance = cli.api.DevelopersApi(cli.api.ApiClient(configuration))
save = cli.api.Save() # Save | The data needed to save this script (optional)

try:
    # Save a script
    api_response = api_instance.save_script(save=save)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->save_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save** | [**Save**](Save.md)| The data needed to save this script | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

