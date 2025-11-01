Neurofiq Unified Content Creation Agent
=======================================

This project is a sophisticated, all-in-one content creation and deployment agent. Built with Python, it automates the entire blogging workflow, from initial topic research to final deployment on a live server. The agent is designed to be an elite content specialist, combining SEO research, advanced content writing, and web deployment into a seamless, conversational experience.

Overview
--------

The Unified Content Creation Agent is a powerful command-line application that interacts with the user to generate and publish high-quality, SEO-optimized blog posts. It leverages the agno framework to structure its operations, integrates with large language models via Ollama, and uses custom tools for functionalities like image uploading and cPanel deployment. The agent is meticulously instructed to follow a multi-phase workflow, ensuring that every piece of content is well-researched, well-written, and technically sound.

Features
--------

*   **End-to-End Automation**: Handles the entire content lifecycle: from gathering requirements and performing SEO research to writing, formatting, and deploying the content.
    
*   **Advanced SEO Research**: Conducts in-depth research using Searxng and DuckDuckGo to find high-volume keywords, analyze competitors, and understand user intent.
    
*   **High-Quality Content Generation**: Writes comprehensive, 3000-word articles that are fact-checked, humanized, and optimized for search engines, passing AI detection.
    
*   **Dynamic HTML Conversion**: Converts the generated markdown content into a complete, styled HTML page using a predefined template with Tailwind CSS.
    
*   **Automated Deployment**: Deploys the final HTML file directly to a cPanel server and provides the user with a permalink.
    
*   **Featured Image Support**: Allows users to specify a local image, which the agent uploads to ImgBB and includes in the blog post.
    
*   **Persistent Memory**: Uses an SQLite database to maintain session state, such as storing the featured image URL and deployment permalink.
    
*   **Interactive CLI**: Provides a user-friendly command-line interface for easy interaction.
    

Workflow
--------

The agent operates in a structured, four-phase workflow to ensure a consistent and high-quality output.

Phase 1: Requirements Gathering
-------------------------------

1.  **Topic Inquiry**: The agent starts by asking the user for the desired blog topic.
    
2.  **Featured Image**: It then asks if the user wants to include a featured image. If so, it uses the upload\_image\_to\_imgbb tool to upload the image and stores the URL.
    
3.  **Confirmation**: Once the user confirms, the agent proceeds to the research phase.
    

Phase 2: Elite SEO Research
---------------------------

1.  **Keyword Analysis**: The agent researches primary and long-tail keywords, analyzing their volume and competition.
    
2.  **Competitive Analysis**: It studies the top-ranking content for the target keywords to identify content gaps and successful strategies.
    
3.  **Content Strategy**: Based on its research, the agent formulates a content strategy, including optimal length, structure, and multimedia elements.
    

Phase 3: Advanced Content Creation
----------------------------------

1.  **Writing**: The agent writes a 3000-word article, following a detailed structure that includes an introduction, 5–7 H2 sections, an FAQ section, and a conclusion.
    
2.  **Fact-Checking**: All data and statistics are verified using real-time web searches to ensure accuracy.
    
3.  **SEO Optimization**: The content is optimized for SEO, with a natural keyword density, semantic keywords, and a structure designed for featured snippets.
    
4.  **Humanization**: The writing style is crafted to be conversational and engaging, using techniques that help it pass AI-detection tools.
    

Phase 4: HTML Conversion & Deployment
-------------------------------------

1.  **HTML Generation**: The final markdown content is converted into a full HTML page, adhering to a strict template that includes a responsive navigation bar, a styled content area, and a dynamic footer.
    
2.  **Deployment**: The agent uses the deploy\_to\_cpanel tool to upload the HTML file to the specified web server.
    
3.  **Permalink**: Finally, the agent returns the permanent URL of the newly published blog post to the user.
    

Core Components
---------------

*   **agno.agent.Agent**: The core class from the agno framework used to create the unified\_content\_agent.
    
*   **agno.models.ollama.Ollama**: The language model integration, configured to use deepseek-v3.1:671b-cloud.
    
*   **agno.db.sqlite.SqliteDb**: Handles the session state and history, storing data in a local SQLite database (neurofiq\_content.db).
    
*   **agno.tools**: The module that provides the @tool decorator for creating custom tools.
    
*   **rich**: A Python library for rich text and beautiful formatting in the terminal, used to enhance the CLI's output.
    
*   **python-dotenv**: Used to manage environment variables for API keys.
    

Custom Tools
------------

upload\_image\_to\_imgbb
------------------------

A tool to upload an image from a local path to ImgBB.

*   **Parameter**: image\_path (str) - The local file path of the image to upload.
    
*   **Functionality**: Reads the image file, encodes it in base64, and sends it to the ImgBB API.
    
*   **Output**: Returns the public URL of the uploaded image or an error message.
    

deploy\_to\_cpanel
------------------

A tool to deploy HTML content to a cPanel server.

*   **Parameters**:
    
    *   html\_content (str): The complete HTML content of the blog post.
        
    *   blog\_title (str): The title of the blog, used to generate an SEO-friendly filename.
        
*   **Functionality**:
    
    1.  Creates an SEO-friendly slug from the blog title.
        
    2.  Uses the cPanel API to upload the HTML content to the public\_html directory.
        
*   **Output**: Returns the permalink of the deployed page or an error message.
    

Setup and Installation
----------------------

1.  bashgit clone https://your-repository-url.com/neurofiq-content-agent.gitcd neurofiq-content-agent
    
2.  bashpip install -r requirements.txt_Note: The requirements.txt file should contain all the imported libraries._
    
3.  textimagebb\_api\_key="YOUR\_IMGBB\_API\_KEY"Cpanel\_api\_key="YOUR\_CPANEL\_API\_TOKEN"
    

Usage
-----

To run the agent, execute the script from your terminal:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashpython your_script_name.py   `

The agent will then greet you and ask for the topic you want to write about. Follow the interactive prompts to generate and deploy your content.

Dependencies
------------

*   agno
    
*   requests
    
*   python-dotenv
    
*   rich
