# CreatePurchaseOrderInitialParameter

Class that represents entry parameters for creating new PENDING purchase order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_supplier_id** | **str** | Supplier unique identifier. Use Inventory/GetSupplierList to get the supplier ids | [optional] 
**fk_location_id** | **str** | Location id where the PO will be delivered to. Use Inventory/GetStockLocations to get the location ids | [optional] 
**external_invoice_number** | **str** | Purchase order reference | [optional] 
**currency** | **str** | Currency of the purchase order | [optional] 
**supplier_reference_number** | **str** | Supplier purchase order reference number | [optional] 
**unit_amount_tax_included_type** | **int** | Unit amount includes,excludes or no tax. 0 - Excludes Tax, 1 - Includes tax, 2 - No Tax | [optional] 
**date_of_purchase** | **datetime** | DateTime of the purchase order | [optional] 
**quoted_delivery_date** | **datetime** | DateTime of the expected delivery date. | [optional] 
**postage_paid** | **float** | **DEPRECIATED**   Use additional costs with Shipping flag to record shipping costs. This field remains available in the API for backward compatibility and acts pretty much like an additional cost item with type | [optional] 
**shipping_tax_rate** | **float** | **DEPRECIATED**   Use additional costs with Shipping flag to record shipping costs. This field remains available in the API for backward compatibility and acts pretty much like an additional cost item with type | [optional] 
**conversion_rate** | **float** | Currency conversion rate, multiplier to change the purchase order currency into the system currecny | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.create_purchase_order_initial_parameter import CreatePurchaseOrderInitialParameter

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePurchaseOrderInitialParameter from a JSON string
create_purchase_order_initial_parameter_instance = CreatePurchaseOrderInitialParameter.from_json(json)
# print the JSON string representation of the object
print(CreatePurchaseOrderInitialParameter.to_json())

# convert the object into a dict
create_purchase_order_initial_parameter_dict = create_purchase_order_initial_parameter_instance.to_dict()
# create an instance of CreatePurchaseOrderInitialParameter from a dict
create_purchase_order_initial_parameter_from_dict = CreatePurchaseOrderInitialParameter.from_dict(create_purchase_order_initial_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


