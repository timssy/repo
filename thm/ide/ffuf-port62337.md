# FFUF Report

  Command line : `ffuf -ic -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://10.10.167.143:62337/FUZZ -e php,txt,html,js,css -t 100 -of md -o ffuf-port62337.md`
  Time: 2024-05-02T11:19:31&#43;08:00

  | FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash
  | :- | :-- | :--------------- | :---- | :------- | :---------- | :------------- | :------------ | :--------- | :----------- | :------------ | :-------- |
  | js | http://10.10.167.143:62337/js | http://10.10.167.143:62337/js/ | 5 | 301 | 320 | 20 | 10 | text/html; charset=iso-8859-1 | 332.503286ms |  |  | b44515
  |  | http://10.10.167.143:62337/ |  | 1 | 200 | 5239 | 1739 | 87 | text/html; charset=UTF-8 | 345.919693ms |  |  | b44511
  | themes | http://10.10.167.143:62337/themes | http://10.10.167.143:62337/themes/ | 679 | 301 | 324 | 20 | 10 | text/html; charset=iso-8859-1 | 312.291502ms |  |  | b44512a7
  | data | http://10.10.167.143:62337/data | http://10.10.167.143:62337/data/ | 1009 | 301 | 322 | 20 | 10 | text/html; charset=iso-8859-1 | 311.408386ms |  |  | b44513f1
  | plugins | http://10.10.167.143:62337/plugins | http://10.10.167.143:62337/plugins/ | 3031 | 301 | 325 | 20 | 10 | text/html; charset=iso-8859-1 | 309.472506ms |  |  | b4451bd7
  | lib | http://10.10.167.143:62337/lib | http://10.10.167.143:62337/lib/ | 4243 | 301 | 321 | 20 | 10 | text/html; charset=iso-8859-1 | 310.039991ms |  |  | b44511093
  | languages | http://10.10.167.143:62337/languages | http://10.10.167.143:62337/languages/ | 5527 | 301 | 327 | 20 | 10 | text/html; charset=iso-8859-1 | 316.0075ms |  |  | b44511597
  | js | http://10.10.167.143:62337/js | http://10.10.167.143:62337/js/ | 5635 | 301 | 320 | 20 | 10 | text/html; charset=iso-8859-1 | 317.162917ms |  |  | b44511603
  | components | http://10.10.167.143:62337/components | http://10.10.167.143:62337/components/ | 5947 | 301 | 328 | 20 | 10 | text/html; charset=iso-8859-1 | 310.17543ms |  |  | b4451173b
  | workspace | http://10.10.167.143:62337/workspace | http://10.10.167.143:62337/workspace/ | 41593 | 301 | 327 | 20 | 10 | text/html; charset=iso-8859-1 | 312.30651ms |  |  | b4451a279
  | js | http://10.10.167.143:62337/js | http://10.10.167.143:62337/js/ | 271361 | 301 | 320 | 20 | 10 | text/html; charset=iso-8859-1 | 312.697641ms |  |  | b445142401
  |  | http://10.10.167.143:62337/ |  | 271357 | 200 | 5239 | 1739 | 87 | text/html; charset=UTF-8 | 314.994217ms |  |  | b4451423fd
  | server-status | http://10.10.167.143:62337/server-status |  | 573061 | 403 | 281 | 20 | 10 | text/html; charset=iso-8859-1 | 310.106267ms |  |  | b44518be85
  