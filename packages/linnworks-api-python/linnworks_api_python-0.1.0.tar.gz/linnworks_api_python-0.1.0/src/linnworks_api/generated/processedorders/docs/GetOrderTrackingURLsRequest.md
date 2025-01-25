# GetOrderTrackingURLsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TrackingURLRequestItem]**](TrackingURLRequestItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.get_order_tracking_urls_request import GetOrderTrackingURLsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderTrackingURLsRequest from a JSON string
get_order_tracking_urls_request_instance = GetOrderTrackingURLsRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrderTrackingURLsRequest.to_json())

# convert the object into a dict
get_order_tracking_urls_request_dict = get_order_tracking_urls_request_instance.to_dict()
# create an instance of GetOrderTrackingURLsRequest from a dict
get_order_tracking_urls_request_from_dict = GetOrderTrackingURLsRequest.from_dict(get_order_tracking_urls_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


