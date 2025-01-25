# DeleteMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_id** | **int** | Id of the stock move to delete | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.delete_move_request import DeleteMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMoveRequest from a JSON string
delete_move_request_instance = DeleteMoveRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMoveRequest.to_json())

# convert the object into a dict
delete_move_request_dict = delete_move_request_instance.to_dict()
# create an instance of DeleteMoveRequest from a dict
delete_move_request_from_dict = DeleteMoveRequest.from_dict(delete_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


