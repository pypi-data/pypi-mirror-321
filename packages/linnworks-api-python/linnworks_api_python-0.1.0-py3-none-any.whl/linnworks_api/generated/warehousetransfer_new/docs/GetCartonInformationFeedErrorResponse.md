# GetCartonInformationFeedErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_carton_information_feed_error_response import GetCartonInformationFeedErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCartonInformationFeedErrorResponse from a JSON string
get_carton_information_feed_error_response_instance = GetCartonInformationFeedErrorResponse.from_json(json)
# print the JSON string representation of the object
print(GetCartonInformationFeedErrorResponse.to_json())

# convert the object into a dict
get_carton_information_feed_error_response_dict = get_carton_information_feed_error_response_instance.to_dict()
# create an instance of GetCartonInformationFeedErrorResponse from a dict
get_carton_information_feed_error_response_from_dict = GetCartonInformationFeedErrorResponse.from_dict(get_carton_information_feed_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


