# GetRefundLinesByHeaderIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** | The unique identifier for the loaded refund | [optional] 
**refund_lines** | [**List[VerifiedRefund]**](VerifiedRefund.md) | A collection of all refunds associated with the loaded header | [optional] 
**refund_options** | [**RefundOptions**](RefundOptions.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_refund_lines_by_header_id_response import GetRefundLinesByHeaderIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRefundLinesByHeaderIdResponse from a JSON string
get_refund_lines_by_header_id_response_instance = GetRefundLinesByHeaderIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetRefundLinesByHeaderIdResponse.to_json())

# convert the object into a dict
get_refund_lines_by_header_id_response_dict = get_refund_lines_by_header_id_response_instance.to_dict()
# create an instance of GetRefundLinesByHeaderIdResponse from a dict
get_refund_lines_by_header_id_response_from_dict = GetRefundLinesByHeaderIdResponse.from_dict(get_refund_lines_by_header_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


