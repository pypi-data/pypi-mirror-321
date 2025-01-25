# GetShipmentCardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[ShipmentCardModel]**](ShipmentCardModel.md) |  | [optional] 
**last_update_date** | **datetime** |  | [optional] 
**amazon_config_errors** | [**List[AmazonConfigErrorResponse]**](AmazonConfigErrorResponse.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.get_shipment_cards_response import GetShipmentCardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentCardsResponse from a JSON string
get_shipment_cards_response_instance = GetShipmentCardsResponse.from_json(json)
# print the JSON string representation of the object
print(GetShipmentCardsResponse.to_json())

# convert the object into a dict
get_shipment_cards_response_dict = get_shipment_cards_response_instance.to_dict()
# create an instance of GetShipmentCardsResponse from a dict
get_shipment_cards_response_from_dict = GetShipmentCardsResponse.from_dict(get_shipment_cards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


