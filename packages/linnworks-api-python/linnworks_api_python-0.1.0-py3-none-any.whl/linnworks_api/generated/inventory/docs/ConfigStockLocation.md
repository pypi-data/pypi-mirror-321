# ConfigStockLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_stock_location_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**fk_channel_location_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.config_stock_location import ConfigStockLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigStockLocation from a JSON string
config_stock_location_instance = ConfigStockLocation.from_json(json)
# print the JSON string representation of the object
print(ConfigStockLocation.to_json())

# convert the object into a dict
config_stock_location_dict = config_stock_location_instance.to_dict()
# create an instance of ConfigStockLocation from a dict
config_stock_location_from_dict = ConfigStockLocation.from_dict(config_stock_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


