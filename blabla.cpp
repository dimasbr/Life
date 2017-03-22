#include <iostream>
#include <sstream>
#include <string>
#include <regex>
#include <stack>

float lineResult (std::stringstream* input)
{
    std::stack<float> stck;
    std::regex num("[0-9]+");
    std::regex oper("[\\+-/\\*]");
    std::smatch mtch;

    std::string temp;
    while(*(input)>>temp)
    {
        std::regex_match (temp, mtch, num);
//std::cerr<<temp;
        if (mtch.size()!=0)
        {
            stck.push((float)std::stoi(mtch[0]));
        }
        else
        {
            std::regex_match (temp, mtch, oper);
            if(mtch.size()!=0)
            {
                int b=stck.top();
                stck.pop();
                int a=stck.top();
                stck.pop();
                
                if(mtch[0]=="+") stck.push(a+b);
                if(mtch[0]=="-") stck.push(a-b);
                if(mtch[0]=="*") stck.push(a*b);
                if(mtch[0]=="/") stck.push((float)a/b);
            }
            else std::cout<<"something wrong";
        } 
    }

    return stck.top();

}



int main()
{
std::cout<<"write some"<<std::endl;
std::string some;
std::getline(std::cin, some);
std::stringstream str(some);
std::string res=std::to_string(lineResult(&str));
std::cout<<res<<std::endl;
}