# GetLabelByShipmentIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_url** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.get_label_by_shipment_id_response import GetLabelByShipmentIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLabelByShipmentIdResponse from a JSON string
get_label_by_shipment_id_response_instance = GetLabelByShipmentIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetLabelByShipmentIdResponse.to_json())

# convert the object into a dict
get_label_by_shipment_id_response_dict = get_label_by_shipment_id_response_instance.to_dict()
# create an instance of GetLabelByShipmentIdResponse from a dict
get_label_by_shipment_id_response_from_dict = GetLabelByShipmentIdResponse.from_dict(get_label_by_shipment_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


