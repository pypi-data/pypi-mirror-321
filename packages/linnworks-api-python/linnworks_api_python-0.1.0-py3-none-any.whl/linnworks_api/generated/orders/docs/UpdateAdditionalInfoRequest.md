# UpdateAdditionalInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Linnworks Order Id | [optional] 
**order_item_row_id** | **str** | The Row Id for the order item | [optional] 
**additional_info** | [**List[OrderItemOptionUpdate]**](OrderItemOptionUpdate.md) | A list of additional information to update or delete from the order item | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.update_additional_info_request import UpdateAdditionalInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdditionalInfoRequest from a JSON string
update_additional_info_request_instance = UpdateAdditionalInfoRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdditionalInfoRequest.to_json())

# convert the object into a dict
update_additional_info_request_dict = update_additional_info_request_instance.to_dict()
# create an instance of UpdateAdditionalInfoRequest from a dict
update_additional_info_request_from_dict = UpdateAdditionalInfoRequest.from_dict(update_additional_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


