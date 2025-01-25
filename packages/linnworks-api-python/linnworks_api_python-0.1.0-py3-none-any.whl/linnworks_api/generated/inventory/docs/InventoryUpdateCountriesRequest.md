# InventoryUpdateCountriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | [**List[Country]**](Country.md) | Countries to udpate | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_countries_request import InventoryUpdateCountriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateCountriesRequest from a JSON string
inventory_update_countries_request_instance = InventoryUpdateCountriesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateCountriesRequest.to_json())

# convert the object into a dict
inventory_update_countries_request_dict = inventory_update_countries_request_instance.to_dict()
# create an instance of InventoryUpdateCountriesRequest from a dict
inventory_update_countries_request_from_dict = InventoryUpdateCountriesRequest.from_dict(inventory_update_countries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


