from .gdpr_validator import GDPRCompliance
from .hipaa_validator import HIPAACompliance
from .ccpa_validator import CCPACompliance
from .iso27001_validator import ISO27001Compliance

class ComplianceFrameworkValidator:
    def __init__(self):
        self.validators = {
            "GDPR": GDPRCompliance(),
            "HIPAA": HIPAACompliance(),
            "CCPA": CCPACompliance(),
            "ISO27001": ISO27001Compliance(),
        }

    def validate(self, framework, data, validation_type=None):
        """
        Validate data against a specific compliance framework.

        Args:
            framework (str): Compliance framework name.
            data (dict): Data to validate.
            validation_type (str, optional): Specific validation type for CCPA.

        Returns:
            bool: Validation result.
        """
        if framework not in self.validators:
            raise ValueError(f"Unsupported compliance framework: {framework}")
        validator = self.validators[framework]

        if framework == "CCPA":
            if validation_type == "opt_out":
                return validator.validate_opt_out(data)
            elif validation_type == "deletion_requests":
                return validator.validate_deletion_requests(data)
            else:
                raise ValueError("Invalid validation type for CCPA")
        else:
            results = []
            for method in dir(validator):
                if method.startswith("validate_"):
                    validation_method = getattr(validator, method)
                    results.append(validation_method(data))
            return all(results)
