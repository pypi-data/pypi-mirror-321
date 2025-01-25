# CreateTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**parameters** | [**InventorySearchParameters**](InventorySearchParameters.md) |  | [optional] 
**pagination_parameters** | [**PaginationParameters**](PaginationParameters.md) |  | [optional] 
**configurator_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.create_templates_request import CreateTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplatesRequest from a JSON string
create_templates_request_instance = CreateTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTemplatesRequest.to_json())

# convert the object into a dict
create_templates_request_dict = create_templates_request_instance.to_dict()
# create an instance of CreateTemplatesRequest from a dict
create_templates_request_from_dict = CreateTemplatesRequest.from_dict(create_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


