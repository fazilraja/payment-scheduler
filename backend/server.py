from flask import Flask, request, jsonify
import json
import datetime
app = Flask(__name__)

startDate = ""
endDate = ""
frequency = ""
country = ""
endOfMonthRule = False 
businessDayRule = False
timeZone = ""
days = []
dateList =[]
# Method used for obtaining front end input
@app.route("/add_dates", methods = ['POST'])
def add_dates():

    global days
    days.clear()
    
    global dateList
    dateList.clear()
    
    # Gets the input values in form of json object
    state_values = request.get_json(force = True)
    
    # Turns json object into json string
    data_string = json.dumps(state_values)

    # Turns json string into dictionary
    data_dictionary = json.loads(data_string)

    global startDate 
    startDate = data_dictionary[1]

    global endDate 
    endDate = data_dictionary[2]

    global frequency
    frequency = data_dictionary[0]['state']['frequency']

    global country
    country = data_dictionary[0]['state']['country']

    global endOfMonthRule
    endOfMonthRule = data_dictionary[0]['state']['endOfMonthRule']

    global businessDayRule
    businessDayRule = data_dictionary[0]['state']['businessDayRule']

    return 'Done', 201



# Method used for outputting dates back to frontend 
@app.route("/dates", methods = ['GET'])
def dates():
    import payment
    schedule = payment.PaymentSchedule(startDate, endDate, frequency, country, businessDayRule, endOfMonthRule)
    # dateList = json.dumps(schedule.get_payment_dates(), default = str)
    # # dateList = json.dumps(dateList, indent = 4, sort_keys= True, default = str)
    dates = schedule.generate_payment_dates()
    for i in range(len(dates)):
        month = str(dates[i].get_month()).zfill(2)
        day = str(dates[i].get_day()).zfill(2)
        year = str(dates[i].get_year())
        dateString = month + '-' + day + '-' + year
        if (dateList.count(dateString) == 0):
            dateList.append(dateString)
    return jsonify({'dateList' : dateList})

# Method used for outputting dates back to frontend 
@app.route("/holidays", methods = ['GET'])
def holidays():
    import holidays
    import payment
    schedule = payment.PaymentSchedule(startDate, endDate, frequency, country, businessDayRule, endOfMonthRule)
    country_holidays = schedule.get_holidays()
    dates = list(country_holidays.keys())
    holidayNames = list(country_holidays.values())
    parsedList = {}
    for i in range(len(dates)):
        month = str(dates[i].get_month()).zfill(2)
        day = str(dates[i].get_day()).zfill(2)
        year = str(dates[i].get_year())
        dateString = month + '-' + day + '-' + year
        parsedList[dateString] = holidayNames[i]
    return json.dumps(parsedList)

    
app.run()