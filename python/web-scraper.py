import urllib.request

url = "https://giraffe.uvm.edu/~rgweb/batch/enrollment/curr_enroll_199501.txt"
response = urllib.request.urlopen(url)

for line in response:
    print(line.decode('utf-8'))