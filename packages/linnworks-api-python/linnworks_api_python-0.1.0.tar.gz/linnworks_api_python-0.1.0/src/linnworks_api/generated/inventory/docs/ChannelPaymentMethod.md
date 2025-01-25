# ChannelPaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_channel_id** | **int** |  | [optional] 
**pk_row_id** | **int** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**is_changed** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.channel_payment_method import ChannelPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPaymentMethod from a JSON string
channel_payment_method_instance = ChannelPaymentMethod.from_json(json)
# print the JSON string representation of the object
print(ChannelPaymentMethod.to_json())

# convert the object into a dict
channel_payment_method_dict = channel_payment_method_instance.to_dict()
# create an instance of ChannelPaymentMethod from a dict
channel_payment_method_from_dict = ChannelPaymentMethod.from_dict(channel_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


