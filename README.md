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

   Understood. Here is a brief user flow with the provided information:

# NCRP Assistant User Flow

The NCRP Assistant provides a seamless experience for users to submit and manage their complaints. The key steps in the user flow are:

1. **Complaint Submission**: Users can easily submit their complaints through the NCRP Assistant application. 

2. **Categorization and Suggestions (Version 2)**: As the user is typing their complaint, the NCRP Assistant's powerful AI models analyze the input and provide real-time categorization as well as smart suggestions to help the user improve the quality and clarity of their complaint.

3. **Personalized Recommendations**: The NCRP Assistant leverages the user's previous complaint history and the organization's knowledge base to suggest relevant information, resources, or actions that can help resolve the issue more effectively.

4. **Efficient Complaint Management**: The NCRP Assistant's advanced categorization and suggestion capabilities enable organizations to quickly understand the nature of the complaint and provide a more tailored response, leading to better outcomes for all stakeholders.

Refer to the diagram below for a visual representation of the NCRP Assistant user flow:

![User Flow of NCRP Assistant](https://github.com/user-attachments/assets/e80b9dbd-4fcd-4b86-8f35-e9e075c31710)
   
Refer to the video below for a guide on running the NCRP Assistant Streamlit App.


https://github.com/user-attachments/assets/16adfe89-cce3-479d-988f-7d4d2f0deef7
