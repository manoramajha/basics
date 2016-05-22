import requests
from bs4 import BeautifulSoup
import time
x = {'USD': 'US Dollar','EUR': 'Euro','GBP': 'British Pound','INR': 'Indian Rupee','AUD': 'Australian Dollar','CAD': 'Canadian Dollar','SGD': 'Singapore Dollar','CHF': 'Swiss Franc','MYR': 'Malaysian Ringgit','JPY': 'Japanese Yen','CNY': 'Chinese Yuan Renminbi','NZD': 'New Zealand Dollar','THB': 'Thai Baht','HUF': 'Hungarian Forint','AED': 'Emirati Dirham','HKD': 'Hong Kong Dollar','MXN': 'Mexican Peso','ZAR': 'South African Rand','PHP': 'Philippine Peso','SEK': 'Swedish Krona','IDR': 'Indonesian Rupiah','SAR': 'Saudi Arabian Riyal','BRL': 'Brazilian Real','TRY': 'Turkish Lira','KES': 'Kenyan Shilling','KRW': 'South Korean Won','EGP': 'Egyptian Pound','IQD': 'Iraqi Dinar','NOK': 'Norwegian Krone','KWD': 'Kuwaiti Dinar','RUB': 'Russian Ruble','DKK': 'Danish Krone','PKR': 'Pakistani Rupee','ILS': 'Israeli Shekel','PLN': 'Polish Zloty','QAR': 'Qatari Riyal','XAU': 'Gold Ounce','OMR': 'Omani Rial','COP': 'Colombian Peso','CLP': 'Chilean Peso','TWD': 'Taiwan New Dollar','ARS': 'Argentine Peso','CZK': 'Czech Koruna','VND': 'Vietnamese Dong','MAD': 'Moroccan Dirham','JOD': 'Jordanian Dinar','BHD': 'Bahraini Dinar','XOF': 'CFA Franc','LKR': 'Sri Lankan Rupee','UAH': 'Ukrainian Hryvnia','NGN': 'Nigerian Naira','TND': 'Tunisian Dinar','UGX': 'Ugandan Shilling','RON': 'Romanian New Leu','BDT': 'Bangladeshi Taka','PEN': 'Peruvian Sol','GEL': 'Georgian Lari','XAF': 'Central African CFA Franc BEAC','FJD': 'Fijian Dollar','VEF': 'Venezuelan Bolivar','BYR': 'Belarusian Ruble','HRK': 'Croatian Kuna','UZS': 'Uzbekistani Som','BGN': 'Bulgarian Lev','DZD': 'Algerian Dinar','IRR': 'Iranian Rial','DOP': 'Dominican Peso','ISK': 'Icelandic Krona','XAG': 'Silver Ounce','CRC': 'Costa Rican Colon','SYP': 'Syrian Pound','LYD': 'Libyan Dinar','JMD': 'Jamaican Dollar','MUR': 'Mauritian Rupee','GHS': 'Ghanaian Cedi','AOA': 'Angolan Kwanza','UYU': 'Uruguayan Peso','AFN': 'Afghan Afghani','LBP': 'Lebanese Pound','XPF': 'CFP Franc','TTD': 'Trinidadian Dollar','TZS': 'Tanzanian Shilling','ALL': 'Albanian Lek','XCD': 'East Caribbean Dollar','GTQ': 'Guatemalan Quetzal','NPR': 'Nepalese Rupee','BOB': 'Bolivian Bolíviano','ZWD': 'Zimbabwean Dollar','BBD': 'Barbadian or Bajan Dollar','CUC': 'Cuban Convertible Peso','LAK': 'Lao or Laotian Kip','BND': 'Bruneian Dollar','BWP': 'Botswana Pula','HNL': 'Honduran Lempira','PYG': 'Paraguayan Guarani','ETB': 'Ethiopian Birr','NAD': 'Namibian Dollar','PGK': 'Papua New Guinean Kina','SDG': 'Sudanese Pound','MOP': 'Macau Pataca','NIO': 'Nicaraguan Cordoba','BMD': 'Bermudian Dollar','KZT': 'Kazakhstani Tenge','PAB': 'Panamanian Balboa','BAM': 'Bosnian Convertible Marka','GYD': 'Guyanese Dollar','YER': 'Yemeni Rial','MGA': 'Malagasy Ariary','KYD': 'Caymanian Dollar','MZN': 'Mozambican Metical','RSD': 'Serbian Dinar','SCR': 'Seychellois Rupee','AMD': 'Armenian Dram','SBD': 'Solomon Islander Dollar','AZN': 'Azerbaijani New Manat','SLL': 'Sierra Leonean Leone','TOP': 'Tongan Paanga','BZD': 'Belizean Dollar','MWK': 'Malawian Kwacha','GMD': 'Gambian Dalasi','BIF': 'Burundian Franc','SOS': 'Somali Shilling','HTG': 'Haitian Gourde','GNF': 'Guinean Franc','MVR': 'Maldivian Rufiyaa','MNT': 'Mongolian Tughrik','CDF': 'Congolese Franc','STD': 'Sao Tomean Dobra','TJS': 'Tajikistani Somoni','KPW': 'North Korean Won','MMK': 'Burmese Kyat','LSL': 'Basotho Loti','LRD': 'Liberian Dollar','KGS': 'Kyrgyzstani Som','GIP': 'Gibraltar Pound','XPT': 'Platinum Ounce','MDL': 'Moldovan Leu','CUP': 'Cuban Peso','KHR': 'Cambodian Riel','MKD': 'Macedonian Denar','VUV': 'Ni-Vanuatu Vatu','MRO': 'Mauritanian Ouguiya','ANG': 'Dutch Guilder','SZL': 'Swazi Lilangeni','CVE': 'Cape Verdean Escudo','SRD': 'Surinamese Dollar','XPD': 'Palladium Ounce','SVC': 'Salvadoran Colon','BSD': 'Bahamian Dollar','XDR': 'IMF Special Drawing Rights','RWF': 'Rwandan Franc','AWG': 'Aruban or Dutch Guilder','DJF': 'Djiboutian Franc','BTN': 'Bhutanese Ngultrum','KMF': 'Comoran Franc','WST': 'Samoan Tala','SPL': 'Seborgan Luigino','ERN': 'Eritrean Nakfa','FKP': 'Falkland Island Pound','SHP': 'Saint Helenian Pound','JEP': 'Jersey Pound','TMT': 'Turkmenistani Manat','TVD': 'Tuvaluan Dollar','IMP': 'Isle of Man Pound','GGP': 'Guernsey Pound','ZMW': 'Zambian Kwacha'}
key = []
value = []
print("Hello , Welcome to Currency Exchange rate!\nEnter the S.no of the two currencies you want exchange rate of")
time.sleep(1.5)
for k,v in x.items():
    key.append(k)
    value.append(v)
for random in range(1,167):
    random_for_set_slicing = int(int(random) - 1)
    print("S.no " + str(random) + " " + value[random_for_set_slicing])
first_country = int(input("Enter the S.no of thee first country "))
second_country = int(input("Enter the S.no of thee second country "))
key1_for_link = key[int(first_country)-1]
key2_for_link = key[int(second_country)-1]

url = "http://xe.com/currencyconverter/convert/?Amount=&From=" + str(key1_for_link) +  "&To=" + str(key2_for_link)

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

response = requests.get(url, headers=headers)
plain = response.text
soup = BeautifulSoup(plain,"lxml")


for p in soup.findAll('td', { 'width':"47%"} , {'class' :"leftCol"}):

    print(p.string)