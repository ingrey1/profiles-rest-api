from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """allow users to update their own status"""
    def has_object_permission(self, request, view, obj):
        """check if the user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id 