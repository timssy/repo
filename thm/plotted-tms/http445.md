# FFUF Report

  Command line : `ffuf -ic -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://10.10.159.59:445/FUZZ -t 90 -of md -o http445.md`
  Time: 2024-05-01T14:46:46&#43;08:00

  | FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash
  | :- | :-- | :--------------- | :---- | :------- | :---------- | :------------- | :------------ | :--------- | :----------- | :------------ | :-------- |
  | management | http://10.10.159.59:445/management | http://10.10.159.59:445/management/ | 428 | 301 | 322 | 20 | 10 | text/html; charset=iso-8859-1 | 296.565938ms |  |  | b4ac11ac
  |  | http://10.10.159.59:445/ |  | 1 | 200 | 10918 | 3499 | 376 | text/html | 6.664020138s |  |  | b4ac11
  |  | http://10.10.159.59:445/ |  | 45227 | 200 | 10918 | 3499 | 376 | text/html | 297.931387ms |  |  | b4ac1b0ab
  | server-status | http://10.10.159.59:445/server-status |  | 95511 | 403 | 278 | 20 | 10 | text/html; charset=iso-8859-1 | 297.108581ms |  |  | b4ac117517
  