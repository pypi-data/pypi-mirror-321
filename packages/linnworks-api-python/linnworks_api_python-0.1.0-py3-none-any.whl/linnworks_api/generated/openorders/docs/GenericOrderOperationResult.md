# GenericOrderOperationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful_orders** | **List[str]** | List of orders that were moved | [optional] 
**keyed_errors** | **Dict[str, str]** | Dictionary of keyed errors. These are the same errors as per the Errors property, but indexable by orderId | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.generic_order_operation_result import GenericOrderOperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of GenericOrderOperationResult from a JSON string
generic_order_operation_result_instance = GenericOrderOperationResult.from_json(json)
# print the JSON string representation of the object
print(GenericOrderOperationResult.to_json())

# convert the object into a dict
generic_order_operation_result_dict = generic_order_operation_result_instance.to_dict()
# create an instance of GenericOrderOperationResult from a dict
generic_order_operation_result_from_dict = GenericOrderOperationResult.from_dict(generic_order_operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


