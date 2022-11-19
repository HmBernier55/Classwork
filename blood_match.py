import requests


def blood_match_calc(BT1, BT2):
    if BT1 == "A+" and BT2 in ["A+", "A-", "O+", "O-"]:
        return "Yes"
    elif BT1 == "A-" and BT2 in ["A-", "O-"]:
        return "Yes"
    elif BT1 == "B+" and BT2 in ["B+", "B-", "O+", "O-"]:
        return "Yes"
    elif BT1 == "B-" and BT2 in ["B-", "O-"]:
        return "Yes"
    elif BT1 == "AB+":
        return "Yes"
    elif BT2 == "AB-" and BT2 in ["AB-", "A-", "B-", "O-"]:
        return "Yes"
    elif BT1 == "O+" and BT2 in ["O+", "O-"]:
        return "Yes"
    elif BT1 == "O-" and BT2 == "O-":
        return "Yes"
    else:
        return "No"


r_id = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/hmb39")
patient_ids = r_id.json()
print(patient_ids)


r_blood_type_recip = requests.get("http://vcm-7631.vm.duke.edu:5002/"
                                  "get_blood_type/{}"
                                  .format(patient_ids["Recipient"]))
r_blood_type_donor = requests.get("http://vcm-7631.vm.duke.edu:5002/"
                                  "get_blood_type/{}"
                                  .format(patient_ids["Donor"]))
print(r_blood_type_recip.text)
print(r_blood_type_donor.text)

answer = blood_match_calc(r_blood_type_recip.text, r_blood_type_donor.text)

out_data = {"Name": "hmb39", "Match": answer}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json=out_data)
print(r.status_code)
print(r.text)
