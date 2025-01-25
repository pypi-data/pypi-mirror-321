# WarehouseLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_name** | **str** |  | [optional] 
**pk_stock_location_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.warehouse_location import WarehouseLocation

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseLocation from a JSON string
warehouse_location_instance = WarehouseLocation.from_json(json)
# print the JSON string representation of the object
print(WarehouseLocation.to_json())

# convert the object into a dict
warehouse_location_dict = warehouse_location_instance.to_dict()
# create an instance of WarehouseLocation from a dict
warehouse_location_from_dict = WarehouseLocation.from_dict(warehouse_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


