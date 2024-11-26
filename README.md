# azure-ai-labs
ThisA collection of hands-on labs, tutorials, and resources for exploring Azure AI capabilities. This repository provides an overview of Azure’s AI services and practical projects for real-world applications. Topics include Machine Learning, Cognitive Services, Computer Vision, Natural Language Processing, and more.

#01Azure-lab-restclient.py
This script uses Azure AI’s Text Analytics service to detect the language of a given text input by the user. It leverages environment variables to securely manage the service’s endpoint and API key, making the script easy to configure and secure. Here’s how it works:

Key Features
Environment Variable Configuration: The script loads the Azure AI service endpoint and API key from a .env file.
Language Detection via Text Analytics: It uses Azure’s Text Analytics API to identify the language of any user-provided text.
Interactive Prompt: Users can input text until they enter “quit” to stop the program.

Programs lists:

1.Get Started with Azure AI Services : Sdk-client.py

2.Analyze Images with Azure AI Vision : image-analysis.py

3.Read Text in Images : Read-text.py

4.Classify images with a Azure AI Vision custom model : Same above code

./replace.ps1 Image-classification.

5.Analyze Text : Analyze-load.py

6.Create a Question Answering Solution : Ana-app.py

7.Create a language understanding model with the Language service : Clock-client.py

8.Recognize and synthesize speech : Speaking-clock.py

9.Integrate Azure OpenAI into your app : Test-openai-model.py

10.Utilize prompt engineering in your app : Prompt-engineering.py

11.Use your own data with Azure OpenAI : ownData.py
