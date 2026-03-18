from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import os


# Try to fetch env variables to authenticate
try:
    endpoint = os.environ["VISION_ENDPOINT"]
    key = os.environ["VISION_KEY"]
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

folder_path = './assets'
image_binaries = {}
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg')):
        file_path = os.path.join(folder_path, filename)
        # Open in 'rb' (read binary) mode
        with open(file_path, 'rb') as f:
            binary_data = f.read()
            image_binaries[filename] = binary_data



client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

result = client.analyze(
    image_data=image_binaries['coffeeShopImage.jpg'], # Binary data from your image file
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS],
    gender_neutral_caption=True,
)

print(result)