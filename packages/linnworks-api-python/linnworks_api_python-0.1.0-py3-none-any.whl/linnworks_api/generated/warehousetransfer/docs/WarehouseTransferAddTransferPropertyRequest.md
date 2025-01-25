# WarehouseTransferAddTransferPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_transfer_id** | **str** | The transfer to add the property to. | [optional] 
**property_name** | **str** | The property name. | [optional] 
**property_value** | **str** | The property value. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_add_transfer_property_request import WarehouseTransferAddTransferPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferAddTransferPropertyRequest from a JSON string
warehouse_transfer_add_transfer_property_request_instance = WarehouseTransferAddTransferPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferAddTransferPropertyRequest.to_json())

# convert the object into a dict
warehouse_transfer_add_transfer_property_request_dict = warehouse_transfer_add_transfer_property_request_instance.to_dict()
# create an instance of WarehouseTransferAddTransferPropertyRequest from a dict
warehouse_transfer_add_transfer_property_request_from_dict = WarehouseTransferAddTransferPropertyRequest.from_dict(warehouse_transfer_add_transfer_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


