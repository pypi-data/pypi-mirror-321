# GenericListingsCreateTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CreateTemplatesRequest**](CreateTemplatesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_create_templates_request import GenericListingsCreateTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsCreateTemplatesRequest from a JSON string
generic_listings_create_templates_request_instance = GenericListingsCreateTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsCreateTemplatesRequest.to_json())

# convert the object into a dict
generic_listings_create_templates_request_dict = generic_listings_create_templates_request_instance.to_dict()
# create an instance of GenericListingsCreateTemplatesRequest from a dict
generic_listings_create_templates_request_from_dict = GenericListingsCreateTemplatesRequest.from_dict(generic_listings_create_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


