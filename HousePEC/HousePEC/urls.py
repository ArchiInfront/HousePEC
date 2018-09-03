"""
Definition of urls for HousePEC.
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from pecbyapi import views
from accounts import views as accounts_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# Admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Login
urlpatterns += [
    url(r'^signup/$', accounts_views.signup, name='signup')
    ]

urlpatterns += [
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout')
    ]

urlpatterns += [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login')
    ]

urlpatterns += [
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),    
    ]

urlpatterns += [
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),    
    ]

#Home
urlpatterns += [
    url(r'^$', views.home, name='home')
    ]

#HouseBasic
urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/$', views.house_list, name='house_list')
    #url(r'^builder/(?P<pk>\d+)/$', views.HouseListView.as_view(), name='house_list')
    ]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/detail/$', views.house_list_detail, name='house_list_detail')    
    ]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/delete/$', views.house_confirm_delete, name='house_confirm_delete')    
    ]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/update/$', views.house_update, name='house_update')    
    #url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/update/$', views.HouseUpdateView.as_view(), name='house_update')    
    ]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/update/detail/$', views.house_update_detail, name='house_update_detail')    
    ]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/copy/$', views.house_copy, name='house_copy')    
    #url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/copy/$', views.HouseCopyView.as_view(), name='house_copy')    
    ]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/new/$', views.house_new, name='house_new')
    #url(r'^builder/(?P<pk>\d+)/new/$', views.NewHouseView.as_view(), name='new_house')
    ]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/new/detail/$', views.house_new_detail, name='house_new_detail')
    ]


# HaouseSpec
urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/$', views.spec_list, name='spec_list')    
    #url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/$', views.SpecListView.as_view(), name='spec_list')    
]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/new/$', views.spec_new, name='spec_new')    
]

#urlpatterns += [
#    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/new/detail/$', views.spec_new_detail, name='spec_new_detail')    
#]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/spec/(?P<spec_pk>\d+)/update/$', views.spec_update, name='spec_update')
]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/spec/(?P<spec_pk>\d+)/copy/$', views.spec_copy, name='spec_copy')
]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/spec/(?P<spec_pk>\d+)/delete/$', views.spec_confirm_delete, name='spec_confirm_delete')
]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/calc/$', views.spec_calc, name='spec_calc')
]

urlpatterns += [
    url(r'^builder/(?P<pk>\d+)/house/(?P<house_pk>\d+)/test/$', views.spec_calc_test, name='spec_calc_test')
]

