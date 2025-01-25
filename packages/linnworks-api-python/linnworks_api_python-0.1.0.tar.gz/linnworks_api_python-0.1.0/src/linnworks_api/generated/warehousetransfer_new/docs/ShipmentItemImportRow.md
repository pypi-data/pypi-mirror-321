# ShipmentItemImportRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ImportProductColumn**](ImportProductColumn.md) |  | [optional] 
**name** | **str** |  | [optional] 
**sample** | **str** |  | [optional] 
**group** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_item_import_row import ShipmentItemImportRow

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItemImportRow from a JSON string
shipment_item_import_row_instance = ShipmentItemImportRow.from_json(json)
# print the JSON string representation of the object
print(ShipmentItemImportRow.to_json())

# convert the object into a dict
shipment_item_import_row_dict = shipment_item_import_row_instance.to_dict()
# create an instance of ShipmentItemImportRow from a dict
shipment_item_import_row_from_dict = ShipmentItemImportRow.from_dict(shipment_item_import_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


