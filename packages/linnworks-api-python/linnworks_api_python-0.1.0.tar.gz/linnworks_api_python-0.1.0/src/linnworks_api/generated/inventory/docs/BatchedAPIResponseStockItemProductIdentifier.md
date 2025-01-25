# BatchedAPIResponseStockItemProductIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[APIResultResponseStockItemProductIdentifier]**](APIResultResponseStockItemProductIdentifier.md) |  | [optional] 
**total_results** | **int** |  | [optional] [readonly] 
**result_status** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.batched_api_response_stock_item_product_identifier import BatchedAPIResponseStockItemProductIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of BatchedAPIResponseStockItemProductIdentifier from a JSON string
batched_api_response_stock_item_product_identifier_instance = BatchedAPIResponseStockItemProductIdentifier.from_json(json)
# print the JSON string representation of the object
print(BatchedAPIResponseStockItemProductIdentifier.to_json())

# convert the object into a dict
batched_api_response_stock_item_product_identifier_dict = batched_api_response_stock_item_product_identifier_instance.to_dict()
# create an instance of BatchedAPIResponseStockItemProductIdentifier from a dict
batched_api_response_stock_item_product_identifier_from_dict = BatchedAPIResponseStockItemProductIdentifier.from_dict(batched_api_response_stock_item_product_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


