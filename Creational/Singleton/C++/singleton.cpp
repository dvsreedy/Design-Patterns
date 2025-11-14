#include <iostream>
#include <string>

class Singleton {
private:
    static Singleton* instance;
    std::string data;

    // Private constructor to prevent direct instantiation
    Singleton(const std::string& data) : data(data) {}

public:
    // Deleted copy/move to enforce single instance
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    Singleton(Singleton&&) = delete;
    Singleton& operator=(Singleton&&) = delete;

    // Lazy, non-thread-safe singleton accessor
    static Singleton* getInstance() {
        if (instance == nullptr) {
            instance = new Singleton("Default");
        }
        return instance;
    }

    const std::string& getData() const { return data; }
    void setData(const std::string& d) { data = d; }
};

// Initialize static member
Singleton* Singleton::instance = nullptr;

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