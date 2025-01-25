# GetOrderItemIndicatorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OrderItemIndicator]**](OrderItemIndicator.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_order_item_indicator_response import GetOrderItemIndicatorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderItemIndicatorResponse from a JSON string
get_order_item_indicator_response_instance = GetOrderItemIndicatorResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrderItemIndicatorResponse.to_json())

# convert the object into a dict
get_order_item_indicator_response_dict = get_order_item_indicator_response_instance.to_dict()
# create an instance of GetOrderItemIndicatorResponse from a dict
get_order_item_indicator_response_from_dict = GetOrderItemIndicatorResponse.from_dict(get_order_item_indicator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


