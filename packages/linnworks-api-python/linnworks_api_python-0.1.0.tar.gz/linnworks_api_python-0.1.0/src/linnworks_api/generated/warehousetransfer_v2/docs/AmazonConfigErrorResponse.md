# AmazonConfigErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**channel_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.amazon_config_error_response import AmazonConfigErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonConfigErrorResponse from a JSON string
amazon_config_error_response_instance = AmazonConfigErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AmazonConfigErrorResponse.to_json())

# convert the object into a dict
amazon_config_error_response_dict = amazon_config_error_response_instance.to_dict()
# create an instance of AmazonConfigErrorResponse from a dict
amazon_config_error_response_from_dict = AmazonConfigErrorResponse.from_dict(amazon_config_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


