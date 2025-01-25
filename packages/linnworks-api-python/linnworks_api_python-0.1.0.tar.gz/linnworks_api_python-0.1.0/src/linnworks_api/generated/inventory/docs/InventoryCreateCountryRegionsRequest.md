# InventoryCreateCountryRegionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CreateCountryRegionsRequest**](CreateCountryRegionsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_country_regions_request import InventoryCreateCountryRegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateCountryRegionsRequest from a JSON string
inventory_create_country_regions_request_instance = InventoryCreateCountryRegionsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateCountryRegionsRequest.to_json())

# convert the object into a dict
inventory_create_country_regions_request_dict = inventory_create_country_regions_request_instance.to_dict()
# create an instance of InventoryCreateCountryRegionsRequest from a dict
inventory_create_country_regions_request_from_dict = InventoryCreateCountryRegionsRequest.from_dict(inventory_create_country_regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


