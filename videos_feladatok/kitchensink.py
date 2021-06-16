from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/filltablewithsum.html")

# product = driver.find_element_by_id("product")  # kiválasztjuk az elemet
# product.send_keys("Ford Focus")  # beleírunk
# quantity = driver.find_element_by_id("quantity")
# quantity.send_keys("1")
# price = driver.find_element_by_id("price")
# price.send_keys(75000)
# 
# add_button = driver.find_element_by_id("add")  # megkeressük az add gombot
# add_button.click()  #klikkelünk rajta
# 
# # ha ismételni szeretnénk, akkor ki kell törölni a kitöltött mezőket
# product.clear()
# quantity.clear()
# price.clear()
# 
# # majd második kitöltésre elég az értékeket megadni
# product.send_keys("Audi")
# quantity.send_keys(2)
# price.send_keys(80000)
# 
# add_button = driver.find_element_by_id("add")
# add_button.click()

# a fenti sorok egy funkcióban megírva p-product, q-quantity, pr-price
def add(p, q, pr):
    product = driver.find_element_by_id("product")
    quantity = driver.find_element_by_id("quantity")
    price = driver.find_element_by_id("price")
    add_button = driver.find_element_by_id("add")

    # töröljük a mezőket
    product.clear()
    quantity.clear()
    price.clear()

    # változónevekkel feltöltjük a függvényeket
    product.send_keys(p)
    quantity.send_keys(q)
    price.send_keys(pr)
    add_button.click()


# majd meghívjuk 2x az add függvényt
add("Ford", 1, 75000)
add("Audi", 2, 80000)

# driver.close()
