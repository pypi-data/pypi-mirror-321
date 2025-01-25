# BinrackSkuResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skus** | [**List[StockItemBatch]**](StockItemBatch.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.binrack_sku_response import BinrackSkuResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BinrackSkuResponse from a JSON string
binrack_sku_response_instance = BinrackSkuResponse.from_json(json)
# print the JSON string representation of the object
print(BinrackSkuResponse.to_json())

# convert the object into a dict
binrack_sku_response_dict = binrack_sku_response_instance.to_dict()
# create an instance of BinrackSkuResponse from a dict
binrack_sku_response_from_dict = BinrackSkuResponse.from_dict(binrack_sku_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


