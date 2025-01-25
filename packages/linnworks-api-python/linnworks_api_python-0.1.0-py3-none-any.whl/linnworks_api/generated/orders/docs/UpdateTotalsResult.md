# UpdateTotalsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals_info** | [**OrderTotalsInfo**](OrderTotalsInfo.md) |  | [optional] 
**shipping_info** | [**OrderShippingInfo**](OrderShippingInfo.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.update_totals_result import UpdateTotalsResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTotalsResult from a JSON string
update_totals_result_instance = UpdateTotalsResult.from_json(json)
# print the JSON string representation of the object
print(UpdateTotalsResult.to_json())

# convert the object into a dict
update_totals_result_dict = update_totals_result_instance.to_dict()
# create an instance of UpdateTotalsResult from a dict
update_totals_result_from_dict = UpdateTotalsResult.from_dict(update_totals_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


