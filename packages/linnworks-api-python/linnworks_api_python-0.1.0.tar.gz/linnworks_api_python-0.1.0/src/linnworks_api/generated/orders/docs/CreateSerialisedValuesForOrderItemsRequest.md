# CreateSerialisedValuesForOrderItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_serial_data** | [**List[OrderItemSerialModel]**](OrderItemSerialModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.create_serialised_values_for_order_items_request import CreateSerialisedValuesForOrderItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSerialisedValuesForOrderItemsRequest from a JSON string
create_serialised_values_for_order_items_request_instance = CreateSerialisedValuesForOrderItemsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSerialisedValuesForOrderItemsRequest.to_json())

# convert the object into a dict
create_serialised_values_for_order_items_request_dict = create_serialised_values_for_order_items_request_instance.to_dict()
# create an instance of CreateSerialisedValuesForOrderItemsRequest from a dict
create_serialised_values_for_order_items_request_from_dict = CreateSerialisedValuesForOrderItemsRequest.from_dict(create_serialised_values_for_order_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


