# GetShippingPlanCardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**update_date** | **datetime** |  | [optional] 
**from_location** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 
**packing_type** | **int** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**shipment_items_count** | **int** |  | [optional] 
**shipment_received** | **int** |  | [optional] 
**shipment_shipped** | **int** |  | [optional] 
**ship_to** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**to_location** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**items** | [**List[StockItemSearchModel]**](StockItemSearchModel.md) |  | [optional] 
**shipments** | [**List[ShipmentSearchModel]**](ShipmentSearchModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_shipping_plan_cards_response import GetShippingPlanCardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetShippingPlanCardsResponse from a JSON string
get_shipping_plan_cards_response_instance = GetShippingPlanCardsResponse.from_json(json)
# print the JSON string representation of the object
print(GetShippingPlanCardsResponse.to_json())

# convert the object into a dict
get_shipping_plan_cards_response_dict = get_shipping_plan_cards_response_instance.to_dict()
# create an instance of GetShippingPlanCardsResponse from a dict
get_shipping_plan_cards_response_from_dict = GetShippingPlanCardsResponse.from_dict(get_shipping_plan_cards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


