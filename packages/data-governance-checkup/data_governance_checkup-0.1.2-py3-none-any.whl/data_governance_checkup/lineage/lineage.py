import json
from typing import Dict, List, Optional

class DataLineageTracker:
    """
    Tracks data lineage by recording the source, transformations, and destination of data.
    """

    def __init__(self):
        self.lineage_data = {}

    def add_source(self, data_id: str, source_details: Dict):
        """
        Add a source to the lineage.
        
        Args:
            data_id (str): Unique identifier for the data.
            source_details (Dict): Details about the data source (e.g., filename, database).
        """
        self.lineage_data[data_id] = {
            "source": source_details,
            "transformations": [],
            "destination": None,
        }

    def add_transformation(self, data_id: str, transformation: str):
        """
        Record a transformation step for the data.
        
        Args:
            data_id (str): Unique identifier for the data.
            transformation (str): Description of the transformation performed.
        """
        if data_id not in self.lineage_data:
            raise ValueError(f"Data ID {data_id} not found in lineage.")
        
        self.lineage_data[data_id]["transformations"].append(transformation)

    def set_destination(self, data_id: str, destination_details: Dict):
        """
        Set the destination for the data.
        
        Args:
            data_id (str): Unique identifier for the data.
            destination_details (Dict): Details about the data destination (e.g., filename, table).
        """
        if data_id not in self.lineage_data:
            raise ValueError(f"Data ID {data_id} not found in lineage.")
        
        self.lineage_data[data_id]["destination"] = destination_details

    def get_lineage(self, data_id: str) -> Optional[Dict]:
        """
        Retrieve the lineage for a specific data ID.
        
        Args:
            data_id (str): Unique identifier for the data.
        
        Returns:
            Optional[Dict]: Lineage details if data ID exists, else None.
        """
        return self.lineage_data.get(data_id)

    def export_lineage(self, file_path: str):
        """
        Export lineage data to a JSON file.
        
        Args:
            file_path (str): File path to save the lineage data.
        """
        with open(file_path, "w") as file:
            json.dump(self.lineage_data, file, indent=4)

    def import_lineage(self, file_path: str):
        """
        Import lineage data from a JSON file.
        
        Args:
            file_path (str): File path to load the lineage data.
        """
        with open(file_path, "r") as file:
            self.lineage_data = json.load(file)
