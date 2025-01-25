# BatchedAPIResponseDeleteInventoryItemImagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[APIResultResponseDeleteInventoryItemImagesResponse]**](APIResultResponseDeleteInventoryItemImagesResponse.md) |  | [optional] 
**total_results** | **int** |  | [optional] [readonly] 
**result_status** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.batched_api_response_delete_inventory_item_images_response import BatchedAPIResponseDeleteInventoryItemImagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchedAPIResponseDeleteInventoryItemImagesResponse from a JSON string
batched_api_response_delete_inventory_item_images_response_instance = BatchedAPIResponseDeleteInventoryItemImagesResponse.from_json(json)
# print the JSON string representation of the object
print(BatchedAPIResponseDeleteInventoryItemImagesResponse.to_json())

# convert the object into a dict
batched_api_response_delete_inventory_item_images_response_dict = batched_api_response_delete_inventory_item_images_response_instance.to_dict()
# create an instance of BatchedAPIResponseDeleteInventoryItemImagesResponse from a dict
batched_api_response_delete_inventory_item_images_response_from_dict = BatchedAPIResponseDeleteInventoryItemImagesResponse.from_dict(batched_api_response_delete_inventory_item_images_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


