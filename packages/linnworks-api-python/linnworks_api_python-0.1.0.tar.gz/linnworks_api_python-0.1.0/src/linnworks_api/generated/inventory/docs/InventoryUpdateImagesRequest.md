# InventoryUpdateImagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**List[StockItemImageSimple]**](StockItemImageSimple.md) | Images to edit | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_images_request import InventoryUpdateImagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateImagesRequest from a JSON string
inventory_update_images_request_instance = InventoryUpdateImagesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateImagesRequest.to_json())

# convert the object into a dict
inventory_update_images_request_dict = inventory_update_images_request_instance.to_dict()
# create an instance of InventoryUpdateImagesRequest from a dict
inventory_update_images_request_from_dict = InventoryUpdateImagesRequest.from_dict(inventory_update_images_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


