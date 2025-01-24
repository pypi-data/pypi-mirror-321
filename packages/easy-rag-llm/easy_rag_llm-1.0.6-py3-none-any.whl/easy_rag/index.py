import os
import faiss
import json

class IndexManager:
    def save(self, index, metadata, index_file="faiss_index.bin", metadata_file="metadata.json"):
        faiss.write_index(index, index_file)
        with open(metadata_file, "w") as f:
            json.dump(metadata, f)
        print(f"Index saved to {index_file}, metadata saved to {metadata_file}")

    def load(self, index_file="faiss_index.bin", metadata_file="metadata.json"):
        if not os.path.exists(index_file) or not os.path.exists(metadata_file):
            print("Index or metadata file not found.")
            return None, None
        index = faiss.read_index(index_file)
        with open(metadata_file, "r") as f:
            metadata = json.load(f)
        print(f"Index loaded from {index_file}, metadata loaded from {metadata_file}")
        return index, metadata
