# PrinterUserConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**printer_name** | **str** |  | [optional] 
**margin_left** | **float** |  | [optional] 
**margin_top** | **float** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label_format** | **str** |  | [optional] 
**duplex** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.printer_user_config import PrinterUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterUserConfig from a JSON string
printer_user_config_instance = PrinterUserConfig.from_json(json)
# print the JSON string representation of the object
print(PrinterUserConfig.to_json())

# convert the object into a dict
printer_user_config_dict = printer_user_config_instance.to_dict()
# create an instance of PrinterUserConfig from a dict
printer_user_config_from_dict = PrinterUserConfig.from_dict(printer_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


