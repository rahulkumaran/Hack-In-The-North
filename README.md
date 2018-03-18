# HINT 3.0 Hack
## Anti Depressant Bot
This bot analyses whether one is depressed or not, and if one actually is depressed then it'll try to determine whether that person will suffer from depression again.<br>
Also, it'll suggest a treatment for people to overcome depression.<br>

This bot can be used by doctors as a way to analyse depression and can suggest possible treatments too.<br><br>

The bot can be one's best friend as you can share whatever you want here.<br>

Here we're using Rasa.ai for the nlp part. We've also created a messenger bot for proper analysis of data.<br><br>
Currently, we'll be suggesting 3 different treatments:<br>
#### 1) Placebo
#### 2) Imipramine
#### 3) Lithium

### Some commands that are being used to train and run the bot using rasa:
    To install dependencies, use the following command:
    pip install -r requirements.txt
    -----------------------------------------------------------------------------------------------
    Use the following commands to run the bot and train it. You can use the last command to just run the bot!
    python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current -- Train with nlu data
    python -m rasa_core.train -s data/stories.md -d concert_domain_remote.yml -o models/dialogue -- Train with stories
    python -m rasa_core.server -d models/dialogue -u models/nlu/current -o out.log -- To run the bot
    
We've connected it to messenger (Facebook), using the provision given by Rasa.<br>

The project is in its budding stages, anyone interested to contribute can do so. :) 
