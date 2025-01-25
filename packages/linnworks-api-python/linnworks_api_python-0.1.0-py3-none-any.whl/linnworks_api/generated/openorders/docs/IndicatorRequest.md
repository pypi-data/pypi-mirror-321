# IndicatorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.indicator_request import IndicatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IndicatorRequest from a JSON string
indicator_request_instance = IndicatorRequest.from_json(json)
# print the JSON string representation of the object
print(IndicatorRequest.to_json())

# convert the object into a dict
indicator_request_dict = indicator_request_instance.to_dict()
# create an instance of IndicatorRequest from a dict
indicator_request_from_dict = IndicatorRequest.from_dict(indicator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


