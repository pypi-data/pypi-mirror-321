# UpdateRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** | The identifier for the refund header to update | [optional] 
**order_id** | **str** | The unique identifier for the order the refund lines pertain to | [optional] 
**refund_lines** | [**List[UpdatedRefundLine]**](UpdatedRefundLine.md) | A list of refund lines to update within the given refund | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.update_refund_request import UpdateRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRefundRequest from a JSON string
update_refund_request_instance = UpdateRefundRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRefundRequest.to_json())

# convert the object into a dict
update_refund_request_dict = update_refund_request_instance.to_dict()
# create an instance of UpdateRefundRequest from a dict
update_refund_request_from_dict = UpdateRefundRequest.from_dict(update_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


