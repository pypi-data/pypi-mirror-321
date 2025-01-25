# GetRefundLinesByHeaderIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** | The unique identifier for the refund header to load | [optional] 
**order_id** | **str** | The unique identifier for the order this refund pertains to. Used as a safety to ensure the correct refund is being worked with | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_refund_lines_by_header_id_request import GetRefundLinesByHeaderIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRefundLinesByHeaderIdRequest from a JSON string
get_refund_lines_by_header_id_request_instance = GetRefundLinesByHeaderIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetRefundLinesByHeaderIdRequest.to_json())

# convert the object into a dict
get_refund_lines_by_header_id_request_dict = get_refund_lines_by_header_id_request_instance.to_dict()
# create an instance of GetRefundLinesByHeaderIdRequest from a dict
get_refund_lines_by_header_id_request_from_dict = GetRefundLinesByHeaderIdRequest.from_dict(get_refund_lines_by_header_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


