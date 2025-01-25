# OrderXML


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_tag** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**xml** | **str** |  | [optional] [readonly] 
**xml_doc** | **List[object]** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_xml import OrderXML

# TODO update the JSON string below
json = "{}"
# create an instance of OrderXML from a JSON string
order_xml_instance = OrderXML.from_json(json)
# print the JSON string representation of the object
print(OrderXML.to_json())

# convert the object into a dict
order_xml_dict = order_xml_instance.to_dict()
# create an instance of OrderXML from a dict
order_xml_from_dict = OrderXML.from_dict(order_xml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


