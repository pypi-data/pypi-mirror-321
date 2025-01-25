# GenericListingsSaveConfiguratorDescriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SaveConfiguratorDescriptionRequest**](SaveConfiguratorDescriptionRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_save_configurator_description_request import GenericListingsSaveConfiguratorDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsSaveConfiguratorDescriptionRequest from a JSON string
generic_listings_save_configurator_description_request_instance = GenericListingsSaveConfiguratorDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsSaveConfiguratorDescriptionRequest.to_json())

# convert the object into a dict
generic_listings_save_configurator_description_request_dict = generic_listings_save_configurator_description_request_instance.to_dict()
# create an instance of GenericListingsSaveConfiguratorDescriptionRequest from a dict
generic_listings_save_configurator_description_request_from_dict = GenericListingsSaveConfiguratorDescriptionRequest.from_dict(generic_listings_save_configurator_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


