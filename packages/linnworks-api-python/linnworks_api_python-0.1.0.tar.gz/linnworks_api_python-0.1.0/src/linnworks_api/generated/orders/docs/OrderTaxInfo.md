# OrderTaxInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_number** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_tax_info import OrderTaxInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTaxInfo from a JSON string
order_tax_info_instance = OrderTaxInfo.from_json(json)
# print the JSON string representation of the object
print(OrderTaxInfo.to_json())

# convert the object into a dict
order_tax_info_dict = order_tax_info_instance.to_dict()
# create an instance of OrderTaxInfo from a dict
order_tax_info_from_dict = OrderTaxInfo.from_dict(order_tax_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


