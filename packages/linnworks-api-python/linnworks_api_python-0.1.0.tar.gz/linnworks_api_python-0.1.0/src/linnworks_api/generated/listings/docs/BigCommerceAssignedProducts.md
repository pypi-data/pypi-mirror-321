# BigCommerceAssignedProducts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 
**child_id** | **str** |  | [optional] 
**sku_id** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 
**upc** | **str** |  | [optional] 
**mpn** | **str** |  | [optional] 
**gtin** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**manage_stock** | **bool** |  | [optional] 
**collision_number** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**weight** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**in_stock_channel** | **bool** |  | [optional] 
**product_image_url** | **str** |  | [optional] 
**options_values** | [**List[ChildOption]**](ChildOption.md) |  | [optional] 
**sale_price** | **float** |  | [optional] 
**retail_price** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.big_commerce_assigned_products import BigCommerceAssignedProducts

# TODO update the JSON string below
json = "{}"
# create an instance of BigCommerceAssignedProducts from a JSON string
big_commerce_assigned_products_instance = BigCommerceAssignedProducts.from_json(json)
# print the JSON string representation of the object
print(BigCommerceAssignedProducts.to_json())

# convert the object into a dict
big_commerce_assigned_products_dict = big_commerce_assigned_products_instance.to_dict()
# create an instance of BigCommerceAssignedProducts from a dict
big_commerce_assigned_products_from_dict = BigCommerceAssignedProducts.from_dict(big_commerce_assigned_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


