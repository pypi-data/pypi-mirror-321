# CreateTemplatesInBulkChannelParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**configurator_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.create_templates_in_bulk_channel_parameters import CreateTemplatesInBulkChannelParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplatesInBulkChannelParameters from a JSON string
create_templates_in_bulk_channel_parameters_instance = CreateTemplatesInBulkChannelParameters.from_json(json)
# print the JSON string representation of the object
print(CreateTemplatesInBulkChannelParameters.to_json())

# convert the object into a dict
create_templates_in_bulk_channel_parameters_dict = create_templates_in_bulk_channel_parameters_instance.to_dict()
# create an instance of CreateTemplatesInBulkChannelParameters from a dict
create_templates_in_bulk_channel_parameters_from_dict = CreateTemplatesInBulkChannelParameters.from_dict(create_templates_in_bulk_channel_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


