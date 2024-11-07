# NCRP Assistant - Streamlit App

## Prerequisites
- Anaconda for managing environments
- Python 3.9.4
- Google Cloud Service Account key (if applicable)

## Steps to Follow

1. **Create a New Environment**
   ```bash
   conda create -n venv python==3.9.4
   ```

2. **Activate the Virtual Environment**
   ```bash
   conda activate venv
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your Gemini Google API Key**
   1. Open the `env.txt` file in the project directory.
   2. Add your Gemini Google API key, like this:
      ```plaintext
      GEMINI_API_KEY=YOUR_GEMINI_API_KEY
      ```

5. **Set Up Google Cloud Authentication (If Applicable)**
   - **Create a Service Account Key**:
     1. In the Google Cloud Console, go to **IAM & Admin > Service Accounts**.
     2. Select your project and click **Create Service Account**.
     3. Assign the required permissions to the service account.
     4. Download the JSON key file.
   - **Set the `GOOGLE_APPLICATION_CREDENTIALS` Environment Variable**:
     - On Linux/macOS:
       ```bash
       export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-file.json"
       ```
     - On Windows:
       ```cmd
       set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\service-account-file.json
       ```
   - **Troubleshooting**: If you encounter issues such as `Compute Engine Metadata server unavailable` or `Gemini Model Initialization Failed`, confirm that the `GOOGLE_APPLICATION_CREDENTIALS` path is correct and the environment variable is set.

6. **Run the Streamlit Application**
   ```bash
   streamlit run app.py
   ```
   If the application fails due to authentication issues, revisit **Step 5** for setting up the service account key.

   
Refer to the video below for a guide on running the NCRP Assistant Streamlit App.


https://github.com/user-attachments/assets/16adfe89-cce3-479d-988f-7d4d2f0deef7
