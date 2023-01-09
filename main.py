"""
udemy coupones
"""

import json
import csv
import datetime
from pathlib import Path

from jinja2 import Template
import pytz


# def get_start_time():
#     """
#     get start time in US pacific time zone
#     """
#     pacific = pytz.timezone('US/Pacific')
#     now = datetime.datetime.now(pacific)
#     five_days_later = now + datetime.timedelta(days=5)
#     month_in_short = now.strftime('%b')
#     return now.strftime('%Y-%m-%d %H:%M'), five_days_later.strftime('%Y-%m-%d %H:%M')


# with open('course.json', "r") as f:
#     course_list = json.load(f)
#     start = 1111
#     for course in course_list:
#         course['start_time'],  course['end_time'] = get_start_time()
#         course["link_with_coupon"] = f"{course['course_url']}/?couponCode=DCE-{start}"
#         course["link_with_referral"] = f"{course['course_url']}/?referralCode={course['referralCode']}"
#         start += 1
# with open('templates/README.md.j2') as f:
#     template = Template(f.read())
# with open('profile/README.md', 'w') as f:
#     f.write(template.render(course_list=course_list))

# with open('templates/udemy.j2') as f:
#     template = Template(f.read())
#     print(template.render(course_list=course_list))


def main(promotion=True):
    """main function"""

    f = open('course.json', "r", encoding="utf-8")
    course_list = json.load(f)
    f.close()

    if promotion:
        pacific = pytz.timezone('US/Pacific')
        now = datetime.datetime.now(pacific)
        five_days_later = now + datetime.timedelta(days=5)
        month_in_short = now.strftime('%b')
        year = now.strftime('%Y')

        # create coupon request csv file
        with open(Path('data') / f"{year}_{month_in_short}{now.strftime('%d')}.csv", 'w', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                ['course_id', 'coupon_type', 'coupon_code', 'start_date', 'start_time'])
            for course in course_list:
                coupon_code = f"{year}-{month_in_short}-{course['course_id']}".upper(
                )
                writer.writerow(
                    [course['course_id'],
                     'best_price',
                     coupon_code,
                     now.strftime('%Y-%m-%d'),
                     now.strftime('%H:%M')])
                course['start_time'] = now.strftime('%Y-%m-%d %H:%M')
                course['end_time'] = five_days_later.strftime('%Y-%m-%d %H:%M')
                course["link_with_coupon"] = f"{course['course_url']}/?couponCode={coupon_code}"
                course["link_with_referral"] = f"{course['course_url']}/?referralCode={course['referralCode']}"
        # udemy promotion email template
        with open('templates/udemy.j2', encoding="utf-8") as f:
            template = Template(f.read())
            print(template.render(course_list=course_list))
        with open('templates/README-coupon.md.j2', encoding="utf-8") as f:
            template = Template(f.read())
            with open('profile/README.md', 'w', encoding="utf-8") as f:
                f.write(template.render(course_list=course_list))
# with open('templates/README.md.j2') as f:
#     template = Template(f.read())
# with open('profile/README.md', 'w') as f:
#     f.write(template.render(course_list=course_list))


if __name__ == '__main__':
    main()
