

# driver.py


import sys
from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

engine = knowledge_engine.engine(__file__)


def forwardChani():
    
    try:

        engine.reset()
        engine.activate('rules')

        with engine.prove_goal('rules.diagnostico($resultado)') as gen:
            for i, (vars, no_plan) in enumerate(gen):
                resultado = vars['resultado']
                total = resultado[0] + resultado[1] + resultado[2] + resultado[3]
                print ("Denge: ",  round(100*resultado[0]/total) , "% de chance ")
                print ("Zika: ",  round(100*resultado[1]/total), "% de chance ")
                print ("Chikungunya: ", round( 100*resultado[2]/total), "% de chance ")
                print ("Outro: ",  round(100*resultado[3]/total), "% de chance ")



    except:
        krb_traceback.print_exc()
        sys.exit(1)


