# UpdateAdditionalCostItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_additional_cost_item_id** | **int** | Additional cost line row id, uniquely identifying each cost line | [optional] 
**id** | **str** | Each item in the request can have unique Id supplied (uniqueidentifier) this Id will be returned to you in the response so you can match request item with the response | [optional] 
**additional_cost_type_id** | **int** |  | [optional] 
**reference** | **str** | Additional cost reference | [optional] 
**sub_total_line_cost** | **float** | Line Subtotal (Total less tax) | [optional] 
**tax_rate** | **float** | Tax rate | [optional] 
**currency** | **str** | Currency code | [optional] 
**conversion_rate** | **float** | Conversion rate from system currency, i.e. system currency rate to additional cost currency. For example if your system currency is GBP and additional cost is in USD the converted value is USD / Rate, example calculation, Rate 1.27, Additional cost total is 100, converted value &#x3D; 100 USD / 1.27 &#x3D; 78.98 GBP | [optional] 
**allocation_locked** | **bool** | If this flag is set, new items added to PO will not be part of the allocation cost | [optional] 
**var_print** | **bool** | Indicate if the type will appear on prints and emaisl | [optional] 
**allocation_method** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_additional_cost_item import UpdateAdditionalCostItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdditionalCostItem from a JSON string
update_additional_cost_item_instance = UpdateAdditionalCostItem.from_json(json)
# print the JSON string representation of the object
print(UpdateAdditionalCostItem.to_json())

# convert the object into a dict
update_additional_cost_item_dict = update_additional_cost_item_instance.to_dict()
# create an instance of UpdateAdditionalCostItem from a dict
update_additional_cost_item_from_dict = UpdateAdditionalCostItem.from_dict(update_additional_cost_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


