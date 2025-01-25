# WarehouseTransferProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_property_id** | **str** |  | [optional] 
**transfer_property_name** | **str** |  | [optional] 
**transfer_property_value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_property import WarehouseTransferProperty

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferProperty from a JSON string
warehouse_transfer_property_instance = WarehouseTransferProperty.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferProperty.to_json())

# convert the object into a dict
warehouse_transfer_property_dict = warehouse_transfer_property_instance.to_dict()
# create an instance of WarehouseTransferProperty from a dict
warehouse_transfer_property_from_dict = WarehouseTransferProperty.from_dict(warehouse_transfer_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


