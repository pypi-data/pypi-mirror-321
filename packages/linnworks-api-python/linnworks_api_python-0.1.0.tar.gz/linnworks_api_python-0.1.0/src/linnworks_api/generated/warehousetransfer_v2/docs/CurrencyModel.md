# CurrencyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.currency_model import CurrencyModel

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyModel from a JSON string
currency_model_instance = CurrencyModel.from_json(json)
# print the JSON string representation of the object
print(CurrencyModel.to_json())

# convert the object into a dict
currency_model_dict = currency_model_instance.to_dict()
# create an instance of CurrencyModel from a dict
currency_model_from_dict = CurrencyModel.from_dict(currency_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


