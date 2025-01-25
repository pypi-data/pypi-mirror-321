# ModifyAdditionalCostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_to_add** | [**List[AddAdditionalCostItem]**](AddAdditionalCostItem.md) | list of additional cost items to add. Each item has Id which will be returned to you to match the item you are adding to array on your side | [optional] 
**items_to_update** | [**List[UpdateAdditionalCostItem]**](UpdateAdditionalCostItem.md) | List of items to update. Each line is identified by | [optional] 
**items_to_delete** | **List[int]** | List of items to delete, provide list of PurchaseAdditionalCostItemId&#39;s | [optional] 
**purchase_id** | **str** | Purchase order id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modify_additional_cost_request import ModifyAdditionalCostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyAdditionalCostRequest from a JSON string
modify_additional_cost_request_instance = ModifyAdditionalCostRequest.from_json(json)
# print the JSON string representation of the object
print(ModifyAdditionalCostRequest.to_json())

# convert the object into a dict
modify_additional_cost_request_dict = modify_additional_cost_request_instance.to_dict()
# create an instance of ModifyAdditionalCostRequest from a dict
modify_additional_cost_request_from_dict = ModifyAdditionalCostRequest.from_dict(modify_additional_cost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


