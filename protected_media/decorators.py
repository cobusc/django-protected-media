from django.http import Http404
from functools import wraps
from django.utils.module_loading import import_string


def permission_check(permission_func_path):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            path = kwargs.get("path", "")
            try:
                permission_func = import_string(permission_func_path)
            except AttributeError:
                permission_func = None
            if permission_func and not permission_func(request.user, path):
                raise Http404()
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
