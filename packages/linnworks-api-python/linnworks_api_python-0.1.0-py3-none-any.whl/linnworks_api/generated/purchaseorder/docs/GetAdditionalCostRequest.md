# GetAdditionalCostRequest

Request class for getting purchase order additional costs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_id** | **str** | Purchase order unique identifier of a PO | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_additional_cost_request import GetAdditionalCostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdditionalCostRequest from a JSON string
get_additional_cost_request_instance = GetAdditionalCostRequest.from_json(json)
# print the JSON string representation of the object
print(GetAdditionalCostRequest.to_json())

# convert the object into a dict
get_additional_cost_request_dict = get_additional_cost_request_instance.to_dict()
# create an instance of GetAdditionalCostRequest from a dict
get_additional_cost_request_from_dict = GetAdditionalCostRequest.from_dict(get_additional_cost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


