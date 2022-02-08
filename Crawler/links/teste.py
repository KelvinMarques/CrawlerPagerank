from django.test import RequestFactory

from links.views import crawlerView



request_factory = RequestFactory()
my_url = 'http://mtwitt.herokuapp.com/'  # Replace with your URL -- or use reverse
my_request = request_factory.get(my_url)
response = crawlerView.as_view()(my_request)  # Replace with your view
response.render()
print(response)