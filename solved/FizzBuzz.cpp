#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

int main(int argc, char *argv[])
{
   std::ifstream stream(argv[1]);
   std::string line = "", temp = "", result = "";
   std::vector<int> v;
   int X=0, Y=0, N=0;

   while (getline(stream, line)) {
      std::stringstream os(line);

      while (os >> temp)
         v.push_back(stoi(temp));

      X = v[0];
      Y = v[1];
      N = v[2];

      if ((X >= 1 && X <= 20) && (Y >= 1 && Y <= 20) && (N >= 21 && N <= 100)){
         for (int i=1;i<=N;i++)
            if (i % X == 0 && i % Y == 0)
               result += "FB ";
            else if (i % X == 0)
               result += "F ";
            else if (i % Y == 0)
               result += "B ";
            else
               result += std::to_string(i) + " ";

         std::cout << result << std::endl;
      }
      temp=result="";
      v.clear();
   }
   return 0;
}
