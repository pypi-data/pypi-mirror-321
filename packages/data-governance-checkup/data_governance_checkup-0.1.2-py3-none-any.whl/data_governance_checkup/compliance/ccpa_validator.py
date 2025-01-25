class CCPACompliance:
    def validate_opt_out(self, data):
        """
        Validate CCPA data sales opt-out compliance.
        
        Args:
            data (dict): Input data to validate.
        
        Returns:
            bool: True if data sales opt-out is enabled, False otherwise.
        """
        return data.get("data_sales_opt_out", False)

    def validate_deletion_requests(self, deletion_log):
        """
        Validate if deletion requests comply with CCPA standards.
        
        Args:
            deletion_log (list): List of deletion request entries.
        
        Returns:
            bool: True if all deletion requests are completed, False otherwise.
        """
        if not isinstance(deletion_log, list) or not all(isinstance(req, dict) for req in deletion_log):
            raise ValueError("The 'deletion_log' must be a list of dictionaries.")
        return all(req.get("status") == "completed" for req in deletion_log)
