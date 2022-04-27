#include <string>
#include <iostream>
using namespace std;

class Rectangle {
    public:
        double height;
        double width;

        double getPerimeter(){
            return (width + height) * 2;
        }
        double getArea(){
            return width * height;
        }
};