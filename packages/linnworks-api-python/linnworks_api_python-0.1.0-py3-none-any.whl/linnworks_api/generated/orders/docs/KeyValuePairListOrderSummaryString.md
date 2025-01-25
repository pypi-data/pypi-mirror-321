# KeyValuePairListOrderSummaryString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**List[OrderSummary]**](OrderSummary.md) |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.orders.models.key_value_pair_list_order_summary_string import KeyValuePairListOrderSummaryString

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairListOrderSummaryString from a JSON string
key_value_pair_list_order_summary_string_instance = KeyValuePairListOrderSummaryString.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairListOrderSummaryString.to_json())

# convert the object into a dict
key_value_pair_list_order_summary_string_dict = key_value_pair_list_order_summary_string_instance.to_dict()
# create an instance of KeyValuePairListOrderSummaryString from a dict
key_value_pair_list_order_summary_string_from_dict = KeyValuePairListOrderSummaryString.from_dict(key_value_pair_list_order_summary_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


