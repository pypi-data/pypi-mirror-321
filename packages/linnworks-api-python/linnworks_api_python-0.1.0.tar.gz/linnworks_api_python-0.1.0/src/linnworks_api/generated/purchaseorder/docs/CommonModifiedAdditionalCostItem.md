# CommonModifiedAdditionalCostItem

Newly added purchase additional cost item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Each item in the request can have unique Id supplied (uniqueidentifier) this Id will be returned to you in the response so you can match request item with the response | [optional] 
**purchase_additional_cost_item_id** | **int** |  | [optional] 
**additional_cost_type_id** | **int** |  | [optional] 
**reference** | **str** |  | [optional] 
**sub_total_line_cost** | **float** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**total_line_cost** | **float** |  | [optional] 
**cost_allocation** | [**List[CommonPurchaseOrderAdditionalCostAllocation]**](CommonPurchaseOrderAdditionalCostAllocation.md) |  | [optional] 
**allocation_locked** | **bool** |  | [optional] 
**additional_cost_type_name** | **str** |  | [optional] 
**additional_cost_type_is_shipping_type** | **bool** |  | [optional] 
**additional_cost_type_is_partial_allocation** | **bool** |  | [optional] 
**var_print** | **bool** |  | [optional] 
**allocation_method** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.common_modified_additional_cost_item import CommonModifiedAdditionalCostItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommonModifiedAdditionalCostItem from a JSON string
common_modified_additional_cost_item_instance = CommonModifiedAdditionalCostItem.from_json(json)
# print the JSON string representation of the object
print(CommonModifiedAdditionalCostItem.to_json())

# convert the object into a dict
common_modified_additional_cost_item_dict = common_modified_additional_cost_item_instance.to_dict()
# create an instance of CommonModifiedAdditionalCostItem from a dict
common_modified_additional_cost_item_from_dict = CommonModifiedAdditionalCostItem.from_dict(common_modified_additional_cost_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


