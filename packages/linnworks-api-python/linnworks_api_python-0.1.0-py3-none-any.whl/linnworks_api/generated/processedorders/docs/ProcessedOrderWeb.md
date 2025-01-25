# ProcessedOrderWeb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 
**c_shipping_address** | **str** |  | [optional] 
**d_received_date** | **datetime** |  | [optional] 
**d_processed_on** | **datetime** |  | [optional] 
**time_diff** | **float** |  | [optional] 
**f_postage_cost** | **float** |  | [optional] 
**f_total_charge** | **float** |  | [optional] 
**postage_cost_ex_tax** | **float** |  | [optional] 
**subtotal** | **float** |  | [optional] 
**f_tax** | **float** |  | [optional] 
**total_discount** | **float** |  | [optional] 
**profit_margin** | **float** |  | [optional] 
**country_tax_rate** | **float** |  | [optional] 
**n_order_id** | **int** |  | [optional] 
**n_status** | **int** |  | [optional] 
**c_currency** | **str** |  | [optional] 
**postal_tracking_number** | **str** |  | [optional] 
**c_country** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**postal_service_code** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**billing_email_address** | **str** |  | [optional] 
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
**d_cancelled_on** | **datetime** |  | [optional] 
**package_category** | **str** |  | [optional] 
**package_title** | **str** |  | [optional] 
**item_weight** | **float** |  | [optional] 
**total_weight** | **float** |  | [optional] 
**folder_collection** | **str** |  | [optional] 
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
**hold_or_cancel** | **bool** |  | [optional] 
**is_resend** | **bool** |  | [optional] 
**is_exchange** | **bool** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**fulfilment_location_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_order_web import ProcessedOrderWeb

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrderWeb from a JSON string
processed_order_web_instance = ProcessedOrderWeb.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrderWeb.to_json())

# convert the object into a dict
processed_order_web_dict = processed_order_web_instance.to_dict()
# create an instance of ProcessedOrderWeb from a dict
processed_order_web_from_dict = ProcessedOrderWeb.from_dict(processed_order_web_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


