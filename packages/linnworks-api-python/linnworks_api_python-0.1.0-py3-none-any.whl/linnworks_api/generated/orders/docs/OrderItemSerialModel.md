# OrderItemSerialModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_row_id** | **str** |  | [optional] 
**correlation_serials** | **List[List[SerialModel]]** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_item_serial_model import OrderItemSerialModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemSerialModel from a JSON string
order_item_serial_model_instance = OrderItemSerialModel.from_json(json)
# print the JSON string representation of the object
print(OrderItemSerialModel.to_json())

# convert the object into a dict
order_item_serial_model_dict = order_item_serial_model_instance.to_dict()
# create an instance of OrderItemSerialModel from a dict
order_item_serial_model_from_dict = OrderItemSerialModel.from_dict(order_item_serial_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


