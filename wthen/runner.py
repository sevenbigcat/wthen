import yaml

class RuleRunner():
  @classmethod
  def evaluate_conditions(cls, when, scope):
    eval_result = False
    for w in when:
      eval_result = eval(w, globals(), scope)
      if eval_result == False:
        break
    return eval_result

  @classmethod
  def run_rule(cls, r, scope):
    output = r.get('output', None)
    g = globals()
    pre = r.get('pre', [])
    for p in pre:
      exec(p, g, scope)

    when = r.get('when', [])
    eval_result = cls.evaluate_conditions(when, scope)
    if eval_result == False:
      if output == None:
        return False
      else:
        return None

    then = r.get('then', [])
    for t in then:
      exec(t, globals(), scope)

    if output == None:
      return True
    else:
      rule_output = []
      for o in output:
        ov = scope.get(o)
        if ov != None:
          rule_output.append({o: ov})
      return rule_output

  def run_file(self, rule_file, rule_name_to_match=None, scope=None):
    with open(rule_file) as file:
      content = file.read()
    return self.run_text(content, rule_name_to_match, scope)

  def run_text(self, rule_text, rule_name_to_match=None, scope=None):
    rules = yaml.load(rule_text)
    rule_array = rules.get('rules')
    if rule_array != None:
      all_results = []
      for rule in rule_array:
        r = rule.get('rule')
        rule_name = r.get('name')
        
        if rule_name_to_match == None or rule_name_to_match == rule_name:
          rule_output = self.run_rule(r, scope)
          all_results.append(rule_output)
      all_filter_rules = True
      final_result = None
      for res in all_results:
        if type(res) == bool:
          final_result = final_result != False and res == True
        else:
          all_filter_rules = False
          break
        
      if all_filter_rules == True:
        return final_result
      else:
        if len(all_results) == 1:
          if all_results[0] == None:
            return None
          if len(all_results[0]) == 1:
            return all_results[0][0]
        return all_results
  def __init__(self):
    pass
