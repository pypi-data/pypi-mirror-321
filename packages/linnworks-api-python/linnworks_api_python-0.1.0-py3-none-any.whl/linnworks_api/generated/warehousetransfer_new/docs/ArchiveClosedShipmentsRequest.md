# ArchiveClosedShipmentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.archive_closed_shipments_request import ArchiveClosedShipmentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveClosedShipmentsRequest from a JSON string
archive_closed_shipments_request_instance = ArchiveClosedShipmentsRequest.from_json(json)
# print the JSON string representation of the object
print(ArchiveClosedShipmentsRequest.to_json())

# convert the object into a dict
archive_closed_shipments_request_dict = archive_closed_shipments_request_instance.to_dict()
# create an instance of ArchiveClosedShipmentsRequest from a dict
archive_closed_shipments_request_from_dict = ArchiveClosedShipmentsRequest.from_dict(archive_closed_shipments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


