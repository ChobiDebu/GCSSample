from google.cloud import storage as gcs
import tempfile


class GCSUtil():
    # Class to access GCS
    # Refer to https://googleapis.github.io/google-cloud-python/latest/storage/client.html

    def Read(self, project, bucket, fileName):

        # Create client
        client = gcs.Client(project)
        # Get bucket
        bucket = client.get_bucket(bucket)
        # Create Blob
        blob = gcs.Blob(fileName, bucket)
        # Download file as string
        content = blob.download_as_string()
        return content

    def Write(self, project, bucket, fileName, text):

        # Create client
        client = gcs.Client(project)
        # Get bucket
        bucket = client.get_bucket(bucket)
        # Create Blob
        blob = gcs.Blob(fileName, bucket)
        # Write string to file
        blob.upload_from_string(text)

    def Download(self, project, bucket, fileName):

        # Create client
        client = gcs.Client(project)
        # Get bucket
        bucket = client.get_bucket(bucket)
        # Create Blob
        blob = gcs.Blob(fileName, bucket)
        # Write string to file
        temp_filename = tempfile.mktemp()
        with open(temp_filename, "wb") as file_obj:
            client.download_blob_to_file(blob, file_obj)
        return temp_filename

    def Upload(self, project, bucket, localFileName, gcsFileName):

        # Create client
        client = gcs.Client(project)
        # Get bucket
        bucket = client.get_bucket(bucket)
        # Create Blob to Upload
        blob = gcs.Blob(gcsFileName, bucket)
        # Upload
        blob.upload_from_filename(filename=localFileName)

    def Copy(self, project, srcbucket, srcFileName, destbucket, destFileName):

        # Download srcFile to local
        downloadFile = self.Download(project, srcbucket, srcFileName)
        # Upload file
        self.Upload(project, destbucket, downloadFile, destFileName)

    def Copy2(self, srcPath, destPath):

        # Download a blob using a URI.(Not working)
        # Create client
        client = gcs.Client()
        temp_filename = tempfile.mktemp()
        with open(temp_filename, "wb") as file_obj:
            client.download_blob_to_file(srcPath, file_obj)

        # Create client
        client = gcs.Client('ShigaRedirectMock')
        # Get bucket
        bucket = client.get_bucket('shiga_test_backet')
        # Create Blob
        blob2 = bucket.blob(destPath)
        blob2.upload_from_filename(filename=temp_filename)
