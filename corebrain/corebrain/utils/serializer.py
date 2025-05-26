"""
Serialization utilities for Corebrain SDK.
"""
import json

from datetime import datetime, date, time
from bson import ObjectId
from decimal import Decimal

class JSONEncoder(json.JSONEncoder):
    """Custom JSON serializer for special types."""
    def default(self, obj):
        # Objects datetime
        if isinstance(obj, (datetime, date, time)):
            return obj.isoformat()
        # Objects timedelta
        elif hasattr(obj, 'total_seconds'):  # For objects timedelta
            return obj.total_seconds()
        # ObjectId from MongoDB
        elif isinstance(obj, ObjectId):
            return str(obj)
        # Bytes o bytearray
        elif isinstance(obj, (bytes, bytearray)):
            return obj.hex()
        # Decimal
        elif isinstance(obj, Decimal):
            return float(obj)
        # Other types
        return super().default(obj)

def serialize_to_json(obj):
    """Serializes any object to JSON using the custom encoder"""
    return json.dumps(obj, cls=JSONEncoder)