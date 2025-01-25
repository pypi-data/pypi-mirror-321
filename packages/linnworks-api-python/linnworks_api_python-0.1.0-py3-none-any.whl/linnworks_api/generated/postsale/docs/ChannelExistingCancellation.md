# ChannelExistingCancellation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.channel_existing_cancellation import ChannelExistingCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelExistingCancellation from a JSON string
channel_existing_cancellation_instance = ChannelExistingCancellation.from_json(json)
# print the JSON string representation of the object
print(ChannelExistingCancellation.to_json())

# convert the object into a dict
channel_existing_cancellation_dict = channel_existing_cancellation_instance.to_dict()
# create an instance of ChannelExistingCancellation from a dict
channel_existing_cancellation_from_dict = ChannelExistingCancellation.from_dict(channel_existing_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


