
pip install django==1.11.2
cd /Users/pengtao/code/mysite/mydjango
mkdir student_house
cd student_house && django-admin startproject student_sys
cd student_sys
python manage.py startapp student



python manage.py makemigrations 创建迁移文件
python manage.py migrate 创建表
python manage.py createsuperuser 根据提示，输出用户名，邮箱，密码
