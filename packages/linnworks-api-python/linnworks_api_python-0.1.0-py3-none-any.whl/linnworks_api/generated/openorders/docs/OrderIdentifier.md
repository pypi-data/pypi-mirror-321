# OrderIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_order_id** | **str** |  | [optional] 
**identifier_id** | **int** |  | [optional] 
**is_custom** | **bool** |  | [optional] 
**image_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.order_identifier import OrderIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of OrderIdentifier from a JSON string
order_identifier_instance = OrderIdentifier.from_json(json)
# print the JSON string representation of the object
print(OrderIdentifier.to_json())

# convert the object into a dict
order_identifier_dict = order_identifier_instance.to_dict()
# create an instance of OrderIdentifier from a dict
order_identifier_from_dict = OrderIdentifier.from_dict(order_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


