# GetProductIdentifiersBulkByStockItemIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_product_identifiers_bulk_by_stock_item_id_request import GetProductIdentifiersBulkByStockItemIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductIdentifiersBulkByStockItemIdRequest from a JSON string
get_product_identifiers_bulk_by_stock_item_id_request_instance = GetProductIdentifiersBulkByStockItemIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetProductIdentifiersBulkByStockItemIdRequest.to_json())

# convert the object into a dict
get_product_identifiers_bulk_by_stock_item_id_request_dict = get_product_identifiers_bulk_by_stock_item_id_request_instance.to_dict()
# create an instance of GetProductIdentifiersBulkByStockItemIdRequest from a dict
get_product_identifiers_bulk_by_stock_item_id_request_from_dict = GetProductIdentifiersBulkByStockItemIdRequest.from_dict(get_product_identifiers_bulk_by_stock_item_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


