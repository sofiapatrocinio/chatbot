A simple chatbot to compliment 

1. You can train the Rasa NLU model by running:  
```python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. In a new terminal start the server for the custom action by running:  
```make action-server```  
This will start the server for emulating the custom action.

4. Test the assistant by running:  
```make cmdline```  
This will load the assistant in your terminal for you to chat.
