# APIResultResponseDeleteInventoryItemImagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**DeleteInventoryItemImagesResponse**](DeleteInventoryItemImagesResponse.md) |  | [optional] 
**result_status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.api_result_response_delete_inventory_item_images_response import APIResultResponseDeleteInventoryItemImagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIResultResponseDeleteInventoryItemImagesResponse from a JSON string
api_result_response_delete_inventory_item_images_response_instance = APIResultResponseDeleteInventoryItemImagesResponse.from_json(json)
# print the JSON string representation of the object
print(APIResultResponseDeleteInventoryItemImagesResponse.to_json())

# convert the object into a dict
api_result_response_delete_inventory_item_images_response_dict = api_result_response_delete_inventory_item_images_response_instance.to_dict()
# create an instance of APIResultResponseDeleteInventoryItemImagesResponse from a dict
api_result_response_delete_inventory_item_images_response_from_dict = APIResultResponseDeleteInventoryItemImagesResponse.from_dict(api_result_response_delete_inventory_item_images_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


