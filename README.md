# dhruv

user register url :
http://127.0.0.1:8000/api/user/register/

request payload:
{
    "email" : "rathoddhruv77@gmail.com",
    "name" : "Dhruv Rathod",
    "password" : "1234",
    "password2" : "1234"

}

login url:
http://127.0.0.1:8000/api/user/login/

request payload:

{
    "email" : "rathoddhruv77@gmail.com",
    "password" : "1234"
}

todo create url:
http://127.0.0.1:8000/api/create/

request payload:

{
    "title" : "pepsi",
    "description" : "this is colddrink",
    "category" : "colddrink",
     "user": 1
}

get url:
for all data : http://127.0.0.1:8000/api/

for searching data: http://127.0.0.1:8000/api/?search=colddrink     in searching use title, category or due date

update url : http://127.0.0.1:8000/api/1/
request payload:

{
    "title" : "Cord4",
    "description" : "this is It Company",
    "category" : "IT",
    "user": 1
}

delete url : http://127.0.0.1:8000/api/delete/

{
    "id" : [1]
}