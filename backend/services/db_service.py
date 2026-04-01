from pymongo import MongoClient
from typing import Dict, List, Optional
from datetime import datetime
from config import MONGODB_URL, DATABASE_NAME


class DatabaseService:
    def __init__(self):
        self.client = MongoClient(MONGODB_URL)
        self.db = self.client[DATABASE_NAME]
        self.marking_schemes = self.db["marking_schemes"]
        self.evaluations = self.db["evaluations"]
        self.batches = self.db["batches"]
    
    @staticmethod
    def serialize_doc(doc):
        """Convert MongoDB document to JSON-serializable dictionary"""
        if not doc:
            return None
        
        doc_copy = dict(doc)
        if '_id' in doc_copy:
            doc_copy['_id'] = str(doc_copy['_id'])
        if 'created_at' in doc_copy:
            doc_copy['created_at'] = doc_copy['created_at'].isoformat()
        return doc_copy

    def save_marking_scheme(self, file_name: str, content: str, embeddings: dict = None) -> str:
        """Save marking scheme to database"""
        try:
            doc = {
                "file_name": file_name,
                "content": content,
                "embeddings_dir": embeddings,
                "created_at": datetime.utcnow()
            }
            result = self.marking_schemes.insert_one(doc)
            return str(result.inserted_id)
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")

    def get_marking_scheme(self, scheme_id: str):
        """Retrieve marking scheme"""
        try:
            from bson.objectid import ObjectId
            # Try to find by ObjectId first
            try:
                result = self.marking_schemes.find_one({"_id": ObjectId(scheme_id)})
                if result:
                    return result
            except:
                pass
            
            # Try to find by scheme_id field
            result = self.marking_schemes.find_one({"scheme_id": scheme_id})
            return result
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")

    def save_evaluation(self, batch_id: str, script_name: str, evaluation_result: dict) -> str:
        """Save evaluation result"""
        try:
            doc = {
                "batch_id": batch_id,
                "script_name": script_name,
                "result": evaluation_result,
                "created_at": datetime.utcnow()
            }
            result = self.evaluations.insert_one(doc)
            return str(result.inserted_id)
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")

    def create_batch(self, marking_scheme_id: str, total_scripts: int) -> str:
        """Create evaluation batch"""
        try:
            from bson.objectid import ObjectId
            # Generate a user-friendly batch ID
            batch_number = self.batches.count_documents({}) + 1
            batch_id_str = f"BATCH_{batch_number:04d}"
            
            doc = {
                "batch_id": batch_id_str,
                "marking_scheme_id": marking_scheme_id,
                "total_scripts": total_scripts,
                "evaluated_scripts": 0,
                "status": "pending",
                "created_at": datetime.utcnow()
            }
            result = self.batches.insert_one(doc)
            # Return the user-friendly batch ID
            return batch_id_str
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")

    def get_batch(self, batch_id: str):
        """Get batch details"""
        try:
            from bson.objectid import ObjectId
            # Try to find by ObjectId first
            try:
                result = self.batches.find_one({"_id": ObjectId(batch_id)})
                if result:
                    return result
            except:
                pass
            
            # Try to find by batch_id field
            result = self.batches.find_one({"batch_id": batch_id})
            return result
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")

    def update_batch_status(self, batch_id: str, status: str, evaluated_count: int = None):
        """Update batch status"""
        try:
            from bson.objectid import ObjectId
            update_data = {"status": status}
            if evaluated_count is not None:
                update_data["evaluated_scripts"] = evaluated_count
            
            # Try to update by ObjectId first
            try:
                result = self.batches.update_one(
                    {"_id": ObjectId(batch_id)},
                    {"$set": update_data}
                )
                if result.matched_count > 0:
                    return
            except:
                pass
            
            # Try to update by batch_id field
            self.batches.update_one(
                {"batch_id": batch_id},
                {"$set": update_data}
            )
        except Exception as e:
            raise Exception(f"Database Error: {str(e)}")
