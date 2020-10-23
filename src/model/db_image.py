from minio import Minio
from minio.error import ResponseError
class DBImage():
    def __init__(self):
        self.client = Minio('192.168.56.2:9000', access_key='minioadmin', secret_key='minioadmin', secure=False)
        self.bucket_name = 'hardorm-images'
        self.create_bucket()
    def create_bucket(self):
        found = self.client.bucket_exists(self.bucket_name)
        if not found:
            self.client.make_bucket(self.bucket_name)
    def insert_to_minio_server(self,name,data,length):
        print(data)
        return self.client.put_object(
            self.bucket_name,name,data,length
        )
        
