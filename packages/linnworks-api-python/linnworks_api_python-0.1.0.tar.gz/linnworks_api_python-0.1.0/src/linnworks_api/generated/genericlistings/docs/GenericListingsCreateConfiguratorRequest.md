# GenericListingsCreateConfiguratorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CreateConfiguratorRequest**](CreateConfiguratorRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_create_configurator_request import GenericListingsCreateConfiguratorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsCreateConfiguratorRequest from a JSON string
generic_listings_create_configurator_request_instance = GenericListingsCreateConfiguratorRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsCreateConfiguratorRequest.to_json())

# convert the object into a dict
generic_listings_create_configurator_request_dict = generic_listings_create_configurator_request_instance.to_dict()
# create an instance of GenericListingsCreateConfiguratorRequest from a dict
generic_listings_create_configurator_request_from_dict = GenericListingsCreateConfiguratorRequest.from_dict(generic_listings_create_configurator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


