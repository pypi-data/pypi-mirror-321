# GetItemBinracksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_locations** | [**List[StockItemBatch]**](StockItemBatch.md) | A list of other batches that are available in the given linnworks stock location | [optional] 
**pickable_bins** | [**List[BinRackStockItem]**](BinRackStockItem.md) | A list of stock that is available to pick from | [optional] 
**non_pickable_bins** | [**List[BinRackStockItem]**](BinRackStockItem.md) | A list of stock that cannot directly be picked from | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.get_item_binracks_response import GetItemBinracksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetItemBinracksResponse from a JSON string
get_item_binracks_response_instance = GetItemBinracksResponse.from_json(json)
# print the JSON string representation of the object
print(GetItemBinracksResponse.to_json())

# convert the object into a dict
get_item_binracks_response_dict = get_item_binracks_response_instance.to_dict()
# create an instance of GetItemBinracksResponse from a dict
get_item_binracks_response_from_dict = GetItemBinracksResponse.from_dict(get_item_binracks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


