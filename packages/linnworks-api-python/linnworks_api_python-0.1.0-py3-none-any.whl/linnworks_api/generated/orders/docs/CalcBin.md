# CalcBin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_bin_id** | **str** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**label_id** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**print_date** | **datetime** |  | [optional] 
**cost** | **float** |  | [optional] 
**fk_packaging_type_id** | **str** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**packaging_weight** | **float** |  | [optional] 
**item_weight** | **float** |  | [optional] 
**manual_adjust** | **bool** |  | [optional] 
**items** | [**List[CalcBinItem]**](CalcBinItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.calc_bin import CalcBin

# TODO update the JSON string below
json = "{}"
# create an instance of CalcBin from a JSON string
calc_bin_instance = CalcBin.from_json(json)
# print the JSON string representation of the object
print(CalcBin.to_json())

# convert the object into a dict
calc_bin_dict = calc_bin_instance.to_dict()
# create an instance of CalcBin from a dict
calc_bin_from_dict = CalcBin.from_dict(calc_bin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


