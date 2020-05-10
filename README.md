# Functionality
The scraper currently scrapes all cases in the first page of the supreme court cases list
`scrapy crawl ng`

# The Database
![alt text](https://github.com/cleve02/nigerian-judgements/blob/master/db_model.jpg)
## cases

 - **url** = TextField `url to the summary page of the judgement`
 - **name** =  TextField `full case name`
 - **name_abbreviation** =  CharField `
 - **suite_no** =  CharField 
 - **decision_date** =  DateField `formatted date text`
 - **citations** =  TextField
 - **court** =  CharField `currently defaults to "Supreme Court of Nigeria" `
 - **full_judgement** =  TextField 
 - **appellants** =  TextField `each appellant is in a new line`
 - **respondents** =  TextField `each respondent is in a new line`
 - **full_html** =  TextField `full html of the case page incase you need further parsing`

## opinions

 - **case_id** =  ForeignKeyField
 - **author** =  TextField
 - **text** = TextField

## ratio_decidendi

 - **case_id** =  ForeignKeyField
 - **matter** =  CharField
 - **topic** =  CharField
 - **text** = TextField
 - **author_ref** = TextField `author & reference`

## judges

 - **case_id** =  ForeignKeyField
 - **name** =  TextField
 - **title** = TextField

## attorneys

 - **case_id** =  ForeignKeyField
 - **name** =  TextField
 - **representing** = TextField `either "Appellant(s)" or "Respondent(s)"` 
 

 # Pending Issues
 - prefect.io flow
 - Self sufficiency with the spider

