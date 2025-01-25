# RefundError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_row_id** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**date_stamp** | **datetime** |  | [optional] 
**acknowledged** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.refund_error import RefundError

# TODO update the JSON string below
json = "{}"
# create an instance of RefundError from a JSON string
refund_error_instance = RefundError.from_json(json)
# print the JSON string representation of the object
print(RefundError.to_json())

# convert the object into a dict
refund_error_dict = refund_error_instance.to_dict()
# create an instance of RefundError from a dict
refund_error_from_dict = RefundError.from_dict(refund_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


