# GenericListingsGetConfiguratorDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetConfiguratorDataRequest**](GetConfiguratorDataRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_get_configurator_data_request import GenericListingsGetConfiguratorDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsGetConfiguratorDataRequest from a JSON string
generic_listings_get_configurator_data_request_instance = GenericListingsGetConfiguratorDataRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsGetConfiguratorDataRequest.to_json())

# convert the object into a dict
generic_listings_get_configurator_data_request_dict = generic_listings_get_configurator_data_request_instance.to_dict()
# create an instance of GenericListingsGetConfiguratorDataRequest from a dict
generic_listings_get_configurator_data_request_from_dict = GenericListingsGetConfiguratorDataRequest.from_dict(generic_listings_get_configurator_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


