# CancellationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_channel_cancellation** | **bool** |  | [optional] 
**is_channel_initiated** | **bool** |  | [optional] 
**is_channel_cancellation_confirmed** | **bool** |  | [optional] 
**is_free_text** | **bool** |  | [optional] 
**free_text_or_note** | **str** |  | [optional] 
**reason_tag** | **str** |  | [optional] 
**sub_reason_tag** | **str** |  | [optional] 
**create_full_refund** | **bool** |  | [optional] 
**refund_already_processed** | **bool** |  | [optional] 
**refund_status_tag** | **str** |  | [optional] 
**refund_reference** | **str** |  | [optional] 
**header_id** | **int** |  | [optional] 
**order_id** | **str** |  | [optional] 
**internal_only** | **bool** |  | [optional] 
**is_retry** | **bool** |  | [optional] 
**action_form** | [**ActionForm**](ActionForm.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.cancellation_request import CancellationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationRequest from a JSON string
cancellation_request_instance = CancellationRequest.from_json(json)
# print the JSON string representation of the object
print(CancellationRequest.to_json())

# convert the object into a dict
cancellation_request_dict = cancellation_request_instance.to_dict()
# create an instance of CancellationRequest from a dict
cancellation_request_from_dict = CancellationRequest.from_dict(cancellation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


