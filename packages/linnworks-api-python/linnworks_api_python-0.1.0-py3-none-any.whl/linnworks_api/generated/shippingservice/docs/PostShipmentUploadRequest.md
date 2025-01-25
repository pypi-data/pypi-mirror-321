# PostShipmentUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_upload_items** | [**List[FileUploadItem]**](FileUploadItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.post_shipment_upload_request import PostShipmentUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostShipmentUploadRequest from a JSON string
post_shipment_upload_request_instance = PostShipmentUploadRequest.from_json(json)
# print the JSON string representation of the object
print(PostShipmentUploadRequest.to_json())

# convert the object into a dict
post_shipment_upload_request_dict = post_shipment_upload_request_instance.to_dict()
# create an instance of PostShipmentUploadRequest from a dict
post_shipment_upload_request_from_dict = PostShipmentUploadRequest.from_dict(post_shipment_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


