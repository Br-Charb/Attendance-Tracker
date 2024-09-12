import pandas as pd

#attendance csv file goes here ↓↓↓↓↓↓
attendanceForm = '9_5 Lunch BETA Attendance Form (Responses) - Form Responses 1.csv'

#opens csv and extracts emails column
attForm = (pd.read_csv(attendanceForm))
emails = attForm['Email Address']

#adds first 10 char of email (480s) to list
att = ['4804315070', '4806003682', '4804169889', '4804168512', '4804170072', '4806894848', '4804169951', '4804209159', '4804189176', '4804174096', '4804205750']
for i, num in enumerate(emails):
    if (emails.isna()[i] == False):
        att.append(num.strip()[0:10])
att = list(set(att))
#attendance csv file goes here ↓↓↓↓↓↓ <- if updated for new members needs to be re-downloaded
betaLog = 'Beta Attendance 2024-2025 - Sheet1.csv'

#opens csv and extracts student nums column
log = (pd.read_csv(betaLog))
stuNums = log['Student Number']


#checks each student num to see if recorded in form
for p in stuNums:
    if str(p).strip() in att:
        print("Yes")
        att.remove(str(p))
    else:
        print("No")

#prints list of all numbers that were unused
print("\n\n", att)