# AddScrapItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrap_item** | [**ScrapItem**](ScrapItem.md) |  | [optional] 
**location_id** | **str** |  | [optional] 
**ignore_consumption** | **bool** | Consumption should not be recorded for this scrap request | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.add_scrap_item_request import AddScrapItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddScrapItemRequest from a JSON string
add_scrap_item_request_instance = AddScrapItemRequest.from_json(json)
# print the JSON string representation of the object
print(AddScrapItemRequest.to_json())

# convert the object into a dict
add_scrap_item_request_dict = add_scrap_item_request_instance.to_dict()
# create an instance of AddScrapItemRequest from a dict
add_scrap_item_request_from_dict = AddScrapItemRequest.from_dict(add_scrap_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


