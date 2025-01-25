# UpdateItemReceivedQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **int** |  | [optional] 
**transfer_item_id** | **int** |  | [optional] 
**received_quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_item_received_quantity_request import UpdateItemReceivedQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateItemReceivedQuantityRequest from a JSON string
update_item_received_quantity_request_instance = UpdateItemReceivedQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateItemReceivedQuantityRequest.to_json())

# convert the object into a dict
update_item_received_quantity_request_dict = update_item_received_quantity_request_instance.to_dict()
# create an instance of UpdateItemReceivedQuantityRequest from a dict
update_item_received_quantity_request_from_dict = UpdateItemReceivedQuantityRequest.from_dict(update_item_received_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


