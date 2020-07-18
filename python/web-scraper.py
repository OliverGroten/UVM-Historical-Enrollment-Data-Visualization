import urllib.request

url_base = "https://giraffe.uvm.edu/~rgweb/batch/enrollment/curr_enroll_"

for i in range(1995, 2021):
    for j in [1, 6, 9]:
        url_end = str(i) + "0" + str(j) + ".txt"
        url = url_base + url_end
        f = open("../data/" + url_end, 'w')
        response = urllib.request.urlopen(url)
        for line in response:
            f.write(line.decode('utf-8'))
        f.close()
