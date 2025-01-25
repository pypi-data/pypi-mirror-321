# GetProductIdentifiersByStockItemIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_identifiers** | [**List[StockItemProductIdentifier]**](StockItemProductIdentifier.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_product_identifiers_by_stock_item_id_response import GetProductIdentifiersByStockItemIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductIdentifiersByStockItemIdResponse from a JSON string
get_product_identifiers_by_stock_item_id_response_instance = GetProductIdentifiersByStockItemIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetProductIdentifiersByStockItemIdResponse.to_json())

# convert the object into a dict
get_product_identifiers_by_stock_item_id_response_dict = get_product_identifiers_by_stock_item_id_response_instance.to_dict()
# create an instance of GetProductIdentifiersByStockItemIdResponse from a dict
get_product_identifiers_by_stock_item_id_response_from_dict = GetProductIdentifiersByStockItemIdResponse.from_dict(get_product_identifiers_by_stock_item_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


