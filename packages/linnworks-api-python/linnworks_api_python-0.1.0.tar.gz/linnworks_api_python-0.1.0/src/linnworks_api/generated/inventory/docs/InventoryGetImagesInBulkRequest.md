# InventoryGetImagesInBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetImagesInBulkRequest**](GetImagesInBulkRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_images_in_bulk_request import InventoryGetImagesInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetImagesInBulkRequest from a JSON string
inventory_get_images_in_bulk_request_instance = InventoryGetImagesInBulkRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetImagesInBulkRequest.to_json())

# convert the object into a dict
inventory_get_images_in_bulk_request_dict = inventory_get_images_in_bulk_request_instance.to_dict()
# create an instance of InventoryGetImagesInBulkRequest from a dict
inventory_get_images_in_bulk_request_from_dict = InventoryGetImagesInBulkRequest.from_dict(inventory_get_images_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


