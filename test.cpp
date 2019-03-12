#include <stdlib.h>
#include <vector>
#include <string>
#include <random>
#include <iostream>
#include <assert.h>
//Picks a new random day from the list. This function shouldn't pick the same day
//that we start with.
void randomize(const std::vector<std::string> &days, int & current_day)
{
	int prev_day = current_day;
	current_day = rand() % (days.size() + 1);
	while(current_day == prev_day)
	{
		current_day = rand() % (days.size() + 1);
	}
}
//Implement prev function
void prev(const std::vector<std::string> &days, int & current_day)
{

}
//Implement next function
void next(const std::vector<std::string> &days, int & current_day)
{

}
//Write tests here
void test(const std::vector<std::string> &days, int & current_day)
{

	// Sunday Test
	//assert(days[current_day] == "MONDAY");
	// Tuesday test
	//assert(days[current_day] == "SUNDAY");
	//Friday Test
	//assert (days[current_day] =="WEDNESDAY");
	//Wednesday Test
	//assert (days[current_day] =="SUNDAY");
}

//Compile using -std=c++11
int main()
{
	srand (time(NULL));
	std::vector<std::string> days	 {"MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"};
	//Can set current day to any to start with.
	int current_day = 0;
	std::cout << "Your starting day is: " << days[current_day] << std::endl;
	randomize(days, current_day);
	std::cout << "Your new random day is: " << days[current_day] << std::endl;
	test(days, current_day);
	return 0;
}