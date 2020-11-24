### RADIUS CDR
Remote Authentication Dial In User Service (RADIUS) for streaming the Call Detail Records (CDR).

https://wiki.freeradius.org/Home

https://networkradius.com/doc/FreeRADIUS%20Technical%20Guide.pdf

https://habr.com/ru/post/51882/

https://www.dialogic.com/webhelp/BorderNet2020/2.2.0/WebHelp/radius_ov.htm

https://support.sonus.net/display/UXDOC61/Working+with+Call+Detail+Records

https://support.sonus.net/display/UXDOC61/Retreiving+Call+Detail+Records+From+a+RADIUS+Server

https://support.sonus.net/display/UXDOC61/Call+Detail+Records+Primer

https://wifisoft.zendesk.com/hc/en-us/articles/203566091-Understanding-RADIUS-session-records-CDRs-


## analyze_company_groups  640


## analyze_company_devices_radius 317

### radius_traffic = 2,882,647

select company, count(*) from radius_traffic group by company order by 2

3663	6
3731	6
3681	8
3673	12
3748	16
3725	54
3494	102
3680	127
3694	176
3552	352
0	1164
3717	1418
3678	1892
3612	2542
3453	3050
3333	3603
3662	3677
3690	5262
3641	5720
3666	6475
3682	10972
3002	11608
3579	12377
2924	12971
3529	15638
3652	16790
2944	22229
2926	23318
3655	38783
3611	41193
3413	64312
3445	78744
3659	252380
3061	701037
3361	735208
3116	809452


## analyze_company_gamma 445
