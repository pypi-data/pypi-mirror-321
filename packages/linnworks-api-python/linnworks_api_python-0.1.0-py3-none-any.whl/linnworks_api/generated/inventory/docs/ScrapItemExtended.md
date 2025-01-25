# ScrapItemExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_scrap_id** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**fk_stock_item_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**scrap_category** | **str** |  | [optional] 
**scrap_reason** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.scrap_item_extended import ScrapItemExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapItemExtended from a JSON string
scrap_item_extended_instance = ScrapItemExtended.from_json(json)
# print the JSON string representation of the object
print(ScrapItemExtended.to_json())

# convert the object into a dict
scrap_item_extended_dict = scrap_item_extended_instance.to_dict()
# create an instance of ScrapItemExtended from a dict
scrap_item_extended_from_dict = ScrapItemExtended.from_dict(scrap_item_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


