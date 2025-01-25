# ReturnsRefundsEditBookedItemInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | unique ID of the order | [optional] 
**booked_returns_exchange_item** | [**BookedReturnsExchangeItem**](BookedReturnsExchangeItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_edit_booked_item_info_request import ReturnsRefundsEditBookedItemInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsEditBookedItemInfoRequest from a JSON string
returns_refunds_edit_booked_item_info_request_instance = ReturnsRefundsEditBookedItemInfoRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsEditBookedItemInfoRequest.to_json())

# convert the object into a dict
returns_refunds_edit_booked_item_info_request_dict = returns_refunds_edit_booked_item_info_request_instance.to_dict()
# create an instance of ReturnsRefundsEditBookedItemInfoRequest from a dict
returns_refunds_edit_booked_item_info_request_from_dict = ReturnsRefundsEditBookedItemInfoRequest.from_dict(returns_refunds_edit_booked_item_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


