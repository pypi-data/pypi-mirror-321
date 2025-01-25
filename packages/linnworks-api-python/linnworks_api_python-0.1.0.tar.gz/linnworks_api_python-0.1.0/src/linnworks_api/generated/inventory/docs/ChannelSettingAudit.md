# ChannelSettingAudit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_audit_id** | **int** |  | [optional] 
**fk_channel_id** | **int** |  | [optional] 
**property_name** | **str** |  | [optional] 
**property_value_is** | **str** |  | [optional] 
**audit_date_time** | **datetime** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.channel_setting_audit import ChannelSettingAudit

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelSettingAudit from a JSON string
channel_setting_audit_instance = ChannelSettingAudit.from_json(json)
# print the JSON string representation of the object
print(ChannelSettingAudit.to_json())

# convert the object into a dict
channel_setting_audit_dict = channel_setting_audit_instance.to_dict()
# create an instance of ChannelSettingAudit from a dict
channel_setting_audit_from_dict = ChannelSettingAudit.from_dict(channel_setting_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


