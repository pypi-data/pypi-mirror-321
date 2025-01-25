# StockLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**county** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**is_not_trackable** | **bool** |  | [optional] 
**location_tag** | **str** |  | [optional] 
**count_in_order_until_acknowledgement** | **bool** |  | [optional] 
**fulfilment_center_deduct_stock_when_processed** | **bool** |  | [optional] 
**is_warehouse_managed** | **bool** |  | [optional] 
**stock_location_id** | **str** |  | [optional] 
**location_name** | **str** |  | [optional] 
**is_fulfillment_center** | **bool** |  | [optional] 
**stock_location_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.stock_location import StockLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StockLocation from a JSON string
stock_location_instance = StockLocation.from_json(json)
# print the JSON string representation of the object
print(StockLocation.to_json())

# convert the object into a dict
stock_location_dict = stock_location_instance.to_dict()
# create an instance of StockLocation from a dict
stock_location_from_dict = StockLocation.from_dict(stock_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


