"""automated_stock_trading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path, include
from home import views
urlpatterns = [

    # user urls (non registered : guest)
    path('', views.indexPage, name='index'),
    path('login', views.loginPage, name='login'),
    path('signup', views.signupPage, name='signup'),
    path('forget_password', views.forget_password_page, name='forget_password'),

    # registered user
    path("logout", views.logout, name='logout'),
    path('user_page', views.userPage, name='user_page'),
    path('profile', views.profilePage, name='profile'),
    path('edituserprofile', views.edituserprofilePage, name='edituserprofile'),
    path('stock', views.stockPage, name='stock'),
    path('stockView/<int:id>', views.stockViewPage, name='stockView'),
    path('mystocks', views.myStocksPage, name='mystocks'),
    path('mystockView/<int:id>', views.my_stockViewPage, name='mystockView'),
    
    path('bidToStock/<int:id1>/<int:id2>', views.bid_to_stock, name='bidToStock'),
    path('sold_stock/<int:id1>/<int:id2>', views.sold_stock, name='sold_stock'),


    # admin urls
    path('admin', views.admin_indexPage, name='admin'),
    path('adminlogin', views.adminloginPage, name='adminlogin'),
    path('adminhome', views.adminhomePage, name='adminhome'),
    path('adminalluser', views.adminAllUserPage, name='adminalluser'),
    path('adminprofile', views.adminprofilePage, name='adminprofile'),
    path('adminlogout', views.adminlogoutPage, name='adminlogout'),
    path('view_user/<int:id>', views.adminViewUserPage, name='view_user'),
    path('adminEditUserProfile/<int:id>', views.adminEditUserPage, name='edit_user'),
    path('deleteuser/<int:id>', views.adminDeleteUserPage, name='delete_user'),
    path('admin_stock', views.admin_stockPage, name='admin_stock'),
    path('admin_stockView/<int:id>', views.adminstockViewPage, name='admin_stockView'),
    path('deletestock/<int:id>', views.adminDeleteStockPage, name='deletestock'),
    path('admin_update_stock/<int:id>', views.adminUpdateStockPage, name='admin_update_stock'),
    path('admin_add_stock', views.admin_add_stockPage, name='admin_add_stock'),
    path('admin_view_user_stock/<int:id>', views.admin_view_user_stock_page, name='admin_view_user_stock'),



    # for all user
    path('terms_and_condition', views.terms_and_condition_page, name='terms_and_condition'),
    path('privacy_policy', views.privacy_policy_page, name='privacy_policy'),

    # just for data saving perpose
    # path('add_stock_data', views.addStockData, name='add_stock_data'),

    # for testing
    # path('table', views.table_show, name='table'),

]