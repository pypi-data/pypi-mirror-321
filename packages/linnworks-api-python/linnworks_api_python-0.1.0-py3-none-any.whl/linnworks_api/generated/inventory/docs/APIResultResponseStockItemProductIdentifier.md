# APIResultResponseStockItemProductIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**StockItemProductIdentifier**](StockItemProductIdentifier.md) |  | [optional] 
**result_status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.api_result_response_stock_item_product_identifier import APIResultResponseStockItemProductIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of APIResultResponseStockItemProductIdentifier from a JSON string
api_result_response_stock_item_product_identifier_instance = APIResultResponseStockItemProductIdentifier.from_json(json)
# print the JSON string representation of the object
print(APIResultResponseStockItemProductIdentifier.to_json())

# convert the object into a dict
api_result_response_stock_item_product_identifier_dict = api_result_response_stock_item_product_identifier_instance.to_dict()
# create an instance of APIResultResponseStockItemProductIdentifier from a dict
api_result_response_stock_item_product_identifier_from_dict = APIResultResponseStockItemProductIdentifier.from_dict(api_result_response_stock_item_product_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


