# ListDeliveryWindowOptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_type** | [**AvailabilityType**](AvailabilityType.md) |  | [optional] 
**delivery_window_option_id** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.list_delivery_window_option_response import ListDeliveryWindowOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeliveryWindowOptionResponse from a JSON string
list_delivery_window_option_response_instance = ListDeliveryWindowOptionResponse.from_json(json)
# print the JSON string representation of the object
print(ListDeliveryWindowOptionResponse.to_json())

# convert the object into a dict
list_delivery_window_option_response_dict = list_delivery_window_option_response_instance.to_dict()
# create an instance of ListDeliveryWindowOptionResponse from a dict
list_delivery_window_option_response_from_dict = ListDeliveryWindowOptionResponse.from_dict(list_delivery_window_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


