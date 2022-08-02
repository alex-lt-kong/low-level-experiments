#include "utils.h"

unsigned long long get_timestamp_now() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (unsigned long long)(tv.tv_sec) * 1000 + (unsigned long long)(tv.tv_usec) / 1000;
}

double standard_deviation(unsigned long long* arr, size_t arr_len) {
    if (arr_len <= 0) {
        fprintf(stderr, "arr_len must be greater than 0\n");
        return -1;
    }
    double sum = 0, mean, std = 0;
    for(size_t i = 0; i < arr_len; ++i) {
        sum += (double)arr[i];        
    }    
    mean = sum / arr_len;
    for(size_t i = 0; i < arr_len; ++i) {
        std += pow(arr[i] - mean, 2);
    }
        
    return sqrt(std / arr_len);
}