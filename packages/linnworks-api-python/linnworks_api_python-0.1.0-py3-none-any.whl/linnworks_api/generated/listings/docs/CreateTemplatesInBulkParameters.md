# CreateTemplatesInBulkParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**channels_configurators** | [**List[CreateTemplatesInBulkChannelParameters]**](CreateTemplatesInBulkChannelParameters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.create_templates_in_bulk_parameters import CreateTemplatesInBulkParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplatesInBulkParameters from a JSON string
create_templates_in_bulk_parameters_instance = CreateTemplatesInBulkParameters.from_json(json)
# print the JSON string representation of the object
print(CreateTemplatesInBulkParameters.to_json())

# convert the object into a dict
create_templates_in_bulk_parameters_dict = create_templates_in_bulk_parameters_instance.to_dict()
# create an instance of CreateTemplatesInBulkParameters from a dict
create_templates_in_bulk_parameters_from_dict = CreateTemplatesInBulkParameters.from_dict(create_templates_in_bulk_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


