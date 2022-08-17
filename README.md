# MS_Fintech_Published_Assignments
This repositiory was created to publish code written as an assignment 
throughout my Master of Science in Financial Technology and Analytics degree program.


##Payroll_Program_KevinBurch_2022.08.15.py

	This first program is a basic payroll program that recieves input from a
	user and returns a paystub for an employee. Students were given broad latitute
	to create a program with little restrictions. I sourced the uploaded support
	from the IRS as reference, and this code was my product.   

	The purpose of this program is to communicate an understanding of some
	elementary concepts in Python, including variables, expresions, 
	statements, conditional execution, functions, loops & iterations, and 
	strings. It also demponstrates applied knowledge of recieving and 
	validating user inputs, modular programing styles, and communication 
	(comments) with the back-end user or analyst who maintains the code. 

	The program itself calculates the payroll for a population of
	employees in a payroll cycle. The program has a broad scope, and can
	apply to most businesses opporated in the United States of America.

	The program makes some assumptions, such as: 
		1) This payroll is the only source of W4 income for each employee
			*This program does not account for additional W4 employment
			*This program does not account for additional withholdings income 
		2) the federal minimum wage is still $7.50/hr;
		3) the program does not consider overtime or holiday pay rates
		4) hourly employees grossing >=$250K annually will be converted to salary
		5) utilizes 2022 tax brackets   

	 As the program iterates, a individual contributor will manually input 
	 the following employee payroll data fields:

		Age; 
		Tax Status;
	    	Number of Dependants per the most recent Form W-4;
		Wage Type; 
	   	Wage Rate - either Hourly, or Annualized;
	    	Hours worked -
			The program will only prompt for hours worked if the employee 
			is a hourly employee. The program will not prompt for salaried
			employees;

		401(k) contribution amount;
	    	401(k) catch-up contribution amount -
			The program will only prompt for catch-up amount if the employee 
			is 50 years of age or senior. The program will not prompt for 
			a catch-up amount if the employee is 49 or junior;
	    	403(b) contribution amount;
		403(b) catch-up contribution amount;
			The program will only prompt for catch-up amount if the employee 
			is 50 years of age or senior. The program will not prompt for 
			a catch-up amount if the employee is 49 or junior;
	    	Health Savings Account contribution amount;
		-No entry for post-tax deductions;

	 Based on the entry of the data points above, the program will calculate
	 the payroll tax amount for each employee and display that information 
	 formatted in a logical manner. 
