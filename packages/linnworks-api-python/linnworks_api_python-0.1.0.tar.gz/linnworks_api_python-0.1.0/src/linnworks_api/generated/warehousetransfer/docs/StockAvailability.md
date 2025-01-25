# StockAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_id** | **str** |  | [optional] 
**level_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.stock_availability import StockAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of StockAvailability from a JSON string
stock_availability_instance = StockAvailability.from_json(json)
# print the JSON string representation of the object
print(StockAvailability.to_json())

# convert the object into a dict
stock_availability_dict = stock_availability_instance.to_dict()
# create an instance of StockAvailability from a dict
stock_availability_from_dict = StockAvailability.from_dict(stock_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


