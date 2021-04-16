from django.urls import path
from api.views import fbv
from api.views.auth import UserList, login, logout

urlpatterns = [
    path('companies/', fbv.companies),
    path('companies/<int:company_id>/', fbv.company_details),
    path('companies/<int:company_id>/vacancies/', fbv.get_vacancies_by_company),

    path('vacancies/', fbv.vacancies),
    path('vacancies/<int:vacancy_id>/', fbv.vacancy_details),
    path('vacancies/top_ten/', fbv.get_top_ten_vacancies),

    path('users/', UserList.as_view()),
    path('login/', login),
    path('logout/', logout)
]