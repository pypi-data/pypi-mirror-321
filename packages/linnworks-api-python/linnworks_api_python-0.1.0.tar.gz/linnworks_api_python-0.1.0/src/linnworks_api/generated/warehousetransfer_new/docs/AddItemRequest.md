# AddItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **int** |  | 
**stock_item_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_item_request import AddItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemRequest from a JSON string
add_item_request_instance = AddItemRequest.from_json(json)
# print the JSON string representation of the object
print(AddItemRequest.to_json())

# convert the object into a dict
add_item_request_dict = add_item_request_instance.to_dict()
# create an instance of AddItemRequest from a dict
add_item_request_from_dict = AddItemRequest.from_dict(add_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


