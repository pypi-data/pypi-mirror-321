# WarehouseTOTE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tote_id** | **int** |  | [optional] 
**tote_barcode** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.warehouse_tote import WarehouseTOTE

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTOTE from a JSON string
warehouse_tote_instance = WarehouseTOTE.from_json(json)
# print the JSON string representation of the object
print(WarehouseTOTE.to_json())

# convert the object into a dict
warehouse_tote_dict = warehouse_tote_instance.to_dict()
# create an instance of WarehouseTOTE from a dict
warehouse_tote_from_dict = WarehouseTOTE.from_dict(warehouse_tote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


