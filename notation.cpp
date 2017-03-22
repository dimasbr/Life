#include <iostream>
#include <sstream>
#include <string>
#include <regex>
#include <stack>
#include <stdlib.h>
#include <fstream>

std::map<std::string, float> variables;

void lineResult (std::stringstream* input)
{
    std::stack<float> stck;
    std::regex num("[0-9]+");
    std::regex oper("[\\+-/\\*]");
    std::regex var("[a-zA-Z]+");
    std::regex eqv("=");
    std::regex prnt("!print!");
    std::regex ex("!exit!");
    std::smatch mtch;

    std::string leftVar;
    bool eqviv=false;

    std::string temp;
    while(*(input)>>temp)
    {
        std::regex_match (temp, mtch, num);
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

            else
            {
                std::regex_match (temp, mtch, var);
                if(mtch.size() != 0)
                {
                    if (variables.count(temp) == 0)
                    {
                        variables[temp]=0;
                        stck.push(0);
                        if(!eqviv) leftVar = temp;
                    }
                    else
                    {
                        stck.push(variables[temp]);
                        if (!eqviv) leftVar = temp;
                    }
                    
                }
                else
                {
                    std::regex_match (temp, mtch, eqv);
                    if(mtch.size()!=0)
                    {
                        eqviv=true;
                    }
                    else
                    {
                        std::regex_match(temp, mtch, prnt);
                        if(mtch.size()!=0)
                        {
                            std::string res=std::to_string(stck.top());
                            std::cout<<res<<std::endl;
                        }
                    
                        else
                        {
                            std::regex_match(temp, mtch, ex);
                            if(mtch.size()!=0)
                            {
                                exit(EXIT_FAILURE);
                            }
                        }
                    }
                }
                
            }
            
        } 
    }

    if(eqviv)
    {
        variables[leftVar] = stck.top();
    }

}



int main()
{
    std::cout<<"Type \"FILE\" if you want open file or \"TERMINAL\" for working in terminal"<<std::endl;
    std::string mode;
    std::getline(std::cin, mode);

    if (mode == "TERMINAL")
    {
        while(true)
        {
            std::string some;
            std::getline(std::cin, some);
            std::stringstream str(some);
            lineResult(&str);
        }
    }
    else if (mode == "FILE")
    {
        std::cout<<"Write the name of your file"<<std::endl;
        std::cin>>mode;
        std::ifstream fl;
        fl.open(mode);
        while (std::getline(fl, mode))
        {
            std::stringstream str(mode);            
            lineResult(&str);
        }
    }
}
