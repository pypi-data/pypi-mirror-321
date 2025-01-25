# AmazonVariation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_ignored** | **bool** |  | [optional] 
**ignored_msg** | **str** |  | [optional] 
**collision_number** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**business_price** | [**KeyValueGenericGuidDouble**](KeyValueGenericGuidDouble.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**pictures** | [**List[AmazonAttribute]**](AmazonAttribute.md) |  | [optional] 
**attributes** | [**List[AmazonAttribute]**](AmazonAttribute.md) |  | [optional] 
**message_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.amazon_variation import AmazonVariation

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonVariation from a JSON string
amazon_variation_instance = AmazonVariation.from_json(json)
# print the JSON string representation of the object
print(AmazonVariation.to_json())

# convert the object into a dict
amazon_variation_dict = amazon_variation_instance.to_dict()
# create an instance of AmazonVariation from a dict
amazon_variation_from_dict = AmazonVariation.from_dict(amazon_variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


