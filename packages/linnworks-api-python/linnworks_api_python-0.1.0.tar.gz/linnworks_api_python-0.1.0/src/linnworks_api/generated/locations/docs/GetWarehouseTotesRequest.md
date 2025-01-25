# GetWarehouseTotesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | Location Id of the TOTs | [optional] 
**tote_barcode** | **str** | (Optional) Barcode of the TOT. If provided the response will contain one record that matches exactly to the TotBarcode or returns an empty response if nothing is found. If not provided, empty string or null and TotId is null or not specified all TOTs for the warehouse will be returned. | [optional] 
**tot_id** | **int** | (Optional) Id of the TOT, if specified TotBarcode is ignored. If null and TotBarcode not specified then returns all tots in the warehouse | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.get_warehouse_totes_request import GetWarehouseTotesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseTotesRequest from a JSON string
get_warehouse_totes_request_instance = GetWarehouseTotesRequest.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseTotesRequest.to_json())

# convert the object into a dict
get_warehouse_totes_request_dict = get_warehouse_totes_request_instance.to_dict()
# create an instance of GetWarehouseTotesRequest from a dict
get_warehouse_totes_request_from_dict = GetWarehouseTotesRequest.from_dict(get_warehouse_totes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


