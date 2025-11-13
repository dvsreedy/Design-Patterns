#include <iostream>
#include <string>

public class Singleton {
private:
    static Singleton instance;
    string data;
    // Private constructor to prevent instantiation
    Singleton(string data) {
        this->data = data;
    }
public:
    static Singleton getInstance() {   
        if (instance == nullptr) {
            instance = new Singleton();
        }
        return instance;
    }   
};


int main() {
    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();

    if (s1 == s2) {
        std::cout << "Both instances are the same." << std::endl;
    } else {
        std::cout << "Instances are different." << std::endl;
    }

    return 0;
}