# linnworks_api.generated.rulesengine.RulesEngineApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_action**](RulesEngineApi.md#add_action) | **POST** /api/RulesEngine/AddAction | AddAction
[**check_condition_name_exists**](RulesEngineApi.md#check_condition_name_exists) | **GET** /api/RulesEngine/CheckConditionNameExists | CheckConditionNameExists
[**copy_action**](RulesEngineApi.md#copy_action) | **POST** /api/RulesEngine/CopyAction | CopyAction
[**copy_condition**](RulesEngineApi.md#copy_condition) | **POST** /api/RulesEngine/CopyCondition | CopyCondition
[**create_draft_from_existing**](RulesEngineApi.md#create_draft_from_existing) | **POST** /api/RulesEngine/CreateDraftFromExisting | CreateDraftFromExisting
[**create_new_condition**](RulesEngineApi.md#create_new_condition) | **POST** /api/RulesEngine/CreateNewCondition | CreateNewCondition
[**create_new_draft**](RulesEngineApi.md#create_new_draft) | **POST** /api/RulesEngine/CreateNewDraft | CreateNewDraft
[**create_new_draft_from_existing**](RulesEngineApi.md#create_new_draft_from_existing) | **POST** /api/RulesEngine/CreateNewDraftFromExisting | CreateNewDraftFromExisting
[**delete_action**](RulesEngineApi.md#delete_action) | **POST** /api/RulesEngine/DeleteAction | DeleteAction
[**delete_condition**](RulesEngineApi.md#delete_condition) | **POST** /api/RulesEngine/DeleteCondition | DeleteCondition
[**delete_rule_by_id**](RulesEngineApi.md#delete_rule_by_id) | **POST** /api/RulesEngine/DeleteRuleById | DeleteRuleById
[**get_action_options**](RulesEngineApi.md#get_action_options) | **GET** /api/RulesEngine/GetActionOptions | GetActionOptions
[**get_action_types**](RulesEngineApi.md#get_action_types) | **GET** /api/RulesEngine/GetActionTypes | GetActionTypes
[**get_condition_web**](RulesEngineApi.md#get_condition_web) | **GET** /api/RulesEngine/GetConditionWeb | GetConditionWeb
[**get_evaluation_fields**](RulesEngineApi.md#get_evaluation_fields) | **GET** /api/RulesEngine/GetEvaluationFields | GetEvaluationFields
[**get_evaluator_types**](RulesEngineApi.md#get_evaluator_types) | **GET** /api/RulesEngine/GetEvaluatorTypes | GetEvaluatorTypes
[**get_key_options**](RulesEngineApi.md#get_key_options) | **GET** /api/RulesEngine/GetKeyOptions | GetKeyOptions
[**get_multi_key_options**](RulesEngineApi.md#get_multi_key_options) | **POST** /api/RulesEngine/GetMultiKeyOptions | GetMultiKeyOptions
[**get_multi_options**](RulesEngineApi.md#get_multi_options) | **POST** /api/RulesEngine/GetMultiOptions | GetMultiOptions
[**get_options**](RulesEngineApi.md#get_options) | **GET** /api/RulesEngine/GetOptions | GetOptions
[**get_required_fields_by_rule_id**](RulesEngineApi.md#get_required_fields_by_rule_id) | **GET** /api/RulesEngine/GetRequiredFieldsByRuleId | GetRequiredFieldsByRuleId
[**get_required_fields_by_type**](RulesEngineApi.md#get_required_fields_by_type) | **GET** /api/RulesEngine/GetRequiredFieldsByType | GetRequiredFieldsByType
[**get_rule_condition_nodes**](RulesEngineApi.md#get_rule_condition_nodes) | **GET** /api/RulesEngine/GetRuleConditionNodes | GetRuleConditionNodes
[**get_rules**](RulesEngineApi.md#get_rules) | **GET** /api/RulesEngine/GetRules | GetRules
[**get_rules_by_type**](RulesEngineApi.md#get_rules_by_type) | **GET** /api/RulesEngine/GetRulesByType | GetRulesByType
[**save_condition_changes**](RulesEngineApi.md#save_condition_changes) | **POST** /api/RulesEngine/SaveConditionChanges | SaveConditionChanges
[**set_condition_enabled**](RulesEngineApi.md#set_condition_enabled) | **POST** /api/RulesEngine/SetConditionEnabled | SetConditionEnabled
[**set_draft_live**](RulesEngineApi.md#set_draft_live) | **POST** /api/RulesEngine/SetDraftLive | SetDraftLive
[**set_rule_enabled**](RulesEngineApi.md#set_rule_enabled) | **POST** /api/RulesEngine/SetRuleEnabled | SetRuleEnabled
[**set_rule_name**](RulesEngineApi.md#set_rule_name) | **POST** /api/RulesEngine/SetRuleName | SetRuleName
[**swap_conditions**](RulesEngineApi.md#swap_conditions) | **POST** /api/RulesEngine/SwapConditions | SwapConditions
[**swap_rules**](RulesEngineApi.md#swap_rules) | **POST** /api/RulesEngine/SwapRules | SwapRules
[**test_evaluate_rule**](RulesEngineApi.md#test_evaluate_rule) | **POST** /api/RulesEngine/TestEvaluateRule | TestEvaluateRule
[**update_action**](RulesEngineApi.md#update_action) | **POST** /api/RulesEngine/UpdateAction | UpdateAction


# **add_action**
> ActionWeb add_action(rules_engine_add_action_request)

AddAction

Use this call to add a new action to a condition node. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.action_web import ActionWeb
from linnworks_api.generated.rulesengine.models.rules_engine_add_action_request import RulesEngineAddActionRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_add_action_request = linnworks_api.generated.rulesengine.RulesEngineAddActionRequest() # RulesEngineAddActionRequest | 

    try:
        # AddAction
        api_response = api_instance.add_action(rules_engine_add_action_request)
        print("The response of RulesEngineApi->add_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->add_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_add_action_request** | [**RulesEngineAddActionRequest**](RulesEngineAddActionRequest.md)|  | 

### Return type

[**ActionWeb**](ActionWeb.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_condition_name_exists**
> bool check_condition_name_exists(fk_rule_id=fk_rule_id, fk_condition_id=fk_condition_id, exclude_condition_id=exclude_condition_id, condition_name=condition_name)

CheckConditionNameExists

Use this call to check to see if a condition name already exists at a specific level. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    fk_rule_id = 56 # int | The rule id. (optional)
    fk_condition_id = 56 # int | Must be specified if checking that a condition name exists under a sub-condition. If checking rule-level conditions, do not specify. (optional)
    exclude_condition_id = 56 # int | If the check is for renaming a condition, specify the condition id here to exclude it from the results. (optional)
    condition_name = 'condition_name_example' # str | The name to check. (optional)

    try:
        # CheckConditionNameExists
        api_response = api_instance.check_condition_name_exists(fk_rule_id=fk_rule_id, fk_condition_id=fk_condition_id, exclude_condition_id=exclude_condition_id, condition_name=condition_name)
        print("The response of RulesEngineApi->check_condition_name_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->check_condition_name_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fk_rule_id** | **int**| The rule id. | [optional] 
 **fk_condition_id** | **int**| Must be specified if checking that a condition name exists under a sub-condition. If checking rule-level conditions, do not specify. | [optional] 
 **exclude_condition_id** | **int**| If the check is for renaming a condition, specify the condition id here to exclude it from the results. | [optional] 
 **condition_name** | **str**| The name to check. | [optional] 

### Return type

**bool**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_action**
> RuleAction copy_action(rules_engine_copy_action_request)

CopyAction

Use this call to copy an action from one condition to another condition. Actions may not be attached to the rule header or condition nodes with subconditions. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_action import RuleAction
from linnworks_api.generated.rulesengine.models.rules_engine_copy_action_request import RulesEngineCopyActionRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_copy_action_request = linnworks_api.generated.rulesengine.RulesEngineCopyActionRequest() # RulesEngineCopyActionRequest | 

    try:
        # CopyAction
        api_response = api_instance.copy_action(rules_engine_copy_action_request)
        print("The response of RulesEngineApi->copy_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->copy_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_copy_action_request** | [**RulesEngineCopyActionRequest**](RulesEngineCopyActionRequest.md)|  | 

### Return type

[**RuleAction**](RuleAction.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_condition**
> RuleConditionHeader copy_condition(rules_engine_copy_condition_request)

CopyCondition

Use this call to copy a condition, its subconditions and actions. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_condition_header import RuleConditionHeader
from linnworks_api.generated.rulesengine.models.rules_engine_copy_condition_request import RulesEngineCopyConditionRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_copy_condition_request = linnworks_api.generated.rulesengine.RulesEngineCopyConditionRequest() # RulesEngineCopyConditionRequest | 

    try:
        # CopyCondition
        api_response = api_instance.copy_condition(rules_engine_copy_condition_request)
        print("The response of RulesEngineApi->copy_condition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->copy_condition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_copy_condition_request** | [**RulesEngineCopyConditionRequest**](RulesEngineCopyConditionRequest.md)|  | 

### Return type

[**RuleConditionHeader**](RuleConditionHeader.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_draft_from_existing**
> int create_draft_from_existing(rules_engine_create_draft_from_existing_request)

CreateDraftFromExisting

Use this call to create a draft copy in order to edit an existing rule. Once set live, this draft will replace the rule it was copied from. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_create_draft_from_existing_request import RulesEngineCreateDraftFromExistingRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_create_draft_from_existing_request = linnworks_api.generated.rulesengine.RulesEngineCreateDraftFromExistingRequest() # RulesEngineCreateDraftFromExistingRequest | 

    try:
        # CreateDraftFromExisting
        api_response = api_instance.create_draft_from_existing(rules_engine_create_draft_from_existing_request)
        print("The response of RulesEngineApi->create_draft_from_existing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->create_draft_from_existing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_create_draft_from_existing_request** | [**RulesEngineCreateDraftFromExistingRequest**](RulesEngineCreateDraftFromExistingRequest.md)|  | 

### Return type

**int**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_condition**
> RuleConditionHeader create_new_condition(rules_engine_create_new_condition_request)

CreateNewCondition

Use this call to create a new condition. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_condition_header import RuleConditionHeader
from linnworks_api.generated.rulesengine.models.rules_engine_create_new_condition_request import RulesEngineCreateNewConditionRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_create_new_condition_request = linnworks_api.generated.rulesengine.RulesEngineCreateNewConditionRequest() # RulesEngineCreateNewConditionRequest | 

    try:
        # CreateNewCondition
        api_response = api_instance.create_new_condition(rules_engine_create_new_condition_request)
        print("The response of RulesEngineApi->create_new_condition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->create_new_condition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_create_new_condition_request** | [**RulesEngineCreateNewConditionRequest**](RulesEngineCreateNewConditionRequest.md)|  | 

### Return type

[**RuleConditionHeader**](RuleConditionHeader.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_draft**
> RuleHeaderBasic create_new_draft(rules_engine_create_new_draft_request)

CreateNewDraft

Use this call to create a new draft rule of a specified type. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_header_basic import RuleHeaderBasic
from linnworks_api.generated.rulesengine.models.rules_engine_create_new_draft_request import RulesEngineCreateNewDraftRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_create_new_draft_request = linnworks_api.generated.rulesengine.RulesEngineCreateNewDraftRequest() # RulesEngineCreateNewDraftRequest | 

    try:
        # CreateNewDraft
        api_response = api_instance.create_new_draft(rules_engine_create_new_draft_request)
        print("The response of RulesEngineApi->create_new_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->create_new_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_create_new_draft_request** | [**RulesEngineCreateNewDraftRequest**](RulesEngineCreateNewDraftRequest.md)|  | 

### Return type

[**RuleHeaderBasic**](RuleHeaderBasic.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_draft_from_existing**
> RuleHeaderBasic create_new_draft_from_existing(rules_engine_create_new_draft_from_existing_request)

CreateNewDraftFromExisting

Use this call to create a new draft based on an existing rule. Once set live, this draft will be a unique rule in its own right. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_header_basic import RuleHeaderBasic
from linnworks_api.generated.rulesengine.models.rules_engine_create_new_draft_from_existing_request import RulesEngineCreateNewDraftFromExistingRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_create_new_draft_from_existing_request = linnworks_api.generated.rulesengine.RulesEngineCreateNewDraftFromExistingRequest() # RulesEngineCreateNewDraftFromExistingRequest | 

    try:
        # CreateNewDraftFromExisting
        api_response = api_instance.create_new_draft_from_existing(rules_engine_create_new_draft_from_existing_request)
        print("The response of RulesEngineApi->create_new_draft_from_existing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->create_new_draft_from_existing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_create_new_draft_from_existing_request** | [**RulesEngineCreateNewDraftFromExistingRequest**](RulesEngineCreateNewDraftFromExistingRequest.md)|  | 

### Return type

[**RuleHeaderBasic**](RuleHeaderBasic.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_action**
> delete_action(rules_engine_delete_action_request)

DeleteAction

Use this call to delete an action from a rule. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_delete_action_request import RulesEngineDeleteActionRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_delete_action_request = linnworks_api.generated.rulesengine.RulesEngineDeleteActionRequest() # RulesEngineDeleteActionRequest | 

    try:
        # DeleteAction
        api_instance.delete_action(rules_engine_delete_action_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->delete_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_delete_action_request** | [**RulesEngineDeleteActionRequest**](RulesEngineDeleteActionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_condition**
> delete_condition(rules_engine_delete_condition_request)

DeleteCondition

Use this call to delete a conditio and its subconditions/actions <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_delete_condition_request import RulesEngineDeleteConditionRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_delete_condition_request = linnworks_api.generated.rulesengine.RulesEngineDeleteConditionRequest() # RulesEngineDeleteConditionRequest | 

    try:
        # DeleteCondition
        api_instance.delete_condition(rules_engine_delete_condition_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->delete_condition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_delete_condition_request** | [**RulesEngineDeleteConditionRequest**](RulesEngineDeleteConditionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule_by_id**
> delete_rule_by_id(rules_engine_delete_rule_by_id_request)

DeleteRuleById

Use this call to permanently delete a rule from the system. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_delete_rule_by_id_request import RulesEngineDeleteRuleByIdRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_delete_rule_by_id_request = linnworks_api.generated.rulesengine.RulesEngineDeleteRuleByIdRequest() # RulesEngineDeleteRuleByIdRequest | 

    try:
        # DeleteRuleById
        api_instance.delete_rule_by_id(rules_engine_delete_rule_by_id_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->delete_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_delete_rule_by_id_request** | [**RulesEngineDeleteRuleByIdRequest**](RulesEngineDeleteRuleByIdRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_options**
> Dict[str, List[ActionOption]] get_action_options(type=type)

GetActionOptions

Use this call to get a list of valid options for a given action <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.action_option import ActionOption
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    type = 'type_example' # str | The action type (optional)

    try:
        # GetActionOptions
        api_response = api_instance.get_action_options(type=type)
        print("The response of RulesEngineApi->get_action_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_action_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The action type | [optional] 

### Return type

**Dict[str, List[ActionOption]]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_types**
> List[ActionTypeDescriptor] get_action_types(type=type)

GetActionTypes

Use this call to retrieve a list of valid action types for the rule type <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.action_type_descriptor import ActionTypeDescriptor
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    type = 'type_example' # str | The rule type. (optional)

    try:
        # GetActionTypes
        api_response = api_instance.get_action_types(type=type)
        print("The response of RulesEngineApi->get_action_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_action_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The rule type. | [optional] 

### Return type

[**List[ActionTypeDescriptor]**](ActionTypeDescriptor.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_condition_web**
> ConditionHeaderBasic get_condition_web(pk_condition_id=pk_condition_id)

GetConditionWeb

Use this call to retrieve details about a given condition. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.condition_header_basic import ConditionHeaderBasic
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    pk_condition_id = 56 # int | The condition id. (optional)

    try:
        # GetConditionWeb
        api_response = api_instance.get_condition_web(pk_condition_id=pk_condition_id)
        print("The response of RulesEngineApi->get_condition_web:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_condition_web: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_condition_id** | **int**| The condition id. | [optional] 

### Return type

[**ConditionHeaderBasic**](ConditionHeaderBasic.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation_fields**
> List[FieldDescriptor] get_evaluation_fields(type=type)

GetEvaluationFields

Use this call to get a list of valid evaluation fields for a given rule type. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.field_descriptor import FieldDescriptor
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    type = 'type_example' # str | The rule type. (optional)

    try:
        # GetEvaluationFields
        api_response = api_instance.get_evaluation_fields(type=type)
        print("The response of RulesEngineApi->get_evaluation_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_evaluation_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The rule type. | [optional] 

### Return type

[**List[FieldDescriptor]**](FieldDescriptor.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluator_types**
> List[EvaluatorDescriptor] get_evaluator_types()

GetEvaluatorTypes

Use this call to get a list of valid evaluators and the groups which they belong to. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.evaluator_descriptor import EvaluatorDescriptor
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)

    try:
        # GetEvaluatorTypes
        api_response = api_instance.get_evaluator_types()
        print("The response of RulesEngineApi->get_evaluator_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_evaluator_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EvaluatorDescriptor]**](EvaluatorDescriptor.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_options**
> List[str] get_key_options(type=type, field_name=field_name)

GetKeyOptions

Use this call to get a list of valid keys for a given field. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    type = 'type_example' # str | The rule type (optional)
    field_name = 'field_name_example' # str | The field name (optional)

    try:
        # GetKeyOptions
        api_response = api_instance.get_key_options(type=type, field_name=field_name)
        print("The response of RulesEngineApi->get_key_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_key_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The rule type | [optional] 
 **field_name** | **str**| The field name | [optional] 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_key_options**
> List[MultiKeyOptionResponse] get_multi_key_options(rules_engine_get_multi_key_options_request)

GetMultiKeyOptions

Use this call to get a list of valid keys for a set of fields. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.multi_key_option_response import MultiKeyOptionResponse
from linnworks_api.generated.rulesengine.models.rules_engine_get_multi_key_options_request import RulesEngineGetMultiKeyOptionsRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_get_multi_key_options_request = linnworks_api.generated.rulesengine.RulesEngineGetMultiKeyOptionsRequest() # RulesEngineGetMultiKeyOptionsRequest | 

    try:
        # GetMultiKeyOptions
        api_response = api_instance.get_multi_key_options(rules_engine_get_multi_key_options_request)
        print("The response of RulesEngineApi->get_multi_key_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_multi_key_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_get_multi_key_options_request** | [**RulesEngineGetMultiKeyOptionsRequest**](RulesEngineGetMultiKeyOptionsRequest.md)|  | 

### Return type

[**List[MultiKeyOptionResponse]**](MultiKeyOptionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_options**
> List[MultiOptionResponse] get_multi_options(rules_engine_get_multi_options_request)

GetMultiOptions

Use this call to get a list of valid options for a given set of fields (and, if relevant, keys). <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.multi_option_response import MultiOptionResponse
from linnworks_api.generated.rulesengine.models.rules_engine_get_multi_options_request import RulesEngineGetMultiOptionsRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_get_multi_options_request = linnworks_api.generated.rulesengine.RulesEngineGetMultiOptionsRequest() # RulesEngineGetMultiOptionsRequest | 

    try:
        # GetMultiOptions
        api_response = api_instance.get_multi_options(rules_engine_get_multi_options_request)
        print("The response of RulesEngineApi->get_multi_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_multi_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_get_multi_options_request** | [**RulesEngineGetMultiOptionsRequest**](RulesEngineGetMultiOptionsRequest.md)|  | 

### Return type

[**List[MultiOptionResponse]**](MultiOptionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_options**
> List[str] get_options(field_name=field_name, type=type, key=key)

GetOptions

Use this call to get a list of valid options for a given field (and, if relevant, key). <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    field_name = 'field_name_example' # str | The field name. (optional)
    type = 'type_example' # str | The rule type. (optional)
    key = 'key_example' # str | The key (optional). (optional)

    try:
        # GetOptions
        api_response = api_instance.get_options(field_name=field_name, type=type, key=key)
        print("The response of RulesEngineApi->get_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| The field name. | [optional] 
 **type** | **str**| The rule type. | [optional] 
 **key** | **str**| The key (optional). | [optional] 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_required_fields_by_rule_id**
> RulesFields get_required_fields_by_rule_id(pk_rule_id=pk_rule_id)

GetRequiredFieldsByRuleId

Use this call to get a list of fields and keys used by a given rule. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_fields import RulesFields
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    pk_rule_id = 56 # int | The rule id (optional)

    try:
        # GetRequiredFieldsByRuleId
        api_response = api_instance.get_required_fields_by_rule_id(pk_rule_id=pk_rule_id)
        print("The response of RulesEngineApi->get_required_fields_by_rule_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_required_fields_by_rule_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_rule_id** | **int**| The rule id | [optional] 

### Return type

[**RulesFields**](RulesFields.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_required_fields_by_type**
> RulesFields get_required_fields_by_type(type=type)

GetRequiredFieldsByType

Use this call to get a list of fields and keys used by a given rule type <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_fields import RulesFields
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    type = 'type_example' # str | The rule type. (optional)

    try:
        # GetRequiredFieldsByType
        api_response = api_instance.get_required_fields_by_type(type=type)
        print("The response of RulesEngineApi->get_required_fields_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_required_fields_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The rule type. | [optional] 

### Return type

[**RulesFields**](RulesFields.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_condition_nodes**
> List[RuleConditionHeader] get_rule_condition_nodes(pk_rule_id=pk_rule_id)

GetRuleConditionNodes

Use this call to get information about the nodes belonging to a rule, excluding the condition items. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_condition_header import RuleConditionHeader
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    pk_rule_id = 56 # int | The rule id. (optional)

    try:
        # GetRuleConditionNodes
        api_response = api_instance.get_rule_condition_nodes(pk_rule_id=pk_rule_id)
        print("The response of RulesEngineApi->get_rule_condition_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_rule_condition_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_rule_id** | **int**| The rule id. | [optional] 

### Return type

[**List[RuleConditionHeader]**](RuleConditionHeader.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules**
> List[RuleHeaderBasic] get_rules()

GetRules

Use this call to retrieve a list of rules <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_header_basic import RuleHeaderBasic
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)

    try:
        # GetRules
        api_response = api_instance.get_rules()
        print("The response of RulesEngineApi->get_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_rules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RuleHeaderBasic]**](RuleHeaderBasic.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_by_type**
> List[RuleHeaderBasic] get_rules_by_type(type=type)

GetRulesByType

Use this call to retrieve a list of rules of a given type <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_header_basic import RuleHeaderBasic
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    type = 'type_example' # str | The rule type. (optional)

    try:
        # GetRulesByType
        api_response = api_instance.get_rules_by_type(type=type)
        print("The response of RulesEngineApi->get_rules_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->get_rules_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The rule type. | [optional] 

### Return type

[**List[RuleHeaderBasic]**](RuleHeaderBasic.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_condition_changes**
> save_condition_changes(rules_engine_save_condition_changes_request)

SaveConditionChanges

Use this call to update a conditon and its condition items. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_save_condition_changes_request import RulesEngineSaveConditionChangesRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_save_condition_changes_request = linnworks_api.generated.rulesengine.RulesEngineSaveConditionChangesRequest() # RulesEngineSaveConditionChangesRequest | 

    try:
        # SaveConditionChanges
        api_instance.save_condition_changes(rules_engine_save_condition_changes_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->save_condition_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_save_condition_changes_request** | [**RulesEngineSaveConditionChangesRequest**](RulesEngineSaveConditionChangesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_condition_enabled**
> set_condition_enabled(rules_engine_set_condition_enabled_request)

SetConditionEnabled

Use this call to enable or disable a condition. Any subconditions or actions belonging to the condition will not be evaluated or executed if it is disabled. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_set_condition_enabled_request import RulesEngineSetConditionEnabledRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_set_condition_enabled_request = linnworks_api.generated.rulesengine.RulesEngineSetConditionEnabledRequest() # RulesEngineSetConditionEnabledRequest | 

    try:
        # SetConditionEnabled
        api_instance.set_condition_enabled(rules_engine_set_condition_enabled_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->set_condition_enabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_set_condition_enabled_request** | [**RulesEngineSetConditionEnabledRequest**](RulesEngineSetConditionEnabledRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_draft_live**
> int set_draft_live(rules_engine_set_draft_live_request)

SetDraftLive

Use this call to set a draft rule live (if the draft is a copy for editing an existing rule, the existing rule will be deleted and the draft promoted). <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_set_draft_live_request import RulesEngineSetDraftLiveRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_set_draft_live_request = linnworks_api.generated.rulesengine.RulesEngineSetDraftLiveRequest() # RulesEngineSetDraftLiveRequest | 

    try:
        # SetDraftLive
        api_response = api_instance.set_draft_live(rules_engine_set_draft_live_request)
        print("The response of RulesEngineApi->set_draft_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->set_draft_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_set_draft_live_request** | [**RulesEngineSetDraftLiveRequest**](RulesEngineSetDraftLiveRequest.md)|  | 

### Return type

**int**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_rule_enabled**
> set_rule_enabled(rules_engine_set_rule_enabled_request)

SetRuleEnabled

Use this call to set the enabled state of a rule <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_set_rule_enabled_request import RulesEngineSetRuleEnabledRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_set_rule_enabled_request = linnworks_api.generated.rulesengine.RulesEngineSetRuleEnabledRequest() # RulesEngineSetRuleEnabledRequest | 

    try:
        # SetRuleEnabled
        api_instance.set_rule_enabled(rules_engine_set_rule_enabled_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->set_rule_enabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_set_rule_enabled_request** | [**RulesEngineSetRuleEnabledRequest**](RulesEngineSetRuleEnabledRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_rule_name**
> set_rule_name(rules_engine_set_rule_name_request)

SetRuleName

Use this call to rename a rule. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_set_rule_name_request import RulesEngineSetRuleNameRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_set_rule_name_request = linnworks_api.generated.rulesengine.RulesEngineSetRuleNameRequest() # RulesEngineSetRuleNameRequest | 

    try:
        # SetRuleName
        api_instance.set_rule_name(rules_engine_set_rule_name_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->set_rule_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_set_rule_name_request** | [**RulesEngineSetRuleNameRequest**](RulesEngineSetRuleNameRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swap_conditions**
> swap_conditions(rules_engine_swap_conditions_request)

SwapConditions

Use this call to swap the sort order of two conditions belonging to the same parent <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_swap_conditions_request import RulesEngineSwapConditionsRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_swap_conditions_request = linnworks_api.generated.rulesengine.RulesEngineSwapConditionsRequest() # RulesEngineSwapConditionsRequest | 

    try:
        # SwapConditions
        api_instance.swap_conditions(rules_engine_swap_conditions_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->swap_conditions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_swap_conditions_request** | [**RulesEngineSwapConditionsRequest**](RulesEngineSwapConditionsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swap_rules**
> swap_rules(rules_engine_swap_rules_request)

SwapRules

Use this call to change the executing order of the rules by swapping them with each other. <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_swap_rules_request import RulesEngineSwapRulesRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_swap_rules_request = linnworks_api.generated.rulesengine.RulesEngineSwapRulesRequest() # RulesEngineSwapRulesRequest | 

    try:
        # SwapRules
        api_instance.swap_rules(rules_engine_swap_rules_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->swap_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_swap_rules_request** | [**RulesEngineSwapRulesRequest**](RulesEngineSwapRulesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_evaluate_rule**
> RuleEvaluationResult test_evaluate_rule(rules_engine_test_evaluate_rule_request)

TestEvaluateRule

Use this call to test a rule against a set of test values <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rule_evaluation_result import RuleEvaluationResult
from linnworks_api.generated.rulesengine.models.rules_engine_test_evaluate_rule_request import RulesEngineTestEvaluateRuleRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_test_evaluate_rule_request = linnworks_api.generated.rulesengine.RulesEngineTestEvaluateRuleRequest() # RulesEngineTestEvaluateRuleRequest | 

    try:
        # TestEvaluateRule
        api_response = api_instance.test_evaluate_rule(rules_engine_test_evaluate_rule_request)
        print("The response of RulesEngineApi->test_evaluate_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesEngineApi->test_evaluate_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_test_evaluate_rule_request** | [**RulesEngineTestEvaluateRuleRequest**](RulesEngineTestEvaluateRuleRequest.md)|  | 

### Return type

[**RuleEvaluationResult**](RuleEvaluationResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_action**
> update_action(rules_engine_update_action_request)

UpdateAction

Use this call to update an action <b>Permissions Required: </b> GlobalPermissions.OrderBook.RulesEngineNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.rulesengine
from linnworks_api.generated.rulesengine.models.rules_engine_update_action_request import RulesEngineUpdateActionRequest
from linnworks_api.generated.rulesengine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.rulesengine.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.rulesengine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.rulesengine.RulesEngineApi(api_client)
    rules_engine_update_action_request = linnworks_api.generated.rulesengine.RulesEngineUpdateActionRequest() # RulesEngineUpdateActionRequest | 

    try:
        # UpdateAction
        api_instance.update_action(rules_engine_update_action_request)
    except Exception as e:
        print("Exception when calling RulesEngineApi->update_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rules_engine_update_action_request** | [**RulesEngineUpdateActionRequest**](RulesEngineUpdateActionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

