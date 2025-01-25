# CouponValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_text** | **str** |  | [optional] 
**deduct_visible** | **bool** |  | [optional] 
**deduct_text** | **str** |  | [optional] 
**balance_visible** | **bool** |  | [optional] 
**balance_text** | **str** |  | [optional] 
**value_text** | **str** |  | [optional] 
**discount_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.coupon_validation_result import CouponValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of CouponValidationResult from a JSON string
coupon_validation_result_instance = CouponValidationResult.from_json(json)
# print the JSON string representation of the object
print(CouponValidationResult.to_json())

# convert the object into a dict
coupon_validation_result_dict = coupon_validation_result_instance.to_dict()
# create an instance of CouponValidationResult from a dict
coupon_validation_result_from_dict = CouponValidationResult.from_dict(coupon_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


