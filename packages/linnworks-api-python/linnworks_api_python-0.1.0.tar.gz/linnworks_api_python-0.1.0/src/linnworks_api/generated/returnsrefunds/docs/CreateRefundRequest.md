# CreateRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_initiated** | **bool** | Determines whether the refund was initiated on the channel, or within Linnworks | [optional] 
**order_id** | **str** | The unique identifier for the order this refund is associated with | [optional] 
**refund_lines** | [**List[NewRefundLine]**](NewRefundLine.md) | A collection of line-level refunds detailing the refund as a whole | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.create_refund_request import CreateRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRefundRequest from a JSON string
create_refund_request_instance = CreateRefundRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRefundRequest.to_json())

# convert the object into a dict
create_refund_request_dict = create_refund_request_instance.to_dict()
# create an instance of CreateRefundRequest from a dict
create_refund_request_from_dict = CreateRefundRequest.from_dict(create_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


