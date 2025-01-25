from .metadata_manager import MetadataManager

def get_data_masking():
    from ..masking.masking import DataMasking
    return DataMasking
