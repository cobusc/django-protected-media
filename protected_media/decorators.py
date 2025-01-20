from django.http import Http404
from functools import wraps
from django.utils.module_loading import import_string


def permission_check(permission_func_path):
    """
        Decorator to apply permission checks for the view for the file.

        Args:
            permission_func_path (str): A dotted string path to a permission function.
                                        The function should accept two arguments: `user` and `path`,
                                        and return `True` if the user has permission, or `False` otherwise.

        Returns:
            function: The decorated view with permission check logic applied.

        Raises:
            Http404: If the permission function returns `False` or the user lacks the necessary access.
        """
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
