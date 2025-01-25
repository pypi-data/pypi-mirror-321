# SerialModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.serial_model import SerialModel

# TODO update the JSON string below
json = "{}"
# create an instance of SerialModel from a JSON string
serial_model_instance = SerialModel.from_json(json)
# print the JSON string representation of the object
print(SerialModel.to_json())

# convert the object into a dict
serial_model_dict = serial_model_instance.to_dict()
# create an instance of SerialModel from a dict
serial_model_from_dict = SerialModel.from_dict(serial_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


