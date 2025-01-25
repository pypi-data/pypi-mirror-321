# ConfigStockLocationBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**List[ConfigStockLocation]**](ConfigStockLocation.md) |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_stock_location_binding import ConfigStockLocationBinding

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigStockLocationBinding from a JSON string
config_stock_location_binding_instance = ConfigStockLocationBinding.from_json(json)
# print the JSON string representation of the object
print(ConfigStockLocationBinding.to_json())

# convert the object into a dict
config_stock_location_binding_dict = config_stock_location_binding_instance.to_dict()
# create an instance of ConfigStockLocationBinding from a dict
config_stock_location_binding_from_dict = ConfigStockLocationBinding.from_dict(config_stock_location_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


