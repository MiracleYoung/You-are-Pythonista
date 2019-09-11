#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/6/14 下午11:06
# @Author  : MiracleYoung
# @File    : graph.py

def search_graph(graph: dict, start, end):
    _ret = []
    generate_path(graph, [start], end, _ret)
    # 这一步的排序可有可无，只不过为了显示好看
    _ret.sort(key=lambda x: len(x))
    return _ret


def generate_path(graph: dict, path, end, ret: list):
    _state = path[-1]
    # 如果起始点和终点是同一个位置，则结束
    if _state == end:
        ret.append(path)
    else:
        for _item in graph[_state]:
            if _item not in path:
                # path + [_item] 就是递归调用的关键参数，path的组成
                generate_path(graph, path + [_item], end, ret)


if __name__ == '__main__':
    _GRAPH = {'A': ['B', 'C', 'D'],
             'B': ['E'],
             'C': ['D', 'F'],
             'D': ['B', 'E', 'G'],
             'E': [],
             'F': ['D', 'G'],
             'G': ['E']}
    _ret = search_graph(_GRAPH, 'A', 'E')
    print("******************")
    print(' path A to E')
    print("******************")
    for i in _ret:
        print(i)
