
# **FairSense-AI**

Fairsense-AIis a cutting-edge, AI-driven platform designed to promote transparency, fairness, and equity by analyzing bias in textual and visual content. Built with sustainability in mind, it leverages energy-efficient AI frameworks to ensure an eco-friendly approach to tackling societal biases.

---

## **Installation and Setup**

### **Step 1: Install Fair-Sense-AI**

Install the Fair-Sense-AI package using pip:

```bash
pip install Fair-Sense-AI
```

---

### **Step 2: Quickstart Code Examples**

#### **1. Text Bias Analysis**

```python
from fairsenseai import analyze_text_for_bias

# Example input text to analyze for bias
text_input = "Men are naturally better at decision-making, while women excel at emotional tasks."

# Analyze the text for bias
highlighted_text, detailed_analysis = analyze_text_for_bias(text_input)

# Print the analysis results
print("Highlighted Text:", highlighted_text)
print("Detailed Analysis:", detailed_analysis)
```

#### **2. Image Bias Analysis**

```python
import requests
from PIL import Image
from io import BytesIO
from fairsenseai import analyze_image_for_bias

# URL of the image to analyze
image_url = "https://media.top1000funds.com/wp-content/uploads/2019/12/iStock-525807555.jpg"

# Fetch and load the image
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Analyze the image for bias
highlighted_caption, image_analysis = analyze_image_for_bias(image)

# Print the analysis results
print("Highlighted Caption:", highlighted_caption)
print("Image Analysis:", image_analysis)
```

#### **3. Launch the Interactive Application**

```python
from fairsenseai import main

# Launch the Gradio application (will open in the browser)
main()
```

---
## **Bias Detection Tutorial**

### **Data and Sample Notebooks**

1. **Download the Data**:  
   [Google Drive Link](https://drive.google.com/drive/folders/1_D7lTz-TC6yhV7xsZIDzk-tJvl4TAwyi?usp=sharing)

2. **Colab Notebook**:  
   [Run the Tutorial](https://colab.research.google.com/drive/1en8JtZTAIa5MuV5OZWYNteYl95Ql9xy7?usp=sharing)

---

## **Prerequisites**

1. **Python 3.7+**  
   Ensure Python is installed. Download it [here](https://www.python.org/downloads/).

2. **Tesseract OCR**  
   Required for extracting text from images.

   #### Installation Instructions:
   - **Ubuntu**:
     ```bash
     sudo apt-get update
     sudo apt-get install tesseract-ocr
     ```
   - **macOS (Homebrew)**:
     ```bash
     brew install tesseract
     ```
   - **Windows**:  
     Download and install Tesseract OCR from [this link](https://github.com/UB-Mannheim/tesseract/wiki).

3. **Optional (GPU Acceleration)**  
   Install PyTorch with CUDA support:

   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
   ```

---

## **Usage Instructions**

### **Launching the Application**

Run the following command to start Fair-Sense-AI:

```bash
Fair-Sense-AI
```

This will launch the Gradio-powered interface in your default web browser.

---

### **Features**

#### **1. Text Analysis**
- Input or paste text in the **Text Analysis** tab.
- Click **Analyze** to detect and highlight biases.

#### **2. Image Analysis**
- Upload an image in the **Image Analysis** tab.
- Click **Analyze** to detect biases in embedded text or captions.

#### **3. Batch Text CSV Analysis**
- Upload a CSV file with a `text` column in the **Batch Text CSV Analysis** tab.
- Click **Analyze CSV** to process all entries.

#### **4. Batch Image Analysis**
- Upload multiple images in the **Batch Image Analysis** tab.
- Click **Analyze Images** for a detailed review.

#### **5. AI Governance Insights**
- Navigate to the **AI Governance and Safety** tab.
- Choose a predefined topic or input your own query.
- Click **Get Insights** for recommendations.

---



### **Additional Setup in Colab**

Run the following commands to ensure everything is ready:

```bash
!pip install --quiet fair-sense-ai
!pip uninstall sympy -y
!pip install sympy --upgrade
!apt update
!apt install -y tesseract-ocr
```

**Note**: Restart your system if you're using Google Colab.

---

## **Troubleshooting**

- **Slow Model Download**:  
  Ensure a stable internet connection for downloading models.

- **Tesseract OCR Errors**:  
  Verify Tesseract is installed and accessible in your system's PATH.

- **GPU Support**:  
  Use the CUDA-compatible version of PyTorch for better performance.

---

## **Contact**

For inquiries or support, contact:  
**Shaina Raza, PhD**  
Applied ML Scientist, Responsible AI  
[shaina.raza@vectorinstitute.ai](mailto:shaina.raza@torontomu.ca)

---

## **License**

This project is licensed under the [Creative Commons License](https://creativecommons.org/licenses/).

---

