# OpenTemplatesByInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**parameters** | [**InventorySearchParameters**](InventorySearchParameters.md) |  | [optional] 
**pagination_parameters** | [**PaginationParameters**](PaginationParameters.md) |  | [optional] 
**select_only_with_errors** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.open_templates_by_inventory_request import OpenTemplatesByInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenTemplatesByInventoryRequest from a JSON string
open_templates_by_inventory_request_instance = OpenTemplatesByInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(OpenTemplatesByInventoryRequest.to_json())

# convert the object into a dict
open_templates_by_inventory_request_dict = open_templates_by_inventory_request_instance.to_dict()
# create an instance of OpenTemplatesByInventoryRequest from a dict
open_templates_by_inventory_request_from_dict = OpenTemplatesByInventoryRequest.from_dict(open_templates_by_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


