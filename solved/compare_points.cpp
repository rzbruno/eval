#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

int main(int argc, char *argv[])
{
   std::ifstream stream(argv[1]);
   std::vector<long> v;
   std::string temp="", line="", location="";
   long current_X=0, current_Y=0, target_X=0, target_Y=0;

   while (getline(stream, line)) {
      std::stringstream os(line);
      while (os >> temp)
         v.push_back(stoi(temp));

      current_X = v[0];
      current_Y = v[1];
      target_X  = v[2];
      target_Y  = v[3];

      if (target_X == current_X && target_Y == current_Y)
         location += "here";
      else{
         if (target_Y > current_Y)
         location += "N";
         else if (target_Y < current_Y)
         location += "S";

         if (target_X > current_X)
         location += "E";
         else if (target_X < current_X)
         location += "W";
      }
      std::cout << location << std::endl;

      location = temp = "";
      v.clear();
   }
   return 0;
}
