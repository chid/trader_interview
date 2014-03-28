import speech
import random
from time import sleep
# # simple numerics question

# speech.say(str(2e6)+" minus "+str(291))
# sleep(10)

# # squared

# speech.say("68 squared")
# sleep(10)

# # sqrt

# speech.say("What is the square root of 2049")

# sleep(10)

# # random multiplication

n = int(random.random()*100 + 1)
m = int(random.random()*100 + 1)

speech.say(str(n)+" times "+str(m))
sleep(10)
speech.say(str(n*m)+" is the answer")
