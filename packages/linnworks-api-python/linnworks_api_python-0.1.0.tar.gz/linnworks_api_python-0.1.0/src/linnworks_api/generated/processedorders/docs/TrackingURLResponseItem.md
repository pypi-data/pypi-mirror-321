# TrackingURLResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_url** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**vendor** | **str** |  | [optional] 
**postal_tracking_number** | **str** |  | [optional] 
**postcode** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.tracking_url_response_item import TrackingURLResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingURLResponseItem from a JSON string
tracking_url_response_item_instance = TrackingURLResponseItem.from_json(json)
# print the JSON string representation of the object
print(TrackingURLResponseItem.to_json())

# convert the object into a dict
tracking_url_response_item_dict = tracking_url_response_item_instance.to_dict()
# create an instance of TrackingURLResponseItem from a dict
tracking_url_response_item_from_dict = TrackingURLResponseItem.from_dict(tracking_url_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


