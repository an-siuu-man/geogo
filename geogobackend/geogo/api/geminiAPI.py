import google.generativeai as genai
# import os

keykey=''

for line in open("../../../apiKeys.txt", "r"):
    if "gemini" in line:
        keykey = (line.split(",")[1].strip())

genai.configure(api_key=keykey)

model = genai.GenerativeModel('gemini-pro')

def generateVisaResponse(airports, finalDST, passportCountry):

    b = [str(airports) for airports in airports] 
    comma = ","
    airport_String = comma.join(b)
    print("What are the transit visa requirements of these airports " + airport_String + " if I have a passport from " + str(passportCountry) +" and what are the tourist visa requirements for the country of airport " + str(finalDST) + " if I have a passport from " + str(passportCountry) + ". Generate a Response that has a sentence for each airport with a transit visa requirement inquiry, provide a sentence for the tourist visa requirements of the country of the airport associated with the visa requirements inquiry based on the hypothetical passport proposed. Do Not provide me website links to get the recommended visas for both transit and tourist. Do not include Headers. Each Sentence should be a bullet")
    response = model.generate_content(
        "What are the transit visa requirements of these airports " + airport_String + " if I have a passport from " + str(passportCountry) +" and what are the tourist visa requirements for the country of airport " + str(finalDST) + " if I have a passport from " + str(passportCountry) + ". Generate a Response that has a sentence for each airport with a transit visa requirement inquiry, provide a sentence for the tourist visa requirements of the country of the airport associated with the visa requirements inquiry based on the hypothetical passport proposed. Do Not provide me website links to get the recommended visas for both transit and tourist. Do not include Headers. Each Sentence should be a bullet"
        )
    # print(response.text)
    return(response.text)
# generateResponse(["LAX","LHR"],"DEL","India")
# print(generateVisaResponse(['LAX','LHR', 'ORD', 'MCI'], 'DEL', 'India'))