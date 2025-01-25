# ItemReceiveResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_item_id** | **int** |  | [optional] 
**is_received** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.item_receive_result import ItemReceiveResult

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReceiveResult from a JSON string
item_receive_result_instance = ItemReceiveResult.from_json(json)
# print the JSON string representation of the object
print(ItemReceiveResult.to_json())

# convert the object into a dict
item_receive_result_dict = item_receive_result_instance.to_dict()
# create an instance of ItemReceiveResult from a dict
item_receive_result_from_dict = ItemReceiveResult.from_dict(item_receive_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


