class GDPRCompliance:
    def validate_data_minimization(self, data):
        """
        Validate data minimization principle.
        
        Args:
            data (dict): Input data to validate.
        
        Returns:
            bool: True if data complies with minimization principle, False otherwise.
        """
        # Example rule: No excessive data fields
        required_fields = {"name", "email"}
        extra_fields = set(data.keys()) - required_fields
        return len(extra_fields) == 0

    def validate_right_to_access(self, request_log):
        """
        Validate if user access requests are logged.
        
        Args:
            request_log (list): List of access request logs.
        
        Returns:
            bool: True if all requests are logged, False otherwise.
        """
        return all("user_id" in req and "timestamp" in req for req in request_log)
