# FFUF Report

  Command line : `ffuf -ic -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://smag.thm/FUZZ -t 100 -of md -o ffuf.md`
  Time: 2024-05-04T16:02:03&#43;08:00

  | FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash
  | :- | :-- | :--------------- | :---- | :------- | :---------- | :------------- | :------------ | :--------- | :----------- | :------------ | :-------- |
  |  | http://smag.thm/ |  | 1 | 200 | 402 | 69 | 13 | text/html; charset=UTF-8 | 319.762427ms |  |  | ac82d1
  | mail | http://smag.thm/mail | http://smag.thm/mail/ | 188 | 301 | 303 | 20 | 10 | text/html; charset=iso-8859-1 | 316.437613ms |  |  | ac82dbc
  |  | http://smag.thm/ |  | 45227 | 200 | 402 | 69 | 13 | text/html; charset=UTF-8 | 316.806475ms |  |  | ac82db0ab
  