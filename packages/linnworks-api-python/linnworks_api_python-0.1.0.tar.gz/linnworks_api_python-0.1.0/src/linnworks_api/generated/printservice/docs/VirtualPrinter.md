# VirtualPrinter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printer_name** | **str** |  | [optional] 
**printer_location_name** | **str** |  | [optional] 
**printer_local_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.virtual_printer import VirtualPrinter

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPrinter from a JSON string
virtual_printer_instance = VirtualPrinter.from_json(json)
# print the JSON string representation of the object
print(VirtualPrinter.to_json())

# convert the object into a dict
virtual_printer_dict = virtual_printer_instance.to_dict()
# create an instance of VirtualPrinter from a dict
virtual_printer_from_dict = VirtualPrinter.from_dict(virtual_printer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


