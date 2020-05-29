'''
　问题描述：一维经典装箱问题可描述如下：S=（S1,S2,..Sn）,其中0< Si ≤ 1, 称之为第i个物体的体积（或重量），1≤i≤n,现有n个容积（或载重量）为1
  的箱子，要求如何设法将S1,S2,..Sn放入尽可能少的箱中。
　装箱问题是NP问题,即在多项式时间内无法精确求解,一般采用近似算法,即启发式算法,这样可以迅速得到满意解,而不一定是最优解.
　* 常见的算法：
  NF(Next Fit)近似算法，FF(First Fit)近似算法，FFD（First Fit Decreasing）近似算法，BF(best Fit),BFD(Best Fit Deceasing)等，
　　1.下次适应算法（NF, Next Fit）：NF算法是最简单也是最早研究的一个算法，它的处理方法是始终维持一个当前打开的箱子，对于每一个要装入的物
     品，检查该物品是否可以放入当前打开的箱子，如果无法装入，则打开一个空箱子，装入该物品，以该箱子作为当前的箱子，由于每个物品在装入时，只有
     当前打开的箱子和空箱可以选择，这必然造成装箱的效率低下。
　　2.首次适应算法(First Fit)：针对下次适应算法的缺陷，首次适应算法FF处理当前物品的时候，检查所有非空箱子，找到第一个能够放下当前物品的箱子
     并将该物品放入，否则则开启新的箱子。
　　3.最佳适应算法(Best Fit)：与首次适应算法类似，唯一的区别时当物品装箱时，不是直接装在第一个可装入的箱子中，而是装入在最适合该物体的箱子中，
     如果没有该箱子，则开启空箱。
　　4.首次适应算法和最佳适应算法有一个缺陷，即由于物品没有实现排序，则可能由于先装入小的物品，使大的物品在后来放入时无法装入，只得开启新的箱子，
     造成了空间的浪费,因此才有了这两种算法的改进算法。
　　5.降序首次适应算法(FFD, First Fit Decreasing)：先对物品按降序排序，再按照首次适应算法进行装箱。
　　6.降序最佳适应算法(BFD, Best Fit Decreasing)：先对物品按降序排序，再按照最佳适应算法进行装箱。
'''

# 下次适应算法
def get_min_boxes(things, box_weight):
    things = sorted(things, reverse=True)  # 将数据由大到小排序
    print(things)
    m = len(things) - 1;
    count = 0
    for i in range(len(things)):
        sum = 0
        print('{', end='')
        sum = things[i]
        print(things[i], ' ', end='')
        while m >= 0:
            j = m
            sum += things[j]
            if sum > box_weight:
                count += 1
                break
            print(things[j], '', end='')
            m -= 1
        if j == i:
            # count+=1
            print('}')
            break
        print('}')

    print('最少需要使用', count, '个容积为', box_weight, '的箱子')


if __name__ == '__main__':
    # things = [4, 8, 1, 4, 2, 1]
    # box_weight = 10
    things=[3,5,14,9,13,4,10,4,20,3,1,7,13,8,6,18,20,5,9,8,7,4,3,2]
    box_weight=20
    get_min_boxes(things, box_weight)