# GetSerialisedValuesForOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_row_serial_values_by_order_ids** | **Dict[str, List[OrderItemSerialModel]]** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.get_serialised_values_for_orders_response import GetSerialisedValuesForOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSerialisedValuesForOrdersResponse from a JSON string
get_serialised_values_for_orders_response_instance = GetSerialisedValuesForOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(GetSerialisedValuesForOrdersResponse.to_json())

# convert the object into a dict
get_serialised_values_for_orders_response_dict = get_serialised_values_for_orders_response_instance.to_dict()
# create an instance of GetSerialisedValuesForOrdersResponse from a dict
get_serialised_values_for_orders_response_from_dict = GetSerialisedValuesForOrdersResponse.from_dict(get_serialised_values_for_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


