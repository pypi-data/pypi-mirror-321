# PackingOptionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packing_option_id** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**status** | [**OptionStatus**](OptionStatus.md) |  | [optional] 
**packing_groups** | [**List[PackingGroupModel]**](PackingGroupModel.md) |  | [optional] 
**fees** | [**List[IncentiveModel]**](IncentiveModel.md) |  | [optional] 
**discounts** | [**List[IncentiveModel]**](IncentiveModel.md) |  | [optional] 
**shipping_configurations** | [**List[ShippingConfigurationModel]**](ShippingConfigurationModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.packing_option_model import PackingOptionModel

# TODO update the JSON string below
json = "{}"
# create an instance of PackingOptionModel from a JSON string
packing_option_model_instance = PackingOptionModel.from_json(json)
# print the JSON string representation of the object
print(PackingOptionModel.to_json())

# convert the object into a dict
packing_option_model_dict = packing_option_model_instance.to_dict()
# create an instance of PackingOptionModel from a dict
packing_option_model_from_dict = PackingOptionModel.from_dict(packing_option_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


