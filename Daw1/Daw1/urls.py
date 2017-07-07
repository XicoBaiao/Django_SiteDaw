from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from carts.views import CartView, CheckoutView

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'Daw1.views.about', name='about'),
    url(r'^simulation/$', 'newsletter.views.simulation', name='simulation'),
    # url(r'^cart/$', 'newsletter.views.viewcart', name='cart'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^simulacoes/', include('simulacoes.urls')),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)