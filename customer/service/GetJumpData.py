

def getconnect(dbname, uid):
    dic = {
         "192.168.1.195": "mysql://fuser:kmyln08y6xa5@mysql24-ref-1.istarshine.net.cn:3306/U" + uid,
	     "192.168.1.196": "mysql://fuser:60zwlzg6vf0e@mysql24-ref-2.istarshine.net.cn:3306/U" + uid,
	     "192.168.1.197": "mysql://fuser:s1772170n51z@mysql24-ref-3.istarshine.net.cn:3306/U" + uid,
	     "192.168.1.198": "mysql://fuser:8r6ro5aw4ffxsy0@mysql24-info-1.istarshine.net.cn:3306/U" + uid,
	     "192.168.17.205": "mysql://fuser:kmyln08y6xa5@mysql24-ref-205.istarshine.net.cn:3306/U" + uid,
	     "192.168.17.206": "mysql://fuser:60zwlzg6vf0e@mysql24-ref-206.istarshine.net.cn:3306/U" + uid,
	     "192.168.17.207": "mysql://fuser:s1772170n51z@mysql24-ref-207.istarshine.net.cn:3306/U" + uid,
	      "192.168.19.51": "mysql://fuser:nh24yf239s6z@mysql-ref-51.istarshine.net.cn:3306/U" + uid, #新增库 add By ztf 2017-05-02
	     "192.168.19.52": "mysql://fuser:nh24yf239s6z@mysql-ref-52.istarshine.net.cn:3306/U" + uid,  #新增库 add By ztf 2017-05-02
	     "192.168.19.53": "mysql://fuser:nh24yf239s6z@mysql-ref-53.istarshine.net.cn:3306/U" + uid,  #新增库 add By ztf 2017-05-02
	     "192.168.19.59": "mysql://fuser:x626794p3e2m@mysql-project-1.istarshine.net.cn:3306/U" + uid, #新增库 add By ztf 2017-05-24
	     "192.168.19.54": "mysql://fuser:x626794p3e2m@mysql-network-1.istarshine.net.cn:3306/U" + uid, #新增库 add By ztf 2017-06-06
	     "192.168.19.71": "mysql://fuser:kmyln08y6xa5@mysql-ref-71.istarshine.net.cn:3306/U" + uid,
	     "192.168.19.72": "mysql://fuser:60zwlzg6vf0e@mysql-ref-72.istarshine.net.cn:3306/U" + uid,
	     "192.168.19.73": "mysql://fuser:s1772170n51z@mysql-ref-73.istarshine.net.cn:3306/U" + uid,
	     "192.168.19.74": "mysql://fuser:kmyln08y6xa5@mysql-ref-74.istarshine.net.cn:3306/U" + uid,
	     "192.168.19.61": "mysql://fuser:kmyln08y6xa5@192.168.19.61:3306/U" + uid,
	     #*****alpha环境用户建表地址库****
	     "192.168.16.63": "mysql://falpha:ktl5u090@alpha-mysql-ref-1.istarshine.net.cn:3306/U" + uid,
	     "192.168.16.64": "mysql://falpha:ktl5u090@alpha-mysql-ref-2.istarshine.net.cn:3306/U" + uid,
         #****beta境用户建表地址库 ****
		 "192.168.30.4": "mysql://fbeta:w6c682zz2m@beta-mysql-ref-1.istarshine.net.cn:3306/U" + uid,
	     "192.168.30.5": "mysql://fbeta:w6c682zz2m@beta-mysql-ref-2.istarshine.net.cn:3306/U" + uid,
    }
    return dic.get(dbname, "")

# print(getconnect("192.168.30.5", '123'))