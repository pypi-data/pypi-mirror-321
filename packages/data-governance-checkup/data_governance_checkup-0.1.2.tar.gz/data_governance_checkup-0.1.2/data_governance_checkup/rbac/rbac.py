class RBACManager:
    def __init__(self):
        # Initialize roles, users, and permissions dictionaries
        self.roles = {}
        self.users = {}

    def create_role(self, role_name):
        """Create a new role."""
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles[role_name] = set()

    def assign_permission_to_role(self, role_name, permission):
        """Assign a permission to a role."""
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.roles[role_name].add(permission)

    def create_user(self, user_id):
        """Create a new user."""
        if user_id in self.users:
            raise ValueError(f"User '{user_id}' already exists.")
        self.users[user_id] = set()

    def assign_role_to_user(self, user_id, role_name):
        """Assign a role to a user."""
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' does not exist.")
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.users[user_id].add(role_name)

    def has_permission(self, user_id, permission):
        """Check if a user has a specific permission."""
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' does not exist.")
        # Check all roles assigned to the user for the permission
        for role in self.users[user_id]:
            if permission in self.roles[role]:
                return True
        return False

    def get_user_permissions(self, user_id):
        """Get all permissions for a user."""
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' does not exist.")
        permissions = set()
        for role in self.users[user_id]:
            permissions.update(self.roles[role])
        return permissions

    def revoke_role_from_user(self, user_id, role_name):
        """Revoke a role from a user."""
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' does not exist.")
        if role_name not in self.users[user_id]:
            raise ValueError(f"User '{user_id}' does not have role '{role_name}'.")
        self.users[user_id].remove(role_name)
