# GetOrderItemIndicatorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**items** | [**List[IndicatorRequest]**](IndicatorRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_order_item_indicator_request import GetOrderItemIndicatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderItemIndicatorRequest from a JSON string
get_order_item_indicator_request_instance = GetOrderItemIndicatorRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrderItemIndicatorRequest.to_json())

# convert the object into a dict
get_order_item_indicator_request_dict = get_order_item_indicator_request_instance.to_dict()
# create an instance of GetOrderItemIndicatorRequest from a dict
get_order_item_indicator_request_from_dict = GetOrderItemIndicatorRequest.from_dict(get_order_item_indicator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


