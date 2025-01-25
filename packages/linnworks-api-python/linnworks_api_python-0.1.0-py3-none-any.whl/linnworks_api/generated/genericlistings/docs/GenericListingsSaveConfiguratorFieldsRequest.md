# GenericListingsSaveConfiguratorFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SaveConfiguratorFieldsRequest**](SaveConfiguratorFieldsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_save_configurator_fields_request import GenericListingsSaveConfiguratorFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsSaveConfiguratorFieldsRequest from a JSON string
generic_listings_save_configurator_fields_request_instance = GenericListingsSaveConfiguratorFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsSaveConfiguratorFieldsRequest.to_json())

# convert the object into a dict
generic_listings_save_configurator_fields_request_dict = generic_listings_save_configurator_fields_request_instance.to_dict()
# create an instance of GenericListingsSaveConfiguratorFieldsRequest from a dict
generic_listings_save_configurator_fields_request_from_dict = GenericListingsSaveConfiguratorFieldsRequest.from_dict(generic_listings_save_configurator_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


