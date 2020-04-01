from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #ie we dont explicitly need to check their permissions if the request is within the safe methods
            return True
        
        return obj.id == request.user.id #does the id of the user making the request match the id of the user whose profile they want to modify