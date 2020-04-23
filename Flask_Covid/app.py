import requests
from covid import Covid
from covid_india import states
from flask import Flask, render_template,request,redirect
import time
from datetime import datetime


# readable = time.ctime(1587408140)


app = Flask(__name__)
covid = Covid()
@app.route('/')
def page():
	# print(covid.get_data())
	return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		country_name = request.form['country_name'].title()
		country_cases = covid.get_status_by_country_name(country_name)
		active_cases = country_cases['active']
		confirmed_cases = country_cases['confirmed']
		recovered_cases = country_cases['recovered']
		deaths_cases = country_cases['deaths']
		dateTimeObj = datetime.now()
		print(country_cases)
		print(active_cases,deaths_cases,confirmed_cases,recovered_cases)
		date = dateTimeObj.year,'-', dateTimeObj.month,'-', dateTimeObj.day
		date = str(date)
		date = date[1:5]+'/'+date[12:13]+'/'+date[20:22]
		time = dateTimeObj.hour,':', dateTimeObj.minute,':', dateTimeObj.second,'.', dateTimeObj.microsecond
		# active_cases = country_cases['']
		print(dateTimeObj.year, '-', dateTimeObj.month, '-', dateTimeObj.day)
		print(dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second, '.', dateTimeObj.microsecond)
		# countries = covid.list_countries()
		# print(countries)
		# # print(dt_object)
		# print(last_updated)
		print(country_cases)
		return render_template('index.html',cn = country_name,ac = active_cases,rc = recovered_cases,cc = confirmed_cases,dc = deaths_cases,date=date)
	else:
		print('Mistaken')
		return redirect('/')



@app.route('/state',methods=['GET','POST'])
def state_index():
	if request.method == 'POST':
		state_name = request.form['state_name'].title()
		state_data = states.getdata(state_name)
		sn = state_name
		sc = state_data['Total']
		sr = state_data['Cured']
		sd = state_data['Death']

		return render_template('index.html',sn=sn,sc=sc,sr=sr,sd=sd)





		



if __name__ == '__main__':
	app.run(debug=True)