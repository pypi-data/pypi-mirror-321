import re
class DataMasking:
    def __init__(self):
        pass

    def mask_data(self, data, mask_fields):
        """Mask sensitive fields in the given data."""
        masked_data = data.copy()
        for field in mask_fields:
            if field in masked_data:
                masked_data[field] = "*****"
        return masked_data
    