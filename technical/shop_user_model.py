from dataclasses import dataclass


@dataclass
class ShopUser:
    name: str
    surname: str
    zip_code: str



x = {"name": "Marcin", "surname": "Kowal"}
print(x["namr"])

user = ShopUser("Marcin", "Kowal", "30-123")
print(user.name)