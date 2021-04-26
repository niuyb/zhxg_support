from django.utils.deprecation import MiddlewareMixin
from xman.views._module import get_module_tree

class SidebarMiddleware(MiddlewareMixin):

    def process_request(self, request):
        accept = request.META.get("HTTP_ACCEPT", "")
        if not accept.startswith("application/json"):
            request.modules = get_module_tree(request, status=True, show=True)