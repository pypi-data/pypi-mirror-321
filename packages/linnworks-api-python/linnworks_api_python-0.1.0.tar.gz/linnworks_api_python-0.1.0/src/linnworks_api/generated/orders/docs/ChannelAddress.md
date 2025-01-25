# ChannelAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_country_code** | **str** |  | [optional] 
**match_country_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**town** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**is_empty** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.orders.models.channel_address import ChannelAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelAddress from a JSON string
channel_address_instance = ChannelAddress.from_json(json)
# print the JSON string representation of the object
print(ChannelAddress.to_json())

# convert the object into a dict
channel_address_dict = channel_address_instance.to_dict()
# create an instance of ChannelAddress from a dict
channel_address_from_dict = ChannelAddress.from_dict(channel_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


