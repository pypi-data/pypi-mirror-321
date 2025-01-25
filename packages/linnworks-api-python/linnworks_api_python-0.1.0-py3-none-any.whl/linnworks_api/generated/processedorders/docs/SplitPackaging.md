# SplitPackaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_bin_id** | **str** |  | [optional] 
**fk_order_item_row_id** | **str** |  | [optional] 
**package_title** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**weight** | **float** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**bin_index** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.split_packaging import SplitPackaging

# TODO update the JSON string below
json = "{}"
# create an instance of SplitPackaging from a JSON string
split_packaging_instance = SplitPackaging.from_json(json)
# print the JSON string representation of the object
print(SplitPackaging.to_json())

# convert the object into a dict
split_packaging_dict = split_packaging_instance.to_dict()
# create an instance of SplitPackaging from a dict
split_packaging_from_dict = SplitPackaging.from_dict(split_packaging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


