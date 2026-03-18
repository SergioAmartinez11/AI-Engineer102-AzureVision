# Azure AI Vision - Image Analysis Sample

This repository contains a Python script that leverages the **Azure AI Vision SDK (v4.0)** to automatically generate captions and tags for local images.

---

## Quick Start

### 1. Prerequisites
* **Python 3.8+**
* An active **Azure Subscription**
* A **Computer Vision** or **Azure AI Services** resource

### 2. Installation
Install the necessary Python packages via the terminal:
```bash
pip install azure-ai-vision-imageanalysis
```

### 3. Project Structure
Ensure your folder is organized as follows:
```
.
├── AzureVisionTest.py   # Your script
├── assets/              # Folder containing your .jpg images
│   └── coffeeShopImage.jpg
└── .env                 # (Optional) For environment variables
```
### 4. Configuration
The script requires your Azure credentials to be set as Environment Variables.
```
VISION_ENDPOINTURL
VISION_KEY
```

### How It Works
The script performs the following operations:

1. Environment Check: Validates that authentication keys are present.
2. Binary Processing: Reads all .jpg files from the ./assets folder into memory as binary data.
3. AI Analysis: Sends the binary data to Azure to request:
4. Captions: A natural language description of the image.
5. Tags: Keywords identifying objects and scenery.
6. Gender Neutrality: Uses gender-neutral terms in descriptions.

### Example output
<img width="1280" height="656" alt="image" src="https://github.com/user-attachments/assets/71898850-ae06-4970-b642-0f43e6b29f6f" />


