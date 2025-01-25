# UpdatePurchaseOrderHeaderParameter

Change purchase order status. You can change from PENDING to OPEN, from OPEN to DELIVERED, from PARTIAL to DELIVERED

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Unique identifier for the purchase order. You have to use this ID for all updates to the PO | [optional] 
**supplier_reference_number** | **str** | Supplier reference number for the purchase order | [optional] 
**fk_location_id** | **str** | Unique idenfidier of the location where the PO is expected to be delivered to. Empty Guid is default location. Use Locations API methods to get the names and additional details for the locations | [optional] 
**fk_supplier_id** | **str** | Unique identifier for the supplier. Empty Guid is default supplier. Otherwise use Supplier API to get the names and additional data for the supplier | [optional] 
**currency** | **str** | Currency of the values in the purchase order | [optional] 
**external_invoice_number** | **str** | Purchase order reference | [optional] 
**unit_amount_tax_included_type** | **int** | Unit amount includes,excludes or no tax. 0 - Excludes Tax, 1 - Includes tax, 2 - No Tax. Nullable if null, the value not updated | [optional] 
**date_of_purchase** | **datetime** | DateTime of the purchase order delivered, will be set to DateOfPurchase until the PO is fully delivered UTC | [optional] 
**quoted_delivery_date** | **datetime** | DateTime of the purchase order quoted/expected delivery date UTC | [optional] 
**shipping_tax_rate** | **float** | **DEPRECIATED**   Use additional costs with Shipping flag to record shipping costs. This field remains available in the API for backward compatibility and acts pretty much like an additional cost item with type | [optional] 
**conversion_rate** | **float** | Conversion rate of the purchase order currency. When PO is delivered Stock Value will be multipled by this conversion rate. For example if your system currency is GBP and Purchase order is in EUR the conversion rate is 0.81. | [optional] 
**postage_paid** | **float** | **DEPRECIATED**   Use additional costs with Shipping flag to record shipping costs. This field remains available in the API for backward compatibility and acts pretty much like an additional cost item with type | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_purchase_order_header_parameter import UpdatePurchaseOrderHeaderParameter

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchaseOrderHeaderParameter from a JSON string
update_purchase_order_header_parameter_instance = UpdatePurchaseOrderHeaderParameter.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchaseOrderHeaderParameter.to_json())

# convert the object into a dict
update_purchase_order_header_parameter_dict = update_purchase_order_header_parameter_instance.to_dict()
# create an instance of UpdatePurchaseOrderHeaderParameter from a dict
update_purchase_order_header_parameter_from_dict = UpdatePurchaseOrderHeaderParameter.from_dict(update_purchase_order_header_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


