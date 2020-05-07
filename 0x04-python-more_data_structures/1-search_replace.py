#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search(elm):
        return(elm if elm != search else replace)
    return list(map(search, my_list))
