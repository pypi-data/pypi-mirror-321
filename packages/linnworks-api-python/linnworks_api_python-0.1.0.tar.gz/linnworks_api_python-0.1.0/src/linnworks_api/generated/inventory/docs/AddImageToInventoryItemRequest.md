# AddImageToInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** | SKU number of an item | [optional] 
**stock_item_id** | **str** | pkStockItemId of an item | [optional] 
**is_main** | **bool** | Whether you want to set the image as main | [optional] 
**image_url** | **str** | Image URL | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.add_image_to_inventory_item_request import AddImageToInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddImageToInventoryItemRequest from a JSON string
add_image_to_inventory_item_request_instance = AddImageToInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(AddImageToInventoryItemRequest.to_json())

# convert the object into a dict
add_image_to_inventory_item_request_dict = add_image_to_inventory_item_request_instance.to_dict()
# create an instance of AddImageToInventoryItemRequest from a dict
add_image_to_inventory_item_request_from_dict = AddImageToInventoryItemRequest.from_dict(add_image_to_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


