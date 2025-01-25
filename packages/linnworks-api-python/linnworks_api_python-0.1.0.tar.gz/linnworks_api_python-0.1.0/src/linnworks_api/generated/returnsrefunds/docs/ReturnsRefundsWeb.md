# ReturnsRefundsWeb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** |  | [optional] 
**pk_order_id** | **str** |  | [optional] 
**c_shipping_address** | **str** |  | [optional] 
**d_processed_on** | **datetime** |  | [optional] 
**f_postage_cost** | **float** |  | [optional] 
**f_total_charge** | **float** |  | [optional] 
**postage_cost_ex_tax** | **float** |  | [optional] 
**subtotal** | **float** |  | [optional] 
**f_tax** | **float** |  | [optional] 
**total_discount** | **float** |  | [optional] 
**country_tax_rate** | **float** |  | [optional] 
**n_order_id** | **int** |  | [optional] 
**c_currency** | **str** |  | [optional] 
**postal_tracking_number** | **str** |  | [optional] 
**c_country** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**postal_service_code** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**reference_num** | **str** |  | [optional] 
**secondary_reference** | **str** |  | [optional] 
**external_reference** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**town** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**buyer_phone_number** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**channel_buyer_name** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**c_full_name** | **str** |  | [optional] 
**c_email_address** | **str** |  | [optional] 
**c_post_code** | **str** |  | [optional] 
**d_paid_on** | **datetime** |  | [optional] 
**c_billing_address** | **str** |  | [optional] 
**billing_name** | **str** |  | [optional] 
**billing_company** | **str** |  | [optional] 
**billing_address1** | **str** |  | [optional] 
**billing_address2** | **str** |  | [optional] 
**billing_address3** | **str** |  | [optional] 
**billing_town** | **str** |  | [optional] 
**billing_region** | **str** |  | [optional] 
**billing_post_code** | **str** |  | [optional] 
**billing_country_name** | **str** |  | [optional] 
**billing_phone_number** | **str** |  | [optional] 
**c_item_number** | **str** |  | [optional] 
**c_item_name** | **str** |  | [optional] 
**pk_return_id** | **int** |  | [optional] 
**row_type** | **str** |  | [optional] 
**return_reference** | **str** |  | [optional] 
**pending_refund_amount** | **float** |  | [optional] 
**last_date** | **datetime** |  | [optional] 
**reason** | **str** |  | [optional] 
**channel_reason** | **str** |  | [optional] 
**channel_reason_sec** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**return_qty** | **int** |  | [optional] 
**fk_return_location_id** | **str** |  | [optional] 
**scrapped** | **bool** |  | [optional] 
**scrap_qty** | **int** |  | [optional] 
**return_date** | **datetime** |  | [optional] 
**location** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**new_qty** | **int** |  | [optional] 
**refund_reference** | **str** |  | [optional] 
**pk_refund_row_id** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**cancellation_quantity** | **int** |  | [optional] 
**fk_order_item_return_id** | **str** |  | [optional] 
**action_date** | **datetime** |  | [optional] 
**refund_status** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_web import ReturnsRefundsWeb

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsWeb from a JSON string
returns_refunds_web_instance = ReturnsRefundsWeb.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsWeb.to_json())

# convert the object into a dict
returns_refunds_web_dict = returns_refunds_web_instance.to_dict()
# create an instance of ReturnsRefundsWeb from a dict
returns_refunds_web_from_dict = ReturnsRefundsWeb.from_dict(returns_refunds_web_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


