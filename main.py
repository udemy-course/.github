# import os
# import json
# import datetime
# from jinja2 import Template
# from rich import print


# def main():

#     # get course list
#     with open('course.json') as f:
#         course_list = json.load(f)
#     # create coupon
#     start_date = datetime.date.today()
#     end_date = start_date + datetime.timedelta(days=5)
#     month_name = start_date.strftime("%b")
#     for course in course_list:
#         course['couponCode'] = f"{month_name}-{start}".upper()
#         start += 1


# def create_bulk_request():
#     # course_id,coupon_type,coupon_code,start_date,start_time

#     course_list = get_course()
#     month_name = datetime.datetime.now().strftime("%b")
#     course_list = create_coupon(course_list, month_name)
#     return course_list


# def update_readme_with_coupons():
#     course_list = create_bulk_request()
#     with open('templates') as f:
#         template = Template(f.read())
#     with open('README.md', 'w') as f:
#         f.write(template.render(courses=course_list))


# if __name__ == '__main__':
#     month_name = datetime.date.today().strftime("%b")
#     course = get_course()
#     course = create_coupon(course, month_name)
#     print(course)
#     print(month_name)


# from jinja2 import Template

# name = 'Peter'
# age = 34

# tm = Template("My name is {{ name }} and I am {{ age }}")
# msg = tm.render(name=name, age=age)

# print(msg)

from jinja2 import Template
import json
import datetime
import pytz


def get_start_time():
    pacific = pytz.timezone('US/Pacific')
    now = datetime.datetime.now(pacific)
    five_days_later = now + datetime.timedelta(days=5)
    return now.strftime('%Y-%m-%d %H:%M'), five_days_later.strftime('%Y-%m-%d %H:%M')


with open('course.json') as f:
    course_list = json.load(f)
    start = 1111
    for course in course_list:
        course['start_time'],  course['end_time'] = get_start_time()
        course["link_with_coupon"] = f"{course['course_url']}/?couponCode=DCE-{start}"
        course["link_with_referral"] = f"{course['course_url']}/?referralCode={course['referralCode']}"
        start += 1
with open('templates/README.md.j2') as f:
    template = Template(f.read())
with open('profile/README.md', 'w') as f:
    f.write(template.render(course_list=course_list))

with open('templates/udemy.j2') as f:
    template = Template(f.read())
    print(template.render(course_list=course_list))
