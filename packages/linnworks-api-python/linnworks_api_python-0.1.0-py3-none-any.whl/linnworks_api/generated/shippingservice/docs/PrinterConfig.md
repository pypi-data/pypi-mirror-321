# PrinterConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printer_name** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label_format** | **str** |  | [optional] 
**margin_left** | **float** |  | [optional] 
**margin_top** | **float** |  | [optional] 
**duplex** | **bool** |  | [optional] 
**user_config** | [**List[PrinterUserConfig]**](PrinterUserConfig.md) |  | [optional] 
**print_zone_config** | [**List[PrintZoneConfig]**](PrintZoneConfig.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.printer_config import PrinterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterConfig from a JSON string
printer_config_instance = PrinterConfig.from_json(json)
# print the JSON string representation of the object
print(PrinterConfig.to_json())

# convert the object into a dict
printer_config_dict = printer_config_instance.to_dict()
# create an instance of PrinterConfig from a dict
printer_config_from_dict = PrinterConfig.from_dict(printer_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


