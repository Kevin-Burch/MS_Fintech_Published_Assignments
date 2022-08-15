# Kevin Burch; 8/14/2022

# This program was written as the first weekend assignment for the MS
# Fintech program, for the Fall '22 Cohort. 

# The purpose of this program is to communicate an understanding of some
# elementary concepts in Python, including variables, expresions, 
# statements, conditional execution, functions, loops & iterations, and 
# strings. It also demponstrates applied knowledge of recieving and 
# testing user inputs, modular programing styles, and communication 
# (comments) with the back-end user or analyst who maintains the code. 

# The program itself calculates the payroll for a population of
# employees in a payroll cycle. The program has a broad scope, and can
# apply to most businesses opperated in the United States of America.
 
#
# The program makes some assumptions, such as:
# 1) this payroll is the only source of W4 income for each employee
#		*This program does not account for additional W4 employment
#		*This program does not account for additional withholdings income
# 2) the federal minimum wage is still $7.50/hr
# 3) the program does not consider overtime or holiday pay rates
# 4) hourly employees grossing >=$250K annually will be converted to salary
# 5) utilizes 2022 tax brackets
# 
#
#
# As the program iterates, a individual contributor will manually input 
# the following employee payroll data fields:

# 	Age; 
# 	Tax Status;
#	Number of Dependants per the most recent Form W-4;
# 	Wage Type; 
#	Wage Rate - either Hourly, or Annualized;
#	Hours worked -
# 		The program will only prompt for hours worked if the employee 
#		is a hourly employee. The program will not prompt for salaried
#		employees;

# 	401(k) contribution amount;
#	401(k) catch-up contribution amount -
# 		The program will only prompt for catch-up amount if the employee 
#		is 50 years of age or senior. The program will not prompt for 
#		a catch-up amount if the employee is 49 or junior;
#	403(b) contribution amount;
# 	403(b) catch-up contribution amount;
# 		The program will only prompt for catch-up amount if the employee 
#		is 50 years of age or senior. The program will not prompt for 
#		a catch-up amount if the employee is 49 or junior;
# 	Health Savings Account contribution amount;
# 	-No entry for post-tax deductions;
#
# Based on the entry of the data points above, the program will calculate
# the payroll tax amount for each employee and display that information 
# formatted in a logical manner. 
#


#  

"""	Section 1

	In this first section of the program, I define the functions I will
	call in the main operation of the program. 
	
	The funtions include:
	explain_this_program
		*This funtion introduces the user to the program. It is the only
		function called before the loop containing the body of the program
		
	get_age
		*This funtion accepts the "employee age" data point from the user
		
	get_tax_status
		*This function accepts the "employee tax status" data point from
		the user. Acceptable inputs are (H)ead Of Household, (M)arried, 
		or (S)ingle
		
	get_dependant_info
		*This function accepts the number of dependancies the employee
		listed on their most recent Form W-4. Acceptable inputs are 0-10
		
	get_wage_type
		*This function accepts the "employee wage type" data point from 
		the user. Acceptable inputs are Hourly or Salary
		
	get_pay_frequency
		*This function accepts the "pay frequency" data point from the 
		user. It provides a list of five acceptable inputs:
			*12 - Monthly 
			*24 - Semimonthly
			*26 - Biweekly
			*52 - Weekly
			*260 - Daily
		The user must input one of the five numerical values.
		
	get_wages
		*This function accepts the employee wage rate based on the 
		employee wage type. Acceptable inputs are within the range of 
		$15,000 - $1,000,000/yr for salaried positions and $7.25 - $125.00
		for hourly positions, assuming that an employee making $125.00
		on an hourly basis would be converted to a salaried position if
		possible, and of course, ensuring the company does not pay any 
		employee less than the legally obligated federal minimum of $7.25. 
		
	get_adjusted_annual_wage
		*This function accepts the number of hours worked for salaried 
		employees. Acceptable inputs are 0.01-600 hours for the period.
		*Using the inputs (wage rate, work time, and pay frequency)
		gathered from the user, the function computes an annualized income. 
		*Using the "employee tax status" data point, the function computes
		an adjusted annual income for the employee.
		*Using the computed annualized income, the function computes
		the employees' medicare, additional medicare, and social security
		withholding amounts. 
		
	get_tax_adjustments
		*This function accepts tax deferral input from the user.
		*The function tests the input against maximum ammounts which are
		updated annually by the IRS
		*The tax deferral options are 401(k), 403(b), and HSA.
		*If the employee is 50 years of age or older, the function will
		prompt the user for two additional deferral options, 
		401(k) catch-up and 403(b) catch-up
		
	get_fed_tax
		*This function uses a nested if/elif framework to assign 
		employees to the correct tax bracket based on their tax status
		and adjusted taxable income.
		*The function returns the federal tax withholding for the employee
		for the payperiod.
	
	"""

def explain_this_program ():
	print('Hello!, \n\nThis program is designed to help you calculate ' 
	+ "an employee's net income after payroll deductions and taxes.\n"
	+ "First, it will ask you some questions. Let's get started... \n")
	"""This funtion introduces the user to the program""" 
	
def get_age():
	
	while True:
		try:
			 age = int(input("What is the employee's age?: "))
		except ValueError:
			print("Enter a numerical value for the employee's age.")
			continue
		else:
			break
			
	while age < 15 or age > 99:
		print('You entered ' + str(age))
		try:
			age = int(input('Please enter a number greater than 15 and less than 100: '))
		except ValueError:
			print("Enter a numerical value for the employee's age.")
			continue
		if age < 15 or age > 99:
			continue
		else:
			break
			
	return age
	'''This funtion asks for the employee age from the user and returns
		the employee's age to the main operation of the program'''

def get_tax_status ():
	tax_status = input("What is the employee's tax status? " + \
	'"(M)arried" , "(S)ingle", or "(H)ead Of Household": ')
	while tax_status.title() != "Married" and tax_status.title() \
	!= "M" and tax_status.title() != "Head Of Household" \
	and tax_status.title() != "H" and tax_status.title() != "Single" \
	and tax_status.title() != "S" :
		print('You entered ' + tax_status)
		tax_status = input('Please enter either "Married / M" or '\
		+ '"Single / S" or "Head Of Household / H": ')
	tax_status = tax_status.title()
	return tax_status
	""" This funtion gathers the employees' marriage status. It tests 
	the input and only accepts "(M/m)arried", "(S/s)ingle",
	 or "(H)ead of Household" """
	 
def get_dependant_info():
	while True:
		try:
			number_of_dependancies = int(input('Enter the number of '\
			+"dependancies from this employee's most recent Form W-4: "))
		except ValueError:
			print('Please enter a numerical value from zero to 10')
			continue
		else:
			break
			
	while (number_of_dependancies <0) or (number_of_dependancies >10) :
		try:
			number_of_dependancies = int(input('Enter the number of dependancies'\
			+" from this employee's most recent Form W-4. Enter a numerical "\
			+"value 0-10: "))
		except ValueError:
			print('Please enter a numerical value from zero to 10')
			continue
		if (number_of_dependancies <0) or (number_of_dependancies >10) :
			continue
		else:
			break
			
	
	return number_of_dependancies

	"""This function asks the user to input the number of dependancies
	from the employees' most recent From W-4. It then returns the number
	to the main funtion."""
	 
def get_wage_type ():
	wage_type = input('Is this employee paid hourly or with a salary? '\
	+ '"Hourly" or "Salary": ')
	wage_type = wage_type.title()
	while wage_type.title() != "Hourly" and wage_type.title() != "Salary":
		print('You entered ' + wage_type)
		wage_type = input('Please enter either "Hourly" or "Salary": ')
		wage_type = wage_type.title()
	return wage_type
	""" This funtion gathers the users' wage type (salary vs hourly)"""

def get_pay_frequency ():
	"""have the user input the frequency of pay"""
	while True:
		try:
			pay_frequency = int(input("Please enter the numerical value "\
			+ "representing the frequency of payroll: "\
			+ "\n 12 - Monthly \n 24 - Semimonthly "\
			+ "\n 26 - Biweekly \n 52 - Weekly  "\
			+ "\n 260 - Daily \n user entry: "))
		except ValueError:
			print('Please enter the numberical value ' \
			+'(12, 24, 26, 52, or 260)')
			continue
		if pay_frequency != 12 and pay_frequency != 24 and \
	pay_frequency != 26 and pay_frequency != 52 and \
	pay_frequency != 260:
			continue
		else:
			break
	return pay_frequency
		
def get_wages (wage_type):
	if wage_type == "Salary":
		"""assuming here that salaried employees are making more 
			than the USA federal minimum wage and less than a million """
		while True:
			try:
				salary_wage = float(input("Please enter the employee's "\
				+ "annual salary: "))
			except ValueError:
				print("Enter a numerical value for the employee's wage.")
				continue
			if salary_wage < 15_000 or salary_wage > 1_000_000:
				print('You entered: ' + "${:0,.2f}".format(salary_wage) + \
				'; This wage does not seem likely.')
				continue
			else:
				break
		return salary_wage
	elif wage_type == "Hourly":
		
#assuming here that hourly employees paid >=$250K should be 
#converted to salary and that the entity is not paying
#less than the USA federal minimum hourly wage
				
		while True: 
			try:
				hourly_wage = float(input("Please enter the employee's hourly wage: "))
			except ValueError:
				continue
			if hourly_wage < 7.25:
				print('You entered: ' + "${:0,.2f}".format(hourly_wage)\
				 + ' per hour; The national minimum wage is $7.25 / '\
				 +'hour.')
				continue;
			elif hourly_wage >=125:
				print('You entered: ' + "${:0,.2f}".format(hourly_wage)\
				 + ' per hour. This wage rate does not seem likely.')
				continue;
			else:
				break
		return hourly_wage
	else:
		print('An Error In the Program Has Occured')
		
		"""Based on the wage type passed to this fucntion, the funtion asks
		the user for either their hourly or annualized wages. It tests
		 the input for reasonablility considering things like minimum wage. """
		
def get_adjusted_annual_wage (wage_rate, frequency, tax_status, dependancies):
	if wage_rate <= 125:
		#acceptable inputs are 0.01 - 600 hours; 
		while True:
			try:
				hours_worked = float(input('Please enter the number of hours '\
								+'you worked this period: '))
			except ValueError:
				print('Please enter a numerical value.')
				continue
			else:
				break
		while hours_worked <0.01 or hours_worked >600:
			print('You entered: ' + "{:.2f}".format(hours_worked) + \
				'; This amount does not seem reasonable.' )
			try:
				hours_worked = float(input(' Please enter the number of '\
				+'hours your worked this period: '))
			except ValueError:
				continue
			if hours_worked <0.01 or hours_worked >600:
				continue
			else:
				break
		#Compute gross income for the pay period
		current_period_income = hours_worked * wage_rate
		
		#compute annual income for the pay period
		annual_income = (current_period_income * frequency)
		
		#
		if tax_status == "Married" or tax_status == "M":
			adjusted_annual_income = annual_income -12_900
			"""set additional medicare tax base at 250K for married """
			addl_med_base = 250_000
		
		#
		elif tax_status != "Married" and tax_status != "M":
			adjusted_annual_income = annual_income -8_600
			"""set additional medicare tax base at 200K for non-married"""
			addl_med_base = 200_000
		else:
			print('an error has occured in the program')
		
		#compute adjusted income net of depenancies
		adjusted_annual_income = adjusted_annual_income - \
								(dependancies * 4_300)
		
		#compute Medicare and Social Security tax
		annual_medicare_tax = annual_income * 0.0145
		social_security_tax = annual_income * 0.0620
		
		#compute additional Medicare
		if (annual_income - addl_med_base) > 0:
			additional_medicare_tax = (annual_income - addl_med_base) \
			* 0.009
		else:
			additional_medicare_tax = 0
		
		
		return annual_income, adjusted_annual_income, \
		annual_medicare_tax, additional_medicare_tax, \
		social_security_tax;
	else:
		
		if tax_status == "Married" or tax_status == "M":
			adjusted_annual_income = wage_rate - 12_900
			addl_med_base = 250_000			
		
		elif tax_status != "Married" and tax_status != "M":
			adjusted_annual_income = wage_rate - 8_600
			addl_med_base = 200_000
						
		else:
			print('an error has occured in the program')
		
		#compute adjusted income net of depenancies
		adjusted_annual_income = adjusted_annual_income - \
								(dependancies * 4_300)
		
		#compute Medicare and Social Security tax
		annual_medicare_tax = wage_rate * 0.0145
		social_security_tax = wage_rate * 0.0620
		
		#compute additional medicare tax
		if (wage_rate - addl_med_base) > 0:
			additional_medicare_tax = (wage_rate - addl_med_base) \
			* 0.009
		else:
			additional_medicare_tax = 0
		
		return wage_rate, adjusted_annual_income, annual_medicare_tax, additional_medicare_tax, social_security_tax;
		
		"""Based on the wage rate and frequency passed to this funtion, 
		the function returns a pay computation based on the annual 
		salary, or hours_worked multipled by the hourly wage for 
		employees multiplied by the frequency of pay.  
		
		The function subtracts $8,600 for individuals or $12,900 
		for married employees, per Publication 15-T (2022). The function
		then subtracts a credit for dependancies. This provides the 
		adjusted annual income from page 8, line 1L of 
		Publication 15-T (2022). 
		
		The funtion then returns the adjusted annual income to the main 
		function of the program
		"""
		
def get_tax_adjustments(age, frequency):
	#set variables that change annually for easier code maintainance
	max_contribution = 20_500
	max_catchup_contribution = 6_500
	max_hsa_contribution = 3_650
	
	#PayPeriod maximum conversion from annual
	max_c_payperiod = max_contribution / frequency
	max_cc_payperiod = max_catchup_contribution / frequency
	max_hsa_payperiod = max_hsa_contribution / frequency
	
	#Request input from user and validate it
	print('Please enter the contribution amount to the following tax-deferred accounts: ')
	
	#Accept 401(k) deduction from user
	while True:
		try:
			tax_deduction_401k = float(input('401(k) Savings: '))
		except ValueError:
			print('Please enter a numerical value.')
			continue
		else:
			break
	while tax_deduction_401k > (max_c_payperiod) \
	or tax_deduction_401k <0:
		print('The maximum allowable contribution to your 401(k) is '\
				+ "${:0,.2f}".format(max_c_payperiod))		
		try:
			tax_deduction_401k = float(input('Please enter an amount less '\
				+ 'than ' + "${:0,.2f}".format(max_c_payperiod) +'  :'))
		except ValueError:
			continue
		if tax_deduction_401k > (max_c_payperiod) \
		or tax_deduction_401k <0:
			continue
		else:
			break
	
	#Accept 403(b) deduction from user
	while True:
		try:
			tax_deduction_403b = float(input('403(b) Savings: '))
		except ValueError:
			print('Please enter a numerical value.')
			continue
		else:
			break
	while tax_deduction_403b > (max_c_payperiod) \
	or tax_deduction_403b <0:
		print('The maximum allowable contribution to your 403(b) is '\
				+ "${:0,.2f}".format(max_c_payperiod))		
		try:
			tax_deduction_403b = float(input('Please enter an amount less '\
				+ 'than ' + "${:0,.2f}".format(max_c_payperiod) +'  :'))
		except ValueError:
			continue
		if tax_deduction_403b > (max_c_payperiod) \
		or tax_deduction_403b <0:
			continue
		else:
			break
	
	
	"""only if the employee is 50 or older, prompt for eligible 
	catch-up contribution amounts. This is important because it will 
	save time for the user of the program entering in data for employees
	under the age of 50. If the employees themselves enter the data, it
	will prevent confustion for employees under the age of 50 who are 
	ineligible for these taxable income deferrals."""
	
		
	if age > 49.0 :
		
		#Accept 401(k) catch-up contribution from user
		while True:
			try:
				tax_deduction_401k_catchup = float(input('401(k) Catch-Up Contribution: '))
			except ValueError:
				print('Please enter a numerical value.')
				continue
			else:
				break
		while tax_deduction_401k_catchup > (max_cc_payperiod) \
		or tax_deduction_401k_catchup <0:
			print('The maximum allowable catch-up contribution to your 401(k) is '\
					+ "${:0,.2f}".format(max_cc_payperiod))		
			try:
				tax_deduction_401k_catchup = float(input('Please enter an amount less '\
					+ 'than ' + "${:0,.2f}".format(max_cc_payperiod) +'  :'))
			except ValueError:
				continue
			if tax_deduction_401k_catchcup > (max_cc_payperiod) \
			or tax_deduction_401k_catchup <0:
				continue
			else:
				break
		
		#Accept 403(b) catch-up contribution from user
		while True:
			try:
				tax_deduction_403b_catchup = float(input('403(b) Catch-Up Contribution: '))
			except ValueError:
				print('Please enter a numerical value.')
				continue
			else:
				break
		while tax_deduction_403b_catchup > (max_cc_payperiod) \
		or tax_deduction_403b_catchup <0:
			print('The maximum allowable catch-up contribution to your 403(b) is '\
					+ "${:0,.2f}".format(max_cc_payperiod))		
			try:
				tax_deduction_403b_catchup = float(input('Please enter an amount less '\
					+ 'than ' + "${:0,.2f}".format(max_cc_payperiod) +'  :'))
			except ValueError:
				continue
			if tax_deduction_403b_catchcup > (max_cc_payperiod) \
			or tax_deduction_403b_catchup <0:
				continue
			else:
				break

	else:
		tax_deduction_401k_catchup = 0
		tax_deduction_403b_catchup = 0
		
	while True:
		try:
			tax_deduction_HSA = float(input('HSA Savings: '))
		except ValueError:
			print('Please enter a numerical value.')
			continue
		else:
			break
	while tax_deduction_HSA > (max_hsa_payperiod) or tax_deduction_HSA <0:
		print('The maximum allowable contribution to your 401(k) is '\
				+ "${:0,.2f}".format(max_hsa_payperiod))
		try:
			tax_deduction_HSA = float(input('Please enter an amount less '\
				+ 'than ' + "${:0,.2f}".format(max_hsa_payperiod) +'  :'))
		except ValueError:
			print('Please enter a numerical value.')
			continue
		if tax_deduction_HSA > (max_hsa_payperiod) or tax_deduction_HSA <0:
			continue
		else:
			break
			
	#compute tax adjustment total
	tax_adjustments = tax_deduction_401k + tax_deduction_403b \
					+ tax_deduction_HSA + tax_deduction_401k_catchup \
					+ tax_deduction_403b_catchup
					
	annual_tax_adjustments = tax_adjustments * frequency
	return annual_tax_adjustments, tax_deduction_401k, tax_deduction_403b, \
					tax_deduction_HSA, tax_deduction_401k_catchup, \
					tax_deduction_403b_catchup;
	"""This funtions asks the user to input deductions to his pre-tax income
	these deductions include 401(k), 403(b), and HSA contributions. If 
	the user previously indidcated the employee was over the age of 50, then 
	they are also prompted to enter eligible catch-up contribution ammounts"""

def get_fed_tax(tax_status, adjusted_taxable_income, frequency):
# this funtion uses an if/elif statement to match the employees tax 
# status to the correct tax bracket


# If the employee is single use these tax brackets
	if tax_status == "Single" or tax_status == "S":
		if int(adjusted_taxable_income) < 4_350:
			base = 0
			base_tax = float(0.0)
			marginal_rate = float(0.0)
			
		elif int(adjusted_taxable_income) >= 4_350 \
		and int(adjusted_taxable_income) < 14_625 :
			base = 4_350
			base_tax = float(0.0)
			marginal_rate = float(0.10)
			
		elif int(adjusted_taxable_income) >= 14_625 \
		and int(adjusted_taxable_income) < 46_125 :
			base = 14_625
			base_tax = float(1_027.50)
			marginal_rate = float(0.12)	
			
		elif int(adjusted_taxable_income) >= 46_125 \
		and int(adjusted_taxable_income) < 93_425 :
			base = 46_125
			base_tax = float(4_807.50)
			marginal_rate = float(0.22)
			
		elif int(adjusted_taxable_income) >= 93_425 \
		and int(adjusted_taxable_income) < 174_400 :
			base = 93_425
			base_tax = float(15_213.50)
			marginal_rate = float(0.24)
			
		elif int(adjusted_taxable_income) >= 174_400 \
		and int(adjusted_taxable_income) < 220_300 :
			base = 174_400
			base_tax = float(34_647.50)
			marginal_rate = float(0.32)	
			
		elif int(adjusted_taxable_income) >= 220_300 \
		and int(adjusted_taxable_income) < 544_250 :
			base = 220_300
			base_tax = float(49_335.50)
			marginal_rate = float(0.35)	
			
		elif int(adjusted_taxable_income) >= 544_250:
			base = 544_250
			base_tax = float(162_718.00)
			marginal_rate = float(0.37)	
			
		else:
			print('There was an error formulating the tax rate - sing')	
		
# elif the employee is married use these tax brackets
	elif tax_status == "Married" or tax_status == "M":
		if int(adjusted_taxable_income) < 13_000:
			base = 0
			base_tax = float(0.0)
			marginal_rate = float(0.0)
			
		elif int(adjusted_taxable_income) >= 13_000 \
		and int(adjusted_taxable_income) < 33_550 :
			base = 13_000
			base_tax = float(0.0)
			marginal_rate = float(0.10)
			
		elif int(adjusted_taxable_income) >= 33_550 \
		and int(adjusted_taxable_income) < 96_550 :
			base = 33_550
			base_tax = float(2_055.00)
			marginal_rate = float(0.12)	
			
		elif int(adjusted_taxable_income) >= 96_550 \
		and int(adjusted_taxable_income) < 191_150 :
			base = 96_550
			base_tax = float(9_615.00)
			marginal_rate = float(0.22)
			
		elif int(adjusted_taxable_income) >= 191_150 \
		and int(adjusted_taxable_income) < 353_100 :
			base = 191_150
			base_tax = float(30_427.00)
			marginal_rate = float(0.24)
			
		elif int(adjusted_taxable_income) >= 353_100 \
		and int(adjusted_taxable_income) < 444_900 :
			base = 353_100
			base_tax = float(69_295.00)
			marginal_rate = float(0.32)	
			
		elif int(adjusted_taxable_income) >= 444_900 \
		and int(adjusted_taxable_income) < 660_850 :
			base = 444_900
			base_tax = float(98_671.00)
			marginal_rate = float(0.35)	
			
		elif int(adjusted_taxable_income) >= 660_850:
			base = 660_850
			base_tax = float(174_253.50)
			marginal_rate = float(0.37)	
			
		else:
			print('There was an error formulating the tax rate - M')
		
# elif the employee is Head of Household use these tax brackets
	elif tax_status == "Head of Household" or tax_status == "H":
		if int(adjusted_taxable_income) < 10_800:
			base = 0
			base_tax = float(0.0)
			marginal_rate = float(0.0)
			
		elif int(adjusted_taxable_income) >= 10_800 \
		and int(adjusted_taxable_income) < 25_450 :
			base = 10_800
			base_tax = float(0.0)
			marginal_rate = float(0.10)
			
		elif int(adjusted_taxable_income) >= 25_450 \
		and int(adjusted_taxable_income) < 66_700 :
			base = 25_450
			base_tax = float(1_465.00)
			marginal_rate = float(0.12)	
			
		elif int(adjusted_taxable_income) >= 66_700 \
		and int(adjusted_taxable_income) < 99_850 :
			base = 66_700
			base_tax = float(6_415.00)
			marginal_rate = float(0.22)
			
		elif int(adjusted_taxable_income) >= 99_850 \
		and int(adjusted_taxable_income) < 180_850 :
			base = 99_850
			base_tax = float(13_708.00)
			marginal_rate = float(0.24)
			
		elif int(adjusted_taxable_income) >= 180_850 \
		and int(adjusted_taxable_income) < 226_750 :
			base = 180_850
			base_tax = float(33_148.00)
			marginal_rate = float(0.32)	
			
		elif int(adjusted_taxable_income) >= 226_750 \
		and int(adjusted_taxable_income) < 550_700 :
			base = 226_270
			base_tax = float(47_836.00)
			marginal_rate = float(0.35)	
			
		elif int(adjusted_taxable_income) >= 550_700:
			base = 550_700
			base_tax = float(161_218.50)
			marginal_rate = float(0.37)	
			
		else:
			print('There was an error formulating the tax rate - HOH')

# else something went wrong
	else:
		print('An error occurred while formulating the tax rate - else')
		base = 0
		base_tax = 0
		marginal_rate = 0
		
	
	margin = adjusted_taxable_income - base
	marginal_tax = margin * marginal_rate
	annual_fed_tax = base_tax + marginal_tax
	fed_tax = annual_fed_tax / frequency
	
	return fed_tax


"""Section 2

	In this second section, I utilize the functions defined in section 1
	to perform the mechanisms of the program. I introduce the program, 
	then I start the loop. Octothorpe commentary denotes psuedo-code to 
	follow along.

"""
#Print the first lines of the program. Introduce the program to the user.
explain_this_program()

#Start the loop; set a flag to run; while the flag is set the program will run
loop_flag = "run"
while loop_flag == "run":

	#Begin gathering input from the user
	#	Gather Employee Age
	age = get_age()

	#	Gather Employee Tax Status (M/S/H)
	tax_status = get_tax_status()

	#	Gather number of dependancies
	dependancies = get_dependant_info()

	#	Gather Frequency of Pay
	frequency = get_pay_frequency()

	#	Gather Wage Type (Hourly/Salary)
	wage_type = get_wage_type()

	#	Gather Wage Rate
	wage_rate = get_wages(wage_type)

	#	Gather pre-tax deductions
	tax_deferral_amount, tax_deduction_401k, tax_deduction_403b, \
						tax_deduction_HSA, tax_deduction_401k_catchup, \
						tax_deduction_403b_catchup = \
						get_tax_adjustments(age, frequency)

	#Using gathered inputs, computate gross income, adjusted annual 
	# income before deferrals, medicare tax, and social security tax
	gross_income, adjusted_income_before_deferrals , annual_medicare_tax, addl_medicare_tax, ss_tax = \
	get_adjusted_annual_wage(wage_rate, frequency, tax_status, dependancies)

	#Compute adjusted taxable income
	adjusted_taxable_income = adjusted_income_before_deferrals \
							- tax_deferral_amount
	
	#Compute gross income for the pay period
	payperiod_income = gross_income / frequency

	# Using adjusted income, tax status, and pay frequency,
	# get fed tax withholding for the pay period
	federal_tax = get_fed_tax(tax_status, adjusted_taxable_income, frequency)

	# Compute Medicare tax withholding for the pay period
	medicare_tax = (annual_medicare_tax / frequency)

	# Compute Additional Medicare withholding for the pay period
	additional_medicare_tax = (addl_medicare_tax / frequency)

	# Consolidate Medicare Tax
	medicare = medicare_tax + additional_medicare_tax
	
	# Compute Social Security tax withholding for the pay period
	social_security_tax = (ss_tax / frequency)
	
	# Compute Net Income
	net_income = payperiod_income - tax_deferral_amount - federal_tax \
	-medicare - social_security_tax
	
	# Display results
	print('\n\n\n\n')
	print('********************     PAY STUB     ********************\n\nGross Income: ' + "${:0,.2f}".format(payperiod_income))
	print('\nPRE-TAX DEDUCTIONS:\n 401(k) Contribution:                      ' + "${:0,.2f}".format(tax_deduction_401k))  
	print(' 401(k) Catch-up Contribution:             ' + "${:0,.2f}".format(tax_deduction_401k_catchup)) 
	print(' 403(b) Contribution:                      ' + "${:0,.2f}".format(tax_deduction_403b)) 
	print(' 403(b) Catch-up Contribution:             ' + "${:0,.2f}".format(tax_deduction_403b_catchup)) 
	print(' Health Savings Account Contribution:      ' + "${:0,.2f}".format(tax_deduction_HSA)) 
	print('\nTAX WITHHOLDINGS:\n Fed Tax Withholding:                      '+ "${:0,.2f}".format(federal_tax))
	print(' Fed MED/EE:                               '+ "${:0,.2f}".format(medicare))
	print(' Fed OASDI/EE:                             '+ "${:0,.2f}".format(social_security_tax))
	print('\nAFTER TAX INCOME:\n Net Income                                '+ "${:0,.2f}".format(net_income))


	# Ask the user to iterate through the loop again or exit()
	
	user_feedback_on_loop = input('\n\n\nWould you like to input '\
	+'another employee? (Y/N): ')
	while user_feedback_on_loop.title() != "Y" and \
	user_feedback_on_loop.title() != "N":
		user_feedback_on_loop = input('Please enter "Y" or "N" to '\
		+'reiterate the program or quit: ')
	
	if user_feedback_on_loop.title() == "N":
		loop_flag = "quit"
	else:
		loop_flag = "run"

#EXIT the program
exit()









