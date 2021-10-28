//
// Created by alex holt on 10/28/2021.
//

#include <chrono>
#include <ctime>
#include <iostream>
#include <map>
#include <random>
#include <stdio.h>
#include <unordered_map>
#include <vector>
using namespace std;

multimap<int, int> get_multimap(int n, unsigned seed = 0)
{
    mt19937 gen(seed);
    multimap<int, int> result;
    for (int i = 0; i < n; i++)
    {
        result.insert({gen(), 1});
    }
    return result;
}

unordered_map<int, int> get_unordered_map(int n, unsigned seed = 0)
{
    mt19937 gen(seed);
    unordered_map<int, int> result;
    for (int i = 0; i < n; i++)
    {
        result.insert({gen(), 1});
    }
    return result;
}

int main()
{
    // Get a seed to use for all random generation
    unsigned seed = chrono::system_clock::now().time_since_epoch().count();

    vector<int> sizes{10, 100, 1000, 10000, 100000, 250000, 500000, 750000, 1000000, 1500000, 2000000, 2500000};
    int num_iterations;
    cout << "N,multimap,unordered_map" << endl;
    for (int size : sizes)
    {
        if (size <= 1000)
        {
            num_iterations = 10000;
        }
        else
        {
            num_iterations = 10;
        }

        double multimap_time = 0;
        for (int i = 0; i < num_iterations; i++)
        {
            clock_t start_time = clock();
            get_multimap(size, seed);
            clock_t tot_time = clock() - start_time;
            multimap_time += ((double) tot_time) / (double) CLOCKS_PER_SEC;
        }
        multimap_time = multimap_time / num_iterations;

        double unorderedmap_time = 0;
        for (int i = 0; i < num_iterations; i++)
        {
            clock_t start_time = clock();
            get_unordered_map(size, seed);
            clock_t tot_time = clock() - start_time;
            unorderedmap_time += ((double) tot_time) / (double) CLOCKS_PER_SEC;
        }
        unorderedmap_time = unorderedmap_time / num_iterations;

        printf("%d,%f,%f\n", size, multimap_time, unorderedmap_time);
    }
}
