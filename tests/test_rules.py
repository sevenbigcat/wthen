import wthen

def test_rule_filter():
    scope = {
        'bb' : 3,
        'cc' : 5,
        'dd' : 6,
    }
    assert wthen.run_all('tests/rules_filter.yaml', scope) == True
    
def test_rule_action():
    scope = {
        'bb' : 3,
        'cc' : 5,
        'dd' : 6,
    }
    assert wthen.run_all('tests/rules_action.yaml', scope) == {'aa': 4}

def test_rule_missing_elements():
    assert wthen.run_all('tests/rules_no_then.yaml') == True
    assert wthen.run_all('tests/rules_no_when.yaml') == False
    assert wthen.run_all('tests/rules_no_pre.yaml') == True

def test_rule_reference():
    assert wthen.run_all('tests/rules_references.yaml') == True

def test_rule_obj_reference():
    assert wthen.run_all('tests/rules_object_references.yaml') == True
