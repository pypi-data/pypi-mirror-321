# ProcessOrderResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**processed** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.process_order_result import ProcessOrderResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessOrderResult from a JSON string
process_order_result_instance = ProcessOrderResult.from_json(json)
# print the JSON string representation of the object
print(ProcessOrderResult.to_json())

# convert the object into a dict
process_order_result_dict = process_order_result_instance.to_dict()
# create an instance of ProcessOrderResult from a dict
process_order_result_from_dict = ProcessOrderResult.from_dict(process_order_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


