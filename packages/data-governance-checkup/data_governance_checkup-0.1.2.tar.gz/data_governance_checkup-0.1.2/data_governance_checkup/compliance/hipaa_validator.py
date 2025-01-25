class HIPAACompliance:
    def validate_privacy_rule(self, data):
        """
        Validate HIPAA privacy rule compliance.
        
        Args:
            data (dict): Input data to validate.
        
        Returns:
            bool: True if no unauthorized PHI exposure, False otherwise.
        """
        return "PHI" not in data.get("exposure", [])

    def validate_security_rule(self, security_log):
        """
        Validate if security logs follow HIPAA standards.
        
        Args:
            security_log (list): Security log entries.
        
        Returns:
            bool: True if logs contain required details, False otherwise.
        """
        security_log = security_log['security_log']
        if not isinstance(security_log, list) or not all(isinstance(log, dict) for log in security_log):
            raise ValueError("The 'security_log' must be a list of dictionaries.")
        required_fields = {"user_id", "access_time"}
        return all(required_fields.issubset(log.keys()) for log in security_log)
