#include <functional>
#include <iostream>
#include <map>


//explicit map (const key_compare& comp = key_compare(),  const allocator_type& alloc = allocator_type());
int main ()
{
    const auto mg =
        std::map<int, int, std::function<bool (int, int)>>
        (
            {{1, 1}, {2, 2}, {3, 3}},
            std::greater<int>{}
        );
    const auto ml =
        std::map<int, int, std::function<bool (int, int)>>
        (
            {{1, 1}, {2, 2}, {3, 3}},
            std::less<int>{}
        );

    const auto mm = {mg, ml};

    for (const auto & m: mm)
    {
        for (const auto & p: m)
        {
            std::cout << p.first << ' ' << p.second << std::endl;
        }
        std::cout << std::endl;
    }
}