# prediiNER
### It performs named entity recognition (NER) task on an automotive dataset.

## Notes...
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

Set up `.env` file in which give your OPENAI_API_KEY

```
OPENAI_API_KEY = <your API key>
```
Run test.py
```
python test.py
```

## Example...
**Input:**

Enter the text paragraph: General Motors, LLC (GM) is recalling certain Autoliv Driver Front Air Bags sold as service replacement parts for 2011-2012 Chevrolet Silverado 1500, Suburban, and Tahoe vehicles.  The driver's air bag inflator may deploy improperly due to a manufacturing defect.An air bag that does not deploy properly in a crash increases the risk of injury.	Dealers will inspect and replace the driver air bag module as necessary

**Output:**

  {"Entity": "Autoliv Driver Front Air Bags", "Label": "Component"},
  {"Entity": "2011-2012 Chevrolet Silverado 1500, Suburban, and Tahoe vehicles", "Label": "Vehicle"},
  {"Entity": "driver's air bag inflator", "Label": "Component"},
  {"Entity": "manufacturing defect", "Label": "Failure Issue"},
  {"Entity": "air bag", "Label": "Component"},        
  {"Entity": "deploy improperly", "Label": "Failure Issue"},
  {"Entity": "crash", "Label": "Failure Issue"},      
  {"Entity": "injury", "Label": "Failure Issue"},     
  {"Entity": "driver air bag module", "Label": "Component"}


## Links...

Zero and Few shot.. [collab Notebook](https://colab.research.google.com/github/Nitin6523/prediiNER/blob/main/Predii.ipynb)

Fine tuning Data Preperation... [collab Notebook](https://colab.research.google.com/github/Nitin6523/prediiNER/blob/main/prediiDataPrep.ipynb)

Fine tuning GPT 3.5 Turbo... [collab Notebook](https://colab.research.google.com/github/Nitin6523/prediiNER/blob/main/prediiFineTuning.ipynb)

