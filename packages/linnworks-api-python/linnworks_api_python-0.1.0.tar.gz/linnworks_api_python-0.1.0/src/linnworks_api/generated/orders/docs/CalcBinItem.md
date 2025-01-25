# CalcBinItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_order_item_id** | **int** |  | [optional] 
**bin_id** | **str** |  | [optional] 
**fk_order_item_id** | **str** |  | [optional] 
**box_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.calc_bin_item import CalcBinItem

# TODO update the JSON string below
json = "{}"
# create an instance of CalcBinItem from a JSON string
calc_bin_item_instance = CalcBinItem.from_json(json)
# print the JSON string representation of the object
print(CalcBinItem.to_json())

# convert the object into a dict
calc_bin_item_dict = calc_bin_item_instance.to_dict()
# create an instance of CalcBinItem from a dict
calc_bin_item_from_dict = CalcBinItem.from_dict(calc_bin_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


