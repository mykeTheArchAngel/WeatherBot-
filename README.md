#KALI LINUX
--
Create a Virtual Environment

This keeps your project isolated from system Python packages.
Step-by-Step Instructions:

    Install required system packages:
        sudo apt install python3-venv python3-pip

    Create a project directory:
        mkdir weather_bot && cd weather_bot

    Create a virtual environment:
        python3 -m venv weather_env

    Activate the virtual environment:
        source weather_env/bin/activate
Your terminal prompt should now show (weather_env) at the beginning

    Install requests in the virtual environment:
        pip install requests
        
    Create your script:
        nano weather_bot.py

    Paste weatherBot V1_python_.py code:
    
    Save and exit: Ctrl+O → Enter → Ctrl+X

    Run your bot:
        python weather_bot.py
        
When You Want to Exit:

        deactivate  # To leave the virtual environment
