# TrackingURLRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** |  | [optional] 
**vendor** | **str** |  | [optional] 
**postal_tracking_number** | **str** |  | [optional] 
**postcode** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.tracking_url_request_item import TrackingURLRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingURLRequestItem from a JSON string
tracking_url_request_item_instance = TrackingURLRequestItem.from_json(json)
# print the JSON string representation of the object
print(TrackingURLRequestItem.to_json())

# convert the object into a dict
tracking_url_request_item_dict = tracking_url_request_item_instance.to_dict()
# create an instance of TrackingURLRequestItem from a dict
tracking_url_request_item_from_dict = TrackingURLRequestItem.from_dict(tracking_url_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


