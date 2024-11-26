# azure-ai-labs
ThisA collection of hands-on labs, tutorials, and resources for exploring Azure AI capabilities. This repository provides an overview of Azure’s AI services and practical projects for real-world applications. Topics include Machine Learning, Cognitive Services, Computer Vision, Natural Language Processing, and more.

#01Azure-lab-restclient.py
This script uses Azure AI’s Text Analytics service to detect the language of a given text input by the user. It leverages environment variables to securely manage the service’s endpoint and API key, making the script easy to configure and secure. Here’s how it works:

Key Features
Environment Variable Configuration: The script loads the Azure AI service endpoint and API key from a .env file.
Language Detection via Text Analytics: It uses Azure’s Text Analytics API to identify the language of any user-provided text.
Interactive Prompt: Users can input text until they enter “quit” to stop the program.

