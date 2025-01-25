# GetInventoryItemImagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_id** | **str** | Conditional. If not provided, you must provide ItemNumber | [optional] 
**item_number** | **str** | Conditional. if InventoryItemId is provided, ItemNumber will be ignored | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_inventory_item_images_request import GetInventoryItemImagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItemImagesRequest from a JSON string
get_inventory_item_images_request_instance = GetInventoryItemImagesRequest.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItemImagesRequest.to_json())

# convert the object into a dict
get_inventory_item_images_request_dict = get_inventory_item_images_request_instance.to_dict()
# create an instance of GetInventoryItemImagesRequest from a dict
get_inventory_item_images_request_from_dict = GetInventoryItemImagesRequest.from_dict(get_inventory_item_images_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


