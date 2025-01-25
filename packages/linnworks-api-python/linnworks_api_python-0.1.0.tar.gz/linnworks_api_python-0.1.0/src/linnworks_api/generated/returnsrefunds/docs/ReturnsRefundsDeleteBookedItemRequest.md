# ReturnsRefundsDeleteBookedItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | unique ID of the order | [optional] 
**pk_return_id** | **int** | unique row ID of the return/exchange item | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_booked_item_request import ReturnsRefundsDeleteBookedItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsDeleteBookedItemRequest from a JSON string
returns_refunds_delete_booked_item_request_instance = ReturnsRefundsDeleteBookedItemRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsDeleteBookedItemRequest.to_json())

# convert the object into a dict
returns_refunds_delete_booked_item_request_dict = returns_refunds_delete_booked_item_request_instance.to_dict()
# create an instance of ReturnsRefundsDeleteBookedItemRequest from a dict
returns_refunds_delete_booked_item_request_from_dict = ReturnsRefundsDeleteBookedItemRequest.from_dict(returns_refunds_delete_booked_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


