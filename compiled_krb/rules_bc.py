# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def diagnostico(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'diagnostico1', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.diagnostico: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'int_hipertrofiaganglionar', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.diagnostico: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'int_discrasiahemorragica', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.diagnostico: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(3).match_data(context, context,
                            list(sum(context.lookup_data('result1'),sum(context.lookup_data('hipertrofiaganglionar'),context.lookup_data('discrasia'))))):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def diagnostico1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'int_febre', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.diagnostico1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'int_mancha', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.diagnostico1: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'int_dormuscular', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.diagnostico1: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'freq_dorarticular', context,
                                      (rule.pattern(3),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.diagnostico1: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'tem_conjuntivite', context,
                                          (rule.pattern(4),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.diagnostico1: got unexpected plan from when clause 5"
                            with engine.prove(rule.rule_base.root_name, 'int_edemaart', context,
                                              (rule.pattern(5),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.diagnostico1: got unexpected plan from when clause 6"
                                with engine.prove(rule.rule_base.root_name, 'int_dorcabeca', context,
                                                  (rule.pattern(6),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.diagnostico1: got unexpected plan from when clause 7"
                                    with engine.prove(rule.rule_base.root_name, 'int_acrometimentoNeurologico', context,
                                                      (rule.pattern(7),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.diagnostico1: got unexpected plan from when clause 8"
                                        with engine.prove(rule.rule_base.root_name, 'int_coceira', context,
                                                          (rule.pattern(8),)) \
                                          as gen_9:
                                          for x_9 in gen_9:
                                            assert x_9 is None, \
                                              "rules.diagnostico1: got unexpected plan from when clause 9"
                                            mark10 = context.mark(True)
                                            if rule.pattern(9).match_data(context, context,
                                                    sum(context.lookup_data('febre2'),sum(context.lookup_data('mancha2'),sum(context.lookup_data('dormuscular'),sum(context.lookup_data('articular2'),sum(context.lookup_data('conjuntivite'),sum(context.lookup_data('edemartic'),sum(context.lookup_data('acometimentoneurologico'),sum(context.lookup_data('dordecabeca'),context.lookup_data('coceiraa')))))))))):
                                              context.end_save_all_undo()
                                              rule.rule_base.num_bc_rule_successes += 1
                                              yield
                                            else: context.end_save_all_undo()
                                            context.undo_to_mark(mark10)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_febre(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'febre2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_febre: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Ffebre_manchas (context.lookup_data('ans_febre2'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_mancha(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'manchas2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_mancha: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Ffebre_manchas (context.lookup_data('ans_mancha2'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_dormuscular(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'dorMuscular', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_dormuscular: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Fdor_muscular (context.lookup_data('ans_dor_musc'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def freq_dorarticular(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'dorArticular2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.freq_dorarticular: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Fdor_articular2 (context.lookup_data('ans_dor_art2'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def tem_conjuntivite(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'conjuntivite', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.tem_conjuntivite: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Fconjuntivite (context.lookup_data('ans_conjuntivite'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_edemaart(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'edemaArticulacao2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_edemaart: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    FedemaArticulacao2 (context.lookup_data('ans_edemart'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_dorcabeca(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'dordecabeca2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_dorcabeca: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Fintdorcabeca2 (context.lookup_data('ans_dorcabeca'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_coceira(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'coceira2', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_coceira: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Fintcoceira (context.lookup_data('ans_coceira'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_acrometimentoNeurologico(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'acrometimentoNeurologico', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_acrometimentoNeurologico: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    FacrometimentoNeurologico (context.lookup_data('ans_acrometimentoNeurologico'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_hipertrofiaganglionar(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'hipertrofiaGanglionar', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_hipertrofiaganglionar: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Fhipertrofiaganglionar (context.lookup_data('ans_hipertrofiaganglionar'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def int_discrasiahemorragica(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'discrasiaHemorragica', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.int_discrasiahemorragica: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(1).match_data(context, context,
                    Fdiscrasiahemorragica (context.lookup_data('ans_discrasiahemorragica'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('diagnostico', This_rule_base, 'diagnostico',
                  diagnostico, None,
                  (contexts.variable('resultado'),),
                  (),
                  (contexts.variable('result1'),
                   contexts.variable('hipertrofiaganglionar'),
                   contexts.variable('discrasia'),
                   contexts.variable('resultado'),))
  
  bc_rule.bc_rule('diagnostico1', This_rule_base, 'diagnostico1',
                  diagnostico1, None,
                  (contexts.variable('result1'),),
                  (),
                  (contexts.variable('febre2'),
                   contexts.variable('mancha2'),
                   contexts.variable('dormuscular'),
                   contexts.variable('articular2'),
                   contexts.variable('conjuntivite'),
                   contexts.variable('edemartic'),
                   contexts.variable('dordecabeca'),
                   contexts.variable('acometimentoneurologico'),
                   contexts.variable('coceiraa'),
                   contexts.variable('result1'),))
  
  bc_rule.bc_rule('int_febre', This_rule_base, 'int_febre',
                  int_febre, None,
                  (contexts.variable('intfebre'),),
                  (),
                  (contexts.variable('ans_febre2'),
                   contexts.variable('intfebre'),))
  
  bc_rule.bc_rule('int_mancha', This_rule_base, 'int_mancha',
                  int_mancha, None,
                  (contexts.variable('intmancha'),),
                  (),
                  (contexts.variable('ans_mancha2'),
                   contexts.variable('intmancha'),))
  
  bc_rule.bc_rule('int_dormuscular', This_rule_base, 'int_dormuscular',
                  int_dormuscular, None,
                  (contexts.variable('intdormuscular'),),
                  (),
                  (contexts.variable('ans_dor_musc'),
                   contexts.variable('intdormuscular'),))
  
  bc_rule.bc_rule('freq_dorarticular', This_rule_base, 'freq_dorarticular',
                  freq_dorarticular, None,
                  (contexts.variable('intdorarticular'),),
                  (),
                  (contexts.variable('ans_dor_art2'),
                   contexts.variable('intdorarticular'),))
  
  bc_rule.bc_rule('tem_conjuntivite', This_rule_base, 'tem_conjuntivite',
                  tem_conjuntivite, None,
                  (contexts.variable('temconjuntivite'),),
                  (),
                  (contexts.variable('ans_conjuntivite'),
                   contexts.variable('temconjuntivite'),))
  
  bc_rule.bc_rule('int_edemaart', This_rule_base, 'int_edemaart',
                  int_edemaart, None,
                  (contexts.variable('intedemart'),),
                  (),
                  (contexts.variable('ans_edemart'),
                   contexts.variable('intedemart'),))
  
  bc_rule.bc_rule('int_dorcabeca', This_rule_base, 'int_dorcabeca',
                  int_dorcabeca, None,
                  (contexts.variable('intdorcabeca'),),
                  (),
                  (contexts.variable('ans_dorcabeca'),
                   contexts.variable('intdorcabeca'),))
  
  bc_rule.bc_rule('int_coceira', This_rule_base, 'int_coceira',
                  int_coceira, None,
                  (contexts.variable('intcoceira'),),
                  (),
                  (contexts.variable('ans_coceira'),
                   contexts.variable('intcoceira'),))
  
  bc_rule.bc_rule('int_acrometimentoNeurologico', This_rule_base, 'int_acrometimentoNeurologico',
                  int_acrometimentoNeurologico, None,
                  (contexts.variable('intacrometimentoNeurologico'),),
                  (),
                  (contexts.variable('ans_acrometimentoNeurologico'),
                   contexts.variable('intacrometimentoNeurologico'),))
  
  bc_rule.bc_rule('int_hipertrofiaganglionar', This_rule_base, 'int_hipertrofiaganglionar',
                  int_hipertrofiaganglionar, None,
                  (contexts.variable('inthipertrofiaganglionar'),),
                  (),
                  (contexts.variable('ans_hipertrofiaganglionar'),
                   contexts.variable('inthipertrofiaganglionar'),))
  
  bc_rule.bc_rule('int_discrasiahemorragica', This_rule_base, 'int_discrasiahemorragica',
                  int_discrasiahemorragica, None,
                  (contexts.variable('intdiscrasiahemorragica'),),
                  (),
                  (contexts.variable('ans_discrasiahemorragica'),
                   contexts.variable('intdiscrasiahemorragica'),))

def sum (tuple1, tuple2):
        list1 = list(tuple1)
        list2 = list(tuple2)
        list1[0] = list1[0] + list2[0]
        list1[1] = list1[1] + list2[1]
        list1[2] = list1[2] + list2[2]
        list1[3] = list1[3] + list2[3]
        return tuple(list1)
def Ffebre_manchas(n):
        if n == 0: return (0, 0, 0, 1)
        if n == 1: return (1, 0, 0, 0)
        if n == 2: return (0, 0, 2, 0)
        if n == 3: return (1, 3, 1, 0)
def Fdor_muscular(n):
        if n == 0: return (0, 0, 0, 1)
        if n == 1: return (0, 0, 2, 0)
        if n == 2: return (0, 2, 0, 0)
        if n == 3: return (3, 0, 0, 0)
def Fdor_articular2(n):
        if n == 0: return (0, 0, 0, 1)
        if n == 1: return (1, 0, 0, 0)
        if n == 2: return (0, 1, 0, 0)
        if n == 3: return (0, 0, 2, 0)
def FedemaArticulacao2(n):
        if n == 0: return (1, 0, 0, 1)
        if n == 1: return (0, 1, 0, 0)
        if n == 2: return (0, 0, 2, 0)
        if n == 3: return (0, 0, 2, 0)
def Fconjuntivite(boleano):
        if boleano == True: return (0,2,1,0)
        if boleano == False: return (1,0,0,2)
def Fintdorcabeca2(n):
        if n == 0: return (1, 0, 0, 2)
        if n == 1: return (0, 0, 0, 1)
        if n == 2: return (0, 1, 1, 0)
        if n == 3: return (2, 0, 0, 0)
def Fintcoceira(n):
        if n == 0: return (0, 0, 0, 1)
        if n == 1: return (1, 0, 0, 0)
        if n == 2: return (0, 1, 1, 0)
        if n == 3: return (0, 2, 1, 0)
def FacrometimentoNeurologico(boleano):
        if boleano == True: return (0,2,0,1)
        if boleano == False: return(1,0,2,0)
def Fhipertrofiaganglionar(n):
        if n == 0: return (0, 0, 0, 1)
        if n == 1: return (1, 0, 0, 0)
        if n == 2: return (0, 0, 1, 0)
        if n == 3: return (0, 2, 0, 0)
def Fdiscrasiahemorragica(n):
        if n == 0: return (0, 1, 0, 0)
        if n == 1: return (1, 0, 1, 0)
        if n == 2: return (1, 0, 0, 0)
        if n == 3: return (0, 0, 0, 1)

Krb_filename = '..\\exprtSystem\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (6, 6)),
    ((26, 31), (8, 8)),
    ((32, 37), (10, 10)),
    ((40, 40), (12, 12)),
    ((56, 60), (16, 16)),
    ((62, 67), (20, 20)),
    ((68, 73), (22, 22)),
    ((74, 79), (24, 24)),
    ((80, 85), (26, 26)),
    ((86, 91), (28, 28)),
    ((92, 97), (30, 30)),
    ((98, 103), (32, 32)),
    ((104, 109), (34, 34)),
    ((110, 115), (36, 36)),
    ((118, 118), (38, 38)),
    ((134, 138), (43, 43)),
    ((140, 145), (45, 45)),
    ((148, 148), (47, 47)),
    ((164, 168), (51, 51)),
    ((170, 175), (53, 53)),
    ((178, 178), (55, 55)),
    ((194, 198), (59, 59)),
    ((200, 205), (61, 61)),
    ((208, 208), (63, 63)),
    ((224, 228), (67, 67)),
    ((230, 235), (69, 69)),
    ((238, 238), (71, 71)),
    ((254, 258), (75, 75)),
    ((260, 265), (77, 77)),
    ((268, 268), (79, 79)),
    ((284, 288), (85, 85)),
    ((290, 295), (87, 87)),
    ((298, 298), (89, 89)),
    ((314, 318), (92, 92)),
    ((320, 325), (94, 94)),
    ((328, 328), (96, 96)),
    ((344, 348), (100, 100)),
    ((350, 355), (102, 102)),
    ((358, 358), (104, 104)),
    ((374, 378), (107, 107)),
    ((380, 385), (109, 109)),
    ((388, 388), (111, 111)),
    ((404, 408), (115, 115)),
    ((410, 415), (117, 117)),
    ((418, 418), (118, 118)),
    ((434, 438), (121, 121)),
    ((440, 445), (123, 123)),
    ((448, 448), (124, 124)),
)
