# OrderCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_id** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**customs_required** | **bool** |  | [optional] 
**tax_rate** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_country import OrderCountry

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCountry from a JSON string
order_country_instance = OrderCountry.from_json(json)
# print the JSON string representation of the object
print(OrderCountry.to_json())

# convert the object into a dict
order_country_dict = order_country_instance.to_dict()
# create an instance of OrderCountry from a dict
order_country_from_dict = OrderCountry.from_dict(order_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


