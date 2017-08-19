### Classify the Email in GMail using Machine Learning Algorithms

* Classifiying Emails as Spam or Not Spam Using Text Classification and GMail API with Machine Learning Algorithms.

#### Four Key Files:

**1. Email_Classifier.py:**
     
     To generate Test Data i.e. mails in spam folder along with other mails from your gmail account and stored in csv file.
     Details of Email Fetched using Gmail API:
          
          Mails from Inbox along with existing Spam emails.
          Subject of the Mail
          Snippet of the Mail
          Mail ID of the Sender
          Date and Time of the Email

**2. Client_secret.json:**
      
      A authentication file to access gmail.
      This file will be available once authentication is done.
      Store the file in Workspace.
      https://developers.google.com/gmail/api/quickstart/python
      
**3. Email_Classifiers.py:**
      
      It contains code to fetch updated emails from Gmail Inbox based on Date and Time.
      The function from "Email_Classifier.py" file is called, to access the email and appended 
      to test data for classification purpose.
      It contains all the Machine Learning and text classification methods to classify the email.
      Find the accuracy score of the Email Classification
      
**4. EmailClass.png:**

      Email Data used for classification using Machine Learning Algorithm.
