# ShipmentItemsImportMetaFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv_separator_mappings** | [**List[CsvSeparator]**](CsvSeparator.md) |  | [optional] 
**shipment_item_rows** | [**List[ShipmentItemImportRow]**](ShipmentItemImportRow.md) |  | [optional] 
**stock_request_item_rows** | [**List[StockRequestItemImportRow]**](StockRequestItemImportRow.md) |  | [optional] 
**stock_transfer_item_rows** | [**List[StockTransferItemImportRow]**](StockTransferItemImportRow.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_items_import_meta_fields import ShipmentItemsImportMetaFields

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItemsImportMetaFields from a JSON string
shipment_items_import_meta_fields_instance = ShipmentItemsImportMetaFields.from_json(json)
# print the JSON string representation of the object
print(ShipmentItemsImportMetaFields.to_json())

# convert the object into a dict
shipment_items_import_meta_fields_dict = shipment_items_import_meta_fields_instance.to_dict()
# create an instance of ShipmentItemsImportMetaFields from a dict
shipment_items_import_meta_fields_from_dict = ShipmentItemsImportMetaFields.from_dict(shipment_items_import_meta_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


