from django.db.models.deletion import ProtectedError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def handle_exceptions(exception: Exception, context: dict):
    """
    Custom exception handler to handle registered in EXCEPTION_HANDLERS exceptions 
    """
    response = exception_handler(exception, context)
    if handler := EXCEPTION_HANDLERS.get(type(exception)):
        response = handler(exception=exception)
    return response


def handle_protected_error(exception: ProtectedError) -> Response:
    """
    Handler for ProtectedError exception.
    Returns Response with list of protected objects and 409 status code.
    """
    protected_objects = list(exception.protected_objects)
    data = {
        'detail': "Cannot delete due to existing references",
        'protected_objects': [
            {
                'id': obj.id,
                'model': obj._meta.model_name,
                'str': str(obj)
            } 
            for obj in protected_objects
        ],
        'count': len(protected_objects)
    }
    return Response(data, status=status.HTTP_409_CONFLICT)


EXCEPTION_HANDLERS = {
    ProtectedError: handle_protected_error,
}
