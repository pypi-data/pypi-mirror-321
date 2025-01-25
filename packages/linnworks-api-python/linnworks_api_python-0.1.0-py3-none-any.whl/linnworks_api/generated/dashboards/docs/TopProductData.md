# TopProductData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_num** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**cost** | **float** |  | [optional] 
**title** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.dashboards.models.top_product_data import TopProductData

# TODO update the JSON string below
json = "{}"
# create an instance of TopProductData from a JSON string
top_product_data_instance = TopProductData.from_json(json)
# print the JSON string representation of the object
print(TopProductData.to_json())

# convert the object into a dict
top_product_data_dict = top_product_data_instance.to_dict()
# create an instance of TopProductData from a dict
top_product_data_from_dict = TopProductData.from_dict(top_product_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


