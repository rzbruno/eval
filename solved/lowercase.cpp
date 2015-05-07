#include <iostream>       // std::cout
#include <string>         // std::string
#include <locale>         // std::locale, std::tolower
#include <fstream>        // std::ifstream

int main(int argc, char *argv[])
{
   std::locale loc;
   std::string line="";

   std::ifstream stream(argv[1]);
   while (getline(stream, line)) {
      line += '\n';
      for(auto elem : line)
         std::cout << std::tolower(elem,loc);
   }
   return 0;
}
