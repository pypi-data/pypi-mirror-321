# StockSearchBinracksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SearchBinracksRequest**](SearchBinracksRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_search_binracks_request import StockSearchBinracksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockSearchBinracksRequest from a JSON string
stock_search_binracks_request_instance = StockSearchBinracksRequest.from_json(json)
# print the JSON string representation of the object
print(StockSearchBinracksRequest.to_json())

# convert the object into a dict
stock_search_binracks_request_dict = stock_search_binracks_request_instance.to_dict()
# create an instance of StockSearchBinracksRequest from a dict
stock_search_binracks_request_from_dict = StockSearchBinracksRequest.from_dict(stock_search_binracks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


