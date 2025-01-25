# PlacementOptionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_option_id** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**status** | [**OptionStatus**](OptionStatus.md) |  | [optional] 
**fees** | [**List[IncentiveModel]**](IncentiveModel.md) |  | [optional] 
**discounts** | [**List[IncentiveModel]**](IncentiveModel.md) |  | [optional] 
**shipments** | [**List[ShipmentAmazonModel]**](ShipmentAmazonModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.placement_option_model import PlacementOptionModel

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementOptionModel from a JSON string
placement_option_model_instance = PlacementOptionModel.from_json(json)
# print the JSON string representation of the object
print(PlacementOptionModel.to_json())

# convert the object into a dict
placement_option_model_dict = placement_option_model_instance.to_dict()
# create an instance of PlacementOptionModel from a dict
placement_option_model_from_dict = PlacementOptionModel.from_dict(placement_option_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


