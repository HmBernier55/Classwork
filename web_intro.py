import requests


#r = requests.get("https://api.github.com/repos/HmBernier55/Classwork/branches")
#print(r)
#print(type(r))
#print(r.text)
#if r.status_code == 200:
#    answer = r.json()
#    print(type(answer))
#    for branch in answer:
#        print(branch["name"])
#else:
#    print("Bad request: {}".format(r.text))

#output_info = {"name": "Hunter Bernier",
#               "net_id": "hmb39",
#               "e-mail": "hunter.bernier@duke.edu"}
#r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=output_info)
#print(r)
#print(r.text)

output_file = {"user": "hmb39",
               "message": "hello!"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=output_file)
r1 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/zms14")
print(r1.text)