# AddItemsInBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **int** |  | 
**stock_item_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_items_in_bulk_request import AddItemsInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemsInBulkRequest from a JSON string
add_items_in_bulk_request_instance = AddItemsInBulkRequest.from_json(json)
# print the JSON string representation of the object
print(AddItemsInBulkRequest.to_json())

# convert the object into a dict
add_items_in_bulk_request_dict = add_items_in_bulk_request_instance.to_dict()
# create an instance of AddItemsInBulkRequest from a dict
add_items_in_bulk_request_from_dict = AddItemsInBulkRequest.from_dict(add_items_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


