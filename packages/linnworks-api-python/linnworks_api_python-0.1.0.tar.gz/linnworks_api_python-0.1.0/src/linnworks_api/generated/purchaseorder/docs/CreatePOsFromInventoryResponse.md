# CreatePOsFromInventoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_orders** | [**Dict[str, TupleGuidString]**](TupleGuidString.md) | A dictionary where the key is supplier Id and the tuple represents the purchase order id and the external invoice number for that PO | [optional] 
**skipped_stock_items** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.create_pos_from_inventory_response import CreatePOsFromInventoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePOsFromInventoryResponse from a JSON string
create_pos_from_inventory_response_instance = CreatePOsFromInventoryResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePOsFromInventoryResponse.to_json())

# convert the object into a dict
create_pos_from_inventory_response_dict = create_pos_from_inventory_response_instance.to_dict()
# create an instance of CreatePOsFromInventoryResponse from a dict
create_pos_from_inventory_response_from_dict = CreatePOsFromInventoryResponse.from_dict(create_pos_from_inventory_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


