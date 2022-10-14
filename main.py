import os
from rich import print
import json

a = """
4392922,"HashiCorp Certified - Terraform Associate 考试完全指南2022","best_price","unlimited","OCT-1111","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/terraform-basic/?couponCode=OCT-1111"
3731444,"Vagrant从入门到精通","best_price","unlimited","OCT-1112","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/vagrant-zh/?couponCode=OCT-1112"
3418642,"Prometheus and Grafana for Monitoring and Alerting监控和报警系统","best_price","unlimited","OCT-1113","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/telegraf-prometheus-grafana-cn/?couponCode=OCT-1113"
2321788,"Django 2  Web开发入门与实战","best_price","unlimited","OCT-1114","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","EUR",9.99,"https://www.udemy.com/course/django-2-web/?couponCode=OCT-1114"
2276701,"Python 3 Flask REST APIs入门与实战","best_price","unlimited","OCT-1115","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","EUR",9.99,"https://www.udemy.com/course/flask-rest-api/?couponCode=OCT-1115"
2187592,"Python3之操作主流数据库MySQL/MongoDB","best_price","unlimited","OCT-1116","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/python3-database/?couponCode=OCT-1116"
1878846,"Python 3 编程技巧汇总","best_price","unlimited","OCT-1117","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/python3-tips/?couponCode=OCT-1117"
1865400,"SQL/MySQL 零基础从入门到精通","best_price","unlimited","OCT-1118","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",10.99,"https://www.udemy.com/course/sql-mysql/?couponCode=OCT-1118"
1864936,"MongoDB零基础从入门到精通","best_price","unlimited","OCT-1119","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/best-mongodb/?couponCode=OCT-1119"
1733494,"Certified Kubernetes Administrator (CKA) 考试完全指南（2022版）","best_price","unlimited","OCT-1120","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/k8s-chinese/?couponCode=OCT-1120"
1465666,"Git/GitHub/GitLab完全教程（包括Git底层原理）","best_price","unlimited","OCT-1121","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/git-basic/?couponCode=OCT-1121"
1432416,"Python Flask Web开发入门与实战","best_price","unlimited","OCT-1122","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/python-flask/?couponCode=OCT-1122"
1427824,"零基础七天入门Linux","best_price","unlimited","OCT-1123","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/linux-zh/?couponCode=OCT-1123"
1340588,"Python 3 数据分析 Data Science零基础完全入门","best_price","unlimited","OCT-1124","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/python-for-data-science/?couponCode=OCT-1124"
1294480,"Python高級課程：如何創建/發佈/維護/參與Opensource Software","best_price","unlimited","OCT-1125","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/python-awesome-tools/?couponCode=OCT-1125"
1242424,"Python 3零基础完全入门与提高（面向2022, Python3.8/3.9,不断更新ing）","best_price","unlimited","OCT-1126","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/python3-chinese/?couponCode=OCT-1126"
1147478,"Docker容器技术从入门到精通","best_price","unlimited","OCT-1127","2022-10-15 00:00 PDT","2022-10-20 00:00 PDT","USD",9.99,"https://www.udemy.com/course/docker-china/?couponCode=OCT-1127"
"""
course_list = []

for line in a.split('\n'):
    if not line:
        continue
    line = line.strip()
    line = line.split(',')
    course_list.append(
        {
            'course_id': int(line[0]),
            "coupon_type": "best_price",
            "coupon_code": '',
            "start_date": '',
            "start_time": '',
            "course_name": line[1],
            "course_coupon_url": line[-1].split("?")[0],
        }
    )
with open('course.json', 'w', encoding='utf8') as f:
    json.dump(course_list, f, indent=4, ensure_ascii=False)
