# WarehouseBinRackItemsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_rack_id** | **int** |  | [optional] 
**number_of_items** | **int** |  | [optional] 
**total_quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.warehouse_bin_rack_items_info import WarehouseBinRackItemsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBinRackItemsInfo from a JSON string
warehouse_bin_rack_items_info_instance = WarehouseBinRackItemsInfo.from_json(json)
# print the JSON string representation of the object
print(WarehouseBinRackItemsInfo.to_json())

# convert the object into a dict
warehouse_bin_rack_items_info_dict = warehouse_bin_rack_items_info_instance.to_dict()
# create an instance of WarehouseBinRackItemsInfo from a dict
warehouse_bin_rack_items_info_from_dict = WarehouseBinRackItemsInfo.from_dict(warehouse_bin_rack_items_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


