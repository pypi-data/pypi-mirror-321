# CommonPurchaseOrderHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** |  | [optional] 
**fk_supplier_id** | **str** |  | [optional] 
**fk_location_id** | **str** |  | [optional] 
**external_invoice_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**supplier_reference_number** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**unit_amount_tax_included_type** | **int** |  | [optional] 
**line_count** | **int** |  | [optional] 
**delivered_lines_count** | **int** |  | [optional] 
**date_of_purchase** | **datetime** |  | [optional] 
**date_of_delivery** | **datetime** |  | [optional] 
**quoted_delivery_date** | **datetime** |  | [optional] 
**postage_paid** | **float** |  | [optional] 
**total_cost** | **float** |  | [optional] 
**tax_paid** | **float** |  | [optional] 
**shipping_tax_rate** | **float** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**converted_shipping_cost** | **float** |  | [optional] 
**converted_shipping_tax** | **float** |  | [optional] 
**converted_other_cost** | **float** |  | [optional] 
**converted_other_tax** | **float** |  | [optional] 
**converted_grand_total** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.common_purchase_order_header import CommonPurchaseOrderHeader

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPurchaseOrderHeader from a JSON string
common_purchase_order_header_instance = CommonPurchaseOrderHeader.from_json(json)
# print the JSON string representation of the object
print(CommonPurchaseOrderHeader.to_json())

# convert the object into a dict
common_purchase_order_header_dict = common_purchase_order_header_instance.to_dict()
# create an instance of CommonPurchaseOrderHeader from a dict
common_purchase_order_header_from_dict = CommonPurchaseOrderHeader.from_dict(common_purchase_order_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


