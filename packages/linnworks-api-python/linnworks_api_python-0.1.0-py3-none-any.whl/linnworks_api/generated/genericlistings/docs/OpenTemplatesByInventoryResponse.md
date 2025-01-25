# OpenTemplatesByInventoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** |  | [optional] 
**templates_info** | **List[object]** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.open_templates_by_inventory_response import OpenTemplatesByInventoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpenTemplatesByInventoryResponse from a JSON string
open_templates_by_inventory_response_instance = OpenTemplatesByInventoryResponse.from_json(json)
# print the JSON string representation of the object
print(OpenTemplatesByInventoryResponse.to_json())

# convert the object into a dict
open_templates_by_inventory_response_dict = open_templates_by_inventory_response_instance.to_dict()
# create an instance of OpenTemplatesByInventoryResponse from a dict
open_templates_by_inventory_response_from_dict = OpenTemplatesByInventoryResponse.from_dict(open_templates_by_inventory_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


