# GetRefundOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** | If included, will return the relevant refund header as part of the RefundOptions object in the response | [optional] 
**order_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_refund_options_request import GetRefundOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRefundOptionsRequest from a JSON string
get_refund_options_request_instance = GetRefundOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetRefundOptionsRequest.to_json())

# convert the object into a dict
get_refund_options_request_dict = get_refund_options_request_instance.to_dict()
# create an instance of GetRefundOptionsRequest from a dict
get_refund_options_request_from_dict = GetRefundOptionsRequest.from_dict(get_refund_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


