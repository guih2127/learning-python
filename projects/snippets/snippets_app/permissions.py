from rest_framework import permissions

# Por fim, para que cada usuário possa editar ou apagar apenas seu próprio snippet,
# estamos criando uma permission customizada.

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

# O que acontece nessa permission? Basicamente, se o metódo for GET, HEAD ou OPTIONS,
# o metódo has_object_permisson sempre retornará True. Caso o contrário, se o metódo for
# um UPDATE, DELETE ou POST, por exemplo, retornaremos True apenas se o obj.owner for igual
# ao request.user.