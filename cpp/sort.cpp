
#include <iostream>
using namespace std;

const int n = 15;
string cities[n] = {
	"Красноярск", "Москва", "Новосибирск", "Лондон", "Токио",
	"Пекин", "Волгоград", "Минск", "Владивосток", "Париж",
	"Манчестер", "Вашингтон", "Якутск", "Екатеринбург", "Омск"
};
typedef bool(*CompareFunction) (int i, int j);

bool compareUp(int i, int j) {
	return cities[i] < cities[j];
}

bool compareDown(int i, int j) {
	return cities[i] > cities[j];
}

bool compareLengthUp(int i, int j) {
	return cities[i].length() < cities[j].length();
}

bool compareLengthDown(int i, int j) {
	return cities[i].length() > cities[j].length();
}

void sortCities(CompareFunction compare) {
	for (int i = 0; i < n - 1; i++) {
		int j_min = i;
		for (int j = i+1; j < n; j++) {
			if (compare(j, j_min)) {
				j_min = j;
			}
		}
		string temp = cities[i];
		cities[i] = cities[j_min];
		cities[j_min] = temp;
	}
}

void printCities() {
    for(auto& i : cities)
        std::cout << i << '\n';
}

int main(int argc, char* argv[]) {
	setlocale(LC_ALL, "Russian");
    CompareFunction compares[] = {compareUp, compareDown, compareLengthUp, compareLengthDown};
	for (;;) {
		int choice;
		cout << "Ваш выбор: ";
		cin >> choice;
		sortCities(compares[choice]);
		printCities();
	}
	system("pause");
	return 0;
}