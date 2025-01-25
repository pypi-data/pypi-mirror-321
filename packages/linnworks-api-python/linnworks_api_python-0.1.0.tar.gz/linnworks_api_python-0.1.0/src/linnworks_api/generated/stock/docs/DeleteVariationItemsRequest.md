# DeleteVariationItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_item_id** | **str** |  | [optional] 
**stock_item_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.delete_variation_items_request import DeleteVariationItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVariationItemsRequest from a JSON string
delete_variation_items_request_instance = DeleteVariationItemsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteVariationItemsRequest.to_json())

# convert the object into a dict
delete_variation_items_request_dict = delete_variation_items_request_instance.to_dict()
# create an instance of DeleteVariationItemsRequest from a dict
delete_variation_items_request_from_dict = DeleteVariationItemsRequest.from_dict(delete_variation_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


