
to  interact with program...



                print "USAGE:------------------------------------------\n"
                print "-P  <space> <Name of the place>"
                print "-TP <space> <Type of the place>"
                print "-TH <space> <Type of the hotel>"
                print "-B  <space> <Budget of the hotel> OR <Lower limit>@<Higher limit>"
                print "-W  <space> <Weather of the place>"
                print "-H  <space> <Name of the hotel>"
                print "-D  <space> <Distance> OR <Lower limit>@<Higher limit>"
                print "-DY <space> <No of days>"
                print "-C  <space> <City>"
                print "-S  <space> <State>"
                print "-M  <space> <Name of the month>"
                print "-DL <space> <Distance less than>"
                print "-DG <space> <Distance greater than>"
                print "-BG <space> <Budget greater than>"
                print "_BL <space> <Budget lesser than>\n"



-D can used for specific distance or range
	-D 7000
		gives places with distance 7000
	-D 7000@8000
		gives places with distance in range 7000 and 8000 (both  including)

-B can used for specific budget or range
	-B 7000
		gives places with budget 7000
	-B 7000@8000
		gives places with budget in range 7000 and 8000 (both  including)




Generator.py generates the test data base
