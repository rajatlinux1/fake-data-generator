from faker import Faker
import xlsxwriter
import csv
import json
from tqdm import tqdm
fake = Faker()




def excel(limit=1, filename='fake'):
    
    workbook=xlsxwriter.Workbook(f'{filename}.xlsx')
    worksheet=workbook.add_worksheet()
    worksheet.write(0,0, "Sr.No")
    worksheet.write(0,1, "Name")
    worksheet.write(0,2, "Gender")
    worksheet.write(0,3, "Job")
    worksheet.write(0,4, "Mail")
    worksheet.write(0,5, "DOB")
    worksheet.write(0,6, "SSN")
    worksheet.write(0,7, "Blood Group")
    worksheet.write(0,8, "Address")
    worksheet.write(0,9, "Company")
    worksheet.write(0,10, "Date")

    for _ in tqdm(range(1, limit+1), desc="generating..."):
        profile = fake.profile()
        

        SRNO = _
        NAME = profile.get("name")
        GENDER = profile.get("sex")
        JOB = profile.get("job")
        MAIL = profile.get("mail")
        DOB = str(profile.get("birthdate"))
        SSN = profile.get("ssn")
        BLOODGROUP = profile.get("blood_group")
        ADRESS = str(profile.get("address")).replace("\n", "")
        COMPANY = profile.get("company")
        DATE = str(fake.date_between(start_date="-7y",end_date="-1y"))



        worksheet.write(_, 0, SRNO)
        worksheet.write(_, 1, NAME)
        worksheet.write(_, 2, GENDER)
        worksheet.write(_, 3, JOB)
        worksheet.write(_, 4, MAIL)
        worksheet.write(_, 5, DOB)
        worksheet.write(_, 6, SSN)
        worksheet.write(_, 7, BLOODGROUP)
        worksheet.write(_, 8, ADRESS)
        worksheet.write(_, 9, COMPANY)
        worksheet.write(_, 10, DATE)
    workbook.close()
    print("Done, Excel generated")

def csvfile(limit=0, filename="fake"):

    file = open(f'{filename}.csv', 'w')
    writer = csv.writer(file)
    data = ["Sr.No", "Name", "Gender", "Job", "Mail", "DOB", "SSN", "Blood Group", "Address" "Company" "Date"]
    writer.writerow(data)

    for _ in tqdm(range(1, limit+1), desc="generating..."):
        profile = fake.profile()

        SRNO = _
        NAME = profile.get("name")
        GENDER = profile.get("sex")
        JOB = profile.get("job")
        MAIL = profile.get("mail")
        DOB = str(profile.get("birthdate"))
        SSN = profile.get("ssn")
        BLOODGROUP = profile.get("blood_group")
        ADRESS = str(profile.get("address")).replace("\n", "")
        COMPANY = profile.get("company")
        DATE = str(fake.date_between(start_date="-7y",end_date="-1y"))
        writer.writerow([SRNO, NAME, GENDER, JOB, MAIL, DOB, SSN, BLOODGROUP,ADRESS, COMPANY, DATE])
    file.close()
    print("Done, CSV generated")

def jsonfile(limit=10, filename="fake"):
    data = []
    for _ in tqdm(range(1, limit+1), desc="generating..."):
        dictionary = {}
        profile = fake.profile()

        SRNO = _
        NAME = profile.get("name")
        GENDER = profile.get("sex")
        JOB = profile.get("job")
        MAIL = profile.get("mail")
        DOB = str(profile.get("birthdate"))
        SSN = profile.get("ssn")
        BLOODGROUP = profile.get("blood_group")
        ADRESS = str(profile.get("address")).replace("\n", "")
        COMPANY = profile.get("company")
        DATE = str(fake.date_between(start_date="-7y",end_date="-1y"))

        dictionary["SRNO"] = SRNO
        dictionary["NAME"] = NAME
        dictionary["GENDER"] = GENDER
        dictionary["JOB"] = JOB
        dictionary["MAIL"] = MAIL
        dictionary["DOB"] = DOB
        dictionary["SSN"] = SSN
        dictionary["BLOODGROUP"] = BLOODGROUP
        dictionary["ADRESS"] = ADRESS
        dictionary["COMPANY"] = COMPANY
        dictionary["DATE"] = DATE

        data.append(dictionary)

 
    # Serializing json
    json_object = json.dumps(data, indent=4)
    
    # Writing to sample.json
    file = open(f'{filename}.json', 'w')
    file.write(json_object)
    file.close()
    print("Done, JSON generated")


if __name__ == "__main__":

    attempt = 3
    while attempt>0:

        opt = int(input("1:Excel\n2:CSV\n3:Json\n>> "))
        if opt == 1:
            limit = int(input("Set limit <1\n>> "))
            if limit > 0:
                excel(limit)
            attempt = 0
            
        elif opt == 2:
            limit = int(input("Set limit <1\n>> "))
            if limit > 0:
                csvfile(limit)
            attempt = 0
            
        elif opt == 3:
            limit = int(input("Set limit <1\n>> "))
            if limit > 0:
                jsonfile(limit)
            attempt = 0
            
        else:
            attempt -= 1
            if attempt > 0:
                print(f"\033[91m You have {attempt} attempt left, Chose any digit.\033[0m\n")
            else:
                print(f"\033[91m Sorry, You have no attempt left\033[0m\n")