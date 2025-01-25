# GenericListingsDeleteConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeleteConfiguratorsRequest**](DeleteConfiguratorsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_delete_configurators_request import GenericListingsDeleteConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsDeleteConfiguratorsRequest from a JSON string
generic_listings_delete_configurators_request_instance = GenericListingsDeleteConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsDeleteConfiguratorsRequest.to_json())

# convert the object into a dict
generic_listings_delete_configurators_request_dict = generic_listings_delete_configurators_request_instance.to_dict()
# create an instance of GenericListingsDeleteConfiguratorsRequest from a dict
generic_listings_delete_configurators_request_from_dict = GenericListingsDeleteConfiguratorsRequest.from_dict(generic_listings_delete_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


