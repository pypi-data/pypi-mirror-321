# ImportProductsToShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted_ids** | **List[int]** |  | [optional] 
**updated_ids** | **List[int]** |  | [optional] 
**not_imported_items** | [**List[FailedShippingItem]**](FailedShippingItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.import_products_to_shipment_response import ImportProductsToShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportProductsToShipmentResponse from a JSON string
import_products_to_shipment_response_instance = ImportProductsToShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(ImportProductsToShipmentResponse.to_json())

# convert the object into a dict
import_products_to_shipment_response_dict = import_products_to_shipment_response_instance.to_dict()
# create an instance of ImportProductsToShipmentResponse from a dict
import_products_to_shipment_response_from_dict = ImportProductsToShipmentResponse.from_dict(import_products_to_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


