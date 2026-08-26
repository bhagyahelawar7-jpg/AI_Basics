Knowledge = {
    "fever" : True,
    "cough" : True,
    "headache" :False
}
if Knowledge["fever"] and Knowledge["cough"]:
    Decision = "Posible Infection"
elif Knowledge["headache"] :
    Decision = "Need More information ."
else:
    Decision ="not able to find the condition."
 

print("Knowledge" ,Knowledge)
print("Ai Knowledge" ,Decision)