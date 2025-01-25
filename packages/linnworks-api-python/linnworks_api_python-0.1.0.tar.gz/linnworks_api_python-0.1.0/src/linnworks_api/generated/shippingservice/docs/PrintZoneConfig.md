# PrintZoneConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**print_zone_code** | **str** |  | [optional] 
**printer_destination** | **str** |  | [optional] 
**printer_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.print_zone_config import PrintZoneConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PrintZoneConfig from a JSON string
print_zone_config_instance = PrintZoneConfig.from_json(json)
# print the JSON string representation of the object
print(PrintZoneConfig.to_json())

# convert the object into a dict
print_zone_config_dict = print_zone_config_instance.to_dict()
# create an instance of PrintZoneConfig from a dict
print_zone_config_from_dict = PrintZoneConfig.from_dict(print_zone_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


