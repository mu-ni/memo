1. build competitor-count map, count means competitor's appearance in review
2. build list<list> to store appearance of each comp-list, outter index means appearance
3. build result by iterating list<list> from end to start, that means add most frequency competitor first

time: numCompetitors X numReviews
(btw, Collection.sort() nlogn)
space: numCompetitors

complexity



1. minumum -> BFS algorithm
2. init queue with all updated servers
3. init days' value as -1,  means that is impossible to update all servers
4. start BFS, skip invalid position, skip already updated server, set updated server to 1
5. when queue is empty, all servers are updated, return current days

time: rows*columns
space: rows*columns
