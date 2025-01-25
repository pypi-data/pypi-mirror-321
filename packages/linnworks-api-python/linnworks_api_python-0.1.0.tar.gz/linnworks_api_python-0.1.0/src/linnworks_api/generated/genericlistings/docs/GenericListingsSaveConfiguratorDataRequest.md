# GenericListingsSaveConfiguratorDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SaveConfiguratorDataRequest**](SaveConfiguratorDataRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_save_configurator_data_request import GenericListingsSaveConfiguratorDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsSaveConfiguratorDataRequest from a JSON string
generic_listings_save_configurator_data_request_instance = GenericListingsSaveConfiguratorDataRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsSaveConfiguratorDataRequest.to_json())

# convert the object into a dict
generic_listings_save_configurator_data_request_dict = generic_listings_save_configurator_data_request_instance.to_dict()
# create an instance of GenericListingsSaveConfiguratorDataRequest from a dict
generic_listings_save_configurator_data_request_from_dict = GenericListingsSaveConfiguratorDataRequest.from_dict(generic_listings_save_configurator_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


