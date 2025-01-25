# EbayVariation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_number** | **int** |  | [optional] 
**is_linked** | **bool** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**multiple_identifiers** | [**List[KeyValue]**](KeyValue.md) |  | [optional] 
**title** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**e_pid** | **str** |  | [optional] 
**is_catalog_match** | **bool** |  | [optional] 
**attributes** | [**List[EbayAttribute]**](EbayAttribute.md) |  | [optional] 
**error_mesage** | **str** |  | [optional] 
**pictures** | [**List[ImageData]**](ImageData.md) |  | [optional] 
**price** | [**EbayPrices**](EbayPrices.md) |  | [optional] 
**lot_size** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_variation import EbayVariation

# TODO update the JSON string below
json = "{}"
# create an instance of EbayVariation from a JSON string
ebay_variation_instance = EbayVariation.from_json(json)
# print the JSON string representation of the object
print(EbayVariation.to_json())

# convert the object into a dict
ebay_variation_dict = ebay_variation_instance.to_dict()
# create an instance of EbayVariation from a dict
ebay_variation_from_dict = EbayVariation.from_dict(ebay_variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


