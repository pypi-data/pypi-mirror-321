# GenericListingsOpenTemplatesByInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**OpenTemplatesByInventoryRequest**](OpenTemplatesByInventoryRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_open_templates_by_inventory_request import GenericListingsOpenTemplatesByInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsOpenTemplatesByInventoryRequest from a JSON string
generic_listings_open_templates_by_inventory_request_instance = GenericListingsOpenTemplatesByInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsOpenTemplatesByInventoryRequest.to_json())

# convert the object into a dict
generic_listings_open_templates_by_inventory_request_dict = generic_listings_open_templates_by_inventory_request_instance.to_dict()
# create an instance of GenericListingsOpenTemplatesByInventoryRequest from a dict
generic_listings_open_templates_by_inventory_request_from_dict = GenericListingsOpenTemplatesByInventoryRequest.from_dict(generic_listings_open_templates_by_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


