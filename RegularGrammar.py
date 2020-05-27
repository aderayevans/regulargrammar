import pickle
import numbers
class Production_rule:
    def __init__(self):
        self.the_cause = ''
        self.the_consequence = ''
    def import_(self):
        self.the_cause = input('The cause: ')
        self.the_consequence = input('The consequence: ')
    def display(self):
        print(self.the_cause + ' --> ' + self.the_consequence)
    def set_the_cause(self, the_cause):
        self.the_cause = the_cause
    def set_the_consequence(self, the_consequence):
        self.the_consequence = the_consequence
    def get_the_cause(self):
        return self.the_cause
    def get_the_consequence(self):
        return self.the_consequence
    def get_first_char_in_the_consequence(self):
        return self.the_consequence[0]
    def get_last_char_in_the_consequence(self):
        return self.the_consequence[len(self.the_consequence)-1]
class Regular_grammar:
    def __init__(self):
        self.variables = []
        self.terminal_symbols = []
        self.start_symbol =''
        self.production_rules = []
    def import_(self):
        print('Begin to import regular grammar:')
        while True:
            try:
                v_amount = int(input('How many variables: '))
                if isinstance(v_amount, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        self.variables = ['']*v_amount
        for index in range(0, v_amount):
            while True:
                temp = input('/<' + str(index+1) + '>: ')
                if temp in self.variables:
                    print('DuplicateValue!!!, please type again')
                else:
                    self.variables[index] = temp
                    break
        while True:
            try:
                t_amount = int(input('How many terminal_symbols: '))
                if isinstance(t_amount, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        self.terminal_symbols = ['']*t_amount
        for index in range(0, t_amount):
            while True:
                temp = input('/<' + str(index+1) + '>: ')
                if temp in self.terminal_symbols or temp in self.variables:
                    print('DuplicateValue!!!, please type again')
                else:
                    self.terminal_symbols[index] = temp
                    break
        while True:
            self.start_symbol = input('which is start symbol: ')
            if self.start_symbol in self.variables:
                break
            else:
                print('Symbol Not Found!!!, please type again')
        while True:
            try:
                p_amount = int(input('How many production rules: '))
                if isinstance(p_amount, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        self.production_rules = ['']*p_amount
        for index in range(0, p_amount):
            self.production_rules[index] = Production_rule()
            print('Importing production rule (' + str(index+1) + '):')
            self.production_rules[index].import_()
    def display(self):
        print('>>Regular grammar:')
        print('Variables: ')
        for index in range(0, len(self.variables)):
            print('/<' + str(index+1) + '>: ' + self.variables[index])
        print('Terminal symbols: ')
        for index in range(0, len(self.terminal_symbols)):
            print('/<' + str(index+1) + '>: ' + self.terminal_symbols[index])
        print('P:' + str(len(self.production_rules)))
        for index in range(0, len(self.production_rules)):
            self.production_rules[index].display()
    def get_start_symbol(self):
        return self.start_symbol
    def build_alphabets(self):
        states = self.build_states()
        alphabets = []
        for index in range(0, len(states)):
            if len(states[index]) == 1:
                if states[index] in self.terminal_symbols or states[index] == 'Eps':
                    alphabets.append(states[index])
        return alphabets
    def build_states(self):
        states = []
        for index in range (0, len(self.production_rules)):
            states.append(self.production_rules[index].get_the_cause())
            states.append(self.production_rules[index].get_the_consequence())
        states = list(dict.fromkeys(states))
        return states
    def build_extra_states(self):
        states = self.build_states()
        list_extra = []
        temp_states = []
        for index in range (0, len(states)):
            if len(states[index]) > 1 and states[index] != 'Eps' or states[index] in self.terminal_symbols:
                temp_states.append(states[index])
        while True:
            list_member_amount = 0
            for index in range (0, len(temp_states)):
                if temp_states[index] in self.terminal_symbols:
                    temp_list = [temp_states[index], 'Eps', temp_states[index]]
                    list_extra.append(temp_list)
                    temp_states[index] = ''
            for index in range (0, len(temp_states)):
                if len(temp_states[index]) > 1:
                    list_member_amount += 1
            if list_member_amount == 0:
                break
            for index in range (0, len(temp_states)):
                if len(temp_states[index]) > 1 and temp_states[index][0] in self.terminal_symbols:
                    temp_str = temp_states[index][1:len(temp_states[index])]
                    temp_list = [temp_states[index], temp_str, temp_states[index][0]]
                    list_extra.append(temp_list)
                    temp_states[index] = temp_str
        return(list_extra)
    def get_cause_consequence(self):
        list_caus_cons = []
        for index in range(0, len(self.production_rules)):
            caus_cons = [None]*2
            caus_cons[0] = self.production_rules[index].get_the_cause()
            caus_cons[1] = self.production_rules[index].get_the_consequence()
            list_caus_cons.append(caus_cons)
        return list_caus_cons
    def set_start_symbol(self, start_symbol):
        self.start_symbol = start_symbol
    def set_terminal_symbols(self, terminal_symbols):
        self.terminal_symbols = terminal_symbols
    def set_variables(self, variables):
        self.variables = variables
    def set_production_rules(self, list_inp_out):
        for index in range(0, len(list_inp_out)):
            additional_rules = Production_rule()
            additional_rules.set_the_cause(list_inp_out[index][0])
            additional_rules.set_the_consequence(list_inp_out[index][1])
            self.production_rules.append(additional_rules)
    def is_not_Right_rule(self):
        for index in range (0, len(self.production_rules)):
            if (self.production_rules[index].get_first_char_in_the_consequence() in self.variables
                and self.production_rules[index].get_last_char_in_the_consequence() in self.terminal_symbols):
                return True
        return False
    def reverse_(self, the_str):
        temp_str = the_str[len(the_str)::-1]
        return temp_str
    def reverse_the_consequence(self):
        temp_production_rules = ['']*len(self.production_rules)
        for index in range(0, len(self.production_rules)):
            temp_production_rules[index] = Production_rule()
            temp_production_rules[index].set_the_cause(self.production_rules[index].get_the_cause())
            temp_production_rules[index].set_the_consequence(self.reverse_(self.production_rules[index].get_the_consequence()))
        self.production_rules = temp_production_rules
class Transition:
    def __init__(self):
        self.input_state = ''
        self.output_state = ''
        self.alphabet = ''
    def import_(self):
        self.input_state = input('The input state: ')
        self.alphabet = input('The alphabet: ')
        self.output_state = input('The output state: ')
    def display(self):
        print('Tr(' + self.input_state + ', ' + self.alphabet + ') = ' + self.output_state)
    def set_input_state(self, state):
        self.input_state = state
    def set_output_state(self, state):
        self.output_state = state
    def set_alphabet(self, alphabet):
        self.alphabet = alphabet
    def make_copy(self, input_state, output_state, alphabet):
        self.set_input_state(input_state)
        self.set_output_state(output_state)
        self.set_alphabet(alphabet)
    def get_input_state(self):
        return self.input_state
    def get_output_state(self):
        return self.output_state
    def get_alphabet(self):
        return self.alphabet
class Finite_automata:
    def __init__(self):
        self.states = []
        self.alphabets = []
        self.transitions = []
        self.start_state = ''
        self.final_states = []
        self.current_states = []
    def import_(self):
        print('Begin to import NFA: ')
        while True:
            try:
                s_amount = int(input('How many states: '))
                if isinstance(s_amount, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        self.states = ['']*s_amount
        for index in range(0, s_amount):
            while True:
                temp = input('/<' + str(index+1) + '>: ')
                if temp in self.states:
                    print('DuplicateValue!!!, please type again')
                else:
                    self.states[index] = temp
                    break
        while True:
            try:
                a_amount = int(input('How many alphabets: '))
                if isinstance(a_amount, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        self.alphabets = ['']*a_amount
        for index in range(0, a_amount):
            while True:
                temp = input('/<' + str(index+1) + '>: ')
                if temp in self.alphabets or temp in self.states:
                    print('DuplicateValue!!!, please type again')
                else:
                    self.alphabets[index] = temp
                    break
        while True:
            try:
                t_amount = int(input('How many transition functions: '))
                if isinstance(t_amount, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        self.transitions = ['']*t_amount
        for index in range(0, t_amount):
            self.transitions[index] = Transition()
            print('Importing transition function (' + str(index+1) + '):')
            while True:
                input_temp = input('The input state: ')
                if input_temp in self.states:
                    self.transitions[index].set_input_state(input_temp)
                    break
                else:
                    print('State Not Found!!!, please type again')
            while True:
                alphabet_temp = input('The alphabet: ')
                if alphabet_temp in self.alphabets:
                    self.transitions[index].set_alphabet(alphabet_temp)
                    break
                else:
                    print('Alphabet Not Found!!!, please type again')
            while True:
                output_temp = input('The output state: ')
                if output_temp in self.states:
                    self.transitions[index].set_output_state(output_temp)
                    break
                else:
                    print('State Not Found!!!, please type again')
        while True:
            self.start_state = input('which is start state: ')
            if self.start_state in self.states:
                break
        while True:
            try:
                f_amount = int(input('How many final states: '))
                if f_amount <= 0:
                    print('Required at least one final state')
                elif isinstance(f_amount, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        self.final_states = ['']*f_amount
        for index in range(0, f_amount):
            while True:
                temp = input('/<' + str(index+1) + '>: ')
                if temp in self.final_states or temp in self.alphabets:
                    print('DuplicateValue!!!, please type again')
                elif temp in self.states:
                    self.final_states[index] = temp
                    break
                else:
                    print('State Not Found!!!, please type again')
        self.resetCurrentStates()
    def display(self):
        print('>>Finite automata:')
        print('States: ')
        for index in range(0, len(self.states)):
            print('/<' + str(index+1) + '>: ' + self.states[index])
        print('Alphabets: ')
        for index in range(0, len(self.alphabets)):
            print('/<' + str(index+1) + '>: ' + self.alphabets[index])
        print('Start state: ' + self.start_state)
        if len(self.final_states) == 1:
            print('Final state: ' + self.final_states[0])
        else:
            print('Final states: ')
            for index in range(0, len(self.final_states)):
                print('/<' + str(index+1) + '>: ' + self.final_states[index])
        print('Transition:')
        for index in range(0, len(self.transitions)):
            self.transitions[index].display()
    def get_states(self):
        return self.states
    def get_alphabets(self):
        return self.alphabets
    def get_start_state(self):
        return self.start_state
    def get_final_states(self):
        return self.final_states
    def get_transitions(self):
        list_inp_out = []
        for index in range(0, len(self.transitions)):
            inp_out = [None]*2
            if self.transitions[index].get_output_state() == 'Eps':
                pass
            elif self.transitions[index].get_alphabet() == 'Eps':
                inp_out[0] = self.transitions[index].get_input_state()
                inp_out[1] = self.transitions[index].get_output_state()
            elif self.transitions[index].get_input_state() == self.transitions[index].get_alphabet() + self.transitions[index].get_output_state():
                pass
            else:
                inp_out[0] = self.transitions[index].get_input_state()
                inp_out[1] = self.transitions[index].get_alphabet() + self.transitions[index].get_output_state()
            if inp_out[0] != None:
                list_inp_out.append(inp_out)
        return list_inp_out
    def build_variables(self):
        variables = []
        for index in range(0, len(self.states)):
            if self.states[index] == 'Eps':
                pass
            elif self.states[index][0] in self.alphabets:
                pass
            else:
                variables.append(self.states[index])
        return variables
    def get_extra_transitions(self):
        list_inp_out = []
        for index in range(0, len(self.transitions)):
            if self.final_states[0] == 'Eps':
                list_inp_out = [None]
            elif self.transitions[index].get_output_state() in self.final_states and self.transitions[index].get_alphabet() != 'Eps':
                inp_out = [None]*2
                inp_out[0] = self.transitions[index].get_input_state()
                inp_out[1] = self.transitions[index].get_alphabet()
                list_inp_out.append(inp_out)
        return list_inp_out
    def get_current_states(self):
        return self.current_states
    def set_start_state(self, start_state):
        self.start_state = start_state
    def set_states(self, states):
        self.states = states
        self.states = list(dict.fromkeys(self.states))
    def set_state(self, state):
        self.states.append(state)
        self.states = list(dict.fromkeys(self.states))
    def set_alphabets(self, alphabets):
        self.alphabets = alphabets
        self.alphabets = list(dict.fromkeys(self.alphabets))
    def set_alphabet(self, alphabet):
        self.alphabets.append(alphabet)
        self.alphabets = list(dict.fromkeys(self.alphabets))
    def set_final_states(self, final_state):
        self.final_states = ['']
        self.final_states[0] = final_state
    def define_current(self):
        include_eps = 0
        temp_currents = self.current_states.copy()
        for index_current in range(0, len(self.current_states)):
            currentmultipleways = 0
            for index_transition in range (0, len(self.transitions)):
                if self.current_states[index_current] == self.transitions[index_transition].get_input_state() and self.transitions[index_transition].get_alphabet() == 'Eps':
                    include_eps = 1
                    if currentmultipleways == 0:
                        temp_currents[index_current] = (self.transitions[index_transition].get_output_state() + '.')[:-1]
                        currentmultipleways += 1
                    else:
                        temp_currents.append(self.transitions[index_transition].get_output_state())
        if include_eps == 1: 
            print('Chuyen qua Epsilon ')
            print(temp_currents)          
        self.current_states = temp_currents
    def set_current_states(self, alphabet):
        if self.current_states == []:
            return 1
        temp_currents = self.current_states.copy()
        for index_current in range(0, len(self.current_states)):
            include_alphabet = 0
            currentmultipleways = 0
            for index_transition in range (0, len(self.transitions)):
                if self.current_states[index_current] == self.transitions[index_transition].get_input_state():
                    if alphabet == self.transitions[index_transition].get_alphabet():
                        include_alphabet += 1
                        if currentmultipleways == 0:
                            temp_currents[index_current] = (self.transitions[index_transition].get_output_state() + '.')[:-1]
                            currentmultipleways += 1
                        else:
                            temp_currents.append(self.transitions[index_transition].get_output_state())
            if include_alphabet == 0:
                temp_currents[index_current] = None
        temp_currents = list(filter(None, temp_currents))
        self.current_states = temp_currents
        print('Sau khi nhan ' + alphabet)
        print(self.current_states)
        self.define_current()
        return 0
    def set_transition_type1(self, list_caus_cons):
        for index in range(0, len(list_caus_cons)):
            additional_transition = Transition()
            additional_transition.make_copy(list_caus_cons[index][0], list_caus_cons[index][1], 'Eps')
            self.transitions.append(additional_transition)
    def set_transition_type2(self, input_state, output_state, alphabet):
        additional_transition = Transition()
        additional_transition.make_copy(input_state, output_state, alphabet)
        self.transitions.append(additional_transition)
    def set_extra_states(self, list_extra):
        for extra in list_extra:
            self.set_transition_type2(extra[0], extra[1], extra[2])
            self.set_alphabet(extra[2])
            self.set_state(extra[1])
    def is_not_Right_rule(self):
        if self.start_state == 'Eps':
            return True
        return False
    def reverse_FA(self):
        temp_transitions = ['']*len(self.transitions)
        for index in range(0, len(self.transitions)):
            temp_transitions[index] = Transition()
            temp_transitions[index].make_copy(self.transitions[index].get_output_state(), self.transitions[index].get_input_state(), self.transitions[index].get_alphabet())
        temp_start_state = (self.final_states[0] + '.')[:-1]
        temp_final_state = (self.start_state + '.')[:-1]
        self.start_state = temp_start_state
        self.final_states[0] = temp_final_state
        self.transitions = temp_transitions
    def resetCurrentStates(self):
        self.current_states = ['']
        self.current_states[0] = (self.start_state + '.')[:-1]
    def check_current_states(self):
        print('**Kiem tra, trang thai hien tai la ')
        for index in range(0, len(self.current_states)):
            print('/<' + str(index+1) + '>: ' + self.current_states[index])
    def checkAccept(self):
        checknum = 0
        print('Final states: ')
        for index in range(0, len(self.final_states)):
            print('/<' + str(index+1) + '>: ' + self.final_states[index])
        for index_final in range(0, len(self.final_states)):
            for index_current in range(0, len(self.current_states)):
                if self.current_states[index_current] == self.final_states[index_final]:
                    checknum += 1
        if checknum == 0:
            return False
        else:
            return True
    def check(self):
        is_not_alphabet = 0
        input_languagle = input('Nhap ngon ngu cua ban: ')
        self.resetCurrentStates()
        print(self.current_states)
        self.define_current()
        for index in range(0, len(input_languagle)):
            if input_languagle[index] in self.alphabets:
                tmp = self.set_current_states(input_languagle[index])
                if tmp == 1:
                    is_not_alphabet = 1
                    break
            else:
                is_not_alphabet = 1
        if is_not_alphabet == 0 and self.checkAccept():
            print('******Thuoc automatic. yay.')
        else:
            print('Khong thuoc automatic.')
def convert_RG_to_FA(the_RG):
    if the_RG.is_not_Right_rule():
        the_RG.reverse_the_consequence()
        the_FA = convert_RG_to_FA(the_RG)
        the_FA.reverse_FA()
    else:
        the_FA = Finite_automata()
        the_FA.set_start_state(the_RG.get_start_symbol())
        the_FA.set_final_states('Eps')
        the_FA.set_states(the_RG.build_states())
        the_FA.set_alphabets(the_RG.build_alphabets())
        the_FA.set_transition_type1(the_RG.get_cause_consequence())
        the_FA.set_extra_states(the_RG.build_extra_states())
    return the_FA
def convert_FA_to_RG(the_FA):
    if the_FA.is_not_Right_rule():
        the_FA.reverse_FA()
        the_RG = convert_FA_to_RG(the_FA)
        the_RG.reverse_the_consequence()
    else:
        the_RG = Regular_grammar()
        the_RG.set_variables(the_FA.build_variables())
        the_RG.set_terminal_symbols(the_FA.get_alphabets())
        the_RG.set_start_symbol(the_FA.get_start_state())
        the_RG.set_production_rules(the_FA.get_transitions())
        if the_FA.get_extra_transitions() != [None]:
            the_RG.set_production_rules(the_FA.get_extra_transitions())
    return the_RG
def convert_FA_to_left_RG(the_FA):
    if the_FA.is_not_Right_rule():
        the_FA.reverse_FA()
        the_RG = convert_FA_to_RG(the_FA)
    else:
        the_RG = convert_FA_to_RG(the_FA)
        the_RG.reverse_the_consequence()
    return the_RG
def write_object_to_file(the_object, file_name):
    with open(file_name, 'wb') as output:
        pickle.dump(the_object, output, pickle.HIGHEST_PROTOCOL)
def read_object_from_file(file_name):
    with open(file_name, 'rb') as input:
        the_object = pickle.load(input)
    return the_object
def checkFA():
    print('Bat dau kiem tra xem ngon ngu co thuoc FA hay khong')
    the_FA = read_object_from_file('FA_class.pkl')
    while True:
        the_FA.check()
        while True:
            try:
                doLoop = int(input('Want to do it again? (type 0 to quit): '))
                if isinstance(doLoop, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        if doLoop == 0:
            break
def checkRG():
    print('Bat dau kiem tra xem ngon ngu co thuoc RG hay khong')
    the_RG = read_object_from_file('RG_class.pkl')
    the_FA = convert_RG_to_FA(the_RG)
    while True:
        the_FA.check()
        while True:
            try:
                doLoop = int(input('Want to do it again? (type 0 to quit): '))
                if isinstance(doLoop, numbers.Integral):
                    break
            except ValueError:
                print('ValueError!!!, please type again')
        if doLoop == 0:
            break
print('~~ Chuong trinh chuyen doi qua lai giua Van Pham Chinh Quy(RG) va Tap Hop Chinh Quy(FA) ~~\n'
      '~~ Convert between Regular Grammar and Finite Automata Program ~~\n')
while True:
    choose = input('$ ')
    if choose == 'import fa':
        print('Bat dau nhap Tap hon chinh quy(FA):')
        the_FA = Finite_automata()
        the_FA.import_()
        write_object_to_file(the_FA, 'FA_class.pkl')
    elif choose == 'import rg':
        print('Bat dau nhap Van pham chinh quy(RG):')
        the_RG = Regular_grammar()
        the_RG.import_()
        write_object_to_file(the_RG, 'RG_class.pkl')
    elif choose == 'convert fa':
        the_FA = read_object_from_file('FA_class.pkl')
        the_RG = convert_FA_to_RG(the_FA)
        write_object_to_file(the_RG, 'RG_class.pkl')
    elif choose == 'convert fa -l':
        the_FA = read_object_from_file('FA_class.pkl')
        the_RG = convert_FA_to_left_RG(the_FA)
        write_object_to_file(the_RG, 'RG_class.pkl')
    elif choose == 'convert rg':
        the_RG = read_object_from_file('RG_class.pkl')
        the_FA = convert_RG_to_FA(the_RG)
        write_object_to_file(the_FA, 'FA_class.pkl')
    elif choose == 'check fa':
        checkFA()
    elif choose == 'check rg':
        checkRG()
    elif choose == 'display fa':
        the_FA = read_object_from_file('FA_class.pkl')
        the_FA.display()
    elif choose == 'display rg':
        the_RG = read_object_from_file('RG_class.pkl')
        the_RG.display()
    elif choose == 'init 0':
        break
    elif choose == 'init 6':
        write_object_to_file(read_object_from_file('default_FA_class.pkl'), 'FA_class.pkl')
        write_object_to_file(read_object_from_file('default_RG_class.pkl'), 'RG_class.pkl')
    elif choose == 'help':
        print('#~ import fa: nhap Tap hop chinh quy cua ban\n'
              '#~ import rg: nhap Van pham chinh quy cua ban\n'
              '#~ display fa: hien thi Tap hop chinh quy\n'
              '#~ display rg: hien thi Van pham chinh quy\n'
              '#~ convert fa: de chuyen doi FA sang RG\n'
              '#~ convert fa -l: de chuyen doi FA sang left RG\n'
              '#~ convert rg: de chuyen doi RG sang FA\n'
              '#~ check fa: de kiem tra ngon ngu ban nhap vao co thuoc FA hay khong\n'
              '#~ check rg: de kiem tra ngon ngu ban nhap vao co thuoc RG hay khong\n'
              '#~ help: to get help...\n'
              '#~ init 6: to reboot all data\n'
              '#~ init 0: to quit.\n')
    else:
        print('Nhap $ help : de hien thi bang tro giup ve cac tu khoa cua chuong trinh\n'
              'Type $ help : to see all keywords of the program...\n')
