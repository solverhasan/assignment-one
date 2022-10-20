mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

def usdToTaka(usd):
    taka = float(usd) * 105.84
    return taka


data_list = mobile_data['data']
temporay_dictionary = {}
for i in range(len(data_list)):
    temporay_dictionary = data_list[i]
    print(temporay_dictionary['name'], " is made in ", temporay_dictionary['made'], ". The price is ",
          temporay_dictionary['price'], " which is almost equal to ", sep='', end='')
    taka = usdToTaka(temporay_dictionary['price'][0:-4])
    print(round(taka), "BDT")