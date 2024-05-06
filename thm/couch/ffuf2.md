# FFUF Report

  Command line : `ffuf -ic -w /opt/SecLists/Discovery/Web-Content/big.txt -u http://10.10.17.80:5984/FUZZ -t 100 -of md -o ffuf2.md`
  Time: 2024-04-30T19:40:07&#43;08:00

  | FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash
  | :- | :-- | :--------------- | :---- | :------- | :---------- | :------------- | :------------ | :--------- | :----------- | :------------ | :-------- |
  | _config | http://10.10.17.80:5984/_config |  | 1164 | 200 | 4808 | 80 | 2 | text/plain; charset=utf-8 | 285.259837ms |  |  | cab2e48c
  | _log | http://10.10.17.80:5984/_log |  | 1311 | 200 | 1000 | 148 | 13 | text/plain; charset=utf-8 | 262.355149ms |  |  | cab2e51f
  | _plugins | http://10.10.17.80:5984/_plugins |  | 1364 | 405 | 60 | 3 | 2 | text/plain; charset=utf-8 | 267.532205ms |  |  | cab2e554
  | _utils | http://10.10.17.80:5984/_utils | http://10.10.17.80:5984/_utils/ | 1471 | 301 | 0 | 1 | 1 |  | 272.260575ms |  |  | cab2e5bf
  | _stats | http://10.10.17.80:5984/_stats |  | 1422 | 200 | 4926 | 156 | 2 | text/plain; charset=utf-8 | 265.523884ms |  |  | cab2e58e
  | _users | http://10.10.17.80:5984/_users |  | 1467 | 200 | 230 | 1 | 2 | text/plain; charset=utf-8 | 262.926491ms |  |  | cab2e5bb
  | favicon.ico | http://10.10.17.80:5984/favicon.ico |  | 7429 | 200 | 9326 | 14 | 12 | image/x-icon | 262.95013ms |  |  | cab2e1d05
  | secret | http://10.10.17.80:5984/secret |  | 16082 | 200 | 229 | 1 | 2 | text/plain; charset=utf-8 | 262.030386ms |  |  | cab2e3ed2
  