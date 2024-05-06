# FFUF Report

  Command line : `ffuf -ic -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://10.10.159.59/FUZZ -t 90 -of md -o http80.md`
  Time: 2024-05-01T14:52:47&#43;08:00

  | FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash
  | :- | :-- | :--------------- | :---- | :------- | :---------- | :------------- | :------------ | :--------- | :----------- | :------------ | :-------- |
  | admin | http://10.10.159.59/admin | http://10.10.159.59/admin/ | 246 | 301 | 312 | 20 | 10 | text/html; charset=iso-8859-1 | 295.826482ms |  |  | 8730ff6
  |  | http://10.10.159.59/ |  | 1 | 200 | 10918 | 3499 | 376 | text/html | 4.25708427s |  |  | 8730f1
  | shadow | http://10.10.159.59/shadow |  | 2526 | 200 | 25 | 1 | 2 |  | 296.07325ms |  |  | 8730f9de
  | passwd | http://10.10.159.59/passwd |  | 7491 | 200 | 25 | 1 | 2 |  | 891.60367ms |  |  | 8730f1d43
  |  | http://10.10.159.59/ |  | 45227 | 200 | 10918 | 3499 | 376 | text/html | 1.344537514s |  |  | 8730fb0ab
  | server-status | http://10.10.159.59/server-status |  | 95511 | 403 | 277 | 20 | 10 | text/html; charset=iso-8859-1 | 810.863297ms |  |  | 8730f17517
  