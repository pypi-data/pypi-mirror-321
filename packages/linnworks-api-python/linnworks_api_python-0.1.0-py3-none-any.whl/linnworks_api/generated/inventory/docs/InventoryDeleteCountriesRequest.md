# InventoryDeleteCountriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries_ids** | **List[str]** | Ids of countries to delete | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_countries_request import InventoryDeleteCountriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteCountriesRequest from a JSON string
inventory_delete_countries_request_instance = InventoryDeleteCountriesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteCountriesRequest.to_json())

# convert the object into a dict
inventory_delete_countries_request_dict = inventory_delete_countries_request_instance.to_dict()
# create an instance of InventoryDeleteCountriesRequest from a dict
inventory_delete_countries_request_from_dict = InventoryDeleteCountriesRequest.from_dict(inventory_delete_countries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


