# GetRefundOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_options** | [**RefundOptions**](RefundOptions.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_refund_options_response import GetRefundOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRefundOptionsResponse from a JSON string
get_refund_options_response_instance = GetRefundOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRefundOptionsResponse.to_json())

# convert the object into a dict
get_refund_options_response_dict = get_refund_options_response_instance.to_dict()
# create an instance of GetRefundOptionsResponse from a dict
get_refund_options_response_from_dict = GetRefundOptionsResponse.from_dict(get_refund_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


