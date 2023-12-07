# Benchmark a few producer-consumer queues (pcQueue)

## Dependency

```
apt install libxenium-dev
apt install libreaderwriterqueue-dev
apt install libatomic-queue-dev
```

## Results

```
CPU Model: Intel(R) Xeon(R) CPU E5-1620 v4 @ 3.50GHz


===== moodycamel::BlockingReaderWriterCircularBuffer =====
iter: 0, elasped_ms: 6,576, handled_msg: 100,000,000, ops/sec: 15,206,012, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 1, elasped_ms: 7,538, handled_msg: 100,000,000, ops/sec: 13,264,480, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 2, elasped_ms: 6,657, handled_msg: 100,000,000, ops/sec: 15,021,670, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 3, elasped_ms: 8,415, handled_msg: 100,000,000, ops/sec: 11,882,541, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 4, elasped_ms: 7,289, handled_msg: 100,000,000, ops/sec: 13,717,886, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 5, elasped_ms: 8,628, handled_msg: 100,000,000, ops/sec: 11,589,997, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 6, elasped_ms: 7,477, handled_msg: 100,000,000, ops/sec: 13,373,886, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 7, elasped_ms: 7,898, handled_msg: 100,000,000, ops/sec: 12,660,299, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 8, elasped_ms: 7,800, handled_msg: 100,000,000, ops/sec: 12,819,888, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 9, elasped_ms: 7,799, handled_msg: 100,000,000, ops/sec: 12,820,708, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000


===== moodycamel::ReaderWriterQueue =====
iter: 0, elasped_ms: 1,637, handled_msg: 100,000,000, ops/sec: 61,078,342, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 1, elasped_ms: 1,536, handled_msg: 100,000,000, ops/sec: 65,090,583, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 2, elasped_ms: 1,500, handled_msg: 100,000,000, ops/sec: 66,654,701, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 3, elasped_ms: 1,445, handled_msg: 100,000,000, ops/sec: 69,180,913, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 4, elasped_ms: 1,515, handled_msg: 100,000,000, ops/sec: 65,982,309, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 5, elasped_ms: 1,511, handled_msg: 100,000,000, ops/sec: 66,165,829, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 6, elasped_ms: 1,491, handled_msg: 100,000,000, ops/sec: 67,068,084, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 7, elasped_ms: 1,498, handled_msg: 100,000,000, ops/sec: 66,726,562, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 8, elasped_ms: 1,452, handled_msg: 100,000,000, ops/sec: 68,869,144, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 9, elasped_ms: 1,478, handled_msg: 100,000,000, ops/sec: 67,641,636, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000


===== max0x7ba/OptimistAtomicQueues =====
iter: 0, elasped_ms: 3,156, handled_msg: 100,000,000, ops/sec: 31,685,335, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 1, elasped_ms: 3,092, handled_msg: 100,000,000, ops/sec: 32,338,683, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 2, elasped_ms: 3,090, handled_msg: 100,000,000, ops/sec: 32,354,046, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 3, elasped_ms: 3,118, handled_msg: 100,000,000, ops/sec: 32,065,611, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 4, elasped_ms: 3,096, handled_msg: 100,000,000, ops/sec: 32,293,141, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 5, elasped_ms: 3,156, handled_msg: 100,000,000, ops/sec: 31,685,674, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 6, elasped_ms: 3,065, handled_msg: 100,000,000, ops/sec: 32,618,181, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 7, elasped_ms: 3,187, handled_msg: 100,000,000, ops/sec: 31,371,626, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 8, elasped_ms: 3,085, handled_msg: 100,000,000, ops/sec: 32,411,568, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 9, elasped_ms: 3,118, handled_msg: 100,000,000, ops/sec: 32,067,991, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000


===== xenium/ramalhete_queue =====
iter: 0, elasped_ms: 4,701, handled_msg: 100,000,000, ops/sec: 21,271,324, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 1, elasped_ms: 5,077, handled_msg: 100,000,000, ops/sec: 19,693,219, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 2, elasped_ms: 5,032, handled_msg: 100,000,000, ops/sec: 19,870,729, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 3, elasped_ms: 4,988, handled_msg: 100,000,000, ops/sec: 20,047,533, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 4, elasped_ms: 5,106, handled_msg: 100,000,000, ops/sec: 19,582,846, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 5, elasped_ms: 4,956, handled_msg: 100,000,000, ops/sec: 20,176,071, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 6, elasped_ms: 4,725, handled_msg: 100,000,000, ops/sec: 21,160,513, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 7, elasped_ms: 5,033, handled_msg: 100,000,000, ops/sec: 19,867,915, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 8, elasped_ms: 5,203, handled_msg: 100,000,000, ops/sec: 19,219,559, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 9, elasped_ms: 4,814, handled_msg: 100,000,000, ops/sec: 20,770,172, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000


===== std::deque with std::mutex =====
iter: 0, elasped_ms: 11,353, handled_msg: 100,000,000, ops/sec: 8,807,971, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 1, elasped_ms: 11,569, handled_msg: 100,000,000, ops/sec: 8,643,402, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 2, elasped_ms: 12,220, handled_msg: 100,000,000, ops/sec: 8,183,256, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 3, elasped_ms: 11,368, handled_msg: 100,000,000, ops/sec: 8,795,900, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 4, elasped_ms: 11,137, handled_msg: 100,000,000, ops/sec: 8,978,934, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 5, elasped_ms: 11,631, handled_msg: 100,000,000, ops/sec: 8,597,584, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 6, elasped_ms: 11,711, handled_msg: 100,000,000, ops/sec: 8,538,921, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 7, elasped_ms: 11,695, handled_msg: 100,000,000, ops/sec: 8,550,081, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 8, elasped_ms: 11,749, handled_msg: 100,000,000, ops/sec: 8,511,078, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
iter: 9, elasped_ms: 11,531, handled_msg: 100,000,000, ops/sec: 8,671,806, counter: 10,000,000|0|30,000,000|0|10,000,000|20,000,000|0|10,000,000|10,000,000|10,000,000
```

```
CPU Model: Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz


===== moodycamel::BlockingReaderWriterCircularBuffer =====
iter: 0, elasped_ms: 8380, handled_msg: 100000000, ops/sec: 11932162, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 1, elasped_ms: 8113, handled_msg: 100000000, ops/sec: 12325756, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 2, elasped_ms: 8664, handled_msg: 100000000, ops/sec: 11541648, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 3, elasped_ms: 8191, handled_msg: 100000000, ops/sec: 12208305, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 4, elasped_ms: 8521, handled_msg: 100000000, ops/sec: 11734612, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 5, elasped_ms: 8162, handled_msg: 100000000, ops/sec: 12250401, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 6, elasped_ms: 8257, handled_msg: 100000000, ops/sec: 12109486, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 7, elasped_ms: 8072, handled_msg: 100000000, ops/sec: 12387421, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 8, elasped_ms: 8545, handled_msg: 100000000, ops/sec: 11702222, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 9, elasped_ms: 8017, handled_msg: 100000000, ops/sec: 12473263, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000


===== moodycamel::ReaderWriterQueue =====
iter: 0, elasped_ms: 1537, handled_msg: 100000000, ops/sec: 65059587, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 1, elasped_ms: 1521, handled_msg: 100000000, ops/sec: 65722535, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 2, elasped_ms: 1521, handled_msg: 100000000, ops/sec: 65742602, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 3, elasped_ms: 1519, handled_msg: 100000000, ops/sec: 65820926, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 4, elasped_ms: 1526, handled_msg: 100000000, ops/sec: 65489126, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 5, elasped_ms: 1530, handled_msg: 100000000, ops/sec: 65357251, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 6, elasped_ms: 1464, handled_msg: 100000000, ops/sec: 68280987, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 7, elasped_ms: 1425, handled_msg: 100000000, ops/sec: 70175357, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 8, elasped_ms: 1427, handled_msg: 100000000, ops/sec: 70030556, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 9, elasped_ms: 1436, handled_msg: 100000000, ops/sec: 69606313, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000


===== max0x7ba/OptimistAtomicQueues =====
iter: 0, elasped_ms: 2261, handled_msg: 100000000, ops/sec: 44216100, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 1, elasped_ms: 2194, handled_msg: 100000000, ops/sec: 45573466, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 2, elasped_ms: 2279, handled_msg: 100000000, ops/sec: 43865153, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 3, elasped_ms: 2281, handled_msg: 100000000, ops/sec: 43834062, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 4, elasped_ms: 2249, handled_msg: 100000000, ops/sec: 44458126, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 5, elasped_ms: 2435, handled_msg: 100000000, ops/sec: 41062320, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 6, elasped_ms: 2155, handled_msg: 100000000, ops/sec: 46384863, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 7, elasped_ms: 2274, handled_msg: 100000000, ops/sec: 43973209, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 8, elasped_ms: 2398, handled_msg: 100000000, ops/sec: 41701049, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 9, elasped_ms: 2193, handled_msg: 100000000, ops/sec: 45583629, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000


===== xenium/ramalhete_queue =====
iter: 0, elasped_ms: 3056, handled_msg: 100000000, ops/sec: 32717859, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 1, elasped_ms: 3613, handled_msg: 100000000, ops/sec: 27677681, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 2, elasped_ms: 3250, handled_msg: 100000000, ops/sec: 30767316, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 3, elasped_ms: 3948, handled_msg: 100000000, ops/sec: 25323164, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 4, elasped_ms: 3442, handled_msg: 100000000, ops/sec: 29048385, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 5, elasped_ms: 3055, handled_msg: 100000000, ops/sec: 32729806, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 6, elasped_ms: 5105, handled_msg: 100000000, ops/sec: 19586048, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 7, elasped_ms: 2927, handled_msg: 100000000, ops/sec: 34153564, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 8, elasped_ms: 3234, handled_msg: 100000000, ops/sec: 30919189, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 9, elasped_ms: 2868, handled_msg: 100000000, ops/sec: 34862252, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000


===== std::deque with std::mutex =====
iter: 0, elasped_ms: 9940, handled_msg: 100000000, ops/sec: 10059407, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 1, elasped_ms: 11319, handled_msg: 100000000, ops/sec: 8833969, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 2, elasped_ms: 10733, handled_msg: 100000000, ops/sec: 9316779, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 3, elasped_ms: 9916, handled_msg: 100000000, ops/sec: 10083827, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 4, elasped_ms: 10853, handled_msg: 100000000, ops/sec: 9213483, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 5, elasped_ms: 10874, handled_msg: 100000000, ops/sec: 9196201, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 6, elasped_ms: 9950, handled_msg: 100000000, ops/sec: 10049957, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 7, elasped_ms: 10901, handled_msg: 100000000, ops/sec: 9172914, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 8, elasped_ms: 9896, handled_msg: 100000000, ops/sec: 10104926, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
iter: 9, elasped_ms: 10729, handled_msg: 100000000, ops/sec: 9320525, counter: 10000000|0|30000000|0|10000000|20000000|0|10000000|10000000|10000000
```