# ImportProductsToShipmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_plan_id** | **int** |  | [optional] 
**file_id** | **str** |  | [optional] 
**settings** | [**ImportSettingModel**](ImportSettingModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_shipment_request import ImportProductsToShipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProductsToShipmentRequest from a JSON string
import_products_to_shipment_request_instance = ImportProductsToShipmentRequest.from_json(json)
# print the JSON string representation of the object
print(ImportProductsToShipmentRequest.to_json())

# convert the object into a dict
import_products_to_shipment_request_dict = import_products_to_shipment_request_instance.to_dict()
# create an instance of ImportProductsToShipmentRequest from a dict
import_products_to_shipment_request_from_dict = ImportProductsToShipmentRequest.from_dict(import_products_to_shipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


