import json

class MetadataManager:
    def __init__(self):
        """Initialize the Metadata Manager with an in-memory metadata store."""
        self.metadata_store = {}

    def add_metadata(self, resource_id, metadata):
        """
        Add metadata for a given resource.
        
        Args:
            resource_id (str): Unique identifier for the resource.
            metadata (dict): Metadata to associate with the resource.
        """
        if resource_id in self.metadata_store:
            raise ValueError(f"Metadata for resource ID '{resource_id}' already exists.")
        self.metadata_store[resource_id] = metadata

    def update_metadata(self, resource_id, updated_metadata):
        """
        Update metadata for a given resource.
        
        Args:
            resource_id (str): Unique identifier for the resource.
            updated_metadata (dict): Updated metadata to merge with existing metadata.
        """
        if resource_id not in self.metadata_store:
            raise ValueError(f"No metadata found for resource ID '{resource_id}'.")
        self.metadata_store[resource_id].update(updated_metadata)

    def get_metadata(self, resource_id):
        """
        Retrieve metadata for a given resource.
        
        Args:
            resource_id (str): Unique identifier for the resource.
        
        Returns:
            dict: Metadata associated with the resource.
        """
        return self.metadata_store.get(resource_id, {})

    def delete_metadata(self, resource_id):
        """
        Delete metadata for a given resource.
        
        Args:
            resource_id (str): Unique identifier for the resource.
        """
        if resource_id in self.metadata_store:
            del self.metadata_store[resource_id]
        else:
            raise ValueError(f"No metadata found for resource ID '{resource_id}'.")

    def list_all_metadata(self):
        """
        List all metadata entries.
        
        Returns:
            dict: All metadata entries in the store.
        """
        return self.metadata_store

    def save_metadata_to_file(self, filepath):
        """
        Save all metadata to a file in JSON format.
        
        Args:
            filepath (str): Path to the file where metadata will be saved.
        """
        with open(filepath, "w") as f:
            json.dump(self.metadata_store, f, indent=4)

    def load_metadata_from_file(self, filepath):
        """
        Load metadata from a JSON file.
        
        Args:
            filepath (str): Path to the file containing metadata in JSON format.
        """
        with open(filepath, "r") as f:
            self.metadata_store = json.load(f)
