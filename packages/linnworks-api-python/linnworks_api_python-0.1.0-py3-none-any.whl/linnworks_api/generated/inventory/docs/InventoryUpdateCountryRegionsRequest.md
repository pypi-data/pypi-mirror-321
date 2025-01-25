# InventoryUpdateCountryRegionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdateCountryRegionsRequest**](UpdateCountryRegionsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_country_regions_request import InventoryUpdateCountryRegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateCountryRegionsRequest from a JSON string
inventory_update_country_regions_request_instance = InventoryUpdateCountryRegionsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateCountryRegionsRequest.to_json())

# convert the object into a dict
inventory_update_country_regions_request_dict = inventory_update_country_regions_request_instance.to_dict()
# create an instance of InventoryUpdateCountryRegionsRequest from a dict
inventory_update_country_regions_request_from_dict = InventoryUpdateCountryRegionsRequest.from_dict(inventory_update_country_regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


