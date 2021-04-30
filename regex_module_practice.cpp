#include <iostream>
#include <fstream>
#include <regex>

std::string word_list[50];
int word_amount = 0;
std::string line_list[20];
int line_amount = 0;

bool check_capital(char char_member){
    if (char_member >= 65 && char_member <= 90) return true;
    return false;
}
bool check_endline(char char_member){
    if (char_member == '.' || check_capital(char_member)) return true;
    return false;
}
bool check_doublespace(char char_member){
    if (char_member == ' ') return true;
    return false;
}
void check_grammar(){
    for (int line_num = 0; line_num < line_amount; line_num++){
        char *temp_list_of_char_in_a_line = new char[line_list[line_num].length() + 1];
        strcpy(temp_list_of_char_in_a_line, line_list[line_num].c_str());
        for (int char_num = 0; char_num < line_list[line_num].length(); char_num++){
            if (char_num == 0) 
                if (check_capital(temp_list_of_char_in_a_line[char_num]) == false) 
                    std::cout << "TypeError (capital the first char needed) in line " << line_num + 1 << std::endl;
            if (char_num == line_list[line_num].length()-1)
                if (check_endline(temp_list_of_char_in_a_line[char_num]) == false)
                    std::cout << "TypeError (dot or capital in the end needed) in line " << line_num + 1 << std::endl;
            if (temp_list_of_char_in_a_line[char_num] == ' ' && char_num < line_list[line_num].length()-1)
                if (check_doublespace(temp_list_of_char_in_a_line[char_num+1]))
                    std::cout << "TypeError (double space found) in line " << line_num + 1 << std::endl;
            if (check_capital(temp_list_of_char_in_a_line[char_num]) && char_num < line_list[line_num].length()-1)
                if (check_capital(temp_list_of_char_in_a_line[char_num+1]))
                    std::cout << "TypeError (double capital found) in line " << line_num + 1 << std::endl;
        }
    }
}
void split_up(std::string str[]) {
	std::regex reg_("\\S+");
	for (int line_num = 0; line_num < line_amount; line_num++) {
		const std::sregex_iterator end;
		for (std::sregex_iterator it(str[line_num].begin(), 
										str[line_num].end(), reg_); 
			it != end; it++) {
			word_list[word_amount] = (*it)[0];
			word_amount++;
		}
	}
}
void replace_str(){
    std::string *temp_line_list = new std::string[line_amount];
    for (int linenum = 0; linenum < line_amount; linenum++) {
        temp_line_list[linenum] = line_list[linenum];
    }
    for (int line_num = 0; line_num < line_amount; line_num++) {
		char *temp_linemember_in_char = new char[temp_line_list[line_num].length() + 1];
        strcpy(temp_linemember_in_char, temp_line_list[line_num].c_str());
        for (int str_index = 0; str_index < line_list[line_num].length(); str_index++){
            if (temp_linemember_in_char[str_index] == '.' || temp_linemember_in_char[str_index] == '<' ||           
                temp_linemember_in_char[str_index] == '>' || temp_linemember_in_char[str_index] == '/' || 
                temp_linemember_in_char[str_index] == '@' || temp_linemember_in_char[str_index] == ',')
            {
                temp_line_list[line_num].replace(str_index,1," ");
            }
        }
	}
    split_up(temp_line_list);
}
void readFile() {
	std::fstream infile;
	infile.open("re_practice_text.txt");
	if (infile.is_open()){
		while (!infile.eof()){
			getline(infile, line_list[line_amount]);
			line_amount++;
		}
        check_grammar();
		infile.close();
        replace_str();
	} else std::cout << "!!! Error to read file.\n" << std::endl;
}
void regex_search_word(std::regex reg_) {
	int found_amount = 0;
	for (int word_num = 0; word_num < word_amount; word_num++) {
		std::smatch match;
		if (std::regex_search(word_list[word_num], match, reg_)) {
            if (found_amount == 0) std::cout << "[";
            else std::cout << ", ";
            if (match.str(1) != "") std::cout << "'" << match[1] << "'";
			else std::cout << "'" << word_list[word_num] << "'";
			found_amount++;
		}
	}
	if (found_amount == 0) std::cout << "!!! Not found";
    else std::cout << "]";
	std::cout << std::endl;
}
void regex_search_line(std::regex reg_) {
	int found_amount = 0;
	for (int line_num = 0; line_num < line_amount; line_num++) {
		std::smatch match;
		if (std::regex_search(line_list[line_num], match, reg_)) {
            if (found_amount == 0) std::cout << "[";
			else std::cout << ", ";
            if (match.str(1) != "") std::cout << "'" << match[1] << "'";
			else std::cout << "'" << line_list[line_num] << "'";
			found_amount++;
		}
	}
	if (found_amount == 0) std::cout << "!!! Not found";
    else std::cout << "]";
	std::cout << std::endl;
}
void regex_replace_word (std::regex reg_, const std::string hint){
	int found_amount = 0;
	for (int word_num = 0; word_num < word_amount; word_num++) {
		std::smatch m;
		if (std::regex_search(word_list[word_num], m, reg_)) {
			std::cout << "\t'" << word_list[word_num] << "' >> ";
			word_list[word_num] = regex_replace(word_list[word_num], reg_, hint);
			std::cout << "'" << word_list[word_num] << "'" << std::endl;
			found_amount++;
		}
	}
	if (found_amount == 0) std::cout << "!!! Not found" << std::endl;
}
void func_1 () {
	std::cout << ">> A list of words containing 'a-z' and '0-9':" << std::endl << std::endl;
	std::regex reg_("\\w*[a-z]+\\d+|\\d+[a-z]+\\w*");
	regex_search_word(reg_);}
void func_2 () {
	std::cout << std::endl << ">> A list of words containing 'a' followed by 'b'*:" << std::endl << std::endl;
	std::regex reg_("\\w*ab*\\w*");
	regex_search_word(reg_);}
void func_3 () {
	std::cout << std::endl <<  ">> A list of words starting with 'a' and ending with 'b':" << std::endl << std::endl;
	std::regex reg_("^a.*b$");
	regex_search_word(reg_);}
void func_4 () {
	std::cout << std::endl << ">> A list of words containing only 'a-z' and '_':" << std::endl << std::endl;
	std::regex reg_("^[a-z]+_+$");
	regex_search_word(reg_);}
void func_5 () {
	std::cout << std::endl << ">> A list of words containing 5 characters:" << std::endl << std::endl;
	std::regex reg_("^.{5}$");
	regex_search_word(reg_);}
void func_6 () {
	std::cout << std::endl << ">> A list of words containing 'h':" << std::endl << std::endl;
	std::regex reg_(".*h+.*");
	regex_search_word(reg_);}
void func_7 () {
	std::cout << std::endl << ">> A list of words starting with [0-9]:" << std::endl;	
	std::regex reg_("^\\d+.*");
	regex_search_word(reg_);}
void func_8 () {
	std::cout << std::endl << ">> Replace '_' with ' ':" << std::endl << std::endl;
	std::regex reg_("[_]+");
	const std::string hint(" ");
	regex_replace_word(reg_, hint);}
void func_9 () {
	std::cout << std::endl <<  ">> Replace mm-dd-yy with dd-mm-yy:" << std::endl << std::endl;
	std::regex reg_("(\\w+)-(\\w+)-(\\w+)");
	const std::string hint("$2-$1-$3");
	regex_replace_word(reg_, hint);}
void func_10 () {
	std::cout << std::endl << ">> Lines starting with 't' or 'h' and containing 're':" << std::endl << std::endl;
	std::regex reg_("^[t|h].*re+.*");
	regex_search_line(reg_);}
void func_11 () {
	std::cout << std::endl << ">> A list of words containing at least 20 characters:" << std::endl << std::endl;
	std::regex reg_(".{20,}");
	regex_search_word(reg_);}
void func_12 () {
	std::cout << std::endl << ">> A list of words ending with '?!':" << std::endl << std::endl;
	std::regex reg_(".*[?!]+$");
	regex_search_word(reg_);}
void func_13 () {
	std::cout << std::endl << ">> Lines containing 'a' 'r' 's' 'm' 'l' no need to continuous:" << std::endl << std::endl;
	std::regex reg_(".*a+.*r+.*s+.*m+.*l+.*");
	regex_search_line(reg_);}
void func_14 () {
	std::cout << std::endl << ">> Lines not containing ',' and '.':" << std::endl << std::endl;
	std::regex reg_("^[^\\.|^,]+$");
	regex_search_line(reg_);}
void func_15 () {
	std::cout << std::endl << ">> Lines containing 'mouse':" << std::endl << std::endl;
	std::regex reg_(".*mouse+.*");
	regex_search_line(reg_);}
void func_16 () {
	std::cout << std::endl << ">> A list of words containing 'a'+ followed by 'b':" << std::endl << std::endl;
	std::regex reg_("\\w*ab\\w*");
	regex_search_word(reg_);}
void func_17 () {
	std::cout << std::endl << ">> Domain:" << std::endl << std::endl;
	std::regex reg_("(\\w+)@\\w+[\\.\\w+]+");
    regex_search_line(reg_);}
void func_18 () {
	std::cout << std::endl << ">> Betweem <head> and </head>:" << std::endl << std::endl;
	std::regex reg_("<head>(.*)</head>");
	regex_search_line(reg_);}
int main(){
	readFile();
	//Bai tap ve nha
	func_1();
	func_2();
	func_3();
	func_4();
	func_5();
	func_6();
	func_7();
	func_8();
	func_9();
	//Bai tap tren lop
	func_10();
	func_11();
	func_12();
	func_13();
	func_14();
	func_15();
	func_16();
	func_17();
	func_18();
}