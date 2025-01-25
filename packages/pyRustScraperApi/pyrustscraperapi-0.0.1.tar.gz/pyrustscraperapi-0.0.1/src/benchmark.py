from pyRustScraperApi import Client
from pyRustScraperApi.models import Order
import json
import time


def main():
    client = Client(
        "http://185.204.2.206",
        #"http://127.0.0.1:5050",
        "rs.ikxwaxvQfBCgLt9RcnNCaOB4c"
        #"rs.4DmQ0CbZake4xIsvhRQh82nRi"
    )
    time.sleep(2)
    order = Order(
		products=[
			"oz/1596079870",
      		"ym/1732949807-100352880819-5997015",
			"wb/300365052",
			"mm/100028286032",
			"https://www.ozon.ru/product/nozhnitsy-kantselyarskie-21-sm-calligrata-nerzhaveyushchaya-stal-plastik-173091046/",
			"https://www.wildberries.ru/catalog/95979396/detail.aspx",
			"https://market.yandex.ru/product--igrovaia-pristavka-sony-playstation-5-slim-digital-edition-bez-diskovoda-1000-gb-ssd-2-geimpada-bez-igr-belyi/925519649?sku=103706885579&uniqueId=162025048",
			"https://megamarket.ru/catalog/details/nabor-instrumentov-v-keyse-108-predmetov-100065768905/"
		],
		cookies=[{"domain":"megamarket.ru","httpOnly":False,"name":"spid","path":"/","sameSite":"no_restriction","secure":True,"value":"1734802726745_7255ffb7391e94f3baf87611eff4109c_3opa22ute0u793f4","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":True,"name":"device_id","path":"/","sameSite":"lax","secure":True,"value":"6e5c3dfb-bfc2-11ef-9b3f-469e2808707f","url":"https://megamarket.ru"},{"domain":".megamarket.ru","httpOnly":False,"name":"_sa","path":"/","sameSite":"strict","secure":True,"value":"SA1.b475966e-ee20-429f-85ca-bb32d2285195.1734802742","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":False,"name":"isOldUser","path":"/","sameSite":"lax","secure":True,"value":"True","url":"https://megamarket.ru"},{"domain":".megamarket.ru","httpOnly":False,"name":"adspire_uid","path":"/","sameSite":"no_restriction","secure":True,"value":"AS.1499435573.1734802743","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":False,"name":"ssaid","path":"/","sameSite":"unspecified","secure":False,"value":"78707010-bfc2-11ef-b425-5588617af3cb","url":"https://megamarket.ru"},{"domain":".megamarket.ru","httpOnly":False,"name":"uxs_uid","path":"/","sameSite":"unspecified","secure":False,"value":"79e95470-bfc2-11ef-b1a6-d7760aef56aa","url":"https://megamarket.ru"},{"domain":".megamarket.ru","httpOnly":False,"name":"__zzatw-smm","path":"/","sameSite":"unspecified","secure":False,"value":"MDA0dBA=Fz2+aQ==","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":True,"name":"sbermegamarket_token","path":"/","sameSite":"lax","secure":True,"value":"654f4ded-5036-453e-8a7c-19dcb451e9fb","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":True,"name":"ecom_token","path":"/","sameSite":"lax","secure":True,"value":"654f4ded-5036-453e-8a7c-19dcb451e9fb","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":False,"name":"spjs","path":"/","sameSite":"no_restriction","secure":True,"value":"1737138703075_2e9e8e5a_0134fe03_9643df474886426f83d23d287891c491_85GobMxXT3Ii34YoaZdA8LF5QzdmMMlITlq3UsKmEciY1HjRIWuTSmunHxzMqGSg5QFKqw5rQfgTzSWKYNY88NDdZrg6scg5bbmkVvOizt+6S4nQEC1VSV/GCxPGzwChkUCJiC1PgNsE8Adb+jG6JFX4k3+vBj8izNmBs5AEr7taLjKwgV3EaCg1jYPk69Ibyxe5uOx5gOQhxo46Ks05pYfpkfiZRv4Dw+/mNWMnz7p6mMOzo4Z+Li+h2QRUbNf9n9IqRrZJMGQV8Gk/Dpuj9qFmEd18MFyBcu7329v2a78v2gI0xvFJbHzYiDAST0b6qlQNskFJsu7E4KifPjoW0veELe1MQOgh9/vXGc6yHdD2CuFiMiPqWHs9gTBHgMf6iyJ4JIRbMg4ZdDjZGNlG5CJ1L6uLWWDwFVihzDwBGyABiXJOnmUNLSrsBRMTRx3c7Ngesza+5voP1YuRk49QpLRAGf0tOoJmd/OrGKjUXdGBbRaeaRNv8I/sALWHsmqe71kCFGc/sg28MMjGlq7km7sG6L2MHuKlNuKr3+57LHCQHeU5XpXI0VSa0wFQ1b32jkq1w5Pmvrp50xnU0HbF6oB1HDDvtMu/BoOJP80J4LS0UAeqZOZM0GFWhRlolmvPv0sAFqaRyH09WIIz4R9F+qlWDhEhnMV4I9OPvu2+0VQV0Gm8XZb9cxBehTlaFUjwtN1mt3KynCjPDNQF74Bl2mv32uU1OzJ/eiBayNmttYeGdS7szWviomVJ8a2oGoIeXqL7R5fsO2yKSiPFbZAJ9qzph7IhFMbIiMNLJgbbdcGwVVhpaT9XozP3GRqLH0+zri6kaWYVKCJ/1YmypBpIvqdZsRTUnkZ6qwaOOeJvRPqkdB+UPwviRAXCqJscGF7S5ynwTBzTn3W2OrbV5Revmjoelaf0tDxoz6NLYOAaoJ09EZiioh8mE7KWHi/p7xSSU3Yx6W4zi/Ai7oZb6pANaIkNNfVSUl0qrt/nBhCqtfitUThCVO/GuiE07fipzJeyJ7dOeq6F77ZUiKKPftdJhvZ4d3XHd7woCW8WdsaT0Zg4RD2BAZ62+jtH6hzZyFGVlWGKu3t7kxdVnKFs+eTFcbL9hKh4A9tvPsqWk8UTWd2s1Vd91y/JI9c2jLjok0wHVnIKNEYg1cQtPJY5ah9G/a2u9BmpnVFI4yTjt+yN5L2fecgkS1/4OxWWsXHe3XZ9q3RrP14a8/Yx3pkJ42haU4PfAJrKy8fJVJ3Y6yT3b/KnAEt5FjUYeiBTw=","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":False,"name":"spsc","path":"/","sameSite":"no_restriction","secure":True,"value":"1737149176819_bc04685ec5c05b890cd0eec05c104e33_bf4cd2fa3d30987fd0282ffebd8a9122","url":"https://megamarket.ru"},{"domain":".megamarket.ru","httpOnly":False,"name":"_sas","path":"/","sameSite":"strict","secure":True,"value":"SA1.b475966e-ee20-429f-85ca-bb32d2285195.1734802742.1737149176","url":"https://megamarket.ru"},{"domain":".megamarket.ru","httpOnly":False,"name":"__tld__","path":"/","sameSite":"unspecified","secure":False,"value":"null","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":False,"name":"region_info","path":"/","sameSite":"lax","secure":True,"value":"%7B%22displayName%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%2C%22kladrId%22%3A%225000000000000%22%2C%22isDeliveryEnabled%22%3ATrue%2C%22geo%22%3A%7B%22lat%22%3A55.755814%2C%22lon%22%3A37.617635%7D%2C%22id%22%3A%2250%22%7D","url":"https://megamarket.ru"},{"domain":"megamarket.ru","httpOnly":False,"name":"cfidsw-smm","path":"/","sameSite":"no_restriction","secure":True,"value":"/4dufmS3z3GMDJu5MMtnlCT2h5As3cVr0uZbcQb9PMiQE1wPYpfJ2+SjSVCTDHb3GoUJ+kfP16qpGKQSER8rr0DuKYxcTgBHnWygOmbgcUgjUVvPqVZX/Z9kBKfvR8GzQunde7CqIQdtWiHQY0C8XL+BWIMz3KSfo6WOhpg=","url":"https://megamarket.ru"},{"domain":".megamarket.ru","httpOnly":False,"name":"cfidsw-smm","path":"/","sameSite":"unspecified","secure":False,"value":"/4dufmS3z3GMDJu5MMtnlCT2h5As3cVr0uZbcQb9PMiQE1wPYpfJ2+SjSVCTDHb3GoUJ+kfP16qpGKQSER8rr0DuKYxcTgBHnWygOmbgcUgjUVvPqVZX/Z9kBKfvR8GzQunde7CqIQdtWiHQY0C8XL+BWIMz3KSfo6WOhpg=","url":"https://megamarket.ru"}],
  		proxy_pool=["1kpF8S:GPnFUb@147.45.62.117:8000"]
	)
    order_hash = client.send_order(order)
    for task in client.stream_task(order_hash):
        print(task)
    print(f"\n\n{json.dumps(task.result, ensure_ascii=False, indent=4)}")


if __name__ == "__main__":
    main()
