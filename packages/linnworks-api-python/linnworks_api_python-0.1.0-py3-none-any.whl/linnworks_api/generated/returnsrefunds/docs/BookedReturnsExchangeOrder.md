# BookedReturnsExchangeOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 
**n_order_id** | **int** |  | [optional] 
**reference_num** | **str** |  | [optional] 
**secondary_reference** | **str** |  | [optional] 
**c_full_name** | **str** |  | [optional] 
**return_date** | **datetime** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.booked_returns_exchange_order import BookedReturnsExchangeOrder

# TODO update the JSON string below
json = "{}"
# create an instance of BookedReturnsExchangeOrder from a JSON string
booked_returns_exchange_order_instance = BookedReturnsExchangeOrder.from_json(json)
# print the JSON string representation of the object
print(BookedReturnsExchangeOrder.to_json())

# convert the object into a dict
booked_returns_exchange_order_dict = booked_returns_exchange_order_instance.to_dict()
# create an instance of BookedReturnsExchangeOrder from a dict
booked_returns_exchange_order_from_dict = BookedReturnsExchangeOrder.from_dict(booked_returns_exchange_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


