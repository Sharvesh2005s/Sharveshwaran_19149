def linearSearchProduct(product_list, target_product):
    indices = []

    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)

    return indices

products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = linearSearchProduct(products, target)
print(result)
