# SystemShippingAPIConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_shipping_api_config_id** | **int** |  | [optional] 
**vendor** | **str** |  | [optional] 
**vendor_friendly_name** | **str** |  | [optional] 
**vendor_icon** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**label_format** | **str** |  | [optional] 
**services** | **int** |  | [optional] 
**manifest_pending** | **bool** |  | [optional] 
**last_manifest_with_error_id** | **int** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**printer_config** | [**PrinterConfig**](PrinterConfig.md) |  | [optional] 
**quote_enabled** | **bool** |  | [optional] 
**quote_only_included_services** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.system_shipping_api_config import SystemShippingAPIConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SystemShippingAPIConfig from a JSON string
system_shipping_api_config_instance = SystemShippingAPIConfig.from_json(json)
# print the JSON string representation of the object
print(SystemShippingAPIConfig.to_json())

# convert the object into a dict
system_shipping_api_config_dict = system_shipping_api_config_instance.to_dict()
# create an instance of SystemShippingAPIConfig from a dict
system_shipping_api_config_from_dict = SystemShippingAPIConfig.from_dict(system_shipping_api_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


