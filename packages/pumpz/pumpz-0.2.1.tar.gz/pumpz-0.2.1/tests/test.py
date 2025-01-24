import pumpz as pz

print('hello world')

f_aq = open("aq.ppl", "w")
f_org = open("org.ppl", "w")
f_dummy = open("dummy.ppl", "w")
f_master = open("master.ppl", "w")

aq = pz.Pump(f_aq, 26.59)
org = pz.Pump(f_org, 26.59)
dummy = pz.Pump(f_dummy, 26.59)
master = pz.Masterppl(f_master)
master.quickset({0: org, 1: aq})

pz.Pump.init(aq, org, dummy)

aq.rate(22, 20, "wdr")
org.rate(22, 20, "wdr")
aq.rate(10, 20, "inf")
pz.Pump.sync(aq, org) # sync org to aq

org.rate(10, 20, "inf")
pz.Pump.sync(org,dummy) #sync dummy to org
dummy.pause(3*60)
org.pause(30)
pz.Pump.sync(aq,org) #sync aq to org
aq.rate(22,50,'wdr')
org.rate(22,50,'wdr')
pz.Pump.sync(aq,org,dummy) #sync aq, org to dummy

aq.loopstart(2)
org.loopstart(2)

aq.rate(22,50,'inf')
org.rate(22,50,'inf')
aq.rate(22,50,'wdr')
org.rate(22,50,'wdr')

aq.loopend()
org.loopend()

aq.rate(22,50,'inf')
org.rate(22,50,'inf')

pz.Pump.stop(aq, org)
