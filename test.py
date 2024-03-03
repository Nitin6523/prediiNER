# Libraries and Dependencies
from langchain import PromptTemplate, OpenAI
import openai
from openai import OpenAI

import os
from dotenv import load_dotenv

def configure():
   load_dotenv()

#----------Zero Shot..----------#
zero_shot_prompt_template = """
Please generate a structured output from the provided input text. The input text describes failure issue, vehicle model, corrective action and affected components etc in vehicle. Your task is to extract entities and their corresponding labels.
output in the form of Entity and Labels
"""
#----------few Shot..----------#

prompt_template = """
Please generate a structured output from the provided input text. The input text describes failure issue, vehicle model, corrective action and affected components etc in vehicle. Your task is to extract entities and their corresponding labels.

Example 1:
Input Text:

"ON CERTAIN CLASS A MOTOR HOMES, THE FLOOR TRUSS NETWORK SUPPORT SYSTEM HAS A POTENTIAL TO WEAKEN CAUSING INTERNAL AND EXTERNAL FEATURES TO BECOME MISALIGNED. THE AFFECTED VEHICLES ARE 1999 - 2003 CLASS A MOTOR HOMES MANUFACTURED ON F53 20,500 POUND GROSS VEHICLE WEIGHT RATING (GVWR), FORD CHASSIS, AND 2000-2003 CLASS A MOTOR HOMES MANUFACTURED ON W-22 22,000 POUND GVWR, WORKHORSE CHASSIS. CONDITIONS CAN RESULT IN THE BOTTOMING OUT THE SUSPENSION AND AMPLIFICATION OF THE STRESS PLACED ON THE FLOOR TRUSS NETWORK. THE ADDITIONAL STRESS CAN RESULT IN THE FRACTURE OF WELDS SECURING THE FLOOR TRUSS NETWORK SYSTEM TO THE CHASSIS FRAME RAIL AND/OR FRACTURE OF THE FLOOR TRUSS NETWORK SUPPORT SYSTEM. THE POSSIBILITY EXISTS THAT THERE COULD BE DAMAGE TO ELECTRICAL WIRING AND/OR FUEL LINES WHICH COULD POTENTIALLY LEAD TO A FIRE."

Expected Output Format:

[
  {"Entity": "floor truss network support system", "Label": "Component"},
  {"Entity": "internal and external features", "Label": "Component"},
  {"Entity": "ford chassis", "Label": "Component"},
  {"Entity": "1999 - 2003 Class A motor homes (F53 20,500 pound GVWR, Ford chassis)", "Label": "Vehicle"},
  {"Entity": "2000-2003 Class A motor homes (W-22 22,000 pound GVWR, Workhorse chassis)", "Label": "Vehicle"},
  {"Entity": "bottoming out the suspension", "Label": "Failure Issue"},
  {"Entity": "amplification of the stress", "Label": "Failure Issue"},
  {"Entity": "floor truss network", "Label": "Component"},
  {"Entity": "fracture of welds", "Label": "Failure Issue"},
  {"Entity": "chassis frame rail", "Label": "Component"},
  {"Entity": "damage to electrical wiring", "Label": "Failure Issue"},
  {"Entity": "fuel lines", "Label": "Component"},
  {"Entity": "fire", "Label": "Failure Issue"}
]

Example 2:
Input Text:

"CERTAIN MODELS OF SPORTS UTILITY VEHICLES (SUVs) ARE BEING RECALLED DUE TO A POTENTIAL ISSUE WITH THE REAR SUSPENSION SYSTEM. THE AFFECTED VEHICLES ARE 2018-2020 MODELS OF XYZ SUV, MANUFACTURED BETWEEN MARCH 2017 AND AUGUST 2019. DRIVING UNDER CERTAIN CONDITIONS CAN LEAD TO EXCESSIVE WEAR AND TEAR ON THE REAR SUSPENSION COMPONENTS, INCREASING THE RISK OF A SUSPENSION FAILURE. THIS COULD RESULT IN LOSS OF VEHICLE CONTROL AND POTENTIAL ACCIDENTS."

Expected Output Format:

[
  {"Entity": "rear suspension system", "Label": "Component"},
  {"Entity": "2018-2020 models of XYZ SUV, manufactured between March 2017 and August 2019", "Label": "Vehicle"},
  {"Entity": "driving under certain conditions", "Label": "Failure Issue"},
  {"Entity": "excessive wear and tear", "Label": "Failure Issue"},
  {"Entity": "rear suspension components", "Label": "Component"},
  {"Entity": "suspension failure", "Label": "Failure Issue"},
  {"Entity": "loss of vehicle control", "Label": "Failure Issue"},
  {"Entity": "accidents", "Label": "Failure Issue"}
]

Example 3:
Input Text:

"CERTAIN MODELS OF ELECTRIC CARS MANUFACTURED BETWEEN 2015 AND 2018 MAY EXPERIENCE BATTERY OVERHEATING ISSUES. THE AFFECTED VEHICLES INCLUDE ALL MODELS OF ABC ELECTRIC CAR MANUFACTURED DURING THIS PERIOD. DRIVING IN HIGH TEMPERATURES OR USING FAST CHARGING METHODS CAN EXACERBATE THE PROBLEM. BATTERY OVERHEATING CAN LEAD TO LOSS OF POWER AND IN SOME CASES, FIRE HAZARDS."

Expected Output Format:

[
  {"Entity": "electric cars", "Label": "Vehicle"},
  {"Entity": "battery overheating issues", "Label": "Failure Issue"},
  {"Entity": "2015 and 2018", "Label": "Time Period"},
  {"Entity": "all models of ABC electric car", "Label": "Vehicle"},
  {"Entity": "high temperatures", "Label": "Failure Issue"},
  {"Entity": "fast charging methods", "Label": "Failure Issue"},
  {"Entity": "battery overheating", "Label": "Failure Issue"},
  {"Entity": "loss of power", "Label": "Failure Issue"},
  {"Entity": "fire hazards", "Label": "Failure Issue"}
]
"""

# Function for making few shot prompt

def makePrompt(prompt):
  prompt_temp = PromptTemplate.from_template("""
  {prompt_template}
  Input Text: {mess}
  Output:
  """)

  final_prompt = prompt_temp.format(prompt_template=prompt_template,mess=paragraph)
  # print(final_prompt)
  return final_prompt


# Function for making zero shot prompt

def makeZeroShotPrompt(prompt):
  prompt_temp = PromptTemplate.from_template("""
  {prompt_template}
  Input Text: {mess}
  Output:
  """)

  final_prompt = prompt_temp.format(prompt_template=zero_shot_prompt_template,mess=paragraph)
  # print(final_prompt)
  return final_prompt

#---------Output Function---------#
def get_response(prompt):
    client = OpenAI()

    response = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prompt,
      max_tokens=500
    )

    # Extract output
    output = response.choices[0].text.strip()
    return output

#---------------Driver Function..------------#
if __name__ == "__main__":
    configure()
    # paragraph input
    paragraph = input("Enter the text paragraph: ")

    # made prompt
    final_prompt=makePrompt(paragraph)
    # final_prompt=makeZeroShotPrompt(paragraph)

    # getting output
    output = get_response(final_prompt)

    # print output
    print(output) #Output type is string