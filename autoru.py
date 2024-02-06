from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
import re  # Регулярные выражения
import requests


# Подготовить функцию fetch
# params = { headers, body, method}
def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    method = params["method"]

    if method == "POST":
        return requests.post(url, headers=headers, data=body)

    if method == "GET":
        return requests.get(url, headers=headers)

bmw = fetch("https://auto.ru/-/ajax/desktop/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en,ru;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "167.0.10095387",
    "x-client-date": "1664561845805",
    "x-csrf-token": "9fbf73a9e0920f1257c10d02b30351ca8674e7f6ee98ff56",
    "x-page-request-id": "04196ab8aed1a5932b1d5508230a5ad2",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/cars/honda/all/",
    "x-yafp": "{\"a1\":\"ddI32w==;0\",\"a2\":\"9xbmEsxorsQmzzJh2s+bsViFbMiPiQ==;1\",\"a3\":\"XAZUXdmg6wtN8FNgCmIIXQ==;2\",\"a4\":\"kK/+9xfFmsGWVg==;3\",\"a5\":\"ORYIXSzLvciFFg==;4\",\"a6\":\"RWE=;5\",\"a7\":\"f/SzMjSF18ZOyA==;6\",\"a8\":\"Gh1010RJtfo=;7\",\"a9\":\"saEIlLtw8+e6YA==;8\",\"b1\":\"8D55UFKmIXI=;9\",\"b2\":\"6UTJTguvQsqYnA==;10\",\"b3\":\"7vXeroGqng5A1g==;11\",\"b4\":\"mKWX/izAWp0=;12\",\"b5\":\"G7iRIkviLo2ouA==;13\",\"b6\":\"k2Mm0xP0gr06QA==;14\",\"b7\":\"JCoD/6ole/CxtQ==;15\",\"b8\":\"ko9pTnBQw7jiqQ==;16\",\"b9\":\"3Gzhnr0pt76pQw==;17\",\"c1\":\"r/ZV3w==;18\",\"c2\":\"XqTkmvsO/TDU/IBKylafKQ==;19\",\"c3\":\"tj67fsujNBgM67JL6pxhBQ==;20\",\"c4\":\"ARcjKjK15SY=;21\",\"c5\":\"dm+180bOENw=;22\",\"c6\":\"rSr3ag==;23\",\"c7\":\"yY1WfWggY2Y=;24\",\"c8\":\"Cfs=;25\",\"c9\":\"OXcUKEfwMuM=;26\",\"d1\":\"nl4vf6/CN3w=;27\",\"d2\":\"wC4=;28\",\"d3\":\"3UZ1KJYG7iJbtg==;29\",\"d4\":\"DBxWNMiIY2k=;30\",\"d5\":\"mkaIlaKGqlU=;31\",\"d7\":\"Rsk=;32\",\"d8\":\"BQXacXUMTlYGRNS495fNa+GZXfVvPyHfYiY=;33\",\"d9\":\"Bw3FG0CthnI=;34\",\"e1\":\"HMJjLvaiNGxbpg==;35\",\"e2\":\"2Yvf0Fm4Ak4=;36\",\"e3\":\"5iRVRwxYXDY=;37\",\"e4\":\"DNTwiIobmDU=;38\",\"e5\":\"lQlo58ZFCV06cw==;39\",\"e6\":\"2SImXnZysus=;40\",\"e7\":\"TuPrnBZWz0FyPQ==;41\",\"e8\":\"0DdXx1k9GN0=;42\",\"e9\":\"XmYJSmqGzUU=;43\",\"f1\":\"HoCXCpZSXTK1lg==;44\",\"f2\":\"TBCgdLM8RJ4=;45\",\"f3\":\"/eruSt+pymOU3A==;46\",\"f4\":\"wP4lPFFgr4s=;47\",\"f5\":\"k2NiuLXj8kbyaQ==;48\",\"f6\":\"2ORfMNnCIgFO7g==;49\",\"f7\":\"ACDNszqynPtF/w==;50\",\"f8\":\"UeuuBCUhtDBqrA==;51\",\"f9\":\"5X7r+3p83EM=;52\",\"g1\":\"VVWUIjnaVkcDRw==;53\",\"g2\":\"o9avbI0yDiMZUw==;54\",\"g3\":\"iPB9yQR0Dcc=;55\",\"g4\":\"guBc+5yVwSh0Sw==;56\",\"g5\":\"1fC3iIAvB+8=;57\",\"g6\":\"+p/KeTYOXzc=;58\",\"g7\":\"fo/LE6+9QqQ=;59\",\"g8\":\"wFyy+ZqdXhQ=;60\",\"g9\":\"3KCIc5u/YXA=;61\",\"h1\":\"TbCe42W7ipnLhg==;62\",\"h2\":\"LRlsbdSbAntPog==;63\",\"h3\":\"zFF+YmqTIvRegA==;64\",\"h4\":\"M0OwV0mYlbR1Og==;65\",\"h5\":\"m1VKjNf3JB4=;66\",\"h6\":\"vU+6l/DqngoQiw==;67\",\"h7\":\"5ufLo06VOr92rRE4sZZfV/bgVmAmh7kDcYjVGjLQf/P+j/z/;68\",\"h8\":\"unwI979BX4xR5g==;69\",\"h9\":\"fP3MT7ptXQ25FA==;70\",\"i1\":\"2B76SteyevY=;71\",\"i2\":\"UM3z3iyhO4jf/w==;72\",\"i3\":\"W7DOxHyTR5Iztw==;73\",\"i4\":\"Wk2VVM/+na4BoA==;74\",\"i5\":\"rsHg/guPoG6f9g==;75\",\"z1\":\"kBVaUIGpsP+0umT+9/s82JaXR/ZFc9HuLgnh+sMDwpHIHdtWl9VzOpdJQN6BTyuVCn7eK6rtpBXD2d7UqW50Uw==;76\",\"z2\":\"0zgOkG2y0Y9d3NsIlqkVyGjkekCG0P3B2nddcY4KtIroS1MOoLSUn+y1Ct5hfxAVBvrUNhAKtHEztP3tWWWsdA==;77\",\"y2\":\"ZZ95PbHbmas16Q==;78\",\"y3\":\"b6wjL6R9urfWLQ==;79\",\"y6\":\"8ph/Wze0o44OEw==;80\",\"y8\":\"K0DAUkZ5LJtmCw==;81\",\"x4\":\"tBACNyx3vPnnIg==;82\",\"z5\":\"gDFUzCa8puc=;83\",\"z4\":\"lY2KhITKsm33gw==;84\",\"z6\":\"mMMLkkprgHltNS1O;85\",\"z7\":\"KLiBOqlvpv84wrNI;86\",\"z8\":\"lZ+uhIDva/5EupvPHrA=;87\",\"z9\":\"JgoEmIEvYyQkgXld;88\",\"y1\":\"+NmAZ8+/w2AqIQFb;89\",\"y4\":\"bT+4kuRG2b+aJKRO;90\",\"y5\":\"Nx03BU5JkRB0j6OjPdU=;91\",\"y7\":\"hoj29CpK20TSSFei;92\",\"y9\":\"UdEjrT97SzmdOlMIjqw=;93\",\"y10\":\"5m/BGt0+Jnq1b2zGYSY=;94\",\"x1\":\"fsfE0nMXFwUwOWCn;95\",\"x2\":\"FqqJ6cb+Gs6bO1X/lyE=;96\",\"x3\":\"VCcjEAlBuY3iOjBH;97\",\"x5\":\"wZEBahwQn8oL3Hly;98\",\"z3\":\"D2GC3ADoqQTo2KYQaIUr2Th7y0TSqw9xUFoAiS/TIbU=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"fRKHOZf0jKY8Iu3XmWemx+j6tl0=;100\",\"pgrd\":\"i41b/3pML9YQqkBXtsWo7EjPGKYoqFYASDA7QqrQ/9I9agiP93iT+6nHd5OVgYgeUnbQJ0+5XFiEqKo7THvOf6i4enWdgLM1MsNXmEYldOIKJKo7M2DJterw5tj/aY1ImxLdsf/fv0q8KRn3yalQthK/nkvpKYJxAt3lQkhSbS/TcqcmV6A17LcSoGjS9bw+aV+pakE3225YJUfVdBngFZ/9QEQ=\"}",
    "cookie": "_csrf_token=9fbf73a9e0920f1257c10d02b30351ca8674e7f6ee98ff56; autoru_gdpr=1; suid=85f19f0b88f068335ba14eba3f5e3435.14c9674db7da17f1988676e377b9dc01; from=direct; yandex_login=mike.ovc; gdpr=0; _ym_uid=1645564389770852331; i=W3pN8VedXKw9z/zUZuNtX9crMdBXBkObKZYvjxTIKwCymxxNTPxqI+y7X8XtWcHbLtC+mY8IX+xDWEk3oIGp5yFgIMQ=; autoru_sid=a%3Ag6337310c2tardre4d9t5ucf84easarv.7776dc5fa119e1e595ddbeae3eec6b40%7C1664561420536.604800.3sJwGAup-JhKf1FrlMR_IQ.L3A_yu2Xselzi71OZGiwEs-V4sZDC-Z1l-f3uuAQLiY; autoruuid=g6337310c2tardre4d9t5ucf84easarv.7776dc5fa119e1e595ddbeae3eec6b40; yuidlt=1; yandexuid=6280271851523913546; my=YwA%3D; crookie=FiZMYEApRl+z4KHqO0r5AVHyUjaCHdYdpTzqYuvZi7Y8XEGyTFPLm1zbldswipP9fz0ws3haU4uOC1K9bdyEyON2Bgw=; cmtchd=MTY2NDU2MTQyMjEwNw==; _ym_isad=1; Session_id=3:1664561424.5.0.1610028951543:Y0DWUY4Md_wArzqJAEsBKg:32.1.2:1|348690723.-1.2.0:3.1:63090147|61:10007778.976562.qtWU0SEiq0cIkCT_dKNYqSj8ZEc; ys=udn.cDrQnNC40YXQsNC40Lsg0J7QstGH0LjQvdC90LjQutC%2B0LI%3D#c_chck.1748117221; mda2_beacon=1664561424269; sso_status=sso.passport.yandex.ru:synchronized; _yasc=5c+Y7BmasQ9jndpb1+/6mcELXBTm8Y83UwznqPJvRxnUow3B; los=1; bltsr=1; from_lifetime=1664561775048; _ym_d=1664561812; layout-config={\"win_width\":892.5926513671875,\"win_height\":936.29638671875}",
    "Referer": "https://auto.ru/cars/honda/all/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"catalog_filter\":[{\"mark\":\"BMW\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\"}",
  "method": "POST"
})
offers = bmw.json()["offers"]
for offer in offers:
    price = offer["price_info"]["RUR"]
    name = offer["vehicle_info"]["model_info"]["name"]
    mileage = offer["state"]["mileage"]
    print(f"Продам BMW {name}, пробег всего {mileage} км., отдам за {price} рубликов")

