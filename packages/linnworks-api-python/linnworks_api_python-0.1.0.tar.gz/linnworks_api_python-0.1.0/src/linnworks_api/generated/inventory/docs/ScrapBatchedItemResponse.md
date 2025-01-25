# ScrapBatchedItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrap_item** | [**ScrapItem**](ScrapItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.scrap_batched_item_response import ScrapBatchedItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapBatchedItemResponse from a JSON string
scrap_batched_item_response_instance = ScrapBatchedItemResponse.from_json(json)
# print the JSON string representation of the object
print(ScrapBatchedItemResponse.to_json())

# convert the object into a dict
scrap_batched_item_response_dict = scrap_batched_item_response_instance.to_dict()
# create an instance of ScrapBatchedItemResponse from a dict
scrap_batched_item_response_from_dict = ScrapBatchedItemResponse.from_dict(scrap_batched_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


