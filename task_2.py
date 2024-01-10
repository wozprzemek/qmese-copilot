"""
We have some horse racing statistics (each horse's time in each race).
You have to find the number of the horse which has the most wins.
For example: if the results are `[[“1:13”, “1:26”, “1:11”], [“1:10”, “1:18”, “1:14”], [“1:20”, “1:23”, “1:15”]]`, then the 3rd horse is the fastest, because it has won 2 races out of 3.
Every element in the list - is a string in format m:ss, for example, "1:05" or "2:22". 1:00 <= time <= 5:00 

--Input:--
    Racing times as an array of arrays.

--Output--  
    The number of the fastest horse that has the most wins (Important: in this task the horse numbers starts from "1", not from "0").

--Example:--
    fastest_horse([[“1:13”, “1:26”, “1:11”], [“1:10”, “1:18”, “1:14”], [“1:20”, “1:23”, “1:15”]]) == 3

"""

def fastest_horse(horses: list) -> int:
    # implement
    pass


if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    assert fastest_horse([["1:10", "1:15", "1:20"], ['1:05', '1:10', '1:15'], ['2:59', '2:59', '2:59']]) == 1
    assert fastest_horse([["4:44", "4:11", "4:18"], ["3:10", "3:01", "3:14"], ["2:20", "2:23", "2:15"]]) == 2
    assert fastest_horse([["1:55", "1:50", "1:45", "1:40", "1:35"], ["2:55", "2:50", "2:45", "2:40", "2:35"],
                          ["3:55", "3:50", "3:45", "3:40", "3:35"], ["4:55", "4:50", "4:45", "4:40", "4:35"],
                          ["3:55", "3:50", "3:45", "3:40", "3:35"], ["2:35", "2:40", "2:45", "2:50", "2:55"]]) == 5