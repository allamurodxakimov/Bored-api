from main import Bored
bored = Bored()
# print(bored.get_activity())
# print(bored.get_activity_by_type("recreational"))
# print(bored.get_activity_by_id(9318514))
# print(bored.get_activity_by_accessibility(0.5))
# print(bored.get_activity_by_price(0.2))
print(bored.get_activity_by_price_range(0.1,0.4))