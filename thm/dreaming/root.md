# FFUF Report

  Command line : `ffuf -ic -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://10.10.107.92/FUZZ -t 100 -of md -o root.md`
  Time: 2024-05-03T16:19:02&#43;08:00

  | FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash
  | :- | :-- | :--------------- | :---- | :------- | :---------- | :------------- | :------------ | :--------- | :----------- | :------------ | :-------- |
  |  | http://10.10.107.92/ |  | 1 | 200 | 10918 | 3499 | 376 | text/html | 351.767558ms |  |  | 3e6ab1
  | app | http://10.10.107.92/app | http://10.10.107.92/app/ | 896 | 301 | 310 | 20 | 10 | text/html; charset=iso-8859-1 | 319.81829ms |  |  | 3e6ab380
  |  | http://10.10.107.92/ |  | 45227 | 200 | 10918 | 3499 | 376 | text/html | 321.85331ms |  |  | 3e6abb0ab
  | server-status | http://10.10.107.92/server-status |  | 95511 | 403 | 277 | 20 | 10 | text/html; charset=iso-8859-1 | 319.618067ms |  |  | 3e6ab17517
  