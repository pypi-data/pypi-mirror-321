# CalcOrderHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 
**n_order_id** | **int** |  | [optional] 
**fk_postal_service_id** | **str** |  | [optional] 
**fk_country_id** | **str** |  | [optional] 
**c_country** | **str** |  | [optional] 
**item_weight** | **float** |  | [optional] 
**fk_packaging_group_id** | **str** |  | [optional] 
**fk_packaging_type_id** | **str** |  | [optional] 
**is_split_packaging** | **bool** |  | [optional] [readonly] 
**packaging_weight** | **float** |  | [optional] 
**total_weight** | **float** |  | [optional] 
**total_width** | **float** |  | [optional] 
**total_height** | **float** |  | [optional] 
**total_depth** | **float** |  | [optional] 
**manual_adjust** | **bool** |  | [optional] 
**can_auto_split** | **bool** |  | [optional] [readonly] 
**is_auto_split** | **bool** |  | [optional] 
**split_package_count** | **int** |  | [optional] 
**label_printed** | **bool** |  | [optional] 
**calculation_hints** | **List[str]** |  | [optional] 
**items** | [**List[CalcOrderItem]**](CalcOrderItem.md) |  | [optional] 
**bins** | [**List[CalcBin]**](CalcBin.md) |  | [optional] 
**three_dim_packaging** | [**PackingResult**](PackingResult.md) |  | [optional] 
**dim_method** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.calc_order_header import CalcOrderHeader

# TODO update the JSON string below
json = "{}"
# create an instance of CalcOrderHeader from a JSON string
calc_order_header_instance = CalcOrderHeader.from_json(json)
# print the JSON string representation of the object
print(CalcOrderHeader.to_json())

# convert the object into a dict
calc_order_header_dict = calc_order_header_instance.to_dict()
# create an instance of CalcOrderHeader from a dict
calc_order_header_from_dict = CalcOrderHeader.from_dict(calc_order_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


