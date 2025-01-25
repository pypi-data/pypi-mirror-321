# StockItemBoxConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_id** | **int** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**box_name** | **str** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**length** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**value_percentage** | **float** |  | [optional] 
**barcode** | **str** |  | [optional] 
**packaging_type_id** | **str** |  | [optional] 
**logical_delete** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.stock_item_box_configuration import StockItemBoxConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemBoxConfiguration from a JSON string
stock_item_box_configuration_instance = StockItemBoxConfiguration.from_json(json)
# print the JSON string representation of the object
print(StockItemBoxConfiguration.to_json())

# convert the object into a dict
stock_item_box_configuration_dict = stock_item_box_configuration_instance.to_dict()
# create an instance of StockItemBoxConfiguration from a dict
stock_item_box_configuration_from_dict = StockItemBoxConfiguration.from_dict(stock_item_box_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


