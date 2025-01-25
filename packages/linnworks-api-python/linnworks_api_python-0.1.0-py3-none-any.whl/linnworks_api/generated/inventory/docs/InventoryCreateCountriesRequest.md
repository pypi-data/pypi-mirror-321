# InventoryCreateCountriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | [**List[Country]**](Country.md) | Countries to create | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_countries_request import InventoryCreateCountriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateCountriesRequest from a JSON string
inventory_create_countries_request_instance = InventoryCreateCountriesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateCountriesRequest.to_json())

# convert the object into a dict
inventory_create_countries_request_dict = inventory_create_countries_request_instance.to_dict()
# create an instance of InventoryCreateCountriesRequest from a dict
inventory_create_countries_request_from_dict = InventoryCreateCountriesRequest.from_dict(inventory_create_countries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


