# GetStockItemIdsBySKURequest

Get stock itemids by sku request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skus** | **List[str]** | List of SKU&#39;s to search for | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_stock_item_ids_by_sku_request import GetStockItemIdsBySKURequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemIdsBySKURequest from a JSON string
get_stock_item_ids_by_sku_request_instance = GetStockItemIdsBySKURequest.from_json(json)
# print the JSON string representation of the object
print(GetStockItemIdsBySKURequest.to_json())

# convert the object into a dict
get_stock_item_ids_by_sku_request_dict = get_stock_item_ids_by_sku_request_instance.to_dict()
# create an instance of GetStockItemIdsBySKURequest from a dict
get_stock_item_ids_by_sku_request_from_dict = GetStockItemIdsBySKURequest.from_dict(get_stock_item_ids_by_sku_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


